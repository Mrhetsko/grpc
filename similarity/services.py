from .models import Item
from django_grpc_framework import generics
from similarity.serializers import ItemProtoSerializer


class ItemService(generics.ModelService):
    """
    gRPC service that allows items to be retrieved or updated.
    """
    queryset = Item.objects.all()
    serializer_class = ItemProtoSerializer
