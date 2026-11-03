% 12. Check whether a bird can fly

bird(eagle).
bird(penguin).

can_fly(eagle).

:- initialization(main).

main :-
    can_fly(eagle),
    write('Eagle can fly: true'),
    nl.