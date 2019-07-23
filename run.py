import boto3
from boto3.session import Session
from boto3.dynamodb.conditions import Key, Attr
import json

# `aws configure --profile dynamodb`で設定済み
session = Session(profile_name="dynamodb")

dynamodb = session.resource("dynamodb")

table = dynamodb.Table("sample_table_name")

response = table.scan()

for i in response["Items"]:
    print(json.dumps(i))
