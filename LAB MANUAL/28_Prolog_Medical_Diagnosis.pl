% 18. Simple Medical Diagnosis

symptom(fever, cold).
symptom(cough, flu).
symptom(rash, allergy).

:- initialization(main).

main :-
    symptom(cough, Disease),
    write('Possible disease for cough: '),
    write(Disease),
    nl.