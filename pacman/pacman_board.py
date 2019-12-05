from freegames import floor, vector



class PacmanBoard:
    def __init__(self, tiles, pacman):
        self.tiles = tiles
        self.pacman = pacman

    def get_offset(self, position):
        x = (floor(position.x, 20) + 200) / 20
        y = (180 - floor(position.y, 20)) / 20
        offset = int(x + y * 20)
        return offset

    def valid_move(self, position):
        offset = self.get_offset(position)

        if self.tiles[offset] == 0:
            return False

        offset = self.get_offset(position + 19)

        if self.tiles[offset] == 0:
            return False

        return position.x % 20 == 0 or position.y % 20 == 0

    def update_pacman(self, pacman):
        self.pacman = pacman

    def get_pacman(self):

        return self.pacman

    def moves_from(self, position):
        moves = []
        possible = [
            vector(2.5, 0),
            vector(-2.5, 0),
            vector(0, 2.5),
            vector(0, -2.5)
        ]
        for i in possible:
            if self.valid_move(position + i):
                moves.append(i)
        return moves

    def pacman_moves(self, position):
        moves = []
        possible = [
            vector(5, 0),
            vector(-5, 0),
            vector(0, 5),
            vector(0, -5)
        ]
        for i in possible:
            if self.valid_move(position + i):
                moves.append(i)
        return moves

    def make_vec(self, x, y):
        return vector(x, y)
