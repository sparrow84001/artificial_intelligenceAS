gcd(X,Y,G):-X=Y,G=X.
gcd(X,Y,G):-
    X<Y,
    Y1 is Y-X,
    gcd(X,Y1,G).
gcd(X,Y,G):-
    X>Y,
    gcd(Y,X,G).

%output
%=========
%?- gcd(12,16,G).
%G = 4 .