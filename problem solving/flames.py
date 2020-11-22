a = input("Player 1 name : ")
a = a.lower() 
a.replace(" ", "") 
a_list = list(a) 

b = input("Player 2 name : ") 
b = b.lower() 
b.replace(" ", "") 
b_list = list(b) 

for i in range(len(a_list)):
    for j in range(len(b_list)):
        if(a_list[i]==b_list[j]):
            c=a_list[i]
            a_list.remove(c)
            b_list.remove(c)
            c=a_list+["*"]+b_list
            print(c)








#arr=['f','l','a','m','e','s']
#for i in range(c):
#    if(len(arr)==1):
#        print(arr)
#    else:
#        if(arr[i]==c):
#            arr.pop(i)
        
