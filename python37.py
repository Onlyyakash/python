# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line, type(line))
#         break
f = open('myfile.txt', 'r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"marks of student {i} in chemistry is: {m1}")
    print(f"marks of student {i} in physics is: {m2}")
    print(f"marks of student {i} in maths is: {m3}")
    print(line) 