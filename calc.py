#simple div
str_input = input("Delimoe: ")

delimoe = int(str_input)
#print(type(delimoe))

operation = input("+ / * - ^: ")

str_input2 = input("Delitel: ")

delitel = int(str_input2)
#print(type(delitel))

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

#print(type(result))
print("Result: " + str(result))