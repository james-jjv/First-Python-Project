# Q2 "Success paradox" (40 marks)

---
## Background

In this quesiton, we will work on the movie data based on the data from Kaggle (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). We want to investigate whether some "generalised friendship paradox" discussed in the paper "Generalized friendship paradox in complex networks: The case of scientific collaboration" is observed in the data. Essentially, we want to find out whether in general for actors, their co-actors are more "successful" than them in terms of the number of appearances in movies and also the average revenue.

---
## Data Description

From https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata, two csv files which contain information about 4803 movies were downloaded, merged and simplified. The processed data is then stored in a json file ([`data/movie.json`](data/movie.json)). Note that while the corresponding Kaggle page is called "TMDB 5000 Movie Dataset", there are only details about 4803 movies available in the dataset.

For each movie, the file contains information about the title, cast, budget, revenue and release_date, and is represented like the following:

```
{'title': 'Superman Returns',
 'cast': [{'id': 17271, 'name': 'Brandon Routh'},
  {'id': 1979, 'name': 'Kevin Spacey'},
  {'id': 7517, 'name': 'Kate Bosworth'},
  {'id': 11006, 'name': 'James Marsden'},
  {'id': 7489, 'name': 'Parker Posey'},
  {'id': 8924, 'name': 'Frank Langella'},
  {'id': 53492, 'name': 'Sam Huntington'},
  {'id': 2639, 'name': 'Eva Marie Saint'},
  {'id': 3084, 'name': 'Marlon Brando'},
  {'id': 53493, 'name': 'Kal Penn'},
  {'id': 53494, 'name': 'Tristan Lake Leabu'},
  {'id': 41318, 'name': 'David Fabrizio'},
  {'id': 1224391, 'name': 'Ian Roberts'},
  {'id': 1272955, 'name': 'Vincent Stone'},
  {'id': 193763, 'name': 'Jack Larson'},
  {'id': 243805, 'name': 'Noel Neill'},
  {'id': 1252837, 'name': 'Keegan Joyce'},
  {'id': 971458, 'name': 'Jordana Beatty'}],
 'budget': 270000000,
 'revenue': 391081192,
 'release_date': '2006-06-28'}
 ```

(there may be some more details but you can ignore them)

Note that it is not clear:
* Whether both budgets and revenues all in US dollars
* Whether the revenues are global revenue
* How these 4803 movies were selected

The page also does not seem to have explicitly stated whether the id is unique for each actor/actress.

---
## Instructions

Do the following:

0. Load the data from [`data/movie.json`](data/movie.json) and parse it using the function `load()` from the module `json`

  Note:
  * You are allowed to make use of the official document of `json` module (https://docs.python.org/3/library/json.html) to understand how to use `load()`
  * Make sure relative path is used when loading in the data

1. For each movie, get the actor pairs and create some data structure like a `dict` of `list` or `dict` of `set` to store a sequence of co-actors for each actor that has any co-actors. Example (if name is used to represent the corresponding actor):
```
{'Brandon Routh': set('Kevin Spacey', 'Kate Bosworth', ...),
 ...,
 Frank Langella': set('Brandon Routh', 'Kevin Spacey', ...),
 ...}
```

  Note:
  * Here we assume two actors are co-actors if they appear in the same movie at least once based on the "cast" information
    * If an actor (say `'actor_a'`) is a co-actor of `'actor_b'`, then `'actor_b'` is also a co-actor of `'actor_a'`
  * For each actor, there are two types of information can be used to represent the actor - `'id'` and `'name'`. Please consider which one is a better choice and state the assumptions you have made in the report
  * Each co-actor should only appear once in the corresponding `list` (or `set`)
    * For example, if `Kate Bosworth` and `Brandon Routh` appeared together in more than one movie, `Kate Bosworth` should still only appear once in the `list` (or `set`) that is representing the co-actors of `Brandon Routh`

2. For each actor, find the number of movies that s/he participated in and the average revenue of the movies that s/he participated in. You should use some data structure like a `dict`, with the actor as a key and a `list` with 2 numbers (one for the number of movies, another for the average revenue) as the value to store the results, something like the followings (if name is used to represent the corresponding actor):
```
{'Brandon Routh': [xx, yy],
 ...,
 'Frank Langella': [aa, bb],
 ...}
```

3. Using the data structures from (1) and (2), for each actor find out the average number of movies and average revenue of his/her co-actors. For example, if an actor has 3 co-actors (`'actor_a'`, `'actor_b'` and `'actor_c'`), and `'actor_a'` was in 3 movies. `'actor_b'` was in 5 movies whereas `'actor_c'` was in 1 movie. Then the average number of movies of his/her co-actors in is 3. Similar calculation for average revenue. Again, you should use some data structure like a `dict`, with the actor as a key and a `list` with 2 numbers (one for the _average_ number of movies, another for the _average_ revenue) as the value, something like the followings (if name is used to represent the corresponding actor):
```
{'Brandon Routh': [x, y],
 ...,
 'Frank Langella': [a, b],
 ...}
```

4. Convert the data structure from (2) and (3) into two `Pandas` data frames by using [`pd.DataFrame.from_dict()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html). With the use of some appropriate `Pandas` functionality, find out on average how likely we see an actor was involved in fewer movies than his/her co-actors, and has lower average revenue than this/her co-actors. For example, if there are 10,000 actors, 8,000 of them were in fewer movies than their co-actors, then it is 80%.

  Note:
  * You are allowed to use any functionality from `Pandas` and make related search

5. Based on (4), conclude whether the "success paradox" is observed (i.e. whether in general for actors, their co-actors are more "successful" than them in terms of the number of appearances in movies and the average revenue). Please also state the assumptions you have made, and discuss the limitations and possible improvement of your analysis

---
## Things to show in the report

* You may write all your code for this task in the [`src/report.ipynb`](`src/report.ipynb`), or modularise some of your code in some .py files. No matter which way you use, in the report you _must_ include:
  * Assumptions made in part 1
  * Result, explanation, assumptions, discussion of the limitations and possible improvement of analysis for part 4 and 5
* If you make use of any references for part 4 and/or 5, please state it in the report 
