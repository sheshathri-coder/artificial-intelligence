% 20. Backward chaining
bird(sparrow).
can_fly(X):- bird(X).
% Query: ?- can_fly(sparrow).
% Output: true.