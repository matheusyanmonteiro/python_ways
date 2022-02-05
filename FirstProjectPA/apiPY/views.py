from server import server
from models import UserGraph


app = server.app

users = {
  "Gugamph": [
    "Arzagk",
    "Vyezol",
    "Buofa"
  ],
  "Arzagk": [
    "Xiebe",
    "Yagawi",
    "Celeblie",
    "Gugamph"
  ],
  "Celeblie": [
    "Arzagk",
    "Gurde",
    "Buofa"
  ],
  "Vyezol": [
    "Gugamph"
  ],
  "Buofa": [
    "Gugamph",
    "Buofa"
  ]
}

graphFunc =  UserGraph()