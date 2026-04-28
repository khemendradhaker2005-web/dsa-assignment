def reverseString(s: list[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

arr1 = ["h","e","l","l","o"]
reverseString(arr1)
print(arr1)

arr2 = ["H","a","n","n","a","h"]
reverseString(arr2)
print(arr2)