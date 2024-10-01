from abc import abstractmethod, ABC
# from Pieces import Bishop, King, Queen, Pawn, Rook, Knight

class Board:
    square_dict = {}
    columns = [col for col in "abcdefgh"]  # defining the columns
    rows = [row for row in range(1, 9)]  # defining the rows

    def __init__(self):
        self.make_squares()
        # Creating white pieces
        self.white_queen = Queen("white", "d1")
        self.white_king = King("white", "e1")
        self.white_rook_a = Rook("white", "a1")
        self.white_rook_h = Rook("white", "h1")
        self.white_knight_h = Knight("white", "b1")
        self.white_knight_g = Knight("white", "g1")
        self.white_bishop_c = Bishop("white", "c1")
        self.white_bishop_f = Bishop("white", "f1")
        self.white_pawn_a = Pawn("white", "a2")
        self.white_pawn_b = Pawn("white", "b2")
        self.white_pawn_c = Pawn("white", "c2")
        self.white_pawn_d = Pawn("white", "d2")
        self.white_pawn_e = Pawn("white", "e2")
        self.white_pawn_f = Pawn("white", "f2")
        self.white_pawn_g = Pawn("white", "g2")
        self.white_pawn_h = Pawn("white", "h2")
        # Creating black pieces
        self.black_queen = Queen("black", "d8")
        self.black_king = King("black", "e8")
        self.black_rook_a = Rook("black", "a8")
        self.black_rook_h = Rook("black", "h8")
        self.black_bishop_c = Bishop("black", "c8")
        self.black_bishop_f = Bishop("black", "f8")
        self.black_knight_b = Knight("black", "b8")
        self.black_knight_g = Knight("black", "g8")
        self.black_pawn_a = Pawn("black", "a7")
        self.black_pawn_b = Pawn("black", "b7")
        self.black_pawn_c = Pawn("black", "c7")
        self.black_pawn_d = Pawn("black", "d7")
        self.black_pawn_e = Pawn("black", "e7")
        self.black_pawn_f = Pawn("black", "f7")
        self.black_pawn_g = Pawn("black", "g7")
        self.black_pawn_h = Pawn("black", "h7")

    def make_squares(self):
        squares = [column + str(row) for row in self.rows for column in self.columns]  # creating list of all squares
        for square in squares:
            self.square_dict[square] = None  # setting each square value to None
    
    def print_board(self):
        for sqr in self.square_dict.keys():
            pass



class Piece(ABC):
    def __init__(self, square):
        self.square = square

    @abstractmethod
    def get_name(self):
        pass

    def move(self, new_square):
        if new_square in self.legal_moves():
            Board.square_dict[self.square] = None
            self.square = new_square
            Board.square_dict[self.square] = self.get_name()
        else:
            print("sorry, illegal move")

    @abstractmethod
    def capture(self):
        pass

    @abstractmethod
    def legal_moves(self):
        pass


class Pawn(Piece):
    def __init__(self, color, square):
        super().__init__(square)
        self.color = color
        self.square = square
        Board.square_dict[square] = self.get_name()
        self.value = 1

    def get_name(self):
        return self.color + " Pawn"

    def capture(self):
        moves = []
        left = Board.columns.index(self.square[0]) - 1
        right = Board.columns.index(self.square[0]) + 1
        forward = int(self.square[1]) + 1
        backward = int(self.square[1]) - 1
        if self.color == "white":
            if left>=0 and forward<9:
                attack_left = Board.columns[left] + str(forward)
                if Board.square_dict[attack_left] is not None and Board.square_dict[attack_left][0] != self.color[0]:
                    moves.append(attack_left)
            if right<8 and forward<9:
                attack_right = Board.columns[right] + str(forward)
                if Board.square_dict[attack_right] is not None and Board.square_dict[attack_right][0] != self.color[0]:
                    moves.append(attack_right)
        else:
            if left>=0 and backward>0:
                attack_left = Board.columns[left] + str(backward)
                if Board.square_dict[attack_left] is not None and Board.square_dict[attack_left][0] != self.color[0]:
                    moves.append(attack_left)
            if right<8 and backward>0:
                attack_right = Board.columns[right] + str(backward)
                if Board.square_dict[attack_right] is not None and Board.square_dict[attack_right][0] != self.color[0]:
                    moves.append(attack_right)
        return moves

    def legal_moves(self):
        # creating a list of possible moves
        moves = []
        if self.color == "white":
            new_square1 = self.square[0] + str(int(self.square[1]) + 1)
            new_square2 = self.square[0] + str(int(self.square[1]) + 2)
            start = "2"
        else:
            new_square1 = self.square[0] + str(int(self.square[1]) - 1)
            new_square2 = self.square[0] + str(int(self.square[1]) - 2)
            start = "7"
        # Moving one square forward
        if 0<int(new_square1[1])<9 and Board.square_dict[new_square1] is None:
            moves.append(new_square1)
        # Moving two squares forward (only in its starting position)
        if (self.square[1] == start) and Board.square_dict[new_square1] is None and Board.square_dict[new_square2] is None:
            moves.append(new_square2)

        return moves + self.capture()


class Bishop(Piece):
    def __init__(self, color, square):
        super().__init__(square)
        self.color = color
        self.square = square
        Board.square_dict[square] = self.get_name()
        self.value = 3

    def get_name(self):
        return self.color + " Bishop"

    def capture(self):
        pass

    def legal_moves(self):
        # creating a list of possible moves
        moves = []
        # Moves bishop north-west
        left = Board.columns.index(self.square[0]) - 1  # column index of the column left of bishop
        forward = int(self.square[1]) + 1  # row index of the row in front of bishop
        if left >= 0 and Board.columns[left] + str(forward) in Board.square_dict:  # checks if front-left on the board
            while Board.square_dict[Board.columns[left] + str(forward)] is None or Board.square_dict[Board.columns[left] + str(forward)][0] != self.color[0]:
                moves.append(Board.columns[left] + str(forward))
                if Board.square_dict[Board.columns[left] + str(forward)] is not None and Board.square_dict[Board.columns[left] + str(forward)][0] != self.color[0]:
                    break
                left -= 1
                forward += 1
                if left<0 or Board.columns[left] + str(forward) not in Board.square_dict:
                    break
        # Moves bishop south-west
        left = Board.columns.index(self.square[0]) - 1  # column index of the column left of bishop
        backward = int(self.square[1]) - 1  # row index of the row behind of bishop
        if left >= 0 and Board.columns[left] + str(backward) in Board.square_dict:  # checks if rear-left on the board
            while Board.square_dict[Board.columns[left] + str(backward)] is None or Board.square_dict[Board.columns[left] + str(backward)][0]!=self.color[0]:
                moves.append(Board.columns[left] + str(backward))
                if Board.square_dict[Board.columns[left] + str(backward)] is not None and Board.square_dict[Board.columns[left] + str(backward)][0]!=self.color[0]:
                    break
                left -= 1
                backward -= 1
                if left<0 or Board.columns[left] + str(backward) not in Board.square_dict:
                    break
        # Moves bishop north-east
        right = Board.columns.index(self.square[0]) + 1  # column index of the column right of bishop
        forward = int(self.square[1]) + 1  # row index of the row in front of bishop
        if right < 8 and Board.columns[right] + str(forward) in Board.square_dict:  # front-right otb
            while Board.square_dict[Board.columns[right] + str(forward)] is None or Board.square_dict[Board.columns[right] + str(forward)][0]!=self.color[0]:
                moves.append(Board.columns[right] + str(forward))
                if Board.square_dict[Board.columns[right] + str(forward)] is not None and Board.square_dict[Board.columns[right] + str(forward)][0]!=self.color[0]:
                    break
                right += 1
                forward += 1
                if right>7 or Board.columns[right] + str(forward) not in Board.square_dict:
                    break
        # Moves bishop south-east
        right = Board.columns.index(self.square[0]) + 1  # column index of the column right of bishop
        backward = int(self.square[1]) - 1  # row index of the row in front of bishop
        if right < 8 and Board.columns[right] + str(backward) in Board.square_dict:  # rear_right otb
            while Board.square_dict[Board.columns[right] + str(backward)] is None or Board.square_dict[Board.columns[right] + str(backward)][0]!=self.color[0]:
                moves.append(Board.columns[right] + str(backward))
                if Board.square_dict[Board.columns[right] + str(backward)] is not None and Board.square_dict[Board.columns[right] + str(backward)][0]!=self.color[0]:
                    break
                right += 1
                backward -= 1
                if right>7 or Board.columns[right] + str(backward) not in Board.square_dict:
                    break
        return moves


class Rook(Piece):
    def __init__(self, color, square):
        super().__init__(square)
        self.color = color
        self.square = square
        Board.square_dict[square] = self.get_name()
        self.value = 5

    def get_name(self):
        return self.color + " Rook"

    def capture(self):
        pass

    def legal_moves(self):
        # creating a list of possible moves
        moves = []
        # Moving rook forward
        forward = int(self.square[1]) + 1
        if self.square[0] + str(forward) in Board.square_dict:
            while Board.square_dict[self.square[0] + str(forward)] is None or Board.square_dict[self.square[0] + str(forward)][0]!=self.color[0]:  # while no pieces are in the way
                moves.append(self.square[0] + str(forward))
                if Board.square_dict[self.square[0] + str(forward)] is not None and Board.square_dict[self.square[0] + str(forward)][0]!=self.color[0]:
                    break
                forward += 1
                if self.square[0] + str(forward) not in Board.square_dict:
                    break
        # Moving rook backwards
        backward = int(self.square[1]) - 1
        if self.square[0] + str(backward) in Board.square_dict:
            while Board.square_dict[self.square[0] + str(backward)] is None or Board.square_dict[self.square[0] + str(backward)][0]!=self.color[0]:  # while no pieces are in the way
                moves.append(self.square[0] + str(backward))
                if Board.square_dict[self.square[0] + str(backward)] is not None and Board.square_dict[self.square[0] + str(backward)][0]!=self.color[0]:
                    break
                backward -= 1
                if self.square[0] + str(backward) not in Board.square_dict:
                    break
        # Moving rook to the right
        right = Board.columns.index(self.square[0]) + 1
        if right < 8:
            while Board.square_dict[Board.columns[right] + self.square[1]] is None or Board.square_dict[Board.columns[right] + self.square[1]][0]!=self.color[0]:  # while no pieces are in the way
                moves.append(Board.columns[right] + self.square[1])
                if Board.square_dict[Board.columns[right] + self.square[1]] is not None and Board.square_dict[Board.columns[right] + self.square[1]][0]!=self.color[0]:
                    break
                right += 1
                if right>7:
                    break
        # Moves rook to the left
        left = Board.columns.index(self.square[0]) - 1  # column left of the rook
        if left >= 0:  # if square left of rook on board
            while Board.square_dict[Board.columns[left] + self.square[1]] is None or Board.square_dict[Board.columns[left] + self.square[1]]:  # while no pieces are in the way
                moves.append(Board.columns[left] + self.square[1])
                if Board.square_dict[Board.columns[left] + self.square[1]] is not None and Board.square_dict[Board.columns[left] + self.square[1]]:
                    break
                left -= 1
                if left<0:
                    break
        return moves


class Queen(Piece):
    def __init__(self, color, square):
        super().__init__(square)
        self.color = color
        self.square = square
        Board.square_dict[square] = self.get_name()
        self.value = 10

    def get_name(self):
        return self.color + " Queen"

    def capture(self):
        pass

    def legal_moves(self):
        return Bishop.legal_moves(self) + Rook.legal_moves(self)


class Knight(Piece):
    def __init__(self, color, square):
        super().__init__(square)
        self.color = color
        self.square = square
        Board.square_dict[square] = self.get_name()
        self.value = 3

    def get_name(self):
        return self.color + " Knight"

    def capture(self):
        pass

    def legal_moves(self):
        moves = []
        col = Board.columns.index(self.square[0])
        row = int(self.square[1])
        left = col - 1
        left2 = col - 2
        right = col + 1
        right2 = col + 2
        candidates = []
        if left >= 0 and row < 7:
            candidates.append(Board.columns[left] + (str(row + 2)))
        if left >= 0 and row > 2:
            candidates.append(Board.columns[left] + (str(row - 2)))
        if left2 >= 0 and row < 8:
            candidates.append(Board.columns[left2] + (str(row + 1)))
        if left2 >= 0 and row > 1:
            candidates.append(Board.columns[left2] + (str(row - 1)))
        if right < 8 and row < 7:
            candidates.append(Board.columns[right] + (str(row + 2)))
        if right < 8 and row > 2:
            candidates.append(Board.columns[right] + (str(row - 2)))
        if right2 < 8 and row < 8:
            candidates.append(Board.columns[right2] + (str(row + 1)))
        if right2 < 8 and row > 1:
            candidates.append(Board.columns[right2] + (str(row - 1)))
        for move in candidates:
            if Board.square_dict[move] is None:
                moves.append(move)
            else:
                if Board.square_dict[move][0] != self.color[0]:
                    moves.append(move)
        return moves


class King(Piece):
    def __init__(self, color, square):
        super().__init__(square)
        self.color = color
        self.square = square
        Board.square_dict[square] = self.get_name()

    def get_name(self):
        return self.color + " King"

    def capture(self):
        pass

    def legal_moves(self):
        moves = []
        col = Board.columns.index(self.square[0])
        row = int(self.square[1])
        left = col - 1
        right = col + 1
        candidates = []
        if left>=0:
            candidates.append(Board.columns[left] + (str(row)))
            if row<8:
                candidates.append(Board.columns[left] + (str(row+1)))
            if row>1:
                candidates.append(Board.columns[left] + (str(row-1)))
        if right<8:
            candidates.append(Board.columns[right] + (str(row)))
            if row<8:
                candidates.append(Board.columns[right] + (str(row+1)))
            if row>1:
                candidates.append(Board.columns[right] + (str(row-1)))
        if row+1<9:
            candidates.append(Board.columns[col] + (str(row+1)))
        if row-1>0:
            candidates.append(Board.columns[col] + (str(row-1)))
        for move in candidates:
            if Board.square_dict[move] is None:
                moves.append(move)
            elif Board.square_dict[move][0] != self.color[0]:
                moves.append(move)
        return moves


my_board = Board()
# print(Board.square_dict)
print(my_board.square_dict)
my_board.white_pawn_d.move("d4")
my_board.white_pawn_a.move("a3")
my_board.white_rook_a.move("a5")
print(Board.square_dict["a3"])
print(my_board.square_dict["a3"])

