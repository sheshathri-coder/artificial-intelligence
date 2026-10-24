% 19. Forward chaining
fact(sunny).
rule :- fact(sunny), writeln('Take umbrella').
% Query: ?- rule.
% Output: Take umbrella
% true.