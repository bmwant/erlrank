<div id="task"><h2 class="mod-hidden">Task description</h2><div id="task_description" class=""><div id="standard_task_description" class="protected"><div class="task-description-content">

<meta http-equiv="content-type" content="text/html; charset=utf-8">


<div id="brinza-task-description">
<p>Your monthly phone bill has just arrived, and it's unexpectedly large. You decide to verify the amount by recalculating the bill based on your phone call logs and the phone company's charges.</p>
<p>The logs are given as a string S consisting of N lines separated by end-of-line characters (ASCII code 10). Each line describes one phone call using the following format: <tt style="white-space:pre-wrap">"hh:mm:ss,nnn-nnn-nnn"</tt>, where <tt style="white-space:pre-wrap">"hh:mm:ss"</tt> denotes the duration of the call (in <tt style="white-space:pre-wrap">"hh"</tt> hours, <tt style="white-space:pre-wrap">"mm"</tt> minutes and <tt style="white-space:pre-wrap">"ss"</tt> seconds) and <tt style="white-space:pre-wrap">"nnn-nnn-nnn"</tt> denotes the 9-digit phone number of the recipient (with no leading zeros).</p>
<p>Each call is billed separately. The billing rules are as follows:</p>
<blockquote><ul style="margin: 10px;padding: 0px;"><li>If the call was shorter than 5 minutes, then you pay 3 cents for every started second of the call (e.g. for duration <tt style="white-space:pre-wrap">"00:01:07"</tt> you pay 67 * 3 = 201 cents).</li>
<li>If the call was at least 5 minutes long, then you pay 150 cents for every started minute of the call (e.g. for duration <tt style="white-space:pre-wrap">"00:05:00"</tt> you pay 5 * 150 = 750 cents and for duration <tt style="white-space:pre-wrap">"00:05:01"</tt> you pay 6 * 150 = 900 cents).</li>
<li>All calls to the phone number that has the longest total duration of calls are free. In the case of a tie, if more than one phone number shares the longest total duration, the promotion is applied only to the phone number whose numerical value is the smallest among these phone numbers.</li>
</ul>
</blockquote><p>Write a function:</p>
<blockquote><p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(S)</tt></p></blockquote>
<p>that, given a string S describing phone call logs, returns the amount of money you have to pay in cents.</p>
<p>For example, given string S with N = 3 lines:</p>
<tt style="white-space:pre-wrap">  "00:01:07,400-234-090
   00:05:01,701-080-080
   00:05:00,400-234-090"</tt>
<p>the function should return 900 (the total duration for number 400-234-090 is 6 minutes 7 seconds, and the total duration for number 701-080-080 is 5 minutes 1 second; therefore, the free promotion applies to the former phone number).</p>
<p>Assume that:</p>
<blockquote><ul style="margin: 10px;padding: 0px;"><li>N is an integer within the range [<span class="number">1</span>..<span class="number">100</span>];</li>
<li>every phone number follows the format <tt style="white-space:pre-wrap">"nnn-nnn-nnn"</tt> strictly; there are no leading zeros;</li>
<li>the duration of every call follows the format <tt style="white-space:pre-wrap">"hh:mm:ss</tt>" strictly (00 ≤ <tt style="white-space:pre-wrap">hh</tt> ≤ 99, 00 ≤ <tt style="white-space:pre-wrap">mm</tt>, <tt style="white-space:pre-wrap">ss</tt> ≤ 59);</li>
<li>each line follows the format <tt style="white-space:pre-wrap">"hh:mm:ss,nnn-nnn-nnn"</tt> strictly; there are no empty lines and spaces.</li>
</ul>
</blockquote><p>In your solution, focus on <b><b>correctness</b></b>. The performance of your solution will not be the focus of the assessment.</p>
</div>
<div style="margin-top:5px">
<small>Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.</small>
</div>

</div></div></div><div class="under-task"><div id="test_cases_area" class=""></div><div id="accessible_test_cases_area"></div></div></div>
