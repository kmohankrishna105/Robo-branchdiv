import os

#current file name
print(__file__)

#Current directory name
Base=os.path.dirname(__file__)
print(Base)

#Create a new path or file
print(os.path.join(Base,"templates"))

