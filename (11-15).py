#Exception handling: try,except,else, finally.


try:
    age = int(input("Enter your age:"))
    print("age value taken succesfully")
except:
    print("please enter a valid integer here..")
else:
    print("age value taken succesfully.")
finally:
    print("No matter what, this codes runs")