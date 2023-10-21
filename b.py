# 打印a01b01到a99b99
for num in [str(i).rjust(2, "0") for i in range(1,100)]:
    print(f"a{num}b{num}")