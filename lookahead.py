# lookahead.py
import random
from common import run_benchmark, get_overlap, RANDOM_SEED

def solve_lookahead(n, perms, run_idx):
    random.seed(RANDOM_SEED)
    current = perms[0]
    unvisited = list(perms[1:])
    sequence = list(current)

    while unvisited:
        best_next = None
        best_cost = float('inf')

        for cand in unvisited:
            cost1 = n - get_overlap(current, cand)
            if len(unvisited) == 1:
                total_cost = cost1
            else:
                next_remaining = [x for x in unvisited if x != cand]
                cost2 = min(n - get_overlap(cand, nxt) for nxt in next_remaining)
                total_cost = cost1 + cost2

            if total_cost < best_cost:
                best_cost = total_cost
                best_next = cand

        unvisited.remove(best_next)
        ov = get_overlap(current, best_next)
        sequence.extend(best_next[ov:])
        current = best_next

    return sequence

if __name__ == "__main__":
    run_benchmark(
        "Greedy Lookahead k=2",
        solve_lookahead,
        n=5,
        num_runs=100
    )
