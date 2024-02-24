li = [1, 2, "yogee", 4]
n = len(li)
print(n)
print("*******")
for i in range(n):
    if li[i] == "yogee":
        li[i] = "yogi"
    print(li[i])
