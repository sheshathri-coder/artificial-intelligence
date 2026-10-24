% 9. Student, teacher and subject database
student(arun).
teacher(ravi).
subject(ai).
teaches(ravi,ai).
studies(arun,ai).
% Query: ?- studies(X,ai).
% Output: X = arun.