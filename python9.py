# strings are immutable
a="Akash!!!!!!!!!!!!!"
b="!!!Deku!!!!!!!!!"
c="zig!!!! !!zig!! !!!!!zig"
print(a)
print(len(a))
print(a.lower())
print(a.upper())
print(a.rstrip("!"))
print(b.rstrip("!"))
print(a.replace("Akash","AK"))
print(b.replace("Deku","medoriya"))
print(c.replace("zig","zag"))
print(c.split(" "))
blogHeading="introduction to js"
print(blogHeading.capitalize())
str1="welcome to the concole!!!"
print(len(str1))
print(len(str1.center(50)))
print(str1.endswith("!!!"))
print(c.count("zig"))
str2="hey this car is nice,i like your car"
print(str2.find("car"))
str3="WelcomeToTheConsole"
print(str3.isalnum())
str3="His name is Dan and he Is a Nice Man"
print(str3.swapcase())
str3="His name is Dan and he Is a Nice Man"
print(str3.casefold())