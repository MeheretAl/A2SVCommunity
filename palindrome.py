def isPalindrome(x:int)->bool:
    check = 0
    temp = x
    if temp < 0:
        return False
    while temp > 0:
        digit = temp%10
        check = check*10 + digit
        temp = temp//10
    return check == x
