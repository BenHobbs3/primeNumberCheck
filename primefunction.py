number = int(input())

i = 2

while i < number // 2:
    answer = number % i
    if answer == 0:
        print(number, " is not prime")
        exit()
    i += 1

print(number, "is prime")
