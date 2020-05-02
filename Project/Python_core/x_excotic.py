import os

#current file name
print(__file__)

#Current directory name
Base=os.path.dirname(__file__)
print(Base)

#Create a new path or file
print(os.path.join(Base,"templates"))


#__dir___
class fighter:
    name='Villan'
    health=100
    game='pubg'

    def strike(self):
        self.health=self.health-1

print(dir(fighter))

#------help--------
print(help(fighter))

