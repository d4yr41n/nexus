from http.server import HTTPServer, BaseHTTPRequestHandler

from const import BLACK, WHITE
from game import Game


game = Game()


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        match self.path:
            case "/":
                self.wfile.write(str(game).encode("utf-8"))
            case "/run":
                self.write.write(str(game.run).encode("utf-8"))
            case "/turn":
                print(game.turn)
                self.wfile.write(str(game.turn).encode("utf-8"))


    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        match self.path:
            case "/":
                game.setup()
            case "/black":
                if game.turn == BLACK:
                    game.move(
                        self.rfile.read(
                            int(self.headers['Content-Length'])
                        ).decode("utf-8")
                    )
            case "/white":
                if game.turn == WHITE:
                    game.move(
                        self.rfile.read(
                            int(self.headers['Content-Length'])
                        ).decode("utf-8")
                    )


HTTPServer(("", 8000), RequestHandler).serve_forever()

