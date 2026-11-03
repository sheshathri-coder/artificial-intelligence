% 13. Simple Family Tree

parent(ravi, arun).
parent(arun, kiran).

father(X, Y) :-
    parent(X, Y).

:- initialization(main).

main :-
    father(ravi, arun),
    write('Ravi is the father of Arun: true'),
    nl.