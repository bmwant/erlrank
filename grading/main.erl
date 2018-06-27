%% https://www.hackerrank.com/challenges/grading/problem
-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),


