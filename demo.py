num = int(input())

for i in range(0, num):
    for j in range(0, num-i-1):
        print(" ",end="")
    for j in range(0, i*2+1):
        print(chr(65+j), end="")
    print()

for i in range(1, num):
    for j in range(0, i):
        print(" ",end="")
    for j in range(0, (num-i)*2-1):
        print(chr(65+j), end="")
    print()