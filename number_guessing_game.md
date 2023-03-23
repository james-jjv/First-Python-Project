# Q3a Number guessing game (20 marks)

---
## Background

In this question, you are asked to implement a number guessing game we have seen in Workshop 2, which is played as follows:

* (i) One integer `n` from {1, 2, ..., 100} is chosen as random
* (ii) The player needs to guess what `n` is. Once the player makes a guess (say integer `x`), the player will be informed whether `x` is too high, too low, or correct
* (iii) If the guess is not correct (i.e. `x` is too high or too low), the player makes another guess (i.e. back to (ii))
* (iv) One round of the game is finished when `n` is correctly guessed

You will need to implement the game, and also 3 different types of players with 3 different strategies for this part:
* `Player`: choose `x` randomly from the possible range of integers
* `MinPlayer`: choose `x` as the smallest integer from the possible range of integers
* `MiddlePlayer`: choose `x` as the middle integer from the possible range of integers

You will then retrieve and compare the number of guesses of each type of player and conclude which strategy is the best.

---

## Instructions

1. Write the class definitions for the classes `Player`, `MinPlayer`, `MiddlePlayer` in [`src/player.py`](src/player.py). All three classes have the following three methods:
  * `guess()`: guess the unknown integer based on the corresponding strategy. The method does not take any argument and it returns the guess (type: `int`, possible values: 1, ..., 100)
  * `outcome()`: get the outcome of the guess. The method takes a string (`'too high'`, `'too low'` or `'correct'`) as an argument and it has no return value (or return `None`)
  * `record()`: provide the number of guesses made for the last `n` games played. The method takes 1 argument `n` (type: `int` > 0) and returns a list of non-negative integers

  Below we have some examples to help you understand the required behaviour of each type. Note here only part of the game (players) are implemented, and therefore other parts of the game (e.g. to find out if the guess from the player is too high, too low or correct) are done manually in the examples below.

  Example behaviour of an instance of `Player`:
  ```
  player_1 = Player()
  >>> player_1.guess() # randomly select an integer from 1 to 100, 12 below is just an example  
  12
  >>> player_1.outcome('too high')
  >>> player_1.guess() # randomly select an integer from 1 to 11
  3
  >>> player_1.outcome('too high')
  >>> player_1.guess() # randomly select an integer from 1 to 2
  2
  >>> player_1.outcome('correct') # game finished
  >>> player_1.record(1)
  [3]
  >>> player_1.guess() # new game, randomly select an integer from 1 to 100
  82
  >>> player_1.outcome('correct') # game finished
  >>> player_1.record(2)
  [3, 1]
  ```

  Example behaviour of an instance of `MinPlayer`:
  ```
  player_2 = MinPlayer()
  >>> player_2.guess() # select the smallest integer from 1 to 100, i.e. 1
  1
  >>> player_2.outcome('too low')
  >>> player_2.guess() # select the smallest integer from 2 to 100, i.e. 2
  2
  >>> player_2.outcome('correct') # game finished
  >>> player_2.guess() # new game, select the smallest integer from 1 to 100, i.e. 1
  1
  >>> player_2.outcome('too low')
  >>> player_2.guess() # select the smallest integer from 2 to 100, i.e. 2
  2
  >>> player_2.outcome('too low')
  >>> player_2.guess() # select the smallest integer from 3 to 100, i.e. 3
  3
  >>> player_2.outcome('correct') # game finished
  >>> player_2.record(2)
  [2, 3]
  ```

  Example behaviour of an instance of `MiddlePlayer`:
  ```
  player_3 = MiddlePlayer()
  >>> player_3.guess() # select the middle integer from 1 to 100, depending on your implementation, it can be 50 or 51
  50
  >>> player_3.outcome('too high')
  >>> player_3.guess() # select the middle integer from 1 to 49
  25
  >>> player_3.outcome('correct') # game finished
  >>> player_3.record(1)
  [2]
  >>> player_3.guess() # select the middle integer from 1 to 100, depending on your implementation, it can be 50 or 51
  50
  >>> player_3.outcome('too low')
  >>> player_3.guess() # select the smallest integer from 51 to 100, depending on your implementation, it can be 75 or 76
  75
  >>> player_3.outcome('correct') # game finished
  ```

2. In [`src/number_guessing_game.py`](src/number_guessing_game.py), write code to implement the game logic. The idea of what the code should do with a given player `player` in one round:
  * (i) Choose `n` randomly from in {1, 2, ..., 100}
  * (ii) Call the `guess()` method of `player`
  * (iii) Check the return value from (ii) and call the `outcome()` method in `player` with the corresponding argument. For example, if the value from (ii) is smaller than `n` in (i), the argument is `'too low'`
  * (iv) Repeat (ii) and (iii) until `n` is guessed correctly

  For this part, please write the code in the form of a class or a function so that you can use it in part 3

3. In [`src/report.ipynb`](src/report.ipynb), simulate the games with three players and find out the performance of the players by doing the following:
  * (i) Create an instance of each type of player using the classes defined in part 1. There should be 3 players
  * (ii) Make use of the code written in part 2 and let each player plays the game for 10000 times
  * (iii) Retrieve the record for the last 1000 games from each player after playing 10000 games. Analyse the performance by doing the following:
    * Convert the retrieved record into a `pandas.DataFrame` or `numpy.ndarray`, with each column representing the number of guesses each player made. There should be 1000 rows and 3 columns
    * Calculate some summary statistics for each player, including:
      * Average number of guesses per game
      * Median number of guesses per game
      * Maximum number of guesses per game
      * Minimum number of guesses per game
    * Visualise the performance of each player by the use of some appropriate plots (e.g. box plot, each box represents the performance of one player)
    * Make sure you display the summary statistics and the plots in the report. Based on the summary statistics and the plot(s), in the report comment on the performance of each type of player. Which one has the best performance? Worst performance?

---

## Some more coding details and additional requirements

* You can use `random` module for the whole question, and you are allowed to reference the official documents about the module
* For part 3(iii), You can use any functionality from `numpy`, `pandas`, and some plotting libraries like `matplotlib` and `seaborn`. You can also google as much as you want for this part of the question (e.g. find out how to create boxplots). _However_, if you are referencing other people's code / answer / logic, please state it in your report
* Please make sure you demonstrate the OOP concepts in this task
* Please use `player.py` and `number_guessing_game.py` as modules (i.e. do not copy and paste the code from `player.py` and `number_guessing_game.py` to the report)
* Feel free to add "helper" methods to the classes if you think they are appropriate

---

## Things to show in the report

* As mentioned in `Instructions`, part 3 needs to be shown in the report

---

## Hints

* Inside the class definition(s), there should be some instance variables keeping track of the range of possible integers, the number of guesses, etc. Those instance variables should be updated inside the methods. For example, the range of possible integers is always 1-100 when a new game starts, but it should be updated when the player is informed about the outcome of each guess
