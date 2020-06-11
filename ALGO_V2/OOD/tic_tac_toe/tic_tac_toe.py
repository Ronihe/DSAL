class Game:
    '''
    a game with public and complete state
    '''

    def __init__(self, players, state):
        '''
        init a new game and initial state
        Args:
            players: Player class
            state: gamestate class
        '''
        self._players = players
        self._state = state

    def play(self):
        """
        plays the game and record state
        Returns:

        """
