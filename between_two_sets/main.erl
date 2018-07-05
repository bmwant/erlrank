%% https://www.hackerrank.com/challenges/between-two-sets/problem
-module(main).
-export([start/0]).

start() -> 
    {ok, File} = file:open("input.txt", [read]),
    file:close(File).
