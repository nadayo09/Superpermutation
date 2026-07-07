# random_restart.py
import random
from common import run_benchmark, get_overlap, RANDOM_SEED

def solve_random_restart(n, perms, run_idx):
    random.seed(RANDOM_SEED + run_idx)
    shuffled_perms = list(perms)
    random.shuffle(shuffled_perms)

    current = shuffled_perms[0]
    unvisited = list(shuffled_perms[1:])
    sequence = list(current)

    while unvisited:
        best_next = None
        max_ov = -1
        for node in unvisited:
            ov = get_overlap(current, node)
            if ov > max_ov:
                max_ov = ov
                best_next = node

        unvisited.remove(best_next)
        sequence.extend(best_next[max_ov:])
        current = best_next

    return sequence

if __name__ == "__main__":
    run_benchmark("Greedy Random Restart", solve_random_restart, n=5, num_runs=100)
