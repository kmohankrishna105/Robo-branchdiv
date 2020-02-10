
"""
Given a list of dictionaries.We have an input list

Verify if any value from the list is present in the listed disctionary and
retrieve the position of the value

"""


boIdentityInfoList = [{'ns2:identificationType':'PASSPOR','ns2:identificationValue':'663976709'},
                          {'ns2:identificationType':'MILITAY','ns2:identificationValue':'663976708'},
                          {'ns2:identificationType':'PASSPORT','ns2:identificationValue':'663976707'}]

id_check=['DRIVER LICENSE','MILITARY','PASSPORT','GOVERNMENT ID']


def find_position(id_check):
    for pos, dic in enumerate(boIdentityInfoList):
        if dic['ns2:identificationType'] in id_check:
            return pos
    return -99

for pos, dic in enumerate(boIdentityInfoList):
    print(pos,dic)

correct_position=find_position(id_check)
print(boIdentityInfoList[correct_position]['ns2:identificationValue'])


"""
identify line length and break into multiple lines in accordance to requirement

"""

g="For ex. let’s say we have commits like below, the merge will result as a combination of commits, whereas rebase will add all the changes in feature branch starting from the last commit of the master branch:"

#l1 belongs to flat file
def line_process(l1):
    if len(l1)>60:
        line1=l1[:60]
        line2=l1[61:]
    else:
        line1=l1
        line2=""
    return line1.strip(),line2.strip()

line1,line2=line_process(g)
print(line1)
print(line2)