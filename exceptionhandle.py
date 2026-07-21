# for i in range(5):
#     if i==4:
#         break
#     print(i)
# else:
#     print("done") 



# try :
#     a=int(input("enter a number:"))
#     print(a)
# except valueError as e:
#     print(e)
# else:
#     print("done") 
#  
# 

# a=int(input("enter a number"))
# if a < 0:
#     raise ValueError("number is negative")
# else:
#     print(a)  
# 
     
l=[1,2,3,4,5,6,7,8,9,10]
try:
    print(l[10])
except IndexError as e:
    print(e)



   

