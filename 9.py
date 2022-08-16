def print_hello(name):
    if name != "michael":
        print(f"hello {name}")


def greet_name(name, excluded_name, greeting_word):
    if name != excluded_name:
        return f"hello {name}{excluded_name}{greeting_word}"


def multiply(x, y, c):
    result = x * y + c
    result2 = x / y
    return result, result2


greet_name("moshe", "michael", "bonjour")
bla = multiply(10, 4, 3)
print(bla[0])
print(bla[1])

user_name = input("enter your name: ")
print(greet_name(user_name, "", ""))
