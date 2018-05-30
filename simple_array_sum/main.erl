-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    NumbersCount = io:get_line(File, ''),
    Numbers = io:get_line(File, ''),
    NumbersList = string:lexemes(Numbers, " "),
    Result = sum(NumbersList, 0),
    io:format("~p~n", [Result]),
    file:close(File).

sum([Head|Tail], Acc) ->
    sum(Tail, Acc+erlang:list_to_integer(Head));
sum([], Acc) ->
    Acc.
