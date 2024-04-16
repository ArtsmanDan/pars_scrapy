from pymongo import MongoClient


client = MongoClient('localhost', 27018)

# Установите соединение с сервером MongoDB

# Выберите базу данных
db = client['vacancies11042023']

# Выберите коллекцию
my_collection = db['hhru']

# Найдите все документы и проектируйте только поле "salary"
result = my_collection.find({}, {'salary': 1})

# print(result)
def format_salary(list_salaries: list):
    # Создайте список значений зарплат
    salaries = [doc['salary'] for doc in list_salaries]
    # print(len(salaries))
    for list_item in salaries:
        # убираем пробелы лишние символы
        list_item = [x.strip().replace('\xa0', '') for x in list_item]
        # print(list_item, '>>>>>', len(list_item))
        min_salary = None
        max_solary = None
        comment = None
        currency = None
        if len(list_item) > 0:
            element = 'от'
            try:
                index_min = list_item.index(element)
                min_salary = list_item[index_min + 1]
                # print(f"От: {list_item[index_min + 1]}")
            except ValueError:
                min_salary = None
                # print(f"Минимальной зарплаты нет")

            element = 'до'
            try:
                index_max = list_item.index(element)
                max_solary = list_item[index_max + 1]
                # print(f"До: {list_item[index_max + 1]}")
            except ValueError:
                max_solary = None
                # print(f"Максимальной зарплаты нет")
            comment = list_item[-1]
            currency = list_item[-3]
        #     print(comment)
        #     print(currency)
        # print('===============================================================')
        return min_salary, max_solary, comment, currency



# Создайте список значений зарплат
salaries = [doc['salary'] for doc in result]
print(len(salaries))
for list_item in salaries:
    list_item = [x.strip().replace('\xa0', '') for x in list_item]
    print(list_item, '>>>>>', len(list_item))
    min_salary = None
    max_solary = None
    comment = None
    currency = None
    if len(list_item) > 0:
        element = 'от'
        try:
            index_min = list_item.index(element)
            print(f"От: {list_item[index_min + 1]}")
        except ValueError:
            print(f"Минимальной зарплаты нет")

        element = 'до'
        try:
            index_max = list_item.index(element)
            print(f"До: {list_item[index_max + 1]}")
        except ValueError:
            print(f"Максимальной зарплаты нет")
        comment = list_item[-1]
        currency = list_item[-3]
        print(comment)
        print(currency)
    print('===============================================================')

# Выведите значения зарплат в одной строке
# print(", ".join(salaries))