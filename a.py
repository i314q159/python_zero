# 打印a01b01到a99b99

import os
import time
import concurrent.futures

axxbxx = [str(f"a{i}b{i}").rjust(2, "0") for i in range(1, 100)]
cpu_count = os.cpu_count() or 8
max_workers = cpu_count * 3


def run_cmd_print(cmd):
    print(cmd)


def run_cmd_echo(cmd):
    os.system(cmd)


commands_print = []
for s in axxbxx:
    commands_print.append(f"{s}")
t1 = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    executor.map(run_cmd_print, commands_print)
t2 = time.time()


commands_echo = []
for s in axxbxx:
    commands_echo.append(f"echo {s}")
t3 = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    executor.map(run_cmd_echo, commands_echo)
t4 = time.time()

t5 = time.time()
for s in axxbxx:
    print(f"{s}")
t6 = time.time()

t7 = time.time()
for s in axxbxx:
    os.system(f"echo {s}")
t8 = time.time()


print(f"thread pool print {(t2 - t1) * 1000:.2f} ms")
print(f"thread pool {(t4 - t3) * 1000:.2f} ms")
print(f"for print {(t6 - t5) * 1000:.2f} ms")
print(f"for echo {(t8 - t7) * 1000:.2f} ms")
