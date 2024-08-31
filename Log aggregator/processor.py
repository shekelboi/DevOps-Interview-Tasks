# Count the number of ERROR messages by services

import json

with open('out.txt') as file:
    errors = {}
    for line in file:
        d = json.loads(line)
        service_name = d['service_name']
        if d['log_level'] == 'ERROR':
            if service_name in errors:
                errors[service_name] += 1
            else:
                errors[service_name] = 1
    print(errors)
