You are given a string representing a sequence of N arrows, each pointing in one of the four cardinal directions: up ('^'), down ('v'), left ('<') or right ('>'). Write a function solution that, given a string S denoting the directions of the arrows, returns the minimum number of arrows that must be rotated to make them all point in the same direction.

Examples:
1. Given S = "^vv<v", the function should return 2. After rotating both the first ('^') and fourth ('<') arrows downwards ('v'), all of the arrows would point down.
2. Given S = "v>>>vv", the function should return 3. After rotating the first, fifth and sixth arrow rightwards, all of the arrows would point right.
3. Given S = "<<<" the function should return 0. All of the arrows already point left.

Assume that:
- N is an integer within the range [1..100];
- string S is made only of the following characters: '^', 'v', '<' and/or '>'.