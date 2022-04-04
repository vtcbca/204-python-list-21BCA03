#WAS to enter any word and check it is palindrome or not.
a=input("enter any word:")
c=a
c=a[: : -1]
if(c==a):
    print("{} is pallingdrom".format(a))
else:
    print(" {} is not pallingdrom".format(a))
