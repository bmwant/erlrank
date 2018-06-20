-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    Line = string:strip(io:get_line(File, ''), right, $\n),
    Numbers = [erlang:list_to_integer(Val) || Val <- string:lexemes(Line, " ")],
    SortedNumbers = lists:sort(Numbers),
    MinSum = lists:sum(lists:sublist(SortedNumbers, 4)),
    MaxSum = lists:sum(lists:sublist(lists:reverse(SortedNumbers), 4)),
    io:format("~p ~p~n", [MinSum, MaxSum]),
    file:close(File).
