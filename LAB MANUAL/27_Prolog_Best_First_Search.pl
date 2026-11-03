% 17. Find a Path Between Two Points

edge(a, b).
edge(b, d).
edge(d, e).

find_path(X, X, [X]).
find_path(X, Y, [X|Path]) :-
    edge(X, Z),
    find_path(Z, Y, Path).

:- initialization(main).

main :-
    find_path(a, e, Path),
    write('Path from a to e: '),
    write(Path),
    nl.