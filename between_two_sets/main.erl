%% https://www.hackerrank.com/challenges/between-two-sets/problem
-module(main).
-export([start/0]).

nums(Line) ->
    [erlang:list_to_integer(Val) || Val <- string:lexemes(string:strip(Line, right, $\n), " ")].

is_factor(Val, L) ->
    lists:all(fun(X) -> X rem Val == 0 end, L).

are_factors(Val, L) ->
    lists:all(fun(X) -> Val rem X == 0 end, L).

start() -> 
    {ok, File} = file:open("input.txt", [read]),
    _ = io:get_line(File, ''),
    A = nums(io:get_line(File, '')),
    B = nums(io:get_line(File, '')),
    MaxA = lists:max(A),
    MinB = lists:min(B),
    Res = try
            length([Val || Val <- lists:seq(MaxA, MinB), is_factor(Val, B), are_factors(Val, A)]) 
        catch error:function_clause -> 0 end,
    io:format("~p~n", [Res]),
    file:close(File).

