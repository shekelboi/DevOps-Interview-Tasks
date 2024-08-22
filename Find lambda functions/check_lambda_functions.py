import boto3
import csv

functions = {}
with open('functions.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        arn, region = row.values()
        if region in functions:
            functions[region].add(arn)
        else:
            functions[region] = {arn}

functions_found = {}
for region in functions:
    functions_in_region = set()
    client = boto3.client('lambda', region_name=region)

    marker = None
    while True:
        if marker:
            response = client.list_functions(Marker=marker)  # You can add MaxItems=1 for testing
        else:
            response = client.list_functions()  # You can add MaxItems=1 for testing

        functions_in_region.update(function['FunctionArn'] for function in response['Functions'])

        if 'NextMarker' not in response:
            break
        marker = response['NextMarker']

    functions_found[region] = functions[region].intersection(functions_in_region)

print('The following functions were found within the account:')
print(functions_found)

for region in functions:
    client = boto3.client('lambda', region_name=region)
    print(f'Deleting functions from region {region}')
    for function in functions_found[region]:
        client.delete_function(FunctionName=function)
