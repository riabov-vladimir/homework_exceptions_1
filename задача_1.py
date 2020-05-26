def polish_notation():
	'''В данном варианте мой Польский калькулятор не останавливает программу, но возвращает сообщение об ошибке в
	следующих случаях:
	-- пользователь поставит лишние
	пробелы в любых местах
	-- первый аргумент не входит во множество функций калькулятора
	-- если аргументы 2 и 3 не являются числами (в задании сказано, что числа должны быть больше нуля,
	но калькулятор прекрасно работает с отрицательными числами, так что я решил этот момент опустить - поправьте меня
	если я не прав)
	-- если пользователь задал деление на ноль'''
	user_input = input('Введите выражение в формате [x y z], где x - оператор, а y, z - операнды \n')
	operator = user_input.strip()[0]


	assert len(user_input.split()) == 3, 'Неверное кол-во аргументов'
	assert operator in ['+', '-', '/', '*'], 'Недопустимая операция, первый аргумент должен указывать на ' \
	                                         'арифметическое действие (/, *, -, +)'


	try:
		operand_1 = int(user_input.split()[1])
	except Exception as e:
		return 'Операнд 1 не является числом'

	try:
		operand_2 = int(user_input.split()[2])
	except Exception as e:
		return 'Операнд 2 не является числом'


	if operator == '+':
		return operand_1 + operand_2
	elif operator == '-':
		return operand_1 - operand_2
	elif operator == '*':
		return operand_1 * operand_2
	elif operator == '/':
		try:
			return operand_1 / operand_2
		except ZeroDivisionError as e:
			return e

print(polish_notation())



