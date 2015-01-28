__author__ = 'ParsData'

from Handlers.index_handler import IndexHandler
from Handlers.post_handler import NewPostHandler,ShowHandler,EditHandler,DeleteHandler

urlList=[
    (r'/',IndexHandler),
    (r'/new$',NewPostHandler),
    (r'/show',ShowHandler),
    (r'/edit/(\d+)$',EditHandler),
    (r'/delete/(/d+)$',DeleteHandler)
]


