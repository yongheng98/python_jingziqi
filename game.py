import board
import player
import random
class Game(object):
    def __init__(self):
        self.chess_board=board.Board()
        self.human=player.Player("玩家一")
        self.computer=player.Player("玩家二")
    def random_player(self):
        if random.randint(0,1)==1:
            players=(self.human,self.computer)
        else:
            players=(self.computer,self.human)
        players[0].chess="x"
        players[1].chess="o"
        print("根据随机抽取结果 %s 先行"%players[0].name)
        return players

    def play_round(self):
        self.chess_board.show_board(True)
        current_player,next_player=self.random_player()
        while(True):
            current_player.move(self.chess_board)
            self.chess_board.show_board()
            if self.chess_board.is_win(current_player.chess):
                print("%s 战胜 %s"%(current_player.name,next_player.name))
                current_player.score+=1
                break
            if self.chess_board.is_draw():
                print("%s 和 %s 战成平局"%(current_player.name,next_player.name))
                break
            current_player,next_player=next_player,current_player
        print("[%s] 对战 [%s] 比分是 %d : %d"%(self.human.name,self.computer.name,self.human.score,self.computer.score))
    def start(self):
        while(True):
            self.play_round()
            is_continue=input("是否再来一盘(Y/N)?").upper()
            print(is_continue)
            if(is_continue!="Y"):
                break
            self.chess_board.reset_board()
if __name__=='__main__':
    # board=Board()
    # print(board.board_data)
    # print(board.movable_list)

    # Game().random_player()

    # Game().play_round()
    Game().start()