<div id="task"><h2 class="mod-hidden">Task description</h2><div id="task_description" class=""><div id="standard_task_description" class="protected"><div class="task-description-content">

<meta http-equiv="content-type" content="text/html; charset=utf-8">


<div id="brinza-task-description">
<p>Charlemagne, the King of Frankia, is considering building some castles on the border with Servia. The border is divided into N segments. The King knows the height of the terrain in each segment of the border. The height of each segment of terrain is stored in array A, with A[P] denoting the height of the P-th segment of the border. The King has decided to build a castle on top of every hill and in the bottom of every valley.</p>
<p>Let [P..Q] denote a group of consecutive segments from P to Q inclusive such that (0 ≤ P ≤ Q ≤ N−1). Segments [P..Q] form a hill or a valley if all the following conditions are satisfied:</p>
<blockquote><ul style="margin: 10px;padding: 0px;"><li>The terrain height of each segment from P to Q is the same (A[P] = A[P+1] = ... = A[Q]);</li>
<li>If P &gt; 0 then A[P−1] &lt; A[P] (for a hill) or A[P−1] &gt; A[P] (for a valley);</li>
<li>If Q &lt; N−1 then A[Q+1] &lt; A[Q] (for a hill) or A[Q+1] &gt; A[Q] (for a valley);</li>
</ul>
</blockquote><p>That is, a hill is higher than its surroundings and a valley is lower than its surroundings. Note that if the surroundings on either side of the hill or valley don't exist (i.e. at the edges of the area under consideration, where P = 0 or Q = N−1), then the condition is considered satisfied for that side of the hill/valley.</p>
<p>The king is wondering how many castles is he going to build. Can you help him?</p>
<p>For example, consider the following array A = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5].</p>
<img class="inline-description-image" src="https://codility-frontend-prod.s3.amazonaws.com/media/task_static/castle_building/03bd15fc353d522d6f1897e92836f70a/static/images/castle_building.png"><p>There are two hills: [3..3] and [11..11]. There are also two valleys: [0..1] and [8..9]. There are no other suitable places for castles.</p>
<p>Write a function:</p>
<blockquote><p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(A)</tt></p></blockquote>
<p>that, given an array A consisting of N integers, as explained above, returns the total number of hills and valleys.</p>
<p>For example, given array A as described above, the function should return 4.</p>
<p>Given array A = [−3, −3] describing segments with a terrain height below 0, segment [0..1] forms both a hill and a valley, and only one castle can be built, so the function should return 1.</p>
<p>Assume that:</p>
<blockquote><ul style="margin: 10px;padding: 0px;"><li>N is an integer within the range [<span class="number">1</span>..<span class="number">100,000</span>];</li>
<li>each element of array A is an integer within the range [<span class="number">−1,000,000,000</span>..<span class="number">1,000,000,000</span>].</li>
</ul>
</blockquote><p>Complexity:</p>
<blockquote><ul style="margin: 10px;padding: 0px;"><li>expected worst-case time complexity is O(N);</li>
<li>expected worst-case space complexity is O(1) (not counting the storage required for input arguments).</li>
</ul>
</blockquote></div>
<div style="margin-top:5px">
<small>Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.</small>
</div>

</div></div></div><div class="under-task"><div id="test_cases_area" class=""><div><ul class="test-case-list"></ul><div class="add-test-case test-case-row" tabindex="0"><div class="wide"><span class="title">Custom test cases</span><span class="case-format">format: [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]</span></div><div class="right counter">0/10</div><div class="right plus"><img src="/static/img/cui/add.png"></div></div></div></div><div id="accessible_test_cases_area"></div></div></div>
