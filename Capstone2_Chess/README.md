<img src="Capstone2_Chess/Images/lichess_maintenance.jpg" width="500">

# Exploring Popular Chess Openings and Predicting the Winner

- - -

### 1. Introduction

This project is the precursor to a much larger variation. The largest of chess datasets are saved as PGN files and because of space and hardware limitations we were unable to acquire,
clean, and process the ideal data in an appropriate timeframe for the deadline of this project. However, we were able to set the frame of future testing by developing the successful
methods that future data can be run through.

#### 1.1 Early Hopes

The plan of this project was to explore popular chess openings played on [Lichess](http://lichess.org) a popular free chess site that offers analytical tools for their players.
From these openings we wanted to see the victory rate by mate, resignation, timeouts. After this exploration we hoped to develop a machine learning algorithm that could determine
the opening played by these players by the games other items, such as player ranking, moves played, etc. without actually seeing the moves. After testing it was discovered that
we may not have enough data to provide the model in order to make this feasible. Either this or the model is destined to be unsuccessful, but another attempt will be made in the future.
Transitioning off of this goal it was settled that using the available items to train a machine learning algorithm to predict the winners of the games from these outside variables.
With our relatively small final dataset (sub 2000 games) it would be interesting to see what was possible and what combinations of points would hurt or help the accuracy of the
machine learning algorithm.

### 2.The Data
The data was retrieved off from a user on [Kaggle](https://www.kaggle.com/datasnaek/chess) who was generous enough to provide a workable csv file by using Lichess's api to scrape some games from the Lichess server. Scraping from the server
is not the most efficient way to grab this data as all games cannot be scraped at once and only a little bit at a time by individual users or clubs. Lichess does provide it's own
[database](https://database.lichess.org/) for users to get the games from - this is the data that will be used in the next experiment. 

#### 2.1 Subsetting the Data

We wanted to look for clusters of data that was useful for a model to understand. To achieve this it was important to drop a lot of island points. 
 - Dropped all games that lasted less than 5 moves as this either meant the player just had to leave or made a large blunder that resulted in an early checkmate. These were deemed not useful.
 - Only kept openings that consisted of at least 200 plays. From here our dataset shortened significantly, but we were able to shorten our openings down from 365 to 25.
Now that our data was ready for exploration it was time to develop some visualizations and find points of interest.

