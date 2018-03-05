# TowersOfHanoi

This is an implementation of the recursive "Towers of Hanoi" algorithm described at https://www.tutorialspoint.com/data_structures_algorithms/tower_of_hanoi.htm, with the condition that global variables cannot be used. I found it easier to implement using OO-techniques, but I am not an experienced programmer so this may be a very silly mistake.

example: to initialise the Towers of Hanoi problem for a source stack of "A", a destination stack of "B", and an auxillary stack of "C", with 4 discs initially on the source stack: `TowersOfHanoi("A", "B", "C", 4)`