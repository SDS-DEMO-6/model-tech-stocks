Tech Stocks Price Model
==============

An example model using Ship Data Science for monitoring.

This model makes naive predictions
about the daily closing price of Google stock based on 
the last few day's closing prices for a commodities fund
and a NASDAQ-tracking fund.

Click on the below status badges to see detailed monitoring reports.

Ship Data Science can automatically push Github issues 
when monitoring detects important changes in the data or model's performance, enabling transparent, data-based
discussion, analysis, and prioritization of issues. Check out the issues section for examples.

Seem cool? Check out [Ship Data Science](http://www.shipdatascience.com)  

Monitoring Status Badges
--------------------
[ <img src="http://staging.shipdatascience.com/api/v1/badges?plugin_id=1&statsmodel_id=1&branch=master" > shipDataScience / Stability-Monitoring ](http://staging.shipdatascience.com/app#!/latest/1/master/1 ) 

How it works
-----------
Integrating a model with Ship Data Science monitoring is easy. Just write a .shipit.json file and connect your repository on ShipDataScience.com. 

Each monitoring module you add is just another entry in the 'plugins' list. Guides for choosing options for each plugin and more are available on the ShipDataScience website.

Example:
```
{
  "data" : {
    "module" : {
      "repositoryOwner" : "shipDataScience",
      "repositoryName" : "data-yahoo-finance", 
      "repositoryBranch" : "master"
    },
    "config" : {
      "tickers" : ["GOOG", "DBC", "QQQ"], 
      "lags" : [1,3,5],
      "startDate" : "2014-04-01"
    }
  },
  "scoring" : {
    "skipScoring" : false
  },
  "plugins" : [
    {
      "module" : {
        "repositoryOwner" : "shipDataScience",
        "repositoryName" : "Stability-Monitoring",
        "repositoryBranch" : "master"
      },
      "config": {
        "io" : {
          "strategy" : {
            "identifier" : "CSV",
            "options" : {
              "sep" : "\t"
            }
          }
        },
        "logging" : {
          "logLevel" : "INFO"
        },
        "report": {
          "period" : {
            "field" : "Date",
            "type" : "datetime",
            "benchmark" : {
              "startsAt" : "2014-04-01",
              "endsAt" : "2014-08-01"
            },
            "report" : {
              "startsAt" : "2014-08-01",
              "window" : {
                "type" : "calendar",
                "interval" : "monthly"
              },
              "discardLastPeriod" : true
            }
          },
          "fields" : {
            "included" : ["GOOG", "DBC", "QQQ"]
          },
          "quantiles": {
            "defaultNumberOfTiles" : 3
          }
        }
      }
    }
  ]
}


```


