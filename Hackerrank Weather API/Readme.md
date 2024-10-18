# Retrieve and Parse Data

## Rest API 

You are responsible for collecting weather data from an external REST API service and parsing the results into a simplified format. In some cases, we may also only want to return records where the temperature is lower than n degrees.

## Problem Statement

For a given input, write a script using Python that will:

* Perform a GET request against the API service
    * The API endpoint is: **https://jsonmock.hackerrank.com/api/weather**
    * Queries can be refined with the following syntax: **/search?name={keyword}** where **{keyword}** is any string of characters
    * The query result is paginated and can be further accessed by appending to the query string &page=num where num is the page number.
* Parse the results into a list of comma separated strings, each consisting of: **city_name,temperature,wind,humidity**
* If specified, remove any results that contain a temperature equal to or greater than that given in the **max_temp** parameter

## API Schema

* **page**: the current page
* **per_page**: the maximum number of results per page
* **total**: the total number of records in the search result
* **total_pages**: the total number of pages to query to get all the results
* **data**: an array of JSON objects that contain weather records 

The data field in the response contains a list of weather records with the following schema:

* **name**: the name of the city
* **weather**: temperature recorded
* **status**: an array of wind speed and humidity records

## Output Format 
Filter records to include a given string in the keyword parameter. Return an array such that each element is a string of comma-separated values: **city_name, temperature, wind, humidity**.

For example, given the following record retrieved from the API:
```
{ 
  "name": "Adelaide",
  "weather": "15 degree",
  "status": [
    "Wind: 8Kmph",
    "Humidity: 61%"
  ]
} 
```

The simplified string returned by your script will be: **Adelaide,15,8,61**. If there are multiple matching records, return the list sorted by **city_name**.

### Function Description
Complete the function weatherStation(keyword, max_temp=None) in the editor below.

**weatherStation** has the following parameter(s):
* **_string_ keyword**: the string to search
* **_int_ max_temp**: records containing temperatures above this value should not be returned 

### Returns
**string[]**: the formatted weather data for each city