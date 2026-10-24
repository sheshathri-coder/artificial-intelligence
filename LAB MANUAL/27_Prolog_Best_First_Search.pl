% 17. Best First Search
edge(a,b). edge(b,d). edge(d,e).
path(X,X,[X]).
path(X,Y,[X|P]):- edge(X,Z), path(Z,Y,P).
% Query: ?- path(a,e,P).
% Output: P = [a,b,d,e].