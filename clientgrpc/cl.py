import grpc
import similarity_pb2
import similarity_pb2_grpc

# request = similarity_pb2.Get

# with grpc.insecure_channel('localhost:50051') as channel:
#     stub = similarity_pb2_grpc.SimilaritySearchServiceStub(channel)
#     for user in stub.GetSearchResults(similarity_pb2.DESCRIPTOR()):
#         print(user, end='')

request = similarity_pb2.GetSearchResultsRequest(search_id="your_search_id")

with grpc.insecure_channel('localhost:8000') as channel:
    stub = similarity_pb2_grpc.SimilaritySearchServiceStub(channel)
    response = stub.GetSearchResults(request)
    for result in response.results:
        print(result)