% 16. Fruit and Color

fruit(apple, red).
fruit(banana, yellow).
fruit(grape, green).

:- initialization(main).

main :-
    fruit(apple, Color),
    write('Color of apple: '),
    write(Color),
    nl.