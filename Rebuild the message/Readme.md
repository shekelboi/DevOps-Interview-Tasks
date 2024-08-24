# Rebuild the message

Your task is to rebuild a message that was cut into pieces.

Implement the function `rebuild_message(parts)` which receives
a list of strings as a parameter.

Each part I was cut off from the same message. You have to reconstitute this 
original message, based on the following rules:

* the message always starts with the character *A* and ends with the character *Z*
* two parts can be matched when the last character the first part corresponds to the first character of the second part
* when combining two parts in the output message, do not include the extremity characters twice
(e.g. "A---b" + "b---Z" gives "A---b---Z not "A---bb---Z")

`rebuild_message` must return the rebuilt message.

Constraints: 
* first characters are unique among
* each part has at least 2 characters and at most 1000 characters
* the solution is guaranteed to exist and to be unique
* *parts* is never None, contains at least one element and at most 100 elements
