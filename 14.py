import ast
my_file = open("config.json")
a = "{'name':'aviel'}"
configuration = dict(ast.literal_eval(my_file.read()))
if configuration["name"] == "avile":
    print("bla")


with open("names.txt") as my_file:
    for name in my_file.readlines():
        print(name.strip())