def interpret(command: str) -> str:
        ans = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                ans.append('G')
                i+=1
            elif command[i] == '(' and i < len(command) - 1 and command[i+1] == ')':
                ans.append('o')
                i+=2
            elif command[i] == '(' and i < len(command) - 1 and command[i+1] == 'a':
                ans.append('al')
                i+=3
            else:
                i+=1
     
        return ''.join(ans)
