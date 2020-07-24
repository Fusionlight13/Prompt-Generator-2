Quick-Prompt is a suite of input tools that are designed to get input with ease of use and readability. This program contains the following tools:
<ul>
	<li><b>Multi question input</b> with customizeable return types</li>
	<li><b>Menu input</b> that corresponds with integers</li>
	<li><b>Continuous input</b> to store multiple inputs of the same type</li>

</ul>


<h1>Functions and uses explained</h1>
<p><span style="color:red;">Note:</span> Inside this library, contains many functions to make this script work. Most of these cannot be manually invoked.</p>
<h2>question_init</h2>
<p>Can be invoked directly to trigger <b>Multi-input</b> responses. Parameter overview: <b>Questions</b>: This first parameter requires a list of questions. It can be any length as long as it matches the length of the next parameter, Answers. <b>Answers</b> have to be enclosed in a set of [] and the options to be given have to be enclosed in another list separated by comma's for each question. One special feature of this parameter is the <b>None</b> keyword. None in this context means, "whatever is specified". This could be int or str. This leads into the second to last parameter known as <b>none_type</b>. This is where you can insert the types for each None specified. This must be a list unless there is less than 2 none types. The ordering is <b>left to right</b>. The very last parameter is question_index. <b>question_index</b> converts the question given into integers that scale with the length of choices.</p>
<h2>Important things to consider</h2>
<p>If using None in an answer, it must be in a list and non_type must be specified.</p>
<p> None will always override question_index because no exact options would be given to use as an index.</p>
<p>Integers can be used but as a string in answers.
<h2>Examples(WIP)</h2>
<p>Scenario #1: Making a survey:</p>
<a href="https://pastebin.com/hNx5qyAU">View Example</a>