from freegames import floor, vector

#directions = {[]}

class PacmanBoard:
    def __init__(self, tiles):
        self.tiles = tiles

    def get_offset(self, position):
        x = (floor(position.x, 20) + 200) / 20
        y = (180 - floor(position.y, 20)) / 20
        offset = int(x + y * 20)
        return offset

    def valid_move(self, position):
        offset = self.get_offset(position)
        print("offset:", offset)
        if self.tiles[offset] == 0:
            return False

        offset = self.get_offset(position + 19)

        if self.tiles[offset] == 0:
            return False

        return position.x % 20 == 0 or position.y % 20 == 0

    def make_vec(self, x, y):
        return vector(x, y)
