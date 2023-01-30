import datetime
import requests
#(terminal: pip install requests)


is_true = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
print(type(a == b))
if a < b and (b != 1 or strOne == "moshe" or not strThree == "Three"):
    print("a is smaller then b")
elif a == b:
    print("a equals b")
elif b > 1:
    print("blabla")
else:
    print("something")

names = ["chanan", "tom", "zack"]
print(type(names))

if "tom" in names:
    print()
other_list = []
name_to_find = "ariel"
if name_to_find in names:
    print(f"we found {name_to_find}")

if len(other_list) > 0:
    print("other list has values")

numbers = range(2, 10)
for a in numbers:
    print(a)

k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
if type(k) is int:
    print("I like numbers")
elif type(k) is str :
    print("I like strings")
print(k is f)
print(t == e)
print(t is e)

x = '-1'
while x != 0:
    if x != '-1':
        print("failed")
    x = input("please  enter a number")

x = '-1'
while x != 0:
    x = x + 1
    if x % 2 != 0:
        continue
    print("failed")
    x = input("please  enter a number")


if 0 == 0:
    pass
print("")


numbers = range(100)
for number in numbers:
    if number % 7 == 0 or '7' in str(number):
        print("boom!")
    elif "7" in str(number):
        print("SUPER")
    else:
        print(number)

a = 3
print(type(str(a)))


def print_hi():
    print('hi')
    print('hi again')


for i in range(50):
    print_hi()

print(datetime.datetime.now().minute)

response = requests.get("https://github.com")
print(response.status_code)


file = open('read_this.txt', 'r')
lines = file.readline()
for line in lines:
    print(line,end=' ')
    if line == lines["chanan", "tom", "zack"]:
        print("boom!")
file.write('\ndriving')

def write_name(name):
    file = open('names.txt', 'a')
    file.write('\n' + name)
    file.close()

def read_names():
    file = open('names.txt')
    for line in file.readlines():
        print(f'Welcome {line}')

write_name('doron')
write_name('dan')
write_name('moshe')
read_names()






