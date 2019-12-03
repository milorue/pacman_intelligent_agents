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
        #print("update pacman:", pacman)
        self.pacman = pacman
        #print("self pacman:", self.pacman)
    def get_pacman(self):
        print("pacman:", self.pacman)

        return self.pacman

    def moves_from(self, position):
        moves = []
        possible = [
            vector(10, 0),
            vector(-10, 0),
            vector(0, 10),
            vector(0, -10)
        ]
        for i in possible:
            if self.valid_move(position + i):
                moves.append(i)
        return moves


    def make_vec(self, x ,y):
        return vector(x, y)