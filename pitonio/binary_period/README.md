<div id="task"><h2 class="mod-hidden">Task description</h2><div id="task_description" class=""><div id="standard_task_description" class="protected"><div class="task-description-content">

<meta http-equiv="content-type" content="text/html; charset=utf-8">


<div id="brinza-task-description">
<p>Consider a non-empty string S = <tt style="white-space:pre-wrap">S[0]S[1]...S[Q-1]</tt> consisting of Q characters. The <i>period</i> of this string is the smallest positive integer P such that:</p>
<blockquote><ul style="margin: 10px;padding: 0px;"><li>P ≤ Q / 2 and</li>
<li>S[K] = S[K+P] for every K, where 0 ≤ K &lt; Q − P.</li>
</ul>
</blockquote><p>For example, 8 is the period of "<tt style="white-space:pre-wrap">codilitycodilityco</tt>" and 7 is the period of "<tt style="white-space:pre-wrap">abracadabracadabra</tt>".</p>
<p>A positive integer M is the <i>binary period</i> of a positive integer N if M is the period of the binary representation of N.</p>
<p>For example, 4 is the binary period of 955, because the binary representation of 955 is "<tt style="white-space:pre-wrap">1110111011</tt>" and its period is 4.</p>
<p>You are given an implementation of a function:</p>
<blockquote><p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(N)</tt></p></blockquote>
<p>This function, when given a positive integer N, returns the binary period of N. The function returns −1 if N does not have a binary period.</p>
<p>For example, given N = 955 the function returns 4, as explained in the example above.</p>
<p>The attached code is still <b><b>incorrect</b></b> on some inputs. Despite the error(s), the code may produce a correct answer for the example test cases. The goal of the exercise is to find and fix the bug(s) in the implementation. You can modify at most <b><b>two</b></b> lines.</p>
<p>Assume that:</p>
<blockquote><ul style="margin: 10px;padding: 0px;"><li>N is an integer within the range [<span class="number">1</span>..<span class="number">1,000,000,000</span>].</li>
</ul>
</blockquote><p>In your solution, focus on <b><b>correctness</b></b>. The performance of your solution will not be the focus of the assessment.</p>
</div>
<div style="margin-top:5px">
<small>Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.</small>
</div>

</div></div></div><div class="under-task"><div id="test_cases_area" class=""><div><ul class="test-case-list"></ul><div class="add-test-case test-case-row" tabindex="0"><div class="wide"><span class="title">Custom test cases</span><span class="case-format">format: 955</span></div><div class="right counter">0/10</div><div class="right plus"><img src="/static/img/cui/add.png"></div></div></div></div><div id="accessible_test_cases_area"></div></div></div>
