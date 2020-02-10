"""
Compare two files or strings and validate if both are same
Hint: Place a delimiter to validate each item of the file
"""

import unittest
fileq="hi-r-t-l"
filew="hi-r-t-99"

def compare_file_header(file1,file2):
    file1_items=fileq.split("-")
    file2_items=filew.split("-")
    pass_values=[]
    fail_values = []
    cur_count=0
    total_count=0

    for item in file1_items:
        total_count=len(item)
        if item in file2_items:
            pass_values.append(item)
            print("Passed: "+item + "  --> matching the existing field")
        else:
            print("Failed: " +item + "  --> not matching the existing field")
            fail_values.append(item)
    if not len(fail_values):
        return "{},{} headers are matching-total count :{}".format(file1, file2,total_count)
    else:
        return "{},{} headers are not matching-total count :{}".format(file1, file2,total_count)

#
print(compare_file_header(fileq,filew))

"""
verify  each item of an list and place a counter for item
example: 1 of 7,2 of 7,3 of 7.....7 of 7
"""

c_count=0
t_count=0

q=[1,2,3,4,5,6,7]
for item in q:
    t_count = len(q)
    c_count+=1
    print("{} of {}".format(c_count,t_count))
    print(item)