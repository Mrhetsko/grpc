from django.urls import path
import similarity_pb2_grpc
from similarity.services import ItemService
from . import views


urlpatterns = [
    path('', views.index)
]


def grpc_handlers(server):
    similarity_pb2_grpc.add_SimilaritySearchServiceServicer_to_server(ItemService.as_servicer(), server)
