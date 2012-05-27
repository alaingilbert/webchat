import tornado.ioloop
import tornado.web
import os
from tornado import websocket, template, httpserver
import json, tornado
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


sockets = []


# Websocket handler
class EchoWebSocket(websocket.WebSocketHandler):
   def open(self):
      print 'new one'
      sockets.append(self)

   def on_message(self, message):
      global sockets
      for s in sockets:
         if not s == self:
            s.write_message(message, True)

   def on_close(self):
      print 'lost one'
      sockets.remove(self)


loader = template.Loader("%s" % PROJECT_ROOT)

# Http handler
class MainHandler(tornado.web.RequestHandler):
   def get(self):
      loader.reset()
      self.write(loader.load("index.html").generate(myvalue="XXX"))
      self.finish()


application = tornado.web.Application([
    (r'/websocket/', EchoWebSocket),
    (r'/', MainHandler),
    (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': '%s/css/' % PROJECT_ROOT}),
])


if __name__ == "__main__":
   http_server = tornado.httpserver.HTTPServer(application)
   http_server.listen(1337)
   tornado.ioloop.IOLoop.instance().start()
