def binary_search(string_list, n):
    ls = sorted(string_list)
    left = 0
    right = len(string_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if n == ls[mid]:
            return mid

        if n > ls[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    str_list = ["hello", "my", "name", "is", "Bhavana"]
    word = "name"

    output = binary_search(str_list, word)
    if output == -1:
        print("searched word is not available in list")
    else:
        print(word)
