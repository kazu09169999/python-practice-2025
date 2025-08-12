def is_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# 関数を呼び出す
number = int(input("enter any numbers: "))
is_even_or_odd(number)