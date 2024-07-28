def similarPairs(words:str) -> int:
    ans = 0
    for i in range(len(words)):
        check = set(words[i])
        for j in range(i+1,len(words)):
            if check == set(words[j]):
                ans += 1
    
    return ans