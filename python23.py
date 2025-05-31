letter = "my name is {} and im from {}"
name="akash"
place="raigarh"
print(letter.format(name,place))
# Output: my name is akash and im from raigarh
# print(letter.format(name,place).title())
# Output: My Name Is Akash And Im From Raigarh
print(f"my name is {name} and im from {place}")
# this is a f-string, which is a more modern way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}.
# f-strings are evaluated at runtime and can include any valid Python expression.
# f-strings are more readable and concise than the older string formatting methods, such as the format() method or the % operator.
# f-strings are also faster than the older methods, as they are evaluated at runtime and do not require any additional function calls.
price = 49.099999
print(f"the price is {price:.2f}")
