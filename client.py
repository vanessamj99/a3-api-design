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
                title= "Graduation 2023",
                text= "The class for December 2023 will walk in May 2024",
                mediaUrl= "http://december-grads.com",
                score= "1000",
                state= "NORMAL",
                publicationDate= "12/09/23",
                author= reddit_pb2.User(userID= "1"),
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
                postID="46"
            )
        )
        print("Post client received: " + str(response))


        response = stub.Retrieve(
            reddit_pb2.Post(
                postID= "28"
            )
        )
        print("Post client received: " + str(response))

        response = stub.CreateComment(
            reddit_pb2.Comment(
                commentID= "30",
                author= reddit_pb2.User(
                    userID= "22"
                ),
                score= "-4",
                state= "hidden",
                publicationDate="12/06/23",
                postID= "1"
                
            )
        )
        print("Post client received: " + str(response))

        response = stub.CreateComment(
            reddit_pb2.Comment(
                commentID= "10",
                author= reddit_pb2.User(
                    userID= "22"
                ),
                score= "779",
                state= "Normal",
                publicationDate="12/07/23",
                postID= "89"
            )
        )
        print("Post client received: " + str(response))

        response = stub.CreateComment(
            reddit_pb2.Comment(
                commentID= "46",
                author= reddit_pb2.User(
                    userID= "09"
                ),
                score= "40",
                state= "Normal",
                publicationDate="12/08/23",
                postID= "28"
            )
        )
        print("Post client received: " + str(response))

        response = stub.UpVoteComment(
            reddit_pb2.Comment(
                commentID= "10"
            )
        )
        print("Post client received: " + str(response))
        
        response = stub.DownVoteComment(
            reddit_pb2.Comment(
                commentID="12"
            )
        )
        print("Post client received: " + str(response))


        response = stub.RetrieveListOfNMostUpvotedComments(
            reddit_pb2.TopN(
                postID= "2",
                number = 1
            )
        )
        print("Post client received the following: ")
        for comment in response:
            print(comment)

        response = stub.ExpandCommentBranch(
            reddit_pb2.TopNComments(
                commentID = "10",
                number = 2
            )
        )
        print("Post client received the following: ")
        for comment in response:
            print(comment)

if __name__ == "__main__":
    run()