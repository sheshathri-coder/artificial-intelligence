% 15. Monkey and Banana problem
can_get_banana(monkey):- has_box(monkey), can_climb(monkey), banana_reachable.
has_box(monkey). can_climb(monkey). banana_reachable.
% Query: ?- can_get_banana(monkey).
% Output: true.