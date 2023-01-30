from flask import Flask, app

# 1

try:
    a = 1/0
except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("enter a legal number")
except Exception as e:
    print("something went wrong")
    print(e.args)

# 2 yes
# 3 all exceptions
# 4 I believe that there is nothing wrong with this exception.
# 5 input/output operation fails, dividing by zero fails
# 6,7,8
def open_file(names_file, option):
    my_file = open(names_file, option, encoding="utf-8")
    return my_file


def write_in_file(my_file, data):
    my_file.write(data)
    print(f" writing {data} to file")


def read_file(my_file):
    data = my_file.read()
    print(f" reading file data {data} from file")


write_in_file(open_file("words.txt", "w"), "Nata")
read_file(open_file("words.txt", "r"))
write_in_file(open_file("words.txt", "w"), "שלום")
read_file(open_file("words.txt", "r"))

# 9
app = Flask(__name__)


@app.route('//register')
def register():
    return write_in_file(open_file("words.txt", "w"), "flask"), 201


@app.route('//content')
def read_content():
    return read_file(open_file("words.txt", "r")), 200


if __name__ == '__main__':
       app.run(host='0.0.0.0', port=3000, debug=False)


