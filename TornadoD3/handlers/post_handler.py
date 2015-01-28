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


class ShowHandler(tornado.web.RequestHandler):
    def get(self):
        post = NewPost.select()
        self.render('show_post.html',post=post)

class EditHandler(tornado.web.RequestHandler):
    def get(self, *args):
        catid = args[0]
        post = NewPost.select().where(NewPost.id == catid).get()
        self.render('edit_post',po=post)


    def post(self,*args):
        catid = args[0]
        catinfo = NewPost.select().where(NewPost.id == catid).get()

        catinfo.title = self.get_argument("h_post")
        catinfo.date = self.get_argument("d_post")
        catinfo.text = self.get_argument("t_post")
        catinfo.author = self.get_argument("a_post")

        catinfo.save()

        self.redirect('/')



class DeletHandler(tornado.web.RequestHandler):
    def get(self, *args):
        catid = args[0]
        catinfo = NewPost.select().where(NewPost.id == catid).get().delete_instance()

        self.redirect("/")
