move(1,X,Y,_):-
    write("top disk move from "),
    write(X),
    write(" to "),
    write(Y),
    write("\n").
move(N,X,Y,Z):-
    N>1,
    M is N-1,
    move(M,X,Z,Y),
    move(1,X,Y,Z),
    move(M,Z,Y,X).


%output
%==============================================
%?- move(3,source,destination,aux).
%top disk move from source to destination
%top disk move from source to aux
%top disk move from destination to aux
%top disk move from source to destination
%top disk move from aux to source
%top disk move from aux to destination
%top disk move from source to destination
%true 

%?- move(4,source,destination,aux).
%top disk move from source to aux
%top disk move from source to destination
%top disk move from aux to destination
%top disk move from source to aux
%top disk move from destination to source
%top disk move from destination to aux
%top disk move from source to aux
%top disk move from source to destination
%top disk move from aux to destination
%top disk move from aux to source
%top disk move from destination to source
%top disk move from aux to destination
%top disk move from source to aux
%top disk move from source to destination
%top disk move from aux to destination
%true 