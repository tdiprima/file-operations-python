function [ Dice ] = dice( a, b )
%DICE
%   Compute dice coefficient.

% Compute the sizes of the input point sets
Asize = size(a);
Bsize = size(b);

% Check if the points have the same dimensions
if Asize ~= Bsize
    error('The dimensions of points in the two sets are not equal');
end

a = (a>0);
b = (b>0);

common = numel(find(a == 1 & b == 1));
ca = numel(find(a == 1));
cb = numel(find(b == 1));

Dice = (2 * common) / (ca + cb);

end
