from board import Board
from service import Service
from console import Console


board= Board()

service = Service(board)

ui = Console(service)

ui.run()
