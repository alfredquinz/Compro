setA = {1,2,3,4}
setb = ({8,9,10})

setA.add(5)
setb.update([6,7])
Uset = setA | setb
print(Uset)
print(len(Uset))

setb.update('ABCD')
setA.update([6,7,8])

print(setA.intersection(setb))  
print(setA ^ setb)

setb.remove(8)
setb.discard(10)
print(setb)
print(setA.clear()) 
for val in Uset:
    print(val)