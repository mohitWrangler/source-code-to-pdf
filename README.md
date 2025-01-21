
  
About
-----------------

This is a Python code to generate a PDF file with syntax-highlighted source code listings taken from provided folder containing source code files. The code will recursively look for all files within some folders of the provided folder. 

My motivation for such a program was to generate PDF and then being able to print the code for offline analysis. The Python code executes pdflatex and pdfunite programs to generate the final PDF. The pdflatex uses minted package to provide syntax highlighting for the code. I have tested the Python code in Ubuntu 22.04 LTS. Feel free to modify the Python code to customize it to your case. 

Requirements
-----------------

Make sure `pdfunite` and `pdflatex` command works in your system with minted package dependencies installed. You can try running `pdflatex` on text.tex file and `pdfunite` on pdf

  

Code Use
--------------

The Python code can be executed as follows:

`python3 print_code.py [-h] --source_folder SOURCE_FOLDER --output_folder OUTPUT_FOLDER [--file_extension FILE_EXTENSION] [--syntax_language SYNTAX_LANGUAGE]`

options:\
`-h, --help`<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; show this help message and exit

`--source_folder SOURCE_FOLDER`\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Source folder to scan for code files; the search will be recursive to all subfolders

`--output_folder OUTPUT_FOLDER`\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output folder where temporary files will be generated and processed including final PDF

 
`--file_extension FILE_EXTENSION`\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the file extension of source code files (e.g. cpp, py, java), defaults to .c extension

  

`--syntax_language SYNTAX_LANGUAGE`\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. 'c','java','python','sql', check supported programming languages at https://www.overleaf.com/learn/latex/Code_Highlighting_with_minted, defaults to c syntax  

  

Example
---------------
`python3 print_code.py --source_folder ~/Documents/model_code --output_folder ~/Downloads --file_extension 'spthy' --syntax_language 'cpp'`
