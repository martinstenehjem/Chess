from Chess2 import Board
import tkinter as tk

# Define piece symbols
piece_symbols = {
    "white Pawn": "♙", "white Rook": "♖", "white Knight": "♘", "white Bishop": "♗",
    "white Queen": "♕", "white King": "♔",
    "black Pawn": "♟", "black Rook": "♜", "black Knight": "♞", "black Bishop": "♝",
    "black Queen": "♛", "black King": "♚",
}

# Implement the Tkinter GUI
class ChessGUI:
    def __init__(self, master):
        self.master = master
        self.board = Board()
        self.selected_piece = None
        self.create_board()

    def create_board(self):
        self.buttons = {}
        for row in Board.rows:
            for col in Board.columns:
                square = col + str(row)
                # Alternate colors for the chessboard
                bg_color = "#E5B978" if (row + Board.columns.index(col)) % 2 == 0 else "#D18B34"  # Light and dark brown
                button = tk.Button(self.master, text='', width=5, height=2, bg=bg_color,
                                   command=lambda sq=square: self.on_square_click(sq))
                button.grid(row=8-row, column=Board.columns.index(col), sticky="nsew")
                self.buttons[square] = button

        # Configure row and column weights for proper resizing
        for i in range(8):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

        self.update_board()

    def update_board(self):
        for square, piece_name in self.board.square_dict.items():
            self.buttons[square].config(text=piece_symbols.get(piece_name, ''), font=('Arial', 62))

    def on_square_click(self, square):
        if self.selected_piece:
            # Attempt to move the selected piece
            piece = self.get_piece_at(self.selected_piece)
            if square in piece.legal_moves():
                piece.move(square)
                self.update_board()
                self.selected_piece = None  # Deselect the piece after moving
                self.reset_highlight()  # Reset highlight after move
            else:
                print("Illegal move!")
                self.selected_piece = None  # Reset selection
                self.reset_highlight()  # Reset highlight
        else:
            # Select the piece, regardless of its color
            piece = self.get_piece_at(square)
            if piece:  # If a piece is present on the selected square
                self.selected_piece = square
                self.highlight_square(square)

    def get_piece_at(self, square):
        for piece in [self.board.white_queen, self.board.white_king, self.board.white_rook_a,
                      self.board.white_rook_h, self.board.white_knight_h, self.board.white_knight_g,
                      self.board.white_bishop_c, self.board.white_bishop_f,
                      self.board.white_pawn_a, self.board.white_pawn_b, self.board.white_pawn_c,
                      self.board.white_pawn_d, self.board.white_pawn_e, self.board.white_pawn_f,
                      self.board.white_pawn_g, self.board.white_pawn_h,
                      self.board.black_queen, self.board.black_king, self.board.black_rook_a,
                      self.board.black_rook_h, self.board.black_bishop_c, self.board.black_bishop_f,
                      self.board.black_knight_b, self.board.black_knight_g,
                      self.board.black_pawn_a, self.board.black_pawn_b, self.board.black_pawn_c,
                      self.board.black_pawn_d, self.board.black_pawn_e, self.board.black_pawn_f,
                      self.board.black_pawn_g, self.board.black_pawn_h]:
            if piece.square == square:
                return piece
        return None

    def highlight_square(self, square):
        # Highlight the selected square with red color
        self.buttons[square].config(bg="red")
        # Reset the color after a short delay
        self.master.after(500, lambda: self.reset_square_color(square))

    def reset_square_color(self, square):
        # Determine the original color of the square
        row = int(square[1])
        col = square[0]
        original_color = "#E5B978" if (row + Board.columns.index(col)) % 2 == 0 else "#D18B34"  # Light and dark brown
        self.buttons[square].config(bg=original_color)

    def reset_highlight(self):
        # Reset all squares to their original color
        for row in Board.rows:
            for col in Board.columns:
                square = col + str(row)
                self.reset_square_color(square)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chess Game")
    chess_gui = ChessGUI(root)
    root.mainloop()
