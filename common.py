# common.py
import itertools
import time
import math
import csv

RANDOM_SEED = 42


def get_overlap(seq1, seq2):
    """두 시퀀스 간의 최대 접미사-접두사 오버랩 길이를 계산합니다."""
    max_len = min(len(seq1), len(seq2))
    for k in range(max_len, 0, -1):
        if seq1[-k:] == seq2[:k]:
            return k
    return 0


def generate_permutations(n):
    """지정된 n에 대해 순열 튜플 리스트를 생성합니다."""
    return [tuple(map(str, p)) for p in itertools.permutations(range(1, n + 1))]


def sequence_to_string(sequence, n):
    """토큰 시퀀스를 문자열로 변환합니다."""
    if n <= 9:
        return "".join(sequence)
    return " ".join(sequence)


def verify_superpermutation(sequence, perms):
    """생성된 시퀀스가 모든 순열을 포함하는 유효한 토큰 시퀀스인지 검증합니다."""
    if sequence == "Timeout" or not sequence:
        return False

    for perm in perms:
        found = False
        perm_len = len(perm)
        for i in range(len(sequence) - perm_len + 1):
            if tuple(sequence[i:i + perm_len]) == perm:
                found = True
                break
        if not found:
            return False

    return True


def run_benchmark(algo_name, algo_func, n, num_runs=100):
    """지정된 알고리즘을 num_runs회 반복 실행하여 통계를 내고 결과를 저장합니다."""
    perms = generate_permutations(n)
    runtimes = []
    lengths = []
    best_seq = []
    min_len = float('inf')
    success_count = 0

    print(f"=== {algo_name} 벤치마크 시작 (n={n}, Runs={num_runs}) ===")

    for i in range(num_runs):
        t0 = time.perf_counter()
        seq = algo_func(n, perms, i)
        dt = (time.perf_counter() - t0) * 1000

        is_valid = verify_superpermutation(seq, perms)
        runtimes.append(dt)

        if is_valid:
            success_count += 1
            length = len(seq)
            lengths.append(length)
            if length < min_len:
                min_len = length
                best_seq = seq
        else:
            lengths.append(0)

    valid_lengths = [l for l in lengths if l > 0]
    if not valid_lengths:
        print(f"[{algo_name}] 모든 실행이 타임아웃되었거나 유효하지 않은 시퀀스를 생성했습니다.\n")
        return

    avg_time = sum(runtimes) / num_runs
    avg_len = sum(valid_lengths) / len(valid_lengths)
    max_len = max(valid_lengths)
    success_rate = (success_count / num_runs) * 100
    variance = sum((x - avg_len) ** 2 for x in valid_lengths) / len(valid_lengths)
    std_dev = math.sqrt(variance)

    print(f"Average Time      : {avg_time:.2f} ms")
    print(f"Average Length    : {avg_len:.2f}")
    print(f"Minimum Length    : {min_len}")
    print(f"Maximum Length    : {max_len}")
    print(f"Std Dev           : {std_dev:.2f}")
    print(f"Success Rate      : {success_rate:.1f}%")

    best_file_name = f"best_sequence_{algo_name.lower().replace(' ', '_')}.txt"
    with open(best_file_name, "w", encoding="utf-8") as f:
        f.write(sequence_to_string(best_seq, n))
    print(f"Best Sequence Saved to '{best_file_name}'.")

    csv_file_name = "results.csv"
    file_exists = False
    try:
        with open(csv_file_name, "r", encoding="utf-8"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(csv_file_name, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Algorithm", "n", "Avg Time(ms)", "Avg Length", "Min Length", "Max Length", "Std Dev", "Success Rate(%)"])
        writer.writerow([algo_name, n, f"{avg_time:.2f}", f"{avg_len:.2f}", min_len, max_len, f"{std_dev:.2f}", f"{success_rate:.1f}"])
    print(f"Summary appended to '{csv_file_name}'.\n")
