% 14. Diet Based on Disease

recommend_diet(diabetes, 'low sugar diet').
recommend_diet(hypertension, 'low salt diet').
recommend_diet(anemia, 'iron rich diet').

:- initialization(main).

main :-
    recommend_diet(diabetes, Diet),
    write('Recommended diet for diabetes: '),
    write(Diet),
    nl.