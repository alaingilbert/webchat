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
      self.write_message(u"Server: " + message)

   def on_close(self):
      print "WebSocket closed"


loader = template.Loader("%s" % PROJECT_ROOT)

# Http handler
class MainHandler(tornado.web.RequestHandler):
   def get(self):
      self.write(loader.load("index.html").generate(myvalue="XXX"))


application = tornado.web.Application([
    (r'/websocket/', EchoWebSocket),
    (r'/', MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
