def polish_notation():
	user_input = input('Введите выражение в формате [x y z], где x - оператор, а y, z - операнды \n')
	operator = user_input[0]

	try:
		assert operator in ['+', '-', '/', '*'], 'Недопустимая операция'
	except Exception as e:
		print('Assertion error:', e)

	operand_1 = int(user_input[2])
	operand_2 = int(user_input[4])
	if operator == '+':
		return operand_1 + operand_2
	elif operator == '-':
		return operand_1 - operand_2
	elif operator == '*':
		return operand_1 * operand_2
	elif operator == '/':
		return operand_1 / operand_2

try:
	print(polish_notation())
except Exception as e:
	print('Error:', e)