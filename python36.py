# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()
# f = open('myfile.txt', 'a')
# f.write('Hello World!')
# f.close()
with open('myfile.txt', 'a') as f:
    text = f.write('Hey I am inside with')