% 19. Forward Chaining

fact(sunny).

rule :-
    fact(sunny),
    write('It is sunny, so take an umbrella.'),
    nl.

:- initialization(main).

main :-
    rule.