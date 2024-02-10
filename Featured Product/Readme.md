# Featured Products 
An e-commerce site tracks the purchases made each day. The product that is purchased ALL the most one day is the featured product for the following day. If there is a tie for the product purchased most frequently, those product names are ordered alphabetically ascending and the last name in the list is chosen.

**Example**

products = *['redShirt', 'greenPants', 'redShirt', 'orangeShoes', 'blackPants', 'blackPants']*

* *greenPants* and *orangeShoes* were purchased once.
* *redShirt* and *blackPants* were each purchased 2 times on the given day.
* After ordering the products alphabetically ascending, *redShirt* is the last product listed.
* *redShirt* is the featured product for the following day.

**Function Description**

Complete the function featuredProduct in the editor below. 

*featuredProduct* has the following parameter(s):

string products[n]: an array of strings where each represents a purchased product 

Returns: string: the name of the featured product

**Constraints**

* 1 ≤ n ≤ 10<sup>4</sup>

## Input Format For Custom Testing 

Input from stdin will be processed as follows and passed to the function: 
The first line contains an integer *n*, the number of elements in products. Each of the n subsequent lines contains a string that describes *products[i]* where *0 ≤ i < n*.

### Sample Case 1

#### Sample Input
```
STDIN       Function
---         ---
8           ➔ products[] size n = 8
greenShirt  ➔ products = ['greenShirt', 'bluePants', 'redShirt', 'blackShoes', 'redPants', 'redPants', 'whiteShirt', 'redShirt']
bluePants
redShirt
blackShoes
redPants
redPants
whiteShirt
redShirt
```
**Sample Output**

redShirt

**Explanation** 

* *greenShirt*, *bluePants*, *blackShoes*, and *whiteShirt* were each purchased 1 time.
* *redShirt* and *redPants* were each purchased 2 times. 
* *redShirt* is the last product listed after ordering tne products alphabetically ascending: *redPants*, *redShirt*.
* *redShirt* is the featured product for the following day. 

