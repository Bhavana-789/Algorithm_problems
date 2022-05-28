def anagram(s1, s2):
    """
     function for checking anagram algorithm
    :param s1: first string
    :param s2: second string
    :return: anagram detectiom
    """
    count = 0
    count1 = 0
    if len(s1) == len(s2):
        for i in s1:
            for j in s2:
                if i == j:
                    count += 1
                    if count == len(s1):  # when every letter in str1 is found in str2 then count matches length
                        return "Two strings are anagrams of each other"
                else:  # handle the cases where lengths are same but chars are diff
                    count1 += 1
                    if count1 == len(s1) * len(s2):# when count1 becomes total no of iterations
                        return "not anagram but lengths are same"
                    elif count1 > 0 and count > 0:  # handle case where lengths are same and some chars are same
                        return "not anagram,lengths and some characters are same"
    else:
        return "two strings are not anagram of each other as lengths are different"


if __name__ == "__main__":
    string1 = input("Enter string 1")
    string2 = input("Enter string 2")

    print(anagram(string1, string2))
