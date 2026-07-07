# beam_search.py
import random
from common import run_benchmark, get_overlap, RANDOM_SEED

def solve_beam_search(n, perms, run_idx, beam_width=3):
    random.seed(RANDOM_SEED)
    start_node = perms[0]
    beams = [(list(start_node), start_node, list(perms[1:]))]

    for _ in range(len(perms) - 1):
        new_candidates = []
        for seq, curr, unvisited in beams:
            for nxt in unvisited:
                ov = get_overlap(curr, nxt)
                new_seq = seq + list(nxt[ov:])
                new_unvisited = [x for x in unvisited if x != nxt]
                new_candidates.append((len(new_seq), new_seq, nxt, new_unvisited))

        new_candidates.sort(key=lambda x: (x[0], x[1]))
        beams = [(item[1], item[2], item[3]) for item in new_candidates[:beam_width]]

    return beams[0][0]

if __name__ == "__main__":
    run_benchmark(
        "Greedy Beam Search B=3",
        lambda n, perms, run_idx: solve_beam_search(n, perms, run_idx, beam_width=3),
        n=5,
        num_runs=100
    )
