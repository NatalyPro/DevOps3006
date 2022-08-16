# A
x = 2
y = 1
if x > y:
    print("Big")
elif x < y:
    print("small")

# B
for x in range(4):
    print(x)


# C
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

# D
# will run 10 times , last value :10
count = 1
while count < 11:
    print(count)
    count = count + 1


# E
def get_variables(age, last_name, current_currency, flew_abroad, apt_number):
    return f"{current_currency, age}, {last_name}, {current_currency}, {flew_abroad}, {apt_number}"


print(get_variables(32, "P", "$", True, 4))

# F
phone_number = input("enter your phone: ")
print(f"phone number {phone_number}")


# G
def print_hello():
    print("hello")


def calculate(number1, number2):
    print(number1 + number2)


calculate(5, 3.2)


# H
def print_name(name):
    print(f"{name}")


def divide_number(number):
    result = number / 2
    print(f"result: {result}")


divide_number(4)


# I
def add_number(t, p):
    result = t + p
    return result


def receive_string(first, second):
    result = first + " " + second
    return result


print(add_number(1, 2))

print(receive_string("N", "P"))


# K
def pyramid():
    for i in range(5):
        for j in range(i + 1):
            print("# ", end="")
        print("\r")


pyramid()
