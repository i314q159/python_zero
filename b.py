# 打印a01b01到a99b99

import os
import time

axbx = [str(f"a{i}b{i}").rjust(4, "0") for i in range(1, 10000)]

t5 = time.time()
for s in axbx:
    print(f"{s}")
t6 = time.time()

t7 = time.time()
for s in axbx:
    os.system(f"echo {s}")
t8 = time.time()

print(f"for print {(t6 - t5) * 1000:.2f} ms")
print(f"for echo {(t8 - t7) * 1000:.2f} ms")
