# Retrieve position of value with in same dict key list
#find position of a value in dict



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