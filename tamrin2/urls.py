__author__ = 'ParsData'

from Handlers.index_handler import IndexHandler
from Handlers.post_handler import NewPostHandler

urlList=[
    (r'/',IndexHandler),
    (r'/new$',NewPostHandler)
]


