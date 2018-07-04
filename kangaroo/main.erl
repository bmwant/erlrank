%% https://www.hackerrank.com/challenges/kangaroo/problem
-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    Line = string:lexemes(string:strip(io:get_line(File, ''), right, $\n), " "),
    [X1, V1, X2, V2]= [erlang:list_to_integer(Val) || Val <- Line],
    End = (X1*V2 - X2*V1) / (V2 - V1),
    if 
        floor(End) == End, End >= 0 ->
           io:format("YES~n");
        true ->
            io:format("NO~n")
    end,
    file:close(File).
