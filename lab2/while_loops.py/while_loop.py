#task1
i = 1
while i < 6:
    print(i)
    i += 1
"""1
    2
    3
    4
    5
"""
#task2
i = 1
while i < 6: 
    print(i)
    if i==3:break
    i+=1
    """
    1
    2
    3
    """

    #task3
    i = 0
while i < 6:
    i+=1
    if i==3:
        continue
    print(i)
    """ 
    1
    2
    3
    4
    5
    6"""

    #task4
    i = 1
while i < 6:
    print(i)
    i+=1
else:
    print("i is no longer less tan 6")
    """
    1
    2
    3
    4
    5
    i is no longer less tan 6
    """