
https://medium.com/system-designing-interviews/design-tic-tac-toe-game-1b912bba64cf
### question:  Panel: Design a Tic-tac-toe game that is played between two players on a n x n grid. 
You: Follow below approach to identify whether panel is interested in class design and its relation or interested in backend as it seems This is a pretty broad question.

### classes and its relation, class diagrams. 
### snapshot the tic tac toe game 

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

## S:senarios and use cases
does the user need to log in and save the play history
ranking for the users?
will this be popular

1. a user can start the game
2. view the game board
3. view game status
3. user can make move
4. valid the move, make a move, check game status

## identify the class/objects

- class Game
        
        - constructor:
                players []
                board :[][]
                plyaerTurn: int
        methods:
                reset_baord()
                game_state()
                do_move()
                getPlayer()
                

- class Player:
manage player info, numbers of winning, user_name. etc.
        
        - constructor:
                user_name string
                wins: int
        methods:
                get_wins()
                add_wins()

-Move







 