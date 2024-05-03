from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Node, Edge, ChartType
from .serializers import NodeSerializers, EdgeSerializers, ChartTypeSerializers

@api_view(['GET'])
def get_flow_types(request):
    if request.method == 'GET':
        types = ChartType.objects.all()
        serializer = ChartTypeSerializers(types, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_node(request, id):
    if request.method == 'GET':
        node = Node.objects.filter(id=id)
        serializer = NodeSerializers(node, many=True)
        return Response(serializer.data[0])

@api_view(['GET'])
def get_flow_type(request, id):
    if request.method == 'GET':
        type = ChartType.objects.filter(id=id)
        serializer = ChartTypeSerializers(type, many=True)
        return Response(serializer.data[0])

@api_view(['GET'])
def get_edge(request, id):
    if request.method == 'GET':
        edgg = Edge.objects.filter(id=id)
        serializer = EdgeSerializers(edgg, many=True)
        return Response(serializer.data[0])
    
@api_view(['POST'])
def insert_node(request):
    data = request.data
    serializer = NodeSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'status':'error', 'message':'追加に失敗いたしました。'})

@api_view(['POST'])
def insert_edge(request):
    data = request.data
    serializer = EdgeSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'status':'error', 'message':'追加に失敗いたしました。'})

@api_view(['PATCH'])
def update_node(request, id):
    try:
        node = Node.objects.get(id=id)
    except Node.DoesNotExist:
        return Response({
            "node":None,
            "message":{'status':'error', 'message':'そのようなノードは見つかりません。'}
        })
    if request.method == 'PATCH':
        data = request.data['data']
        serializer = NodeSerializers(node, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "node":serializer.data,
            "message":{'status':'success', 'message':'変更が完了いたしました。'}
        })
    print(serializer.errors)
    serializer = NodeSerializers(node)
    return Response({
            "node":None,
            "message":{'status':'error', 'message':'変更に失敗いたしました。'}
        })

@api_view(['PATCH'])
def update_edge(request, id):
    try:
        edge = Edge.objects.get(id=id)
    except Edge.DoesNotExist:
        return Response({
            "edge":None,
            "message":{'status':'error', 'message':'そのようなノードは見つかりません。'}
        })
    if request.method == 'PATCH':
        data = request.data['data']
        serializer = EdgeSerializers(edge, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "edge":serializer.data,
            "message":{'status':'success', 'message':'変更が完了いたしました。'}
        })
    serializer = EdgeSerializers(edge)
    return Response({
            "edge":None,
            "message":{'status':'error', 'message':'変更に失敗いたしました。'}
        })