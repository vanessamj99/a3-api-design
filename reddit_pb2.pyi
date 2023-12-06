from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["userID"]
    USERID_FIELD_NUMBER: _ClassVar[int]
    userID: str
    def __init__(self, userID: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ["postID", "title", "text", "mediaUrl", "score", "state", "publicationDate", "author"]
    POSTID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MEDIAURL_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATIONDATE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    postID: str
    title: str
    text: str
    mediaUrl: str
    score: str
    state: str
    publicationDate: str
    author: User
    def __init__(self, postID: _Optional[str] = ..., title: _Optional[str] = ..., text: _Optional[str] = ..., mediaUrl: _Optional[str] = ..., score: _Optional[str] = ..., state: _Optional[str] = ..., publicationDate: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ["commentID", "author", "score", "state", "publicationDate"]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATIONDATE_FIELD_NUMBER: _ClassVar[int]
    commentID: str
    author: User
    score: str
    state: str
    publicationDate: str
    def __init__(self, commentID: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[str] = ..., state: _Optional[str] = ..., publicationDate: _Optional[str] = ...) -> None: ...
