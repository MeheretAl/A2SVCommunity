def longestCommonPrefix(strs: list[str]) -> str:
    res = ''
    prefix = strs[0]
    for i in strs:
        prefix = prefix if len(prefix) < len(i) else i
    
    for j in range(len(prefix)):
        for k in strs:
            if j  == len(k) or k[j] != prefix[j]:
                return res
        res += strs[0][j]
    return res