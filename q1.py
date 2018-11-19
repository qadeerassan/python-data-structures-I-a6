"""
----------------------------------------------------


----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-02-28"
----------------------------------------------------
"""
from list_linked import List

l1 = List()
l2 = List()

l1.append(0)
l2.append(1)
l1.append(2)
l2.append(3)
l1.append(4)

l3, l4 = l1.split()
for i in l3:
    print(i)
for i in l4:
    print(i)