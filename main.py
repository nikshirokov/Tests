# Задание «Голосование»
import requests

from config import token


def vote(votes):
    max = 0
    num = -1
    for x in votes:
        if votes.count(x) > max:
            max = votes.count(x)
            num = x
    return num


# Задание «Секретарь»
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    for doc in documents:
        if doc_number == doc['number']:
            return doc['name']
    return 'Документ не найден'


def get_directory(doc_number):
    for key, item in directories.items():
        if doc_number in item:
            return key
    return 'Полки с таким документом не найдено'


def add(document_type, number, name, shelf_number):
    documents.append({"type": document_type, "number": number, "name": name})
    directories[shelf_number] = number


# Задание «Квадратное уравнение»
def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b ** 2 - 4 * a * c


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant(a, b, c) < 0:
        return 'корней нет'
    elif discriminant(a, b, c) == 0:
        x = -b / (2 * a)
        return x
    else:
        x_1 = (-b + discriminant(a, b, c) ** 0.5) / 2 * a
        x_2 = (-b - discriminant(a, b, c) ** 0.5) / 2 * a
        return x_1, x_2


headers = {'Authorization': f'OAuth {token}'}


def create_folder(path, folder_name):
    url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {
        path: folder_name
    }
    response = requests.put(url_create_folder, headers=headers, params=params)
    return response.status_code
