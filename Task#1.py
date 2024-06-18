import requests
# Задание №1 Метод GET
BASE_URL = 'http://127.0.0.1:80/students'
def get_all_students():
    response = requests.get(BASE_URL)
    return response.json()
def get_student(student_id):
    url = f'{BASE_URL}/{student_id}'
    response = requests.get(url)
    return response.json()
all_students = get_all_students()
print('Список студентов:', all_students)
student_id = 1  
student_info = get_student(student_id)
print(f'Информация о студенте {student_id}:', student_info)
#Задание №2 Метод POST
def add_student(student_data):
    response = requests.post(BASE_URL, json=student_data)
    return response.json()
new_student = {
    "id": 4,
    "name": "Новый Студент",
    "age": 22,
    "major": "Биология"
}
response = add_student(new_student)
print(response)
#Задача №3. Метод PUT
import requests
BASE_URL = 'http://127.0.0.1:80/students'
def update_student(student_id, updated_data):
    url = f'{BASE_URL}/{student_id}'
    response = requests.put(url, json=updated_data)
    return response.json()
student_id = 4
updated_student_data = {
    "name": "Новый Студент",
    "age": 23,
    "major": "Химия"
}
response = update_student(student_id, updated_student_data)
print(response)
#Задача №4. Метод DELETE
import requests
BASE_URL = 'http://127.0.0.1:80/students'
def delete_student(student_id):
    url = f'{BASE_URL}/{student_id}'
    response = requests.delete(url)
    return response.json()
student_id = 1

response = delete_student(student_id)
print(response)
