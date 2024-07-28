from collections import defaultdict
def freqAlphabets(s:str) -> str:
    freq = defaultdict()
    chr1 = 97
    for i in range(9):
        freq[str(i+1)] = chr(chr1)
        chr1+=1
    
    for i in range(10,27):
        key = str(i) + "#"
        freq[key] = chr(chr1)
        chr1 += 1
    ans = []
    i = 0
    while i < len(s):
        if i + 2 < len(s) and s[i + 2] == '#':         
            ans.append(freq[s[i:i+3]])
            i += 3
        else:
            
            ans.append(freq[s[i]])
            i += 1
    
    return "".join(ans)