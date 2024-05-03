from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee, EmployeeChart
from .serializers import EmployeeSerializers, EmployeeChartSerializers

@api_view(['GET'])
def get_active_user(request):
    if request.method == 'GET':
        user = Employee.objects.filter(gmail='Admin@dev.com')
        if len(user) == 1:
            active_user = user[0]
            message = {
                "status":"info",
                "message": "おかえりなさい、{}さん".format(active_user.name)
            }
            serializer = EmployeeSerializers(user, many=True).data[0]
        else:
            message = {
                "status":"error",
                "message": "ユーザ認証できませんでした。"
            }
            serializer = {
                "name": "unknown",
                "authority": 0
            }
        return Response({
            "user":serializer,
            "message": message
        })

@api_view(['GET'])
def get_active_flowchart(request, id):
    if request.method == 'GET':
        flows = EmployeeChart.objects.filter(user_id=id)
        serializer = EmployeeChartSerializers(flows, many=True)
        return Response(serializer.data)
    
@api_view(['PATCH'])
def update_active_flowchart(request, id):
    try:
        flow = EmployeeChart.objects.get(id=id)
    except EmployeeChart.DoesNotExist:
        return Response({
            "flow_content":None,
            "message":{'status':'error', 'message':'そのようなチャートは見つかりません。'}
        })
    if request.method == 'PATCH':
        data = request.data['data']
        serializer = EmployeeChartSerializers(flow, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "flow_content":serializer.data,
            "message":{'status':'success', 'message':'変更が完了いたしました。'}
        })
    serializer = EmployeeChartSerializers(flow)
    return Response({
            "flow_content":None,
            "message":{'status':'error', 'message':'変更に失敗いたしました。'}
        })

@api_view(['POST'])
def insert_edge(request):
    data = request.data
    serializer = EmployeeChartSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":{'status':'success', 'message':'追加が完了いたしました。'},
            "flow_content":serializer.data
        })
    print(serializer.errors)
    return Response({"message":{'status':'error', 'message':'追加に失敗いたしました。'}})