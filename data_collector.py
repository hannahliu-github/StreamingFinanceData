import json
import boto3
import os
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')
import yfinance 


def lambda_handler(event, context):
    # parameters
    tickers = "FB SHOP BYND NFLX PINS SQ TTD OKTA SNAP DDOG"
    startDay = '2020-05-14'
    endDay = '2020-05-15'
    
    # download data from yfinance
    data = yfinance.download(tickers=tickers, start=startDay, end=endDay, interval="1m")
    
    # list of tickers 
    tickerList = tickers.split()
    
    # initialize boto3 client
    fh = boto3.client('firehose', 'us-east-2')
    deliveryStream = 'DataTransformer'
    
    # transform data records to json and push to data stream
    for i in range(len(data.index)):
        ts = str(data.index[i])
        for name in tickerList:
            high = data['High'][name].iloc[i]
            low = data['Low'][name].iloc[i]
            datapoint = dict(high=high, low=low, ts=ts, name=name)
            
            # convert it to json
            as_jsonstr = json.dumps(datapoint)
            
            # push to firehose datastream
            fh.put_record(
                DeliveryStreamName=deliveryStream,
                Record={'Data': as_jsonstr.encode('utf-8')})
            
    return {"statusCode": 200, 'body': json.dumps(f'Done!')}