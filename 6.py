print(list(range(1, 2, 5)))
names = ["chanan", "tome", "zack", "aharon"]

for name in names:
    if name == "zack":
        break
    else:
        pass
    if name == "zack":
        continue
    print(name)

a = 0
while a < 5:
    print(a)
    a = a + 1
else:
    print("blabl")


for i in range(len(names)):
    names[i] = "dotan"
    print(names[i])
