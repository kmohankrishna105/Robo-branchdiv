x="Hi everyone this is vandhana"
print(x[0::3])
#print(x[::-1])
#print(x[:len(x)-1])

#print(len(x))

print(x.upper())
a=x.split(" ")
print(a)

print(type(a))
print(type(x))

#mutable sequence:

a.append("new")
a.remove("is")
print(a)
print(a.pop())
print(a)

a.append(5)
print(a)

#tuples---list wich cannot be edited

#[1,2,3]- editable
#(1,2,3)- non-editable

t=(1,2,3)
print(type(t))


#key:value

q={'sit':'url1','uat':'url2',3:4}




# dictionary
#{key:value}

#nested.....list,dictionary

my_dict={'key':'value','userid':13,'password':14}
print(type(my_dict))

print(my_dict['userid'])

#parsing the dictionary
#json,xml-->

employees={'data':
               {'emp1':{'user':1,'dept':['QA','dev']},
                'emp2':{'user':2,'dept':'dev'},
                'emp3':{'user':3,'dept':'admin'}}}

#print(employees['data']['emp1']['dept'][1])

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())


g={1,2,3}
g.add(3)
print(g)

w=[1,2,3,4,5,4,3,2,1]
print(set(w))

#========================

obj=open('new_file.txt','r+')
#obj.write("Hi this is python")
print(obj.readline())
obj.seek(30)
print(obj.readlines())

r=[1,2,3,4,5,'six','seven']

for vandhana in r:
    print(vandhana)


from openpyxl import Workbook
import time

book = Workbook()
sheet = book.active

sheet['A1'] = 56
sheet['A2'] = 43

now = time.strftime("%x")
sheet['A3'] = now

book.save("sample.xlsx")