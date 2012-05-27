import tornado.ioloop
import tornado.web
from tornado import websocket

class EchoWebSocket(websocket.WebSocketHandler):
   def open(self):
      print "WebSocket opened"

   def on_message(self, message):
      self.write_message(u"Server: " + message)

   def on_close(self):
      print "WebSocket closed"

application = tornado.web.Application([
    (r"/", EchoWebSocket),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
