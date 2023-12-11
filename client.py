# mirrored off of the quick start example found here: https://github.com/grpc/grpc
import grpc
import reddit_pb2
import reddit_pb2_grpc

def run():
    print("Trying to run the client")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = reddit_pb2_grpc.RedditStub(channel)
        response = stub.CreatePost(
            reddit_pb2.Post(
                postID= "1",
                title= "Test Title",
                text= "Test Text for Post",
                mediaUrl= "http://google.com/media",
                score= "100",
                state= "NORMAL",
                publicationDate= "12/05/23",
                author= reddit_pb2.User(userID= "1"),
            )
    )
        print("Post client received: " + str(response))
        
        response = stub.Retrieve(
            reddit_pb2.Post(
                postID= "1"
            )
        )
        print("Post client received: " + str(response))

        response = stub.UpVote(
            reddit_pb2.Post(
                postID="1"
            )
        )
        print("Post client received: " + str(response))

        response = stub.DownVote(
            reddit_pb2.Post(
                postID="1"
            )
        )
        print("Post client received: " + str(response))
        
if __name__ == "__main__":
    run()