

list3 = ["192.168.10.9", "192.168.10.4", "192.168.10.11", "192.168.10.35"]
def fun1(list3):
    #print(list3)
    return list3[-2:]
list3.sort(key=fun1)
print(list3)



list1 = [1,2,3,0,2,3,0,1,24,0,1,3,1,0,1,21,0,1,2,0,45]

list1.sort(key=lambda x: (x == 0, x))
print(list1)



list1 = [(10,4),(90,3),(9,1),(10,4),(9,5)]
def fun1(x):
    a,b = x
    return a+b
list1.sort(key = fun1)
print (list1)

