if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sec = []
    maxN =  max(arr)
    
    for num in arr:
        if num != maxN:
            sec.append(num)
    
    print(max(sec))
        