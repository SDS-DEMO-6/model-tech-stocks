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
Integrating a model with Ship Data Science monitoring is designed to be an exceptionally lightweight effort. Just write a .shipit.json file and connect your repository on ShipDataScience.com. Example:
```
{
  "scheduler" : {
    "runEveryTimeIncrement" : "month",
    "runOnCodeChange" : true
  },
  "data" : {
    "cloneUrl" : "git@github.com:shipDataScience/data-copy-paste.git",
    "repositoryBranch" : "master",
    "config": {
      "printMeOut" : "Hi! This is a test."
    }
  },
  "scoring" : {
    "skipScoring" : False,
    "config" : {}
  },
  "plugins" : [
    {
      "alias" : "two-class validity",
      "cloneUrl" : "git@github.com:shipDataScience/Stability-Monitoring.git",
      "repositoryBranch" : "master",
      "config": {}
    }
  ]
}
```


