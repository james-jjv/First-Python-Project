# Q3b Number guessing game with "reinforcement learning" (25 marks)

---

## Background

Note: If you find it difficult to understand the description of how things work below, feel free to ask the instructor for further clarification and explanation.

Here we continue with Q3a, but this time we will create "learning" players inspired by reinforcement learning: The players will "reward" the "good" choices and "punish" the "bad" choices.

Like the random players, the learning players will make their choices randomly. Unlike the random players who assign equal probability to all possible choices, the learning players increase the probability of 'good' choice and reduce the probability of the 'bad' choice. For example, if we have seen from previous rounds that when the possible choices are between (1, 5), if we select 3 then the number of guesses to make is smaller other choices, then instead of choosing between 1, 2, 3, 4, 5 with equal probability, we should select 3 with a higher probability.

To be able to do so, we can have some data structure to store the choices and some "estimation" of number of guesses needed based on previous outcomes. We can do so by having some data structure like a `dict` of `dict` (say it is called `_estimated_num_guesses`) here:
```
{(1,1): {1:1},
 (1,2): {1:2, 2:2},
 (1,3): {1:3, 2:2, 3:3},
 ...
 (1,5): {1:5, 2:4, 3:3, 4:4, 5:5}
 ...
 (1,11): {1:11, 2:10, 3:9, 4:8, 5:7, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11),
 ...
 (2,2): {2:1},
 (2,3): {2:2, 3:2},
 (2,4): {2:3, 3:2, 4:3},
 ...
 (1,100): {1:100, ..., 6:95, ..., 12:89, ..., 100:100},
 ...
 (100,100): {100:1}
}
```

(note this is just an example, you can use some other data structure like a `dict` of `list`):

The key represents the range (upper and lower) of possible integers left to guess, and the value is a `dict` for which the value stores the current "estimated" number of _additional_ guesses need to make when the corresponding choice (i.e. the value of the key) is made. Some details:
* At the beginning, the "estimated" number for the choice `k` is equal to max(upper-k+1, k-lower+1)
* When a new round is done, based on the additional guesses made (`n`) for choice `k`, the "estimated" number for choice `k` is updated by: previous_estimated_value * 0.8 + `n` * 0.2

For example, if below is what happened in the first 2 rounds:
```
player_4 = LearningPlayer()
>>> player_4.guess()
12
>>> player_4.outcome('too high')
>>> player_4.guess()
3
>>> player_4.outcome('too high')
>>> player_4.guess()
2
>>> player_4.outcome('correct') # game finished
>>> player_4.guess()
6
>>> player_4.outcome('too high')
>>> player_4.guess()
3
>>> player_4.outcome('too high')
>>> player_4.guess()
2
>>> player_4.outcome('too high')
>>> player_4.guess()
1
>>> player_4.outcome('correct') # game finished
```

i.e. we have made the following choices with the possible ranges:
* First round :
  | range  | choice | additional number of guesses |
  |--------|--------|------------------------------|
  |(1, 100)| 12     |      3                       |
  |(1, 11) | 3      |      2                       |
  |(1, 2)  | 2      |      1                       |
* Second round:
  | range  | choice | additional number of guesses |
  |--------|--------|------------------------------|
  |(1, 100)| 6      |      4                       |
  |(1, 5)  | 3      |      3                       |
  |(1, 2)  | 2      |      2                       |
  |(1, 1)  | 1      |      1                       |


The data structure will be updated to:
```
{(1,1): {1:1},
 (1,2): {1:2, 2:1.84},
 ...
 (1,5): {1:5, 2:4, 3:3, 4:4, 5:5}
 ...
 (1,11): {1:11, 2:10, 3:7.6, 4:8, 5:7, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11),
 ...
 (1,100): {1:100, ..., 6:76.8, ..., 12:71.8, ..., 100:100},
 ...
}
```

Further explanation: (1,2) with choice 2 is updated by the following:
* first round: 2 * 0.8 + 1 * 0.2 = 1.8
* second round: 1.8 * 0.8 + 2 * 0.2 = 1.84

**i. How to select an interger:**

Suppose now the possible range is (2, 5), and `_estimated_num_guesses` is:

```
{ ...,
 (2,5): {2:2.42, 3:1.80, 4:1.57, 5:2.13},
 ...
}
```

The probability to choose each number is inversely proportional to the "estimated" number of guesses to the power 5:
* P(select 2) = c/2.42^5
* P(select 3) = c/1.8^5
* P(select 4) = c/1.57^5
* P(select 5) = c/2.13^5

Note c is some value so that the sum of the probabilities above is 1.

**ii. How to update `_estimated_num_guesses`:**
1. For each round, store the choice for each of the corresponding range
  * For example:

  | range  | choice |
  |--------|--------|
  |(1, 100)| 12     |  
  |(1, 11) | 3      |   
  |(1, 2)  | 2      |    
2. Once the round is done, update `_estimated_num_guesses` with the formula stated above (i.e. previous_estimated_value * 0.8 + additional_number_of_guesses * 0.2)

---

## Instructions

1. Write the class definition for the class `LearningPlayer` in `src/player.py`. Its instances represent "learning" players using the "reinforcement learning" strategy described above. This class should have the same methods available as `Player`, but the behaviour of some methods is different
2. In the report, update Q3a part 3 so that the performance of `LearningPlayer` is also measured, compared and analysed. Answer the following: Do you think the `LearningPlayer` works? Why or why not? How one may improve the performance of `LearningPlayer`?

---

## Things to show in the report

* As mentioned in `Instructions`, part 2 needs to be shown in the report
