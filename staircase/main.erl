-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    N = erlang:list_to_integer(string:strip(io:get_line(File, ''), right, $\n)),
    print_stair(N, 1),
    file:close(File).

print_stair(N, Iter) when Iter =< N ->
    print(" ", N-Iter),
    print("#", Iter),
    io:format("~n", []),
    print_stair(N, Iter+1);
print_stair(N, Iter) when Iter > N ->
    ok.

print(Ch, N) when N > 0 ->
    io:format("~s", [Ch]),
    print(Ch, N-1);
print(_, 0) ->
    ok.
