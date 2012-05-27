import tornado.ioloop
import tornado.web
import os
from tornado import websocket, template
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


# Websocket handler
class EchoWebSocket(websocket.WebSocketHandler):
   def open(self):
      print "WebSocket opened"

   def on_message(self, message):
      self.write_message(u"Server: Frame received")

   def on_close(self):
      print "WebSocket closed"


loader = template.Loader("%s" % PROJECT_ROOT)

# Http handler
class MainHandler(tornado.web.RequestHandler):
   def get(self):
      loader.reset()
      self.write(loader.load("index.html").generate(myvalue="XXX"))


application = tornado.web.Application([
    (r'/websocket/', EchoWebSocket),
    (r'/', MainHandler),
    (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': '%s/css/' % PROJECT_ROOT}),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
