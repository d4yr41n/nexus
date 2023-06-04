from http.server import HTTPServer, BaseHTTPRequestHandler

from const import BLACK, WHITE
from game import Game


games = [Game()]


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == "/":
            response = games[0]
        elif self.path == "/turn":
            response = int(games[0].turn)
        elif self.path == "/over":
            response = int(games[0].over)
        elif self.path == "/result":
            response = games[0].result
        else:
            return

        self.wfile.write(str(response).encode("utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        if self.path == "/":    
            games[0] = Game()
        elif self.path == "/black" and games[0].turn == BLACK:
            games[0].move(
                self.rfile.read(
                    int(self.headers['Content-Length'])
                ).decode("utf-8")
            )
        elif self.path == "/white" and games[0].turn == WHITE:
            games[0].move(
                self.rfile.read(
                    int(self.headers['Content-Length'])
                ).decode("utf-8") 
            )


HTTPServer(("", 8000), RequestHandler).serve_forever()

