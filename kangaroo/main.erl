%% https://www.hackerrank.com/challenges/kangaroo/problem
-module(main).
-export([start/0]).

is_round(Val) ->
    if
        floor(Val) == Val, Val >= 0 ->
            true;
        true ->
            false
    end.

start() ->
    {ok, File} = file:open("input.txt", [read]),
    Line = string:lexemes(string:strip(io:get_line(File, ''), right, $\n), " "),
    [X1, V1, X2, V2]= [erlang:list_to_integer(Val) || Val <- Line],
    End = try (X1*V2 - X2*V1) / (V2 - V1)
        catch error:badarith -> 0 end,
    Steps = (End - X2) / V2,
    case {is_round(End), is_round(Steps)} of
        {true, true} ->
            io:format("YES~n");
        _Else ->
            io:format("NO~n")
    end,
    file:close(File).
