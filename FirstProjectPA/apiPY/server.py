from flask import Flask

class Server():
  def __init__(self) -> None:
    self.app = Flask(__name__)

  def run(self) -> None:
    self.app.run(debug=True)

server = server()