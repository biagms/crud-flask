from flask import Flask, request, jsonify
from models.task import Task


#CRUD - CREATE, READ, UPDATE AND DELETE 


'''__name__ = main'''
app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST']) #define a rota, o endpoint(que é o /tasks nesse caso) e o método de requisição
def create_task():
    global task_id_control
    data = request.get_json() #recupera o que o usuario enviou
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id}) #o jsonify retorna a mensagem em dicionário

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())
        
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET']) #int:id é um parametro de rota, int é o tipo do parametro e id é o nome do parametro
def get_task(id): #busca uma tarefa pelo id
    task = None
    for t in tasks:
        if t.id == id: #se a tarefa tiver o mesmo id do parametro, retorna ela em forma de dicionário
            return jsonify(t.to_dict())

    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404 #codigo de não encontrado

# @app.route('/user/<username>') #nessa rota, o user é o endpoint, username ´vai ser algum nome de usuário
# def show_user(username):
#     '''no Postman, cria uma nova rota, e na url põe o endpoint
#     junto com o baseUrl. depois põe o nome de usuário, nesse caso.
#     assim: {{baseUrl}}/user/bia.
#     obs: se não colocar o tipo, sempre será string. se quiser fazer conversão,
#     põe assim: @app.route('/user/<int:username>').
#     na documentação do flask tem outros tipos de rota'''
#     print(username)
#     print(type(username))
#     return username

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break 

    print(task) 

    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})



if __name__ == '__main__':
    app.run(debug=True) 
 