operand_1 = input('Операнд 1: ')
operand_2 = input('Операнд 2: ')

try:
    print(operand_1 + operand_2
except SyntaxError as e:
	print('Error 1:', e)

try:
    print(int(operand_1) - operand_2)
except TypeError as e:
	print('Error 2:', e)

try:
    print(operand_1 * operand_2)
except SyntaxError as e:
	print('Error 3:', e)

try:
    print(int(operand_1) / 0)
except ZeroDivisionError as e:
	print('Error 4:', e)