# 打印a01b01到a99b99

import os
import concurrent.futures

cpu_count = os.cpu_count() or 4
max_workers = cpu_count * 3
commands = []


def run_cmd(cmd):
    os.system(cmd)


for s in [str(i).rjust(2, "0") for i in range(1, 100)]:
    commands.append(f"echo a{s}b{s}")

with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    executor.map(run_cmd, commands)
