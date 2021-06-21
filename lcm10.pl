gcd(X,Y,G):-X=Y,G=X.
gcd(X,Y,G):-
    X<Y,
    Y1 is Y-X,
    gcd(X,Y1,G).
gcd(X,Y,G):-
    X>Y,
    gcd(Y,X,G).
lcm(X,Y,L):-gcd(X,Y,G),
    L is X*Y//G.


%output
%=========
%?- lcm(12,16,L).
%L = 48 .
%
%?- lcm(2,12,L).
%L = 12 .