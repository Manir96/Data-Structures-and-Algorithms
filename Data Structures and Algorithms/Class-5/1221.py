def balancedStringSplit(s):
        RL_count = 0
        L_count = 0
        R_count = 0
        for ch in s:
            if ch == "L":
                L_count += 1
            else:
                R_count += 1
            if L_count == R_count:
                RL_count += 1
        return RL_count
s = "LLRLRLRRRLL"
result = balancedStringSplit(s)
print("The result is:", result)
