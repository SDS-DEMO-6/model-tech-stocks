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
  "scheduler" : {
    "runEveryTimeIncrement" : "month",
    "runOnCodeChange" : true
  },
  "data" : {
    "ownerGithubUsername" : "shipDataScience",
    "repositoryName" : "data-yahoo-finance",
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
      "alias" : "Stability",
      "ownerGithubUsername" : "shipDataScience",
      "repositoryName" : "Stability-Monitoring",
      "repositoryBranch" : "master",
      "config": {
        "io" : {
          "strategy" : {
            "identifier" : "CSV",
            "sep" : "\t"
          }
        },
        "logging" : {
          "log_level" : "DEBUG"
        },
        "report": {
          "period" : {
            "period_field" : "Date",
            "period_type" : "time",
            "period_interval" : "30 day",
            "benchmark_starts_at" : "2014-04-01",
            "benchmark_ends_at" : "2014-08-01",
            "report_starts_at" : "2014-08-01"
          },
          "fields" : {
            "included" : ["GOOG", "DBC", "QQQ"]
          },
          "quantiles": {
             "default" : 5
          }
        } 
      }
    }
  ]
}
```


