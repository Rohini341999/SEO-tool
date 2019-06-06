# SEO-tool
An SEO tool for Beginners using xlsxwriter

Created by : Rohini Koli  
Project topic : SEO Analyser tool
Start date : 04-06-2019
End Date : 06-06-2019
Completion time : 16:53

Please read this whole for a better understanding of the project.

These are the Basic Functions that are covered in the following tool.

SEO Tool to analyze web pages.
1. Take a URL of a webpage from the user.
2. Perform the following actions using menu interface:
a. Find total number of scripts
b. Display a list of the script names.
c. Find total number of words excluding scripts and styles.
d. Display all keywords from meta tag.
e. Display all keywords along with their number of occurrences in the page(using dictionary)
f. Create an excel sheet containing the following data:
   A		B
  Keyword	Occurences
   XML		27
   Python	40
g. Create column chart to plot keywords on X axis and
   Occurences on Y axis.
 pythonproject.txt
 Displaying pythonproject.txt.

An output is attached to the repository as well for demo purposes i.e an excel sheet created using xlsxwriter.

Firstly a URL is taken from the user
Then Actions are performed i.e.
The script tags in particular html page are displayed.

What are <script> tags???
The HTML <script> element is used to embed or reference executable code; this is typically used to embed or refer to JavaScript code. The <script> element can also be used with other languages
This element includes the global attributes.

Then the data without script and style tags are displayed

Well then what are style tags in html?
The HTML <style> element contains style information for a document, or part of a document. It contains CSS, which is applied to the contents of the document containing the <style> element.
The <style> element can be included inside the <head> or <body> of the document, and the styles will still be applied, however it is recommended that you include your styles in the <head> for organizational purposes — it is a lot better to separate your content from your presentation as much as possible. Even better, put your styles in external stylesheets and apply them using <link> elements.

Then the real work of SEO tool begins that is finding out the keywords in meta tag
So let me explain u what is meta tag???
The HTML <meta> element represents metadata (data about data in a particular html page) that cannot be represented by other HTML meta-related elements, like <base>, <link>, <script>, <style> or <title>.
Most Probably UTF-8 is the Meta Characterset encoding algorithm used .

Then the Keywords and their occurrences are extracted which define on which rank a particular page can be set

and Apparently at the same time when your code runs an excel sheet with a table and a column chart is created and stored in the same directory as in where the project in your machine is stored.

*****************************************************************THANK YOU***********************************************************************
