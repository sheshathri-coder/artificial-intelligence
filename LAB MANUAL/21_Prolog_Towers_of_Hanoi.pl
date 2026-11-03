% 11. Towers of Hanoi

move_disk(From, To) :-
    write('Move disk from '),
    write(From),
    write(' to '),
    write(To),
    nl.

hanoi(1, From, To, _) :-
    move_disk(From, To).
hanoi(N, From, To, Spare) :-
    N > 1,
    Previous is N - 1,
    hanoi(Previous, From, Spare, To),
    move_disk(From, To),
    hanoi(Previous, Spare, To, From).

:- initialization(main).

main :-
    hanoi(3, left, right, middle).