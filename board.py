class Board(object):
    def __init__(self):
        self.board_data=[" "]*9
        self.movable_list=list(range(9))
    def show_board(self,show_index=False):
        for i in (0,3,6):
            print("    |     |")
            if show_index:
                print("  %d |  %d  |  %d "%(i,i+1,i+2))
            else:
                print("  %s |  %s  |  %s "%(self.board_data[i],self.board_data[i+1],self.board_data[i+2]))
            print("    |     |")
            if i!=6:
                print("-"*23)
    def move_down(self,index,chess):
        if index not in self.movable_list:
            print("%d 位置不允许落子"%index)
            return
        self.board_data[index]=chess
        self.movable_list.remove(index)
    def is_draw(self):
        return len(self.movable_list)==0
    def is_win(self,chess):
        check_dirs=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        data=self.board_data.copy()
        for item in check_dirs:
            if (data[item[0]]==chess and data[item[1]]==chess and data[item[2]]==chess):
                return True
        return False
    def reset_board(self):
        self.movable_list.clear()
        for i in range(9):
            self.board_data[i]=" "
            self.movable_list.append(i)




if __name__=='__main__':
    board=Board()
    # print(board.board_data)
    # print(board.movable_list)
    # print("---显示棋盘---"+"-"*50)
    # board.show_board(True)
    # print("-"*50)
    # board.show_board()
    # print("---测试落子"+"-"*50)
    # board.move_down(0,"x")
    # board.show_board()
    # print(board.movable_list)
    # board.move_down(0,"x")
    # print("---判断平局"+"-"*50)
    # print("是否平局%d"%board.is_draw())
    # board.movable_list.clear()
    # print("是否平局%d"%board.is_draw())

    # print("---判断是否胜利"+"-"*50)
    # print("是否胜利%d"%board.is_win("x"))
    # board.move_down(0,"x")
    # board.move_down(1,"x")
    # board.move_down(2,"x")
    # board.show_board()
    # print("是否胜利%d"%board.is_win("x"))

    # print("---重置棋盘数据"+"-"*50)
    # board.reset_board()
    # board.show_board()
    # print(board.movable_list)


