import  os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


from tornado.options import define, options
from urls import urlList

define("port",define=8090,help="run on the qiven port",type=int)

class MedxApplication(tornado.web.Application):

    def__init__(self):

      handlers="urlList"
      settings=dict(
          debug=True,
          cookie_secret=""
          template path=os.path.join(os.path.dirname(__file__),"templates"),
          static_path=os.path.join(os.path.dirname(__file__),"static")
                   )
      tornado.web.Application.__init__(self,handlers,**settings)



if __name__=='__main__':
    tornado.options.pars_command_line()



    http_server=tornado.httpserver.HTTPServer(MedxApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

