-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    NumbersCount = io:get_line(File, ''),
    Numbers = io:get_line(File, ''),
    io:format("~p~p~n", [NumbersCount, Numbers]),
    NumbersList = string:lexemes(Numbers, " "),
    io:format("~p~n", [NumbersList]),
    file:close(File).
