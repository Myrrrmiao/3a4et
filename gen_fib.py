def fibonacci(n):
    first_num, second_num = 0, 1
    for _ in range(n):
        yield first_num
        first_num, second_num = second_num, first_num + second_num

for num in fibonacci(6):
    print(num)
