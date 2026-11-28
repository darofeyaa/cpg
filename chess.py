from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        if self.color not in ["white", "black"]:
            raise ValueError("Barva musí být 'white' nebo 'black'.")
        if not self.is_position_on_board(self.position):
            raise ValueError("Pozice musí být na šachovnici (1-8, 1-8).")

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'

#пешка
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def possible_moves(self):
        if self.color == "white" and self.position[0] < 8:
            return [(self.position[0] + 1, self.position[1])]
        elif self.color == "black" and self.position[0] > 1:
            return [(self.position[0] - 1, self.position[1])]

        
        
        return self.position[0] == 2 \
         and self.position[0] + 2 == self.new_position[0] \
            and (self.position[0] + 1 , self.new_position[1]) not in self.possible_moves()
        
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'

#конь
class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'

#слон
class Bishop(Piece):
    pass

#ладья
class Rook(Piece):
    pass

#ферзь
class Queen(Piece):
    pass

#король
class King(Piece):
    pass


if __name__ == "__main__":
    #piece = Knight("black", (1, 2))
    piece = Pawn("white", (1, 1))
    print(piece)
    print(piece.possible_moves())
