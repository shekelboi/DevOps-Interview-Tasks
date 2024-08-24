# Problem Statement: 

You are provided with a data file containing lines of alphanumeric characters.

Each line represents a data sample that has been corrupted with extraneous information.
Your task is to focus solely on identifying and summing the highest value single digit from each line.
If a line contains no digits, the value for that line is considered to be zero.

**Consider the following lines:**

```
g7rkd8go2
hly3lm2z
snypk
q5tuvw3
bdOwp
xn8tyle
```

For each line, the highest digits are 8, 3, 0, 5, 0, and 8, respectively.
The sum of these highest digits is 24. 

## Task: 

Write a program that calculates the sum of the highest digits from each line,
even if the data file is extremely large.