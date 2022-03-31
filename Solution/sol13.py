n=int(input("enter any no"))
i = 1
while i <= n :
      j = n
      while j >= i:
         print("*", end=" ")
         j = j - 1
      print()
      i = i + 1
