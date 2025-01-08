class GameState:
    def __init__(self):
        self.keys = 0  # Track the total number of keys

    def add_key(self):
        self.keys += 1

    def get_keys(self):
        return self.keys


# Create a single shared instance of GameState
game_state = GameState()
