# Find lambda functions

You are given a Python script called `lambda_creator.py`.
Install the appropriate libraries (`boto3`), then run the script.
Once the script has finished execution, you should have a file called `functions.csv`.
This file contains numerous ARNs of lambda functions and their region.
However, only a handful of those functions exist, the rest of them are made up.

Your task is to load the functions from the created file and find out which ones actually exist.

## Delete the functions

Once you found the existing functions it is time to delete them.

Iterate through the functions by regions and delete them one by one.