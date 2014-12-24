Tech Stocks Price Model
==============

An example model using Ship Data Science for monitoring.

This model uses the period 2010-2013 as training data, and makes naive predictions 
about the daily closing price of Google stock based on the last few day's closing prices for Apple, Google, and Microsoft.

Click on the below status badges to see detailed monitoring reports!

Check out the Github issues section of this repository to see the automatically generated action items 
suggested by Ship Data Science, providing warnings when the data is changing and the model needs adjustment.

Seem cool? Check out [Ship Data Science](http://www.shipdatascience.com)

Monitoring Status Badges
--------------------

How it works
-----------
Integrating a model with Ship Data Science monitoring is designed to be an exceptionally lightweight effort. Just:

 - Write a scoring script that takes in file and out file parameters, that writes a scored data set to file.
 - Write a Dockerfile that runs your script.
 - Choose a data source and include it in your .shipit.json
 - Select monitoring plugins to run and include their info in .shipit.json
 - (Optionally) Select a frequency to run monitoring.




