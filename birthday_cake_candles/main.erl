%% https://www.hackerrank.com/challenges/birthday-cake-candles/problem
-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    N = erlang:list_to_integer(string:strip(io:get_line(File, ''), right, $\n)),
    Numbers = string:strip(io:get_line(File, ''), right, $\n),
    NumbersList = [erlang:list_to_integer(Val) || Val <- string:lexemes(Numbers, " ")],
    Max = lists:max(NumbersList),
    Result = count(NumbersList, Max, 0),
    io:format("~p~n", [Result]),
    file:close(File).

count([Head|Tail], Val, Counter) when Head =:= Val ->
    count(Tail, Val, Counter+1);
count([Head|Tail], Val, Counter) ->
    count(Tail, Val, Counter);
count([], _, Counter) ->
    Counter.
    
