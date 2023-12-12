import grpc
import reddit_pb2
import reddit_pb2_grpc
from concurrent import futures
import unittest
from server import RedditOverAllService

class TestRedditOverAllService(unittest.TestCase):
    def setUp(self):
        port = "50051"
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        reddit_pb2_grpc.add_RedditServicer_to_server(RedditOverAllService(), self.server)
        self.server.add_insecure_port("[::]:" + port)
        self.server.start()
    def testCreatePost(self):
        channel = grpc.insecure_channel("localhost:50051")
        stub = reddit_pb2_grpc.RedditStub(channel)
        new_post = reddit_pb2.Post(
            postID="30000",
            title="Test Title",
            text= "Test post text",
            mediaUrl="http://testing.com",
            score= "1",
            state="Normal",
            publicationDate="12/11/23",
            author=reddit_pb2.User(userID="333")
        )
        response = stub.CreatePost(new_post)
        self.assertTrue(len(response.postID) != 0)
           
    def testUpVote(self):
       channel = grpc.insecure_channel("localhost:50051")
       stub = reddit_pb2_grpc.RedditStub(channel)
       post = reddit_pb2.Post(
            postID="30000",
            title="Test Title",
            text= "Test post text",
            mediaUrl="http://testing.com",
            score= "1",
            state="Normal",
            publicationDate="12/11/23",
            author=reddit_pb2.User(userID="333")
        )
    #    post.upVote += 1
       response = stub.UpVote(post)
       self.assertTrue(response.upVote == 1)
    def testUpVoteComment(self):
       channel = grpc.insecure_channel("localhost:50051")
       stub = reddit_pb2_grpc.RedditStub(channel)
       comment = reddit_pb2.Comment(
            commentID="30000",
           author= self.service.User(userID= "1"),
           score= "33",
           state= "Normal",
            publicationDate="12/12/22"
        )
       response = stub.UpVoteComment(comment)
       self.assertTrue(response.upVote == 1)
    def testDownVoteComment(self):
       channel = grpc.insecure_channel("localhost:50051")
       stub = reddit_pb2_grpc.RedditStub(channel)
       comment = reddit_pb2.Comment(
            commentID="30000",
           author= self.service.User(userID= "1"),
           score= "33",
           state= "Normal",
            publicationDate="12/12/22"
        )
       response = stub.DownVoteComment(comment)
       self.assertTrue(response.downVote == 1)
    def testDownVote(self):
       channel = grpc.insecure_channel("localhost:50051")
       stub = reddit_pb2_grpc.RedditStub(channel)
       post = reddit_pb2.Post(
            postID="30000",
            title="Test Title",
            text= "Test post text",
            mediaUrl="http://testing.com",
            score= "1",
            state="Normal",
            publicationDate="12/11/23",
            author=reddit_pb2.User(userID="333")
        )
       response = stub.DownVote(post)
       self.assertTrue(response.downVote == 1)

    def testCreateComment(self):
       channel = grpc.insecure_channel("localhost:50051")
       stub = reddit_pb2_grpc.RedditStub(channel)
       new_comment = reddit_pb2.Comment(
            commentID="30000",
           author= self.service.User(userID= "1"),
           score= "33",
           state= "Normal",
            publicationDate="12/12/22"
        )
       response = stub.CreateComment(new_comment)
       self.assertTrue(len(response.commentID) != 0)