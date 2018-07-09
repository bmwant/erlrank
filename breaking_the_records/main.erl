%% https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    _ = io:get_line(File, ''),
    Records = nums(io:get_line(File, '')),
    [Initial | Rest] = Records,
    {MinB, MaxB} = count(Rest, Initial, Initial, 0, 0),
    io:format("~p ~p~n", [MaxB, MinB]),
    file:close(File).

nums(Line) ->
    [erlang:list_to_integer(Val) || Val <- string:lexemes(string:strip(Line, right, $\n), " ")].

count([H|Rest], Min, Max, MinB, MaxB) ->
    case H of
        H when H < Min ->
            count(Rest, H, Max, MinB+1, MaxB);
        H when H > Max ->
            count(Rest, Min, H, MinB, MaxB+1);
        _Else ->
            count(Rest, Min, Max, MinB, MaxB)
    end;
count([], _Min, _Max, MinB, MaxB) ->
    {MinB, MaxB}.
