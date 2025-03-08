import requests
import pytest

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_task_data = {
    "title": "Nova tarefa",
    "description": "Descrição da nova tarefa"
    }

    response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
    assert response.status_code == 200 #verifica se criou a task
    response_json = response.json() 

    assert "message" in response_json #verifica se rodou a mensagem
    assert "id" in response_json #verifica se mostrou o id
    tasks.append(response_json['id'])
    
    
    #para testar, roda o servidor e depois digita no terminal
    # python -m pytest tests.py -v
    #deve rodar isso no repositório corrreto

def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    response_json = response.json()
    assert response.status_code == 200
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']

def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": False,
            "description": "Nova descrição",
            "title": "Titulo atualizado"
        }

        response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=payload)
        response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        #nova requisição a tarefa especifica

        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        response_json = response.json()    
        assert response_json['title'] == payload['title']    
        assert response_json['completed'] == payload['completed']    
        assert response_json['description'] == payload['description']    

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f'{BASE_URL}/tasks/{task_id}')
        response.status_code == 200

        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 404