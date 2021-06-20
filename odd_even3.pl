go:- write("Enter a number"),nl,
     read(X),
     odd_even(X).


     odd_even(X):- A is mod(X,2),
                    A=0,
                    write("even"),nl.
     
     odd_even(X):- A is mod(X,2),
                    A=1,
                    write("odd"),nl.



%output
%==========
%?- go.
%Enter a number
%|: 4.
%even
%true .

%?- go.
%Enter a number
%|: 5.
%odd