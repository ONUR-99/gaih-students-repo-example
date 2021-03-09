list1 = [1,3,5,7,9] #tek sayılar 
list2 = [0,2,4,6,8] #çift sayılar

newlist1 = list1 + list2   #birleşmiş liste
print(newlist1)

newlist2 = [i * 2 for i in newlist1] #listedeki her bir verinin ikiyle çarpılması 
print(newlist2)

for i in newlist2:
    print(i,"veri tipi :", type(i)) 
    i = i + 1 
