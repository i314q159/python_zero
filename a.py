import os
import concurrent.futures

cpu_count = os.cpu_count() or 4
max_workers = cpu_count * 3
commands = []


def run_cmd(cmd):
    os.system(cmd)


for i in range(1, 100):
    commands.append(f"echo a{i}b{i}")

with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    executor.map(run_cmd, commands)
