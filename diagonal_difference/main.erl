-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    NLines = erlang:list_to_integer(string:strip(io:get_line(File, ''), right, $\n)),
    Matrix = read_arr(NLines, File, []),
    Result = diff(1, 1, Matrix, 0),
    io:format("~p~n", [Result]),
    file:close(File).

read_arr(N, File, Acc) when N > 0 ->
    Line = io:get_line(File, ''),
    Nums = line_to_nums(Line),
    read_arr(N-1, File, [Nums | Acc]);
read_arr(0, File, Acc) ->
    file:close(File),
    lists:reverse(Acc).

line_to_nums(Line) ->
    Numbers = string:lexemes(string:strip(Line, right, $\n), " "),
    [erlang:list_to_integer(N) || N <- Numbers].

diff(RowN, ColN, Matrix, Acc) when RowN =< length(Matrix) ->
    Row = lists:nth(RowN, Matrix),
    E1 = lists:nth(ColN, Row),
    E2 = lists:nth(length(Row)-ColN+1, Row),
    diff(RowN+1, ColN+1, Matrix, Acc+E1-E2);
diff(_, _, _, Acc) ->
    abs(Acc).
