import random
import boto3
import string
from random import randint
import csv

IAM_ROLE_NAME = 'lambda-test-role'
ACCOUNT_ID = boto3.client('sts').get_caller_identity()['Account']
REGIONS = ['us-east-2', 'us-west-1', 'us-west-2']
FUNCTIONS_PER_REGION = 5


def random_name(length=10):
    return ''.join(string.ascii_letters[randint(0, len(string.ascii_letters) - 1)] for i in range(length))


iam_client = boto3.client('iam')

lambda_trust_policy = """{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}"""

# Creating the IAM role for lambda if it does not exist
try:
    response = iam_client.create_role(RoleName=IAM_ROLE_NAME, AssumeRolePolicyDocument=lambda_trust_policy)
    print(f'Role {IAM_ROLE_NAME} created.')
except iam_client.exceptions.EntityAlreadyExistsException:
    print(f'Role {IAM_ROLE_NAME} already exists.')
    response = iam_client.get_role(RoleName=IAM_ROLE_NAME)

role_arn = response['Role']['Arn']
clients = [boto3.client('lambda', region_name=region) for region in REGIONS]

functions_created = []
fake_functions = []

total = FUNCTIONS_PER_REGION * len(REGIONS)
count = 0

for client in clients:
    # Adding fake functions
    fake_functions.extend(
        [(f'arn:aws:lambda:{client.meta.region_name}:{ACCOUNT_ID}:function:{random_name()}', client.meta.region_name)
         for i in range(FUNCTIONS_PER_REGION * 10)])

    res = client.list_functions()
    for i in range(FUNCTIONS_PER_REGION):
        result = client.create_function(FunctionName=random_name(),
                                        Role=f'{role_arn}',
                                        Code={'ZipFile': open('empty.zip', 'rb').read()},
                                        Runtime='python3.12',
                                        Handler='empty.py')
        functions_created.append((result['FunctionArn'], client.meta.region_name))
        count += 1
        print(f'==== {"%6.2f" % (count / total * 100)}% ====')

print(functions_created)

all_function_names = functions_created + fake_functions
random.shuffle(all_function_names)

with open('functions.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['function_arn', 'region'])
    writer.writeheader()
    for function in all_function_names:
        writer.writerow({'function_arn': function[0], 'region': function[1]})
