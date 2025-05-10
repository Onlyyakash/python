# def average(a=9,b=1):#this is a default value
#     print("the average is",(a+b)/2)
# # average(6,2)
# average(1,5)

# def name(fname,mname="john",lname="watson"):#this is a default value
#     print("hello",fname,mname,lname)
# name("golu")


def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is:",sum/len(numbers))
average(2,4,6,8)