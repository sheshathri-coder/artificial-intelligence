% 15. Monkey and Banana Problem

has_box(monkey).
can_climb(monkey).
banana_reachable.

can_get_banana(monkey) :-
    has_box(monkey),
    can_climb(monkey),
    banana_reachable.

:- initialization(main).

main :-
    can_get_banana(monkey),
    write('Monkey can get the banana: true'),
    nl.