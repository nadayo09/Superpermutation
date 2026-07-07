import random
from common import run_benchmark, get_overlap, RANDOM_SEED


def solve_lookahead(n, perms, run_idx, k=2):
    random.seed(RANDOM_SEED)

    current = perms[0]
    unvisited = set(perms[1:])
    sequence = current

    def calculate_future_cost(curr, remaining, depth):
        if depth == 0 or not remaining:
            return 0

        min_cost = float('inf')

        for nxt in perms:
            if nxt not in remaining:
                continue

            cost = n - get_overlap(curr, nxt)

            next_remaining = remaining - {nxt}

            cost += calculate_future_cost(
                nxt,
                next_remaining,
                depth - 1
            )

            min_cost = min(min_cost, cost)

        return min_cost


    while unvisited:
        best_next = None
        min_projected_cost = float('inf')

        for cand in perms:
            if cand not in unvisited:
                continue

            temp_unvisited = unvisited - {cand}

            cost = (
                n - get_overlap(current, cand)
                + calculate_future_cost(
                    cand,
                    temp_unvisited,
                    k - 1
                )
            )

            if cost < min_projected_cost:
                min_projected_cost = cost
                best_next = cand

        unvisited.remove(best_next)

        ov = get_overlap(current, best_next)
        sequence += best_next[ov:]

        current = best_next

    return sequence


if __name__ == "__main__":

    for k in range(1, 21):

        print("=" * 60)
        print(f"Lookahead k={k}")
        print("=" * 60)

        run_benchmark(
            f"Greedy Lookahead k={k}",
            lambda n, perms, run_idx, depth=k:
                solve_lookahead(
                    n,
                    perms,
                    run_idx,
                    k=depth
                ),
            n=5,
            num_runs=10
        )