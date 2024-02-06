import boto3
from moto import mock_aws
from boto3_test import write_into_table

@mock_aws
def test_write_into_table():
    "Test the write_into_table with a valid input data"
    dynamodb = boto3.resource('dynamodb')
    table_name = 'test'
    table = dynamodb.create_table(TableName=table_name,
                                  KeySchema=[{'AttributeName': 'date', 'KeyType': 'HASH'}],
                                  AttributeDefinitions=[{'AttributeName': 'date', 'AttributeType': 'S'}],
                                  ProvisionedThroughput={
                                      'ReadCapacityUnits': 5,
                                      'WriteCapacityUnits': 5,
                                  }
                                  )
    data = {'date': '07-Oct-2020', 'company': 'qxf2 services', 'client': 1000}
    write_into_table(data, table_name)
    response = table.get_item(Key={'date': data['date']})
    actual_output = response['Item']
    assert actual_output == data

