
class Duster:
    shape='Rectangle'
    length=20
    def color(self,color):
        return color


d1=Duster()
d2=Duster()
d3=Duster()

print(d1.shape)
print(d2.shape)
print(d3.shape)

print(d1.color('Black'))
print(d2.color('White'))
print(d3.color('Orange'))


class Bucket:
    shape='round'
    class Home_Type:
        type_dir = ['Iron']
        def type(self, metal):
            return metal
    class Office_Type:
        type_dir = {'Plastic':None}
        def type(self, metal):
            return metal

firmid='FirmID'

print(firmid)

b1=Bucket()
b2=Bucket()


print(b1.shape)
print(b2.shape)

#Error statements
#print(b1.color('Black'))


print(b1.Home_Type().type('Steel'))
print(b1.Office_Type().type_dir['Plastic'])

account=set()
account.add('Goutham')

read or write

file open()
write

2

open file= obj
write- obj
close - delete


with fil
