
person('Arun', '2003-05-12').
person('Priya', '2004-08-20').
person('Kumar', '2002-11-15').
person('Ravi', '2003-03-10').

display(Name) :-
    person(Name, DOB),
    write('Name: '),
    write(Name),
    nl,
    write('DOB: '),
    write(DOB).
