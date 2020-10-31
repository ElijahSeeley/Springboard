<img src="/Capstone2_Chess/Images/lichess_maintenance.jpg" width="500">

# Exploring Popular Chess Openings and Predicting the Winner

- - -

### 1. Introduction

Chess is becoming an [esport](https://www.chess.com/news/view/nakamura-tsm-deal-chess-esports) and with its popularity brings more reasons to do early analysis. We forsee analysis being used to place bets, determine players' marketability, and increase viewer engagement.
This project is the precursor to a much larger variation. The largest of chess datasets are saved as PGN files and because of space and hardware limitations we were unable to acquire,
clean, and process the ideal data in an appropriate timeframe for the deadline of this project. However, we were able to set the frame of future testing by developing the successful
methods that future data can be run through.

#### 1.1 Early Hopes

The plan of this project was to explore popular chess openings played on [Lichess](http://lichess.org) a popular free chess site that offers analytical tools for their players.
From these openings we wanted to see the victory rate by mate, resignation, timeouts. After this exploration we hoped to develop a machine learning algorithm that could determine
the opening played by these players by the games other items, such as player ranking, moves played, etc. without actually seeing the moves. After testing it was discovered that
we may not have enough data to provide the model in order to make this feasible. Either this or the model is destined to be unsuccessful, but another attempt will be made in the future.
Transitioning off of this goal it was settled that using the available items to train a machine learning algorithm to predict the winners of the games from these outside variables.
With our relatively small final dataset (about 11000 games) it would be interesting to see what was possible and what combinations of points would hurt or help the accuracy of the
machine learning algorithm.

### 2.The Data
[Data Wrangling](https://github.com/ElijahSeeley/Springboard/blob/master/Capstone2_Chess/Data%20Wrangling%20for%20Chess%20Games.ipynb)

The data was retrieved off from a user on [Kaggle](https://www.kaggle.com/datasnaek/chess) who was generous enough to provide a workable csv file by using Lichess's api to scrape some games from the Lichess server. Scraping from the server
is not the most efficient way to grab this data as all games cannot be scraped at once and only a little bit at a time by individual users or clubs. Because of the collection method it is important to note that this dataset does not represent an average set of chess games. Lichess does provide it's own
[database](https://database.lichess.org/) for users to get the games from - this is the data that will be used in the next experiment. 

#### 2.1 Subsetting the Data

We wanted to look for clusters of data that was useful for a model to understand. To achieve this it was important to drop a lot of island points. 
 - Dropped all games that lasted less than 5 moves as this either meant the player just had to leave or made a large blunder that resulted in an early checkmate. These were deemed not useful.
 - Only kept openings that consisted of at least 200 plays. From here our dataset shortened significantly, but we were able to shorten our openings down from 365 to 25.
Now that our data was ready for exploration it was time to develop some visualizations and find points of interest.

### 3.Exploration
[EDA](https://github.com/ElijahSeeley/Springboard/blob/master/Capstone2_Chess/Chess%20EDA.ipynb)

We were set on finding out what were the most popular openings played by players. So as an initial exploration the games were set in bargraph form with their opening eco. **Note: Opening eco's can contain multiple different versions of an opening. To make the dataset manageable, grouping by opening eco was determined the best way to keep the dataset under control. To learn more about opening eco please check out [this reference](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings).** However, with 365 different openings, the inital bargraph was hard to read. So we limited it down to games with at least 200 plays.

<img src="/Capstone2_Chess/Images/MostPopularOpenings.png" width="700">

Here we see that A00, the uncommon opening, is the most popular for these players. There can only be two explanations for this. Either the players were intentially playing very uncommon openings, or they were playing moves without understanding theory which resulted in openings that are irregular. In order to be fair we will assume a combination of these factors. The expected second and third popular varients are here with C00(King's pawn) and D00(Queen's pawn) - this is expected and intuitive for anyone who plays chess regularly. What was a bit unexpected is what came next when the games were separated between white and black victories. 

<img src="/Capstone2_Chess/Images/MostPopularOpenings_whiteVSblack.png" width="900">

We find here that many openings are lopsided towards white or black. While this is incredibly interesting and warrants further exploration, it is outside of the scope of this project. Initially we did have draws as their own bar graph. But, for some games the draws were insignificant. As with normal club play, draws are less likely to occur because miscalculated play is more frequent. We decided to add draws to black victories, as black is at a disadvantage in tempo from the beginning of the game and in tournament play, depriving white the points of a victory can determine result of an entire tournament. 

<img src="/Capstone2_Chess/Images/MostPopularOpenings_includingDrawsAsBlackWins.png" width="900">

While much did not change, it is interesting to note that it seems black is stronger in the E00 and D00 openings when draws are considered favorable. We look forward to analyzing larger datasets to see how far these points of interest go. 

While a player could go online and view sites like https://www.chessgames.com/ for historical percentages of openings. Chess is constantly evolving and personally we feel like only including the top level of play is ignoring the millions of players who are playing and making their own adjustments to the game. Thanks to the movement of chess to the digital realm, this once impossible form of exploration is now possible and may hold incredible data for players everywhere. 

### 4. Modeling
[Fitting the Data to Models](https://github.com/ElijahSeeley/Springboard/blob/master/Capstone2_Chess/Fitting%20the%20data%20to%20models.ipynb)

Modeling was done under various forms including logreg, KNN, decision trees, and SVM. It was determined that the decision tree classifier was the best combination of effectiveness and efficiency for our model. To prepare, we broke the opening eco down via one hot encoding and made sure to remove all draws from the game. This would allow the algorithm to simply choose between white and black as a winner. We have two versions of the model that are worth presenting.
The first uses a version of the dataset that includes turns, player elo(their skill level), the victory condition(mate, resign, timeout), and increment code(bullet, blitz, etc.) and of course the opening eco. Below are the results from depth 9.

                     precision    recall  f1-score   support

           Black       0.61      0.66      0.63      1579
           White       0.64      0.60      0.62      1632

    accuracy                               0.63      3211
    macro avg          0.63      0.63      0.63      3211
    weighted avg       0.63      0.63      0.63      3211
    
Here we see that the model was able to comfortable predict above 60% accuracy with all of these items. We condsider everything above 50% as significant as this means the engine is picking up on patterns that allow it to determine victories at a higher success rate than a simple coin toss. 

The second model uses a version of the dataset that removes everything except the opening eco. 

                    precision    recall  f1-score   support

           Black       0.73      0.19      0.30      1579
           White       0.54      0.93      0.69      1632

    accuracy                               0.57      3211
    macro avg          0.64      0.56      0.49      3211
    weighted avg       0.63      0.57      0.50      3211

This remarkable model was able to continue to predict above 50% with just the openings alone. Although the recalls are skewed, this gives hope for future model building. This also makes the point that the model is better off with items that were removed for this second iteration. Meaning that in the future if we can feed the models more meaningful data it may be strong enough to accurately predict tournament play, as such is done with sports betting and player purchasing now(the movie 'Moneyball' comes to mind). 

### 5. Conclusory Thoughts

While this implemntation is imperfect this project sets creates some points for moving forward with this form of chess analysis. Chess analysis is currently restricted to the highest form of competitive play. The chess engines are reliant on what games are fed to them, which is normally only the highest level of play. But here we may be able to give something useful to the average player. We may even be able to make discoveries in lower level play that enhances the competitive field. By pushing forward with model creation in determining the outcome of games we may even be able to assist chess's transition into the esport area by providing marketing type metrics. There are a lot of possibilities for the chess realm to explore with new age analytical techniques outside of engines and the future holds opportunity for unveiling rewarding information.
