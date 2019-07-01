import grpc
import todo_pb2
import todo_pb2_grpc


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:8081')
    client = todo_pb2_grpc.apiStub(channel)
    #
    # responseone = client.getAll(todo_pb2.empty())
    # print(responseone)
    # responseaddone = client.addTodo(todo_pb2.todoValue(todoValue='two'))
    # print(responseaddone)
    # responseaddone = client.addTodo(todo_pb2.todoValue(todoValue='three'))
    # print(responseaddone)
    # responsegetone = client.getTodo(todo_pb2.id(id=2))
    # print(responsegetone)
    # responseone = client.getAll(todo_pb2.empty())
    # print(responseone)
    # try:
    #     resp = client.delTodo(todo_pb2.todoValue(todoValue='one'))
    #     print(resp)
    # except:
    #     print("Your todo doesn't have this todo yet")
    #
    # responseone = client.getAll(todo_pb2.empty())
    # print(responseone)

    while True:
        print('Enter 1 to add todo,'
              ' 2 to display all todo,'
              ' 3 to get one todo through id,'
              ' 4 to delete a todo through value')
        print()
        n = input('Enter your choice: ')
        if n == '1':
            print('Welcome to enter')
            y = input('Enter your new Task:')
            res = client.addTodo(todo_pb2.todoValue(todoValue=y))
            print(res.value)
        elif n == '2':
            print('Welcome to get all')
            res = client.getAll(todo_pb2.empty())
            for i in res.todos:
                print(i.value)
        elif n == '3':
            print('Welcome to get one')
            y = input('Enter Value')
            try:
                res = client.getTodo(todo_pb2.todoValue(todoValue=y))
                print(res.value)
            except:
                print("Your todos doesn't have this id yet")
        elif n == '4':
            print('Welcome to delete')
            y = input('Enter todo to delete')
            try:
                res = client.delTodo(todo_pb2.todoValue(todoValue=y))
                print(res.value)
            except:
                print("Your todos doesn't have this todo yet")
        else:
            print('Invalid Input, will exit..')
