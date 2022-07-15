s = "a bcd A BCD".replace(' ','')

for c in s:
    print(ord(c)-ord('A')+1)