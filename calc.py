#simple div
str_input = input("a: ")

delimoe = int(str_input)
#print(type(delimoe))

operation = input("+ / * - ^: ")

str_input2 = input("b: ")

delitel = int(str_input2)
#print(type(delitel))

result = None

if operation == '/':
 result = delimoe / delitel
elif operation == '+':
 result = delimoe + delitel
elif operation == '-':
 result = delimoe - delitel
elif operation == '*':
 result = delimoe * delitel
elif operation == '^':
 result = delimoe ** delitel
else:
 result = "unknown"
#print(type(result))

print("Result: " + str(result))
