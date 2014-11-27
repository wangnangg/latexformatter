latexformatter
==============

Format your latex source code to a nice looking form. And for those who use sublime text as an editor, the indents make it possible to fold your code.

latexfmt.pl is a program written by Andrew Stacey that can format latex source code.

lattexindent.py is to add indents so that sublime text can fold the source code.

#Example Usage:#

	latexfmt.pl -i 4 source.tex > target.tex
	latexindent.py -i 4 target.tex > indentedtarget.tex
