% 20. Backward Chaining

bird(sparrow).

can_fly(X) :-
    bird(X).

:- initialization(main).

main :-
    can_fly(sparrow),
    write('Sparrow can fly: true'),
    nl.