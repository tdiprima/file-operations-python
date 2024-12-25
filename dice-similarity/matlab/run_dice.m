%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% run_dice.m
% Run DICE over specified folders.
% T DiPrima, 2016.10.26
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear; close all; clc; tic;

% Pathologist versus Ground Truth
seg_dir = 'data/pathologists/Anne/just-right/';
gt_dir = 'data/masks/groundTruth1/';

count = 0;
totalTileDice = 0;

name = 'anne_results.txt';
fid = fopen(name, 'w');
fprintf(fid, [name, '\n\n']);

files = dir([seg_dir, '*.txt']);
len = length(files);
for file = files'
    count = count + 1;
    filename = file.name;
    r = strrep(filename,'_gray-label.txt','');
    
    path1 = [seg_dir, filename];
    path2 = fullfile(gt_dir, [r, '_mask.txt']);
    
    fprintf('Evaluating file %d of %d: %s\n', count, len, filename);
    
    A = dlmread(path1, '', 1, 0);
    M = dlmread(path2, '', 1, 0);
    
    tileDice = dice( M, A );
    str = sprintf('%s \t %d', filename, num2str(tileDice));
    fprintf(fid, str);
    totalTileDice = totalTileDice + tileDice;
    
end

str = ['\n\ntotalTileDice = %d\n', totalTileDice];
fprintf(str);
fprintf(fid, str);

str = ['Evaluated ', num2str(count), ' tiles.\n'];
fprintf(str);
fprintf(fid, str);

finalScore = totalTileDice / len;
str = ['finalScore = %d / %d = %d\n', totalTileDice, len, finalScore];
fprintf(str);
fprintf(fid, str);

str = ['FINAL SCORE: ', num2str(finalScore), '\n'];
fprintf(str);
fprintf(fid, str);

fclose(fid);
beep; toc;
