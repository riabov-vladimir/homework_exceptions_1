documents = [
	{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
	{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
	{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
	'1': ['2207 876234', '11-2', '5455 028765'],
	'2': ['10006'],
	'3': []
}


def main():
	while True:
		user_input = input('Введите команду: ').lower()
		if user_input == 'p':
			person(documents)
		elif user_input == 's':
			shelf()
		elif user_input == 'l':
			documents_list(documents)
		elif user_input == 'a':
			add_document(documents, directories)
		elif user_input == 'q':
			goodbye()
			break


def person(data_base):
	'''
	p – people – команда, которая спросит номер документа
	 и выведет имя человека, которому он принадлежит
	'''
	user_input = input('Номер документа: ')
	for client in data_base:
		if client['number'] == user_input:
			print(client['name'], '\n')


def shelf():
	'''
	s – shelf – команда, которая спросит номер документа
	и выведет номер полки, на которой он находится;
	'''
	user_input_number = input('Номер документа: ')

	for shelf, doc in directories.items():
		while user_input_number not in doc:
			user_input_number = input('Документа с таким номером не существует!\nНомер документа: ')
		if user_input_number in doc:
			print(f'Документа находится на полке №{shelf} \n')
		break


def documents_list(documents):
	'''
	l– list – команда, которая выведет список всех документов
	 в формате passport "2207 876234" "Василий Гупкин";
	'''
	print()
	for client in documents:
		print(
			f'{client["type"]} "{client["number"]}" "{client["name"]}"')
	print()


def add_document(documents, directories):
	'''
	a – add – команда, которая добавит новый документ
	в каталог и в перечень полок, спросив его номер,
	тип, имя владельца и номер полки, на котором
	он будет храниться. Корректно обработайте ситуацию,
	когда пользователь будет пытаться добавить документ
	на несуществующую полку.
	'''
	user_input_type = input('Тип документа: ')
	user_input_number = input('Номер документа: ')
	user_input_name = input('Имя и Фамилия: ')

	new_client = {"type": user_input_type,
	              "number": user_input_number, "name": user_input_name}

	documents.append(new_client)

	user_input_shelf = input('Номер полки: ')

	while user_input_shelf not in directories.keys():
		user_input_shelf = input('Полки с таким номером не существует! \nВведите номер полки: ')

	directories[user_input_shelf].append(user_input_number)

	print('Документ добавлен!')


def goodbye():
	print('До свидания!')


main()