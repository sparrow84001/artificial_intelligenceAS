nsum(1,1).
nsum(N,S):-
    N>1,
    N1 is N-1,
    nsum(N1,S1),
    S is N+S1.


%output
%==========
%?- 
%|    nsum(10,S).
%S = 55 .
%?- nsum(11,S).
%S = 66 .