%% https://www.hackerrank.com/challenges/apple-and-orange/problem
-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input11.txt", [read]),
    [S, T, A, B, M, N | Values] = get_all_lines(File),
    Apples = lists:sublist(Values, M),
    Oranges = lists:sublist(Values, M+N-1, N),
    ApplesHits = count_hits(A, S, T, Apples, 0),
    OrangesHits = count_hits(B, S, T, Oranges, 0),
    io:format("~p~n~p~n", [ApplesHits, OrangesHits]),
    file:close(File).

count_hits(A, S, T, [D | Distances], Hits) ->
    if
        A + D >= S, A + D =< T ->
            count_hits(A, S, T, Distances, Hits+1);
        true ->
            count_hits(A, S, T, Distances, Hits)
    end;
count_hits(_, _, _, [], Hits) ->
    Hits.

get_all_lines(File) ->
    case io:get_line(File, '') of
        eof -> [];
        Line -> 
            lists:map(fun(Val) -> erlang:list_to_integer(Val) end, string:lexemes(string:strip(Line, right, $\n), " ")) ++ get_all_lines(File)
    end.
