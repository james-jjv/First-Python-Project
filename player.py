'''
A module containing player classes for a number guessing game
'''

import random

class Player:
    '''
    A class to represent a player in a number guessing game
    '''
    
    def __init__(self):
        '''
        initialises the possible guess interval, number of guesses, current guess and record of previous games
        '''
        self.interval = [1, 100]  # possible range of guesses, inclusive
        self.num_guesses = 0  # number of guesses already made
        self.current_guess = None
        self._historical_num_guesses = []  # number of guesses required in previous rounds

    def guess(self):
        '''
        guesses a random number within the possible interval

        Returns
        -------
        self.current_guess : 1 <= int <= 100
            last guess made on current round

        '''
        self.num_guesses += 1
        self.current_guess = random.randint(self.interval[0], self.interval[1])  # randomly choose a guess from the possible interval
        return self.current_guess

    def outcome(self, result):
        '''
        updates the interval based on outcome of previous guess and records total number of guesses to reach correct answer
        '''
        if result == 'too low':
            self.interval[0] = self.current_guess + 1  # increase lower bound of interval to 1 greater than the last guess
        elif result == 'too high':
            self.interval[1] = self.current_guess - 1  # decrease upper bound of interval to 1 less than the last guess
        else:
            self._historical_num_guesses.append(self.num_guesses)  # if correct, record number of guesses required
            self.num_guesses = 0  # reset values
            self.interval = [1, 100]

    def record(self, n):
        '''
        produces a list of results of the last n rounds played containing the number of guesses made

        Parameters
        ----------
        n : int
            the most recent number of rounds to be displayed (length of the list)

        Returns
        -------
        self._historical_num_guesses[-n:] : list
            a list containing the number of guesses of the most recent n rounds played

        '''
        return self._historical_num_guesses[-n:]  # slice the last n games played


class MinPlayer(Player):
    '''
    A class to represent a player who always guesses the minimum possible value in a number guessing game
    '''
    
    def __init__(self):
        '''
        initialises the possible guess interval, number of guesses, current guess and record of previous games through inheritance
        '''
        Player.__init__(self)  # inherit the Player() class variables
    
    def guess(self):
        '''
        guesses the minimum number within the possible interval

        Returns
        -------
        self.current_guess : 1 <= int <= 100
            the next guess to be made, the minimum possible value
            
        '''
        self.num_guesses += 1
        self.current_guess = self.interval[0]  # guess is always the lower bound
        return self.current_guess


class MiddlePlayer(Player):
    '''
    A class to represent a player who always guesses the middle value in the possible interval in a number guessing game
    '''
    
    def __init__(self):
        '''
        initialises the possible guess interval, number of guesses, current guess and record of previous games through inheritance
        '''
        Player.__init__(self)
    
    def guess(self):
        '''
        guesses the middle value in the possible interval

        Returns
        -------
        self.current_guess : 1 <= int <= 100
            the next guess to be made, the middle possible value

        '''
        self.num_guesses += 1
        self.current_guess = round((self.interval[1] + self.interval[0]) / 2)  # guess the middle (median) of the remaining range
        return self.current_guess


class LearningPlayer(Player):
    '''
    A class to represent a player in a number guessing game that adapts based on outcomes of previous rounds
    '''
    
    def __init__(self):
        '''
        initialises the starting weights of each guess
        '''
        Player.__init__(self)
        self._current_round_guesses = {}  # a dictionary with the current interval as the key, and a list containing the guess made and the number of additional guesses required as a result as the value
        self._estimated_num_guesses = {}  # a dictionary containing all the possible intervals for a guess at any given point in the form of a tuple as the key (e.g. (3, 59)), and another dictionary as the corresponding value containing all the possible guesses within that interval as keys, and the estimated number of guesses remaining if that guess is made as the value
        for i in range(1, 101):  # populating the dictionary
            for j in range(i, 101):  # second loop covers all possible interval combinations
                temp = {}
                for k in range(i, j+1):
                    temp[k] = max(j-k+1, k-i+1)  # formula used to crudely estimate the remaining number of guesses for that guess
                self._estimated_num_guesses[(i,j)] = temp
    
    def guess(self):
        '''
        guesses a random number based on weighted probabilities within the possible interval

        Returns
        -------
        self.current_guess : 1 <= int <= 100
            the next guess to be made

        '''
        self.num_guesses += 1
        self.choices = []  # represents possible choices for each guess in order
        self.proportional_probabilities = []  # represents the weighted likelihood of each choice being selected
        
        for choice, weight in self._estimated_num_guesses[tuple(self.interval)].items():  # all possible guesses that can be made on this round based on the interval, and their respective weights
            self.choices.append(choice)  # populate the list with the possible choices
            self.proportional_probabilities.append(1/((weight)**5))  # the probability to choose each number is inversely proportional to the estimated number of guesses to the power of 5 (an arbitrary formula used to update probabilities)
            
        self.current_guess = random.choices(self.choices, self.proportional_probabilities)[0]  # [0] indexed because random.choices() returns a list of length 1 but we require an integer, select randomly based on weighted probabilities

        self._current_round_guesses[tuple(self.interval)] = [self.current_guess, self.num_guesses] # record which guess was made during each round for a given possible interval of guesses 
        
        return self.current_guess
    
    def outcome(self, result):
        '''
        updates the interval based on outcome of previous guess and updates the weights of each guess based on round performance

        Parameters
        ----------
        result : str
            outcome representing too high, too low or correct guess

        Returns
        -------
        None.

        '''
        if result == 'too low':
            self.interval[0] = self.current_guess + 1
        elif result == 'too high':
            self.interval[1] = self.current_guess - 1
        else:
            counter = 0
            for interval, guess_and_num_guesses in self._current_round_guesses.items():
                self._current_round_guesses[interval][1] = self.num_guesses - counter  # update intervals and guesses with actual number of additional guesses required before guess was made, which is now known after guessing the correct number
                counter += 1
                
            # note: the above and below loop are identical, but have been separated to increase readability, and to allow easier editing, as self._current_round_guesses is fully populated before entering the second loop
            
            for interval, guess_and_num_guesses in self._current_round_guesses.items():  # updating the weights and predicted number of additional guesses required for those guesses made in the previous round based on their performance
                previous_estimated_value = self._estimated_num_guesses[interval][guess_and_num_guesses[0]]
                actual_additional_guesses = guess_and_num_guesses[1]  # number of additional guesses required after a certain guess was made
                new_num_guess = (0.8 * previous_estimated_value) + (0.2 * actual_additional_guesses)  # the updated predicted number of guesses for a certain guess within an interval according to the formula shown
                
                self._estimated_num_guesses[interval][guess_and_num_guesses[0]] = new_num_guess  # updating the predicted number of additional guesses needed
            
            self._historical_num_guesses.append(self.num_guesses)  # record the number of guesses required this round
            self.num_guesses = 0
            self.interval = [1, 100]
            self._current_round_guesses = {}  # reset the intervals and number of guesses required this round