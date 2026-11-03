% 9. Student, Teacher and Subject Database

student(arun).
teacher(ravi).
subject(ai).
teaches(ravi, ai).
studies(arun, ai).

:- initialization(main).

main :-
    studies(Student, ai),
    write('Student studying AI: '),
    write(Student),
    nl.