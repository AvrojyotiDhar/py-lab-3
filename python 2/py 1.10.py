list1=[1,1,1,2,3,2,1]
print(list1.count(1))
print(list1.count(1),(2))

list2=['a','a','a','b','b','a','c','b']
print(list2.count('b'))

list3=['cat','bat','sat','cat','cat','mat']
print(list3.count('cat'))


lst=['cat','bat','sat','cat','mat','cat','sat']
print([[1,lst.count(1)] for l in set(lst)]) 

decimalnumber=[2.01,2.00,3.67,3.28,1.68]
decimalnumber.sort()
print(decimalnumber)
