# 1
x = 2
y = 1
if x > y:
    print("Big")
elif x < y:
    print("small")

# 2
for x in range(4):
    print(x)


# 3
def check_variable(season):
    if season == 1:
        return f"{season} = summer"
    elif season == 2:
        return f"{season} = winter"
    elif season == 3:
        return f"{season} = fall"
    elif season == 4:
        return f"{season} = spring"
    else:
        print("number not found")


for x in range(1, 5):
    print(check_variable(x))


# 4
# will run 10 times , last value :10


# 5
def get_variables(age, last_name, current_currency, flew_abroad, apt_number):
    return f"{current_currency, age}, {last_name}, {current_currency}, {flew_abroad}, {apt_number}"


print(get_variables(32, "P", "$", True, 4))

# 6
phone_number = input("enter your phone: ")
print(f"phone number {phone_number}")


# 7
def print_hello():
    print("hello")


def calculate(number1, number2):
    print(number1 + number2)


calculate(5, 3.2)


# 8
def print_name(name):
    print(f"{name}")


def divide_number(number):
    result = number / 2
    print(f"result: {result}")


divide_number(4)


# 9
def add_number(t, p):
    return t + p


def receive_string(first, second):
    return first + " " + second


print(add_number(1, 2))

print(receive_string("N", "P"))


# 10
def pyramid():
    for i in range(5):
        for j in range(i + 1):
            print("# ", end="")
        print("\r")


pyramid()


# 11
def xshape():
    for i in range(0, 7):
        for j in range(0, 7):
            if i == j or j == 7 - 1 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


xshape()


# 12 (1)
def program():
    bla = 0
    num = select_num()
    for p in range(length(num)):
        number = int(str(num)[p])
        c = number + bla
        bla = c
        print(f"computed number {bla}")


def select_num():
    num = int(input("Enter ANY integer: "))
    print(f"selected number {num}")
    return num


def length(num):
    return len(str(num))


program()


# 12 (2)
def select_num_2():
    num = int(input("Enter an integer 11-99: "))
    print(f"selected number {num}")
    return num


def program_2():
    num = select_num_2()
    if num < 10 or num > 99:
        print(f"error. number {num} not supported")
    else:
        first = int(str(num)[0])
        second = int(str(num)[- 1])
        print(f"computed number {first + second}")
        return first + second


program_2()
