# @ping-game-theory

A compete with code style tournament where each player can submit their strategy to win the most points.

# Quickstart

Please read the whole documentation before just using this. 😛

1. Clone this repository
2. Install requirements
3. Create a python file under strategies folder
4. Use the following skeleton and populate the functions with your logic

```py
import math
import numpy
import random

from utils.types import History, Move

class Strategy:
    def __init__(self):
        self.name = ''
  
    def begin(self) -> Move:
        # Logic Here
        pass

    def turn(self, history: History) -> Move:
        # Logic Here
        pass
```

5. Run the main file, ensure no errors occur.

# The Dilemma

You have been invited to a compete against other people for points. At a time you only face off against one other person. Each showdown goes for a predetermined number of rounds.

Each round, both you and your opponent have two options. SPLIT or STEAL.

1. Both of you choose to SPLIT -> Both of you get 5 points
2. Both of you choose to STEAL -> Both of you get 3 points
3. One of you chooses to SPLIT while the other chooses to STEAL -> The one who chose to steal gets 10 points leaving the other with 0.

The catch? You will be facing off using code. Each player in the dilemma will write a strategy that determines their decision to SPLIT or STEAL.

Each strategy will face off against every other strategy and a copy of themselves.

All the points will be tallied up across all showdowns, and the strategy with the highest number of points will win.

# Types

Documentation for all the types a user will have to interact with.

Please read this and understand it well before proceeding. Ask a helper if you have any doubts.

## 1. Move

An enumeration respresenting the possible moves a player can make in the game.
Members:
- `SPLIT`
- `STEAL`

Example:

```py
# Making comparisions
move: Move
if (move == Move.SPLIT):
    return Move.STEAL
else:
    return Move.SPLIT
```

## 2. HistoryEntry

A named tuple representing a single entry in the games history. It gives you access to your and your opponents moves.
Attributes:
- `opponent` (Move)
- `you` (Move)

You can only read from `HistoryEntry` objects.
Example:

```py
# Accessing moves played by you and your opponent
entry: HistoryEntry
opponents_move: Move = entry.opponent
your_move: Move = entry.you
```

## 3. History

A type alias for `HistoryEntry` objects, representing the game's history as an immutable sequence.

You can only read from the `History` object.
Example:

```py
# Accessing moves from history
history: History
history_len: int = len(history) # To access total number of moves
last_entry: HistoryEntry = history[-1]
last_move_opponent: Move = last_entry.opponent
last_move_you: Move = last_entry.you
```

## 4. Strategy

A base class representing your strategy. It defines two how a player makes their moves based on the game's history.

To make decisions you also get access to the following python modules (will probably increase in the future):

1. random
2. math
3. numpy

Attributes:
- `name` (str): The name of the strategy

Methods:
- `begin(self) -> Move`: Defines the move made by the strategy at the beginning of the game. It is called only once that the beginning of each dilemma. It has to return a Move object
- `turn(self, history: History) -> Move`: Defines the move to make based on the game's history. It is called every time other than the beginning of each dilemma and gives you access to all moves made by you and your opponent throughout the game. It has to return a Move object

# Tutorial

Now that we understand all types. Lets create a very simple strategy that simply steals if the opponent steals on the past round. This strategy is also called titfortat.

PS: Check the pre-existing strategies for other examples

Example:

```py
import math
import numpy
import random

# Type imports
from utils.types import History, Move

class Strategy:
    def __init__(self):
        self.name = 'titfortat'
        # The name of your strategy
  
    def begin(self) -> Move:
        """
            Logic for the first move of any showdown.
            Is only run once on the initial run.

            return
                Move
        """

        # The titfortat strategy returns SPLIT on the first round no matter what
        return Move.SPLIT
  
    def turn(self, history: Histor) -> Move:
        """
            Logic for any move in the showdown after the first move.
            Is run every time except on the initial run.

            arguments
                history: History
        
            return
                Move
        """

        # The titfortat strategy checks if the previous move made by the opponent was a STEAL and if so, STEALS otherwise it always SPLITS

        # Accessing last move by opponent
        latest_entry = history[-1]
        last_move_opponent = latest_entry.opponent

        # Let us now check if this move was a STEAL
        if (last_move_opponent == Move.STEAL):
            # STEAL if so
            return Move.STEAL
        else:
            return Move.SPLIT

    # This is a sample strategy and is quite simple
    # You can come up with any strategy as simple or complex as you want.
```

Let us create one more strategy that just returns a random move regardless of history

Example:

```py
import math
import numpy
import random

from utils.types import History, Move

class Strategy:
    def __init__(self):
        self.name = 'random'
  
    def begin(self) -> Move:
        return random.choice([Move.SPLIT, Move.STEAL])

    def turn(self, history: History) -> Move:
        return random.choice([Move.SPLIT, Move.STEAL])
```
