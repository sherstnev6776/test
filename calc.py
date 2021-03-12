#simple div

str_command = input("Please type command a + b or a - b: ")

signFirst = ''
str_A = ''

signSecond = ''
str_B = ''

operation = ''
i=0
while i < len(str_command):
      print (str_command [i])
      if str_command [i] == '+' or str_command [i] == '-' or str_command [i] == '*' or str_command [i] == '/' or str_command [i] == '^':
             if str_A == '':
                    signFirst = str_command [i]
             elif operation != '':
                    signSecond = str_command [i]
    else:
        if operation == '':
            str_A = str_A + str_command [i]
        else:
            str_B = str_B + str_command [i]
    i += 1 #i=i+1
    pass
    
str_A = signFirst + str_A.strip()
str_B = signSecond + str_B.strip()
print(str_A)
print(str_B)
    
    
#str_input = input("A: ")

delimoe = float(str_A)
#print(type(delimoe))

#operation = input("+ / * - ^ : ")

#str_input2 = input("B: ")
delitel = float(str_B)
#print(type(delitel))
result = None

if operation == '/':
    if delitel == 0:
        result = 'inf'
    else:
        result = delimoe / delitel
#print(type(result))
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
