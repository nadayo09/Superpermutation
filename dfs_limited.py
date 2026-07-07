# dfs_limited.py

import time
from common import run_benchmark, get_overlap


def solve_dfs_limited(
    n,
    perms,
    run_idx,
    timeout_seconds=0.1,
    max_nodes=100000
):

    start_node = perms[0]

    remaining = list(perms[1:])

    start_time = time.perf_counter()

    best_seq = [None]

    min_len = [float("inf")]

    node_counter = [0]



    def dfs(curr, current_seq, remaining_nodes):

        # timeout check
        if time.perf_counter() - start_time > timeout_seconds:
            return


        # node limit check
        if node_counter[0] >= max_nodes:
            return



        # complete solution
        if not remaining_nodes:

            if len(current_seq) < min_len[0]:

                min_len[0] = len(current_seq)

                best_seq[0] = current_seq

            return



        # pruning
        if len(current_seq) >= min_len[0]:

            return



        node_counter[0] += 1



        # greedy ordering + deterministic tie break
        candidates = sorted(
            remaining_nodes,
            key=lambda x: (
                -get_overlap(curr, x),
                x
            )
        )



        for cand in candidates:

            overlap = get_overlap(curr, cand)


            next_sequence = (
                current_seq +
                cand[overlap:]
            )


            next_remaining = [
                x for x in remaining_nodes
                if x != cand
            ]


            dfs(
                cand,
                next_sequence,
                next_remaining
            )


            if time.perf_counter() - start_time > timeout_seconds:
                return


            if node_counter[0] >= max_nodes:
                return



    dfs(
        start_node,
        start_node,
        remaining
    )


    return best_seq[0] if best_seq[0] else "Timeout"



if __name__ == "__main__":

    run_benchmark(
        "Greedy Depth-Limited DFS",
        solve_dfs_limited,
        n=5,
        num_runs=100
    )