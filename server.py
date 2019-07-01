import grpc, time
import todo_pb2
import todo_pb2_grpc
from concurrent import futures

myList = todo_pb2.todos()

myList.todos.append(todo_pb2.todo(id=1, value="one"))


# myList = (todo_pb2.todo(id=1, value='one'))


def serve():
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_apiServicer_to_server(TodoService(), grpc_server)
    grpc_server.add_insecure_port('[::]:8081')
    grpc_server.start()
    while True:
        time.sleep(860000)


class TodoService(todo_pb2_grpc.apiServicer):

    def addTodo(self, request, context):
        l = len(myList.todos)+1
        myList.todos.append(todo_pb2.todo(id= l,value =request.todoValue))
        return myList.todos[l-1]

    def getTodo(self, request, context):
        for t in myList.todos:
            if t.value == request.todoValue:
                return t
        return 'Invalid'

    def getAll(self, request, context):
        return myList

    def delTodo(self, request, context):
        for t in myList.todos:
            if t.value == request.todoValue:
                myList.todos.remove(t)
                return t
        return 'Invalid'
if __name__ == '__main__':
    serve()
