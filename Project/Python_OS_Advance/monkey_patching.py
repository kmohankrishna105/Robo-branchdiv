#dynamic modifications of a class or module
#
#Purpose:
# if developer wants to modify a third party of private code.But does not want to keep a copy of the code.
#in simple terms, we want to write something on top of existing code but not modify the code


class baseClass:
    def __init__(self,age):
        self.age=age

    def method1(self):
        print(" Hi this is your age :{}".format(self.age))

def monkey_patch(age):
    print("Monkey patch updated as age is greater than 100...{}".format(age))


def age_confirmation(age):
    if age>=100:
        c = baseClass(age)
        c.method1 = monkey_patch
        c.method1(age)
    else:
        b = baseClass(age)
        b.method1()


b=baseClass(11)
b.method1()

c=baseClass(11)
c.method1=monkey_patch
c.method1(12)



age_confirmation(100)
age_confirmation(101)