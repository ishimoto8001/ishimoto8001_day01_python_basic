n = int(input())

x = 800 * n     # 払った金額

# レストランからもらう金額
y = 0
if n >= 15:
    y = 200 * (n//15)

# 払った金額 - レストランからもらうお金
ans = x - y
print(ans)