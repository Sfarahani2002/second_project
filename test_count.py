def countm(s, a):
    count = 0 
    for i in range(len(s)):
        if s[i] == a:
            count += 1 
    return count 

print(countm("mohammad","a" ))

