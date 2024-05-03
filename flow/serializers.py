from rest_framework import serializers

from .models import Node, Edge, ChartType

class ChartTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = ChartType
        fields = '__all__'

class NodeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Node
        fields = '__all__'

class EdgeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Edge
        fields = '__all__'