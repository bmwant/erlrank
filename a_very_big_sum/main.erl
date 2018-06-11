-module(main).
-export([start/0]).


read_multiple_lines_as_list_of_strings(N) ->
    read_multiple_lines_as_list_of_strings(N, []).

read_multiple_lines_as_list_of_strings(0, Acc) ->
    lists:reverse(Acc);
read_multiple_lines_as_list_of_strings(N, Acc) when N > 0 ->
    read_multiple_lines_as_list_of_strings(N-1, [string:chomp(io:get_line("")) | Acc]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    NumbersCount = io:get_line(File, ''),
    Numbers = io:get_line(File, ''),
    NumbersList = string:lexemes(Numbers, " "),
    IntList = lists:map(fun(Val) -> erlang:list_to_integer(string:strip(Val, right, $\n)) end, NumbersList),
    Result = lists:sum(IntList),
    io:format("~p~n", [Result]),
    file:close(File).
