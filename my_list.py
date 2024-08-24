# to create my list file
my_list=[]
# insert elements 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# inserting 15 as the middle positon 
my_list.insert(1,15)
# extending my list in another list 
my_list.extend([50,60,70])
#removing some element in my list 
my_list.pop()
#sorting my list in ascending order 
my_list.sort()
# finding value 
index_of_30 = my_list.index(30)
print(index_of_30)