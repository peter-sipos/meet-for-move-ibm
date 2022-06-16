from .serializers import TaskSerializer
from .models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
def getData(request):
    vololo = {"name":"vololo"}
    return Response(vololo)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

    # tmp = {"meh": "lol"}
    # return Response(tmp)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)