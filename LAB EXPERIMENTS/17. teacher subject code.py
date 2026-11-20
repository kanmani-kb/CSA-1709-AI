
student(101, 'Arun').
student(102, 'Priya').
student(103, 'Kumar').

teacher('Ravi', 'Python').
teacher('Anitha', 'AI').
teacher('Kumar', 'Prolog').

subject('Python', CS101).
subject('AI', CS102).
subject('Prolog', CS103).

details(ID, Name, Teacher, Code) :-
    student(ID, Name),
    teacher(Teacher, Sub),
    subject(Sub, Code).

