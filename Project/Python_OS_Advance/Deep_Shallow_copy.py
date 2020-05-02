list1=[1,2,3,4,5,6]
list2=list1

print(list1)
#Amendment done

list1[1]=11

print(list1)
print(id(list1))
print(list2)
print(id(list2))

#ID is like address reference
print(help(id))

#=========================
"""
copy.copy---shallow  [CHANGE THE ORIGINAL COPY
copy.deepcopy()----deep copy [[DO NOT CHANGES THE ORDINAL COPY EVERY TimeoutError
"""

#Shallow Copy
import copy
org_list=[[1,2,3],[4,5,6],[7,8,9]]
new_list=copy.copy(org_list)

new_list[0][1]=8

print(org_list)
print(new_list)
#=================================


#Deep Copy

org_list1=[[1,2,3],[4,5,6],[7,8,9]]
new_list1=copy.deepcopy(org_list1)

new_list1[0][2]=5

print(org_list1)
print(new_list1)

