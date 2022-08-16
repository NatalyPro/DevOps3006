import requests

try:
    f =int(input("enter number:"))
    r = 5 /0

except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("enter a legal number")
except Exception as e:
    print("something went wrong")
    print(e.args)