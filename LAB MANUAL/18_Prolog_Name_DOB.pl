% 8. Name and Date of Birth Database

person(arun, '10-05-2004').
person(bala, '12-08-2003').
person(cathy, '21-01-2005').

:- initialization(main).

main :-
    person(arun, DOB),
    write('Arun DOB: '),
    write(DOB),
    nl.