def prime_number():

    for num in range(1, 1000):
        reverse = int(str(num)[::-1])
        if num == reverse:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                    else:
                        print(num, "is palindromic prime number")


if __name__ == "__main__":
    print(prime_number())