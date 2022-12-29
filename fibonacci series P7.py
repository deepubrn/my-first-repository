# print fibonacci series using recursion


num = int(input("enter num for term = "))


def fibonacci_series(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return(fibonacci_series(number - 1) + fibonacci_series(number - 2))


if num <= 0:
    print("Please entered positive number ")
else:
    for i in range(num + 1):
        print(fibonacci_series(i))
