This question involves some statistical components with a simple dice game involving a single six-sided dice. Each run involves a sequence of throws of the dice until two
consecutive throws each yield the value six which marks the end of the run. The length of a run is the number of throws in it. E.g.
 1 5 4 3 2 1 2 1 5 6 3 2 4 5 6 6 has length 16.
 i) Write a function play() that simulaes a single run of this game and that returns the run length as its result.
 ii) Write Python code based on the above to simulate 1000 runs of this game and that calculates the average and maximum run length.
 iii) Write Python cde based on the above to generate a simple histogram of the form as shown below. Each line represents the number of games whose length falls within the
 indicated range e.g 90-99. Assume each asterisk represents five runs so that four asters for 90-99 indicate 20 runs of that length. Assume that we need only consider runs
 of length < 200.
 0 - 9: ********************
 10 - 19: ***************
 20 - 29: ****************
 30 - 39: **********
 40 - 49: ********
 50 - 59: ******
 60 - 69: ********
 70 - 79: *****
 80 - 89: ******
 90 - 99: ***
 .
 .
 .
 190-199: 
