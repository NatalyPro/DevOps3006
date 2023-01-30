#a = 4
#print(a < 4)
#if a < 4:
#  print("a is small")
#  print("jjjj")
#else:
# print("a is big")

def prirnt(number):
    numbebrs = ['one', 'two']
    if number <= len(numbebrs):
        return numbebrs[number -1]
    else:
        return 'not supported'


print(prirnt(1))

