'''from nt import *
mkdir("isha")'''
#cget method use with button to get the text
'''import random
print(random.choice(range(1,6)))'''
import re
try:
    r=re.search('abc','this is an absolute string')
    print(r.group())
except:
    print(" previous string is not found")
r=re.search('this','this is an absolute string')
print(r.group())
#r.start()-it will give u starting index position
# r.end()-give u the last index position
#print(r.span())-return first and last index position
