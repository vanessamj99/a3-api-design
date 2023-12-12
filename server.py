# mirrored off of the quick start example found here: https://github.com/grpc/grpc
import grpc
import reddit_pb2
import reddit_pb2_grpc
from concurrent import futures
import random

class RedditOverAllService(reddit_pb2_grpc.RedditServicer):
   def __init__(self) -> None:
       self.posts = {"2": reddit_pb2.Post(
           postID= "2",
           title= "First Post Ever",
           text="Genesis of Posts",
           mediaUrl= "http://beginning.com",
           score= "10000",
           state="Normal",
           publicationDate="10/08/21",
           comments= [
         reddit_pb2.Comment(
           commentID= "10",
           author= reddit_pb2.User(
               userID= "23"
           ),
           score= "110",
           state= "Normal",
           publicationDate= "04/01/23",
           postID= "77", 
           text= "Awesome!!!"
       )
            ],
       ),
       "28": reddit_pb2.Post(
           postID= "28",
           title= "Cloud Infrastructure",
           text="Cloud infrastructure was schedule for 7pm on Mondays and Wednesdays",
           mediaUrl= "http://cloud-link.com",
           score= "-50",
           state="Normal",
           publicationDate="11/08/23",
       ),
       "89": reddit_pb2.Post(
            postID= "89",
           title= "Responsible AI",
           text="Responsible AI was on Mondays and Wednesdays at 2pm.",
           mediaUrl= "http://responsible-ai.com",
           score= "89",
           state="Locked",
           publicationDate="12/01/23",
       ),
       "46": reddit_pb2.Post(
            postID= "46",
           title= "Data Focused Python",
           text="Data Focused Python was a remote class at 11am on Mondays and Wednesdays",
           mediaUrl= "http://data-focused-python.com",
           score= "-50",
           state="Normal",
           publicationDate="11/08/23",
           author= reddit_pb2.User(
               userID= "66"
           )
       )
       }
       self.comments = {"46": reddit_pb2.Comment(
            commentID= "46",
           score= "-50",
           state="Normal",
           publicationDate="11/08/23",
           author= reddit_pb2.User(
               userID= "32"
           ),
           postID= "89"
       ),
       "10": reddit_pb2.Comment(
           commentID= "10",
           author= reddit_pb2.User(
               userID= "23"
           ),
           score= "11",
           state= "Normal",
           publicationDate= "04/01/23",
           postID= "28", 
            replies= [
            reddit_pb2.Comment(
           commentID= "12",
           author= reddit_pb2.User(
               userID= "23"
           ),
           score= "11",
           state= "Normal",
           publicationDate= "04/01/23",
           postID= "28", 
           upVote= 20
       ),
        reddit_pb2.Comment(
           commentID= "1010",
           author= reddit_pb2.User(
               userID= "22"
           ),
           score= "198",
           state= "Hidden",
           publicationDate= "04/01/23",
           postID= "709", 
           upVote= 3
       ),
        reddit_pb2.Comment(
           commentID= "124",
           author= reddit_pb2.User(
               userID= "22"
           ),
           score= "132",
           state= "Normal",
           publicationDate= "05/06/23",
           postID= "18", 
           upVote= 1
       ),
        reddit_pb2.Comment(
           commentID= "910",
           author= reddit_pb2.User(
               userID= "05"
           ),
           score= "121",
           state= "Normal",
           publicationDate= "01/03/23",
           postID= "67", 
           upVote= 9
       )
           ]
       ),
       "76": reddit_pb2.Comment(
           commentID= "76",
           author= reddit_pb2.User(
               userID= "99"
           ),
           score= "44",
           state= "Normal",
           publicationDate= "04/01/23",
           postID= "46", 
       )
       }
   def CreatePost(self, request, context):
       random_number = random.randint(0,1)
       if random_number == 1:
           new_post = reddit_pb2.Post(
            postID= request.postID,
            title= request.title,
            text= request.text,
            mediaUrl= request.mediaUrl,
            score= request.score,
            state= request.state,
            publicationDate=request.publicationDate,
            author= request.author,
            comments= [
         reddit_pb2.Comment(
           commentID= "10",
           author= reddit_pb2.User(
               userID= "23"
           ),
           score= "11",
           state= "Normal",
           publicationDate= "04/01/23",
           postID= "28", 
           text= "Great work!"
       )
            ],
           )
           self.posts[new_post.postID] = new_post
           return reddit_pb2.Post(
            postID= request.postID,
            title= request.title,
            text= request.text,
            mediaUrl= request.mediaUrl,
            score= request.score,
            state= request.state,
            publicationDate=request.publicationDate,
            author= request.author,
            post_created_message = "Post was created",
            comments= [
         reddit_pb2.Comment(
           commentID= "10",
           author= reddit_pb2.User(
               userID= "23"
           ),
           score= "11",
           state= "Normal",
           publicationDate= "04/01/23",
           postID= "28", 
           text= "Great work!"
       )
            ],
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
       self.posts[request.postID] = request.upVote + 1
       return request
   def UpVoteComment(self,request,context):
    #    request.upVote += 1
       self.posts[request.commentID] = request.upVote + 1
       return request
   def DownVoteComment(self,request,context):
    #    request.downVote += 1
       self.comments[request.commentID] = request.downVote + 1
       return request
   def DownVote(self, request, context):
    #    request.downVote += 1
       self.comments[request.postID] = request.downVote + 1
       return request
   def Retrieve(self, request, context):
       if request.postID in self.posts.keys():
           #print("Post found")
           return self.posts[request.postID]
       else:
           return reddit_pb2.Post(
               text= "A post with that id does not exist"
           )
   def CreateComment(self, request, context):
       request.was_created = True
       self.comments[request.commentID] = request
       return request
   def RetrieveListOfNMostUpvotedComments(self, request, context):
       if len(self.posts[request.postID].comments) == 0:
           return []
       sorted_comments = sorted(self.posts[request.postID].comments, key=lambda comment: comment.upVote, reverse=True)
       for comment in sorted_comments:
           yield comment
   def ExpandCommentBranch(self, request, context):
       print(self.comments)
       if len(self.comments[request.commentID].replies) == 0:
           return []
       sorted_comments = sorted(self.comments[request.commentID].replies, key=lambda comment: comment.upVote, reverse=True)
       for comment in sorted_comments:
           yield comment


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