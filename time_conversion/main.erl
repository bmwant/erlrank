%% https://www.hackerrank.com/challenges/time-conversion/problem
-module(main).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt", [read]),
    Line = string:strip(io:get_line(File, ''), right, $\n),
    [Hour, Minute, Rest] = string:lexemes(Line, ":"),
    Second = lists:sublist(Rest, 2),
    Marker = lists:sublist(Rest, 3, 2),
    if 
        Marker == "AM" ->
            if
                Hour == "12" ->
                    io:format("00:~s:~s~n", [Minute, Second]);
                true ->
                    io:format("~s:~s:~s~n", [Hour, Minute, Second])
            end;
        Marker == "PM" ->
            if
                Hour == "12" ->
                    io:format("~s:~s:~s~n", [Hour, Minute, Second]);
                true ->
                    HourInt = erlang:list_to_integer(Hour),
                    NewHour = HourInt + 12,
                    io:format("~w:~s:~s~n", [NewHour, Minute, Second])
            end
    end,
    file:close(File).
