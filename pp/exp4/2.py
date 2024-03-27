str = input("enter string:\t")

str2 = ""
l = len(str)
# print(str[-1:-(l+1)])
for i in range(l-1,-1,-1):
# for i in range(l-1,-1):

    # str2+=str[-i:-(i-1)]
    print(str[i],end="")
    
# print(str2)
