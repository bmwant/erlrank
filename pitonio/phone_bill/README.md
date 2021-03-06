## Task description

Your monthly phone bill has just arrived, and it's unexpectedly large. 
You decide to verify the amount by recalculating the bill based on your phone call logs and the phone company's charges.
The logs are given as a string S consisting of N lines separated by end-of-line characters (ASCII code 10). 
Each line describes one phone call using the following format: "_hh:mm:ss,nnn-nnn-nnn_", where "_hh:mm:ss_" denotes the duration of the call 
(in "_hh_" hours, "_mm_" minutes and "_ss_" seconds) and "_nnn-nnn-nnn_" denotes the 9-digit phone number of the recipient (with no leading zeros).
Each call is billed separately. The billing rules are as follows:

* If the call was shorter than 5 minutes, then you pay 3 cents for every started second of the call 
(e.g. for duration "_00:01:07_" you pay 67 * 3 = 201 cents).
* If the call was at least 5 minutes long, then you pay 150 cents for every started minute of the call 
(e.g. for duration "_00:05:00_" you pay 5 * 150 = 750 cents and for duration "_00:05:01_" you pay 6 * 150 = 900 cents).
* All calls to the phone number that has the longest total duration of calls are free. 
In the case of a tie, if more than one phone number shares the longest total duration, 
the promotion is applied only to the phone number whose numerical value is the smallest among these phone numbers.

Write a function:

```
def solution(S)
```

that, given a string S describing phone call logs, returns the amount of money you have to pay in cents.
For example, given string S with N = 3 lines:

```
00:01:07,400-234-090
00:05:01,701-080-080
00:05:00,400-234-090
```

the function should return 900 (the total duration for number 400-234-090 is 6 minutes 7 seconds, 
and the total duration for number 701-080-080 is 5 minutes 1 second; 
therefore, the free promotion applies to the former phone number).

Assume that:

* N is an integer within the range [1..100];
* every phone number follows the format "_nnn-nnn-nnn_" strictly; there are no leading zeros;
* the duration of every call follows the format "_hh:mm:ss_" strictly (00 ≤ hh ≤ 99, 00 ≤ mm, ss ≤ 59);
* each line follows the format "_hh:mm:ss,nnn-nnn-nnn_" strictly; there are no empty lines and spaces.
