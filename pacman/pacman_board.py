from freegames import floor, vector


class PacmanBoard:
    def __init__(self, tiles, pacman, pac_dir, ghosts):
        self.tiles = tiles
        self.pacman = pacman
        self.pac_dir = pac_dir
        self.ghosts = ghosts

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

    def update_ghosts(self, ghosts):
        self.ghosts = ghosts

    def get_pacman(self):
        return self.pacman

    def get_ghosts(self):
        return self.ghosts

    def moves_from(self, position):
        moves = []
        possible = [
            vector(5, 0),
            vector(-5, 0),
            vector(0, 5),
            vector(0, -5)
        ]

        # un-working rn
        # if position == vector(100, 20) or position == vector(-180, 20):  # follow teleport on random chance for fairness
        #     move = position + choice(possible)
        #     while not self.valid_move(move):
        #         move = position + choice(possible)
        #     return move

        for i in possible:
            if self.valid_move(position + i):
                moves.append(i)
        return moves

    def invalid_moves_from(self, position):
        moves = []
        possible = [
            vector(5, 0),
            vector(-5, 0),
            vector(0, 5),
            vector(0, -5)
        ]

        count = 0
        hits = []
        for i in possible:
            count += 1
            if not self.valid_move(position + i):
                hits.append(count)
                moves.append(i)
        return moves

    def pacman_moves(self, position):
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

    def make_vec(self, x, y):
        return vector(x, y)

    def determine_teleports(self, position):
        ports = [
            vector(-200, 20),
            vector(120, 20)
        ]

        if position == ports[0]:
            position = ports[1]
            return position

        elif position == ports[1]:
            position = ports[0]
            return position

        else:
            return position

    def power_pellets(self):
        pellets = [
            vector(-180, -160),
            vector(100, -160),
            vector(-180, 160),
            vector(100, 160)
        ]

        return pellets

    def get_decision_points(self):  # decision mesh for default board (hard coded cause :P)
        points = [
            vector(-180, -160),
            vector(-180, -120),
            vector(-120, -120),
            vector(-60, -120),
            vector(-60, -160),
            vector(-20, -160),
            vector(-20, -120),
            vector(100, -160),
            vector(100, -120),
            vector(100, -80),
            vector(100, -40),
            vector(100, 20),
            vector(100, 80),
            vector(100, 120),
            vector(100, 160),
            vector(80, -120),
            vector(40, -120),
            vector(40, -80),
            vector(80, -80),
            vector(0, -80),
            vector(0, -120),
            vector(-20, -80),
            vector(-20, -40),
            vector(0, -40),
            vector(40, -40),
            vector(40, 20),
            vector(40, 80),
            vector(40, 120),
            vector(40, 160),
            vector(0, 0),
            vector(0, 40),
            vector(0, 120),
            vector(-20, 160),
            vector(-20, 120),
            vector(0, 80),
            vector(-20, 80),
            vector(-20, 40),
            vector(-60, -40),
            vector(-60, -80),
            vector(-60, -60),
            vector(-60, 40),
            vector(-60, 80),
            vector(-60, 120),
            vector(-60, 160),
            vector(-80, -120),
            vector(-80, -80),
            vector(-80, -40),
            vector(-80, 0),
            vector(0, 20),
            vector(-80, 20),
            vector(-80, 40),
            vector(-80, 80),
            vector(-80, 120),
            vector(-120, -80),
            vector(-120, -40),
            vector(-120, 20),
            vector(-120, 80),
            vector(-120, 120),
            vector(-120, 160),
            vector(-160, -80),
            vector(-180, -80),
            vector(-180, -40),
            vector(-180, 20),
            vector(-180, 80),
            vector(-180, 120),
            vector(-180, 160)
        ]

        return points

    def valid_locations(self):
        positions = []
        for index in range(len(self.tiles)):
            currTile = self.tiles[index]

            if currTile == 1:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                pos = vector(x, y)
                positions.append(pos)

        return positions
