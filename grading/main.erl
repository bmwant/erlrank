%% https://www.hackerrank.com/challenges/grading/problem
-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    N = erlang:list_to_integer(string:strip(io:get_line(File, ''), right, $\n)),
    Arr = read_arr(File, N, []),
    Res = [convert_grade(Grade) || Grade <- Arr],
    lists:map(fun(Val) -> io:format("~B~n", [Val]) end, Res),
    file:close(File).

read_arr(File, N, Acc) when N > 0 ->
    Num = erlang:list_to_integer(string:strip(io:get_line(File, ''), right, $\n)),
    read_arr(File, N-1, [Num | Acc]);
read_arr(File, _, Acc) ->
    file:close(File),
    lists:reverse(Acc).

convert_grade(Grade) ->
    Grade.
