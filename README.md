Tech Stocks Price Model
==============

An example model using Ship Data Science for monitoring.

This model makes naive predictions
about the daily closing price of Google stock based on 
the last few day's closing prices for a commodities fund
and a NASDAQ-tracking fund.

Click on the below status badges to see detailed monitoring reports.

Check out the Github issues section of this repository.
 One of the coolest features of Ship Data Science is the ability to automatically push Github issues 
when monitoring detects important changes in the data or model's performance, enabling transparent, data-based
discussion, analysis, and prioritization of issues.

Seem cool? Check out [Ship Data Science](http://www.shipdatascience.com)  

Monitoring Status Badges
--------------------
[![Status Badge for Stability ](http://staging.shipdatascience.com/api/v1/badges?plugin_id=1&statsmodel_id=1 "Stability") Stability Monitoring](http://staging.shipdatascience.com/api/v1/report_summary?statsmodel_id=1&plugin_id=1)


How it works
-----------
Integrating a model with Ship Data Science monitoring is designed to be an exceptionally lightweight effort. Just write a .shipit.json file and connect your repository on ShipDataScience.com. Example:
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
          "log_level" : "DEBUG"
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


