import board
class Player(object):
    def __init__(self,name):
        self.name=name
        self.score=0
        self.chess=None
    def move(self,chess_board):
        index=-1
        while(index not in chess_board.movable_list):
            try:
                index=int(input(" 请 %s 输入落子位置%s:" %(self.name,chess_board.movable_list)))
            except ValueError:
                pass
        chess_board.move_down(index,self.chess)
if __name__=="__main__":
    chess_board=board.Board()
    human=Player("玩家")
    human.chess="x"
    while(not chess_board.is_win(human.chess)):
        human.move(chess_board)
        chess_board.show_board()
