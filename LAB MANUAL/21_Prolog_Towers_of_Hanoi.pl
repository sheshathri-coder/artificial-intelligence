% 11. Towers of Hanoi
hanoi(1,A,B,C):- format('Move disk from ~w to ~w~n',[A,B]).
hanoi(N,A,B,C):- N>1, N1 is N-1, hanoi(N1,A,C,B), hanoi(1,A,B,C), hanoi(N1,C,B,A).
% Query: ?- hanoi(3,left,right,middle).
% Output: seven moves are displayed.