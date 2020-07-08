# Guess the Raptors' Score &#127798;

### A Simple Summer Web Project Using HTML, CSS and Python. 
Check out [guess-the-raptors-score/about](https://shivambhatoolaul.github.io/guess-the-raptors-score/about.html) for more information.
#

### a Quick Note on How I Update the Database:
I used a fairly simple method to maintain and update my database for the game, since this was my first time ever writing anything for the web. 

Essentially, the *clients* answer the questions for the game on a [Google Form](https://www.google.ca/forms/about/). From there, I feed the .csv data from the form into a Python [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html), create Player objects and perform the calculations needed for the game. Lastly, I use a method to export the needed data from the DataFrame to HTML and then I update the site. 

Here were the main pros and cons of this method:

###### Cons:
```diff
-- The site isn't being updated automatically after every game.
- "Clients" can enter the game as many times as they want.
```

###### Pros:
```diff
+++ I don't have to set-up an actual client and server.
+ I can review exactly what changes before every update.
```

Considering the amount of people playing the game and my beginner-level skills in web development, this seemed like the most effective method. Once I learn a bit more about servers and JS in my 3rd year of university, it might be interesting to re-make this, but at a much greater scale...
