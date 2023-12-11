# mirrored off of the quick start example found here: https://github.com/grpc/grpc
import grpc
import reddit_pb2
import reddit_pb2_grpc
from concurrent import futures
import random

class RedditOverAllService(reddit_pb2_grpc.RedditServicer):
   def __init__(self) -> None:
       self.posts = dict()
       self.comments = dict()
   def CreatePost(self, request, context):
       random_number = random.randint(0,1)
       if random_number == 1:
           return reddit_pb2.Post(
            postID= request.postID,
            title= request.title,
            text= request.text,
            mediaUrl= request.mediaUrl,
            score= request.score,
            state= request.state,
            publicationDate=request.publicationDate,
            author= request.author,
            post_created_message = "Post was created"
        )
       else:
            return reddit_pb2.Post(
            postID= request.postID,
            title= request.title,
            text= request.text,
            mediaUrl= request.mediaUrl,
            score= request.score,
            state= request.state,
            publicationDate=request.publicationDate,
            author= request.author,
            post_created_message = "Post was not created"
        )
           
   def UpVote(self, request, context):
       print(type(request))
       return super().UpVote(request, context)
   def DownVote(self, request, context):
       return super().DownVote(request, context)
   def Retrieve(self, request, context):
       if request.postID in self.posts.keys():
           return self.posts[request.postID]
       else:
           return reddit_pb2.Post(
               text= "A post with that id does not exist"
           )
   def CreateComment(self, request, context):
       return super().CreateComment(request, context)
   def RetrieveListOfNMostUpvotedComments(self, request, context):
       return super().RetrieveListOfNMostUpvotedComments(request, context)
   def ExpandCommentBranch(self, request, context):
       return super().ExpandCommentBranch(request, context)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServicer_to_server(RedditOverAllService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    serve()