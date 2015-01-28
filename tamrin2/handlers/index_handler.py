import tornado
from models import NewPost
__author__ = 'ParsData'



class indexHandler(tornado.web.RequesHandler):
    def get(self):
        post = NewPost.select()
        self.render('index.html',post=post)