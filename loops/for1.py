# inclusive []
# exclusive ()
# left exclusive (] 
# right exclusive [)
# left inclusive [)
# right inclusive (]

# range function prototype -> range(start, stop, step)

# for i in range(10): # right exclusive start = 0 (implicit) step = 1
#     print(i)

# for i in range(-10): # wont work
#     print(i)

for i in range(1, 10, 1): # right exclusive
    print(i)