import subprocess
import time

scripts = [
    "baseline_greedy.py",
    "lookahead.py",
    "beam_search.py",
    "random_restart.py",
    "dfs_limited.py"
]

overall = time.time()

for script in scripts:

    print("\n" + "="*70)
    print(script)
    print("="*70)

    start = time.time()

    subprocess.run(["python", script], check=True)

    end = time.time()

    print(f"{script} runtime : {(end-start):.2f} sec")

print("\n")
print("="*70)
print(f"Total runtime : {(time.time()-overall):.2f} sec")
print("="*70)