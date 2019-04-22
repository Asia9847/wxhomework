
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app import tools

@api_view(['GET', 'POST'])
def message(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        print('get')
        return Response('get')

    elif request.method == 'POST':
        print(request.data.get('message'))
        tools.sendMsg(request.data.get('message'))
        return Response(request.data)
