import boto3

client = boto3.client('sns','us-west-2')

def send_profitmsg(data):
        client.publish(PhoneNumber='+15519985623', Message='Current Robinhood Balance is :' + data + ' PROFIT ALERT: Your balance went in PROFIT, Take it out for the day')

def send_lossmsg(data):
        client.publish(PhoneNumber='+15519985623', Message='Current Robinhood Balance is :' + data + ' LOSS ALERT: Please make the adjustment')