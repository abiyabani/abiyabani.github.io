__author__ = 'ParsData'


import  tornado

class NewPostHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('add_post.html')


    def post(self):
        tit = self.get_argument("h_post")
        da = self.get_argument("d_post")
        te = self.get_argument("t_post")
        na = self.get_argument("a_post")
        im = self.get_argument("img")

        im2 = ".../static/img/%s" %(im)

        info = NewPost.create(
            title=tit,
            author=na,
            date=te,
            text=te,
            image=im2
        )

        self.redirect('/')

