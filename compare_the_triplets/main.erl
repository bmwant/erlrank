-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    AliceTriplet = io:get_line(File, ''),
    BobTriplet = io:get_line(File, ''),
    ANumbers = string:lexemes(AliceTriplet, " "),
    BNumbers = string:lexemes(BobTriplet, " "),
    Result = cmp(ANumbers, BNumbers, 0, 0),
    io:format("~p ~p~n", Result),
    file:close(File).


cmp([F|FRest], [S|SRest], FirstScore, SecondScore) ->
    FInt = erlang:list_to_integer(string:strip(F, right, $\n)),
    SInt = erlang:list_to_integer(string:strip(S, right, $\n)),
    if 
        FInt =:= SInt ->
            cmp(FRest, SRest, FirstScore, SecondScore);
        FInt > SInt ->
            cmp(FRest, SRest, FirstScore+1, SecondScore);
        FInt < SInt ->
            cmp(FRest, SRest, FirstScore, SecondScore+1)
    end;
cmp([], [], FirstScore, SecondScore) ->
    [FirstScore, SecondScore].
