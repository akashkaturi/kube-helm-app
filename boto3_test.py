import boto3
from decimal import Decimal


def write_into_table(item, table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    with table.batch_writer() as batch:
        batch.put_item(Item=item)


from pydantic import BaseModel
from boto3.dynamodb.types import TypeSerializer
from decimal import Decimal
import uuid


class Person(BaseModel):
    name: uuid.UUID
    age: Decimal


# Given Pydantic model object
person_obj = Person(name=uuid.uuid4(), age=12.4)

print(person_obj)

# Serialize Pydantic model object to dictionary
person_dict = person_obj.dict()

# Use TypeSerializer to convert dictionary to DynamoDB object
serializer = TypeSerializer()
dynamodb_object = {
    key: serializer.serialize(str(value)) if isinstance(value, uuid.UUID) else serializer.serialize(value) for
    key, value in person_dict.items()}

print(dynamodb_object)

from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
    name: str
    age: int
    phone_number: Optional[str] = None  # Making phone number field optional with a default value of None

# List of dictionaries representing objects
data_list = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 35}
]
for item in data_list:
    if d
# Apply the Person model to each dictionary in the list
person_objects = [Person(**data) for data in data_list]


# Now person_objects is a list of Pydantic model objects
for person in person_objects:
    print(person)

