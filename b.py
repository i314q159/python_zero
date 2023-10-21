# 打印a01b01到a99b99

import os
import time

axxbxx = [str(f"a{i}b{i}").rjust(2, "0") for i in range(1, 100)]

t5 = time.time()
for s in axxbxx:
    print(f"{s}")
t6 = time.time()

t7 = time.time()
for s in axxbxx:
    os.system(f"echo {s}")
t8 = time.time()

print(f"for print {(t6 - t5) * 1000:.2f} ms")
print(f"for echo {(t8 - t7) * 1000:.2f} ms")
