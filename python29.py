emp1 = {111:55, 121: 65, 131: 75, 141: 85}
emp2 = {212:70, 222: 90, 232: 75 }
# emp1.update(emp2)
# emp1.clear()
# emp1.pop(121)
emp1.popitem()
del emp1[111]
print(emp1)