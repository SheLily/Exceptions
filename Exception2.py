documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "paper", "number": "10000"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

from pprint import pprint

def show_doc_names(documents: list):
  for i in documents:
    try:
      print(f'Документ номер {i["number"]} имя владельца {i["name"]}')
    except KeyError:
      print(f'Документ номер {i["number"]} имя владельца не имеет')

def find_people(documents: list):
  '''
   This function requests from user a document
   number and will display the owner's name

  '''
  doc_num = input('Введите номер документа: ')
  c = 0
  for i in documents:
    if i['number'] == doc_num:
      print(i['name'])
      c += 1
  if c == 0:
    print(f'Документ с номером {doc_num} не найден')

# find_people(documents)



def find_shelf(directories: dict):
  '''
  This function requests from user a document
   number and will display the shelf number

  '''
  doc_num = input('Введите номер документа: ')
  c = 0
  for i in directories:
    if doc_num in directories[i]:
      print(i)
      c += 1
  if c == 0:
    print(f'Документ с номером {doc_num} не найден')

# find_shelf(directories)


def show_documents(documents: list):
  '''
  This function displays a list of documents

  '''
  for i in documents:
    print(f'{i["type"]} {i["number"]} {i["name"]}')

# show_documents(documents)


def add_document(documents: list, directories: dict):
  '''
  This function adds new documents to the catalog
  and to the list of shelves

  '''
  doc_type = input('Тип документа: ')
  doc_num = input('Номер документа: ')
  owner_name = input('Имя владельца: ')
  shelf_num = input('Номер полки: ')
  if shelf_num in directories:
    documents.append({'type': doc_type, 'number': doc_num, 'name': owner_name})
    directories[shelf_num].append(doc_num)
  else:
    print(f'Полки с номером {shelf_num} не существует')

# add_document(documents, directories)
# pprint(directories)
# show_documents(documents)
show_doc_names(documents)