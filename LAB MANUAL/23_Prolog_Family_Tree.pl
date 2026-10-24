% 13. Family tree
parent(ravi,arun). parent(arun,kiran).
father(X,Y):- parent(X,Y).
% Query: ?- father(ravi,arun).
% Output: true.