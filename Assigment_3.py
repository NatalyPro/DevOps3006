# 1,2

try:
    a = 1/0
except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("enter a legal number")
except Exception as e:
    print("something went wrong")
    print(e.args)


# 7,8,9,10

def open_file(names_file):
    my_file = open(names_file, "a")
    return my_file


def write_name(my_file, name):
    my_file.write(name)


write_name(open_file("words.txt"), "Nata")
