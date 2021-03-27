"""
хотим калькулятор выражений -2 +3.5 * 2 - 3 ^ 2
"""
#считать строчку от пользователя
instr = input ('Pleae, enter your task: ')

#почистить строку
# "-2 +3.5 * 2 - 3 ^ 2" -> "-2+3.5*2-3^2"
instr = instr.replace(' ', '')

#распарсить
"""
на вход строку
"-2+3.5*2-3^2"
на выход ?структура данных? с операциями +- и значениями
(+*-)
(-2 3.5 2 3 2)
[{'opr: , 'val': -2}, {}, ...]
"""

hp_ops = tuple('^')
mp_ops = ('*','/')
lp_ops = tuple('+-')
supported_ops = hp_ops + mp_ops + lp_ops
digital_chars = tuple ('0123456789.-')

actions = list ()
d = dict()
d['opr']='First'
d['val']= ''
actions.append(d)
print(actions)

#премся по строчке, карент -- текущее, делим на операции и числа
#пока не понимаю, какой алгоритм с отрицательными числами

i=0
for i, letter in enumerate(instr): 
    if letter in supported_ops: 
        actions.append ({'opr': letter, 'val': ''})
    
    elif letter in digital_chars:
        actions [-1]['val'] += letter
 
print (actions)


#вычислить операции 1го приоритета (возведение в степень)
"""
на вход наш набор значений и операций
на выход обновленная ?структура данных? с операциями +- и значениями
2+3.5*2-3^2
2+3.5*2-9
"""


i = 0
while i < len(actions):
	action = actions[i]
	operation = action.get('opr')
	if operation == hp_ops[0]:
	    if operation == '^':
		pre_res = float(actions[i-1].get('val')) ** float(action.get('val'))
		actions[i+1]['val'] = str(pre_res)
		del renove[i]
	else:
		i += 1
actions.reverse()
	
   # pass



#вычислить операции 2го приоритета (умножение и деление)
"""
на вход наш набор значений и операций
на выход обновленная ?структура данных? с операциями +- и значениями
-2+3.5*2-9
2+7-9
"""
i = 0
result = None
while i < len(actions):
	action = actions[i]
	operation = action.get('opr')
	if operation in np_ops:
	    if float(action.get('val')) == 0 and operation == '/':
	     pass
	else:
		i += 1
actions.reverse()
print(actions)

#вычислить операции 3го приоритета (сложение и вычитание)
# -2+7-9 = -4

for action in actions:
    if type(result)
        break
    var_A = result
    var_B = action.get('opr')
    if operation in lp_opr:
        result = eval(val_A + operation + var_B)
    else:
        result = var_B

#вывести результат
print("Result: " + str(result))
