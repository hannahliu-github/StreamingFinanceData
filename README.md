# StreamingFinanceData
Real-time stock data analysis for STA9760 Project III

I created an application to analyze streaming data in python. The data is intraday stock prices for 10 companies in 1-minute periods. I created AWS Lambda functions for downloading and processing the data from Yahoo Finance, then saving in an AWS S3 bucket. I used AWS Athena to support querying the data from the S3 bucket. This technology stack can be used to query streaming data in near real time. 

### Lambda Configuration
![DataCollector Lambda Configuration](DataCollector_configuration.png)