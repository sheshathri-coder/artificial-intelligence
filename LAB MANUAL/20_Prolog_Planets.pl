% 10. Planets Database

planet(mercury, 1).
planet(venus, 2).
planet(earth, 3).
planet(mars, 4).

:- initialization(main).

main :-
    planet(earth, Number),
    write('Earth is planet number: '),
    write(Number),
    nl.