-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    N = erlang:list_to_integer(string:strip(io:get_line(File, ''), right, $\n)),
    Numbers = string:strip(io:get_line(File, ''), right, $\n),
    NumbersList = string:lexemes(Numbers, " "),
    IntList = lists:map(fun(Val) -> erlang:list_to_integer(Val) end, NumbersList),
    {Pos, Neg, Zero} = calc(IntList, 0, 0, 0, N),
    io:format("~.6f~n~.6f~n~.6f~n", [Pos, Neg, Zero]),
    file:close(File).

calc([Head|Tail], PosC, NegC, ZeroC, N) ->
    if Head =:= 0 ->
            calc(Tail, PosC, NegC, ZeroC+1, N);
        Head < 0 ->
            calc(Tail, PosC, NegC+1, ZeroC, N);
        Head > 0 ->
            calc(Tail, PosC+1, NegC, ZeroC, N)
    end;
calc([], PosC, NegC, ZeroC, N) ->
    {PosC/N, NegC/N, ZeroC/N}.

