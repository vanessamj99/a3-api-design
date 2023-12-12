from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["userID"]
    USERID_FIELD_NUMBER: _ClassVar[int]
    userID: str
    def __init__(self, userID: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ["postID", "title", "text", "mediaUrl", "score", "state", "publicationDate", "author", "post_created_message", "upVote", "downVote", "comments"]
    POSTID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MEDIAURL_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATIONDATE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    POST_CREATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPVOTE_FIELD_NUMBER: _ClassVar[int]
    DOWNVOTE_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    postID: str
    title: str
    text: str
    mediaUrl: str
    score: str
    state: str
    publicationDate: str
    author: User
    post_created_message: str
    upVote: int
    downVote: int
    comments: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, postID: _Optional[str] = ..., title: _Optional[str] = ..., text: _Optional[str] = ..., mediaUrl: _Optional[str] = ..., score: _Optional[str] = ..., state: _Optional[str] = ..., publicationDate: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., post_created_message: _Optional[str] = ..., upVote: _Optional[int] = ..., downVote: _Optional[int] = ..., comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ["commentID", "author", "score", "state", "publicationDate", "upVote", "downVote", "has_replies", "replies", "postID", "was_created", "text"]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATIONDATE_FIELD_NUMBER: _ClassVar[int]
    UPVOTE_FIELD_NUMBER: _ClassVar[int]
    DOWNVOTE_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLIES_FIELD_NUMBER: _ClassVar[int]
    REPLIES_FIELD_NUMBER: _ClassVar[int]
    POSTID_FIELD_NUMBER: _ClassVar[int]
    WAS_CREATED_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    commentID: str
    author: User
    score: str
    state: str
    publicationDate: str
    upVote: int
    downVote: int
    has_replies: str
    replies: _containers.RepeatedCompositeFieldContainer[Comment]
    postID: str
    was_created: bool
    text: str
    def __init__(self, commentID: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[str] = ..., state: _Optional[str] = ..., publicationDate: _Optional[str] = ..., upVote: _Optional[int] = ..., downVote: _Optional[int] = ..., has_replies: _Optional[str] = ..., replies: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ..., postID: _Optional[str] = ..., was_created: bool = ..., text: _Optional[str] = ...) -> None: ...

class TopN(_message.Message):
    __slots__ = ["postID", "number"]
    POSTID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    postID: str
    number: int
    def __init__(self, postID: _Optional[str] = ..., number: _Optional[int] = ...) -> None: ...

class TopNComments(_message.Message):
    __slots__ = ["commentID", "number"]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    commentID: str
    number: int
    def __init__(self, commentID: _Optional[str] = ..., number: _Optional[int] = ...) -> None: ...

class Update(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
