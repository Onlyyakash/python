# a = input("enter a number: ")
# print(f"multiplication table of {a} is: ")
# try:
#    for i in range(1, 11):
#      print(f"{int(a)} * {i} = {int(a) * i}")
# except :
#       print("invalid")
# print("done")
# print("yahoo")

try:
    num = (int(input("enter a number: ")))
except ValueError:
    print("number entered is not a integer")