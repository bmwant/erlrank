%% https://www.hackerrank.com/challenges/apple-and-orange/problem
-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    Res = get_all_lines(File),
    io:format("~p~n", [Res]),
    file:close(File).

get_all_lines(File) ->
    case io:get_line(File, '') of
        eof -> [];
        Line -> Line ++ get_all_lines(File)
    end.
