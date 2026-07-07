# baseline_greedy.py
import random
from common import run_benchmark, get_overlap, RANDOM_SEED

def solve_baseline_greedy(n, perms, run_idx):
    random.seed(RANDOM_SEED)
    current = perms[0]
    unvisited = list(perms[1:])
    sequence = list(current)

    while unvisited:
        best_next = None
        max_ov = -1

        for node in unvisited:
            ov = get_overlap(current, node)
            if ov > max_ov:
                max_ov = ov
                best_next = node

        if max_ov == n - 2:
            candidates = [node for node in unvisited if get_overlap(current, node) == max_ov]
            if candidates:
                best_next = candidates[-1]
                max_ov = get_overlap(current, best_next)

        unvisited.remove(best_next)
        sequence.extend(best_next[max_ov:])
        current = best_next

    return sequence

if __name__ == "__main__":
    run_benchmark("Baseline Greedy", solve_baseline_greedy, n=5, num_runs=100)
