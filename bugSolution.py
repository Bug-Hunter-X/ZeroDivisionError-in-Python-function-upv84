def my_function(x):
    try:
        if x == 0:
            return 0
        else:
            return 1 / x
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

print(my_function(0))
print(my_function(5))