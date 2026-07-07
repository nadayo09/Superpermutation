# dfs_limited.py
import time
from common import run_benchmark, get_overlap

def solve_dfs_limited(n, perms, run_idx):
    start_node = perms[0]
    unvisited = set(perms[1:])
    
    best_seq = [None]
    min_len = [float('inf')]
    start_time = time.time()
    
    def dfs(curr, current_seq, visited_set):
        # 1.0초 타임아웃 제한 조건 강제 체크
        if time.time() - start_time > 1.0:
            return
            
        # 모든 순열을 다 방문한 완벽한 슈퍼퍼뮤테이션 발견 시 갱신
        if not visited_set:
            if len(current_seq) < min_len[0]:
                min_len[0] = len(current_seq)
                best_seq[0] = current_seq
            return
            
        # 가지치기(Pruning): 이미 찾은 최소값보다 현재 경로가 길어지면 탈출
        if len(current_seq) >= min_len[0]:
            return
            
        # 그리디 하이브리드 가이드: 오버랩이 가장 큰(비용이 낮은) 순서대로 정렬하여 우선 탐색
        candidates = sorted(list(visited_set), key=lambda x: get_overlap(curr, x), reverse=True)
        for cand in candidates:
            ov = get_overlap(curr, cand)
            dfs(cand, current_seq + cand[ov:], visited_set - {cand})
            
            # 하위 재귀 루프 실행 도중 타임아웃 발생 시 백트래킹 즉시 정지
            if time.time() - start_time > 1.0:
                return

    # 실제 깊이 우선 탐색 개시
    dfs(start_node, start_node, unvisited)
    
    # 1초의 타임아웃 제약으로 인해 탐색을 완료하지 못했으므로 논문 명세대로 "Timeout" 반환
    return best_seq[0] if best_seq[0] else "Timeout"

if __name__ == "__main__":
    run_benchmark("Greedy Depth-Limited DFS", solve_dfs_limited, n=5, num_runs=100)