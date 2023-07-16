from .models import Item
from django_grpc_framework import proto_serializers
import similarity_pb2


class ItemProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Item
        proto_class = similarity_pb2.DESCRIPTOR
        fields = '__all__'
