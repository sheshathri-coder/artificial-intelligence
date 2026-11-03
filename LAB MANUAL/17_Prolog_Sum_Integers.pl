% 7. Sum of integers from 1 to N

sum_to_n(0, 0).
sum_to_n(N, Sum) :-
    N > 0,
    Previous is N - 1,
    sum_to_n(Previous, PreviousSum),
    Sum is PreviousSum + N.

:- initialization(main).

main :-
    sum_to_n(5, Sum),
    write('Sum of numbers from 1 to 5 = '),
    write(Sum),
    nl.