#!/usr/bin/env python3

import os, subprocess
from pathlib import PurePath, Path
import re
import argparse
from datetime import datetime
import shutil

parser = argparse.ArgumentParser()

parser.add_argument('--source_folder', dest='source_folder', help='Source folder to scan for code files; the search will be recursive to all subfolders', required=True)
parser.add_argument('--output_folder', dest='output_folder', help='Output folder where temporary files will be generated and processed including final PDF', required=True)
parser.add_argument( '--file_extension', dest='file_extension', type=str, default='c', help='file extension of source code file (e.g. cpp, py, java), defaults to .c extension')
parser.add_argument( '--syntax_language', dest='syntax_language', type=str, default='c', help='e.g.  \'c\',\'java\',\'python\',\'sql\',  check supported programming languages at https://www.overleaf.com/learn/latex/Code_Highlighting_with_minted, defaults to c syntax' )


args = parser.parse_args()


latex_template1 =r"""\documentclass[letterpaper]{article} 

                        \usepackage{blindtext}
                        \usepackage[letterpaper, margin=.4in]{geometry}

                        \usepackage{caption}
                        \usepackage[newfloat]{minted}
                        \captionsetup[listing]{position=top}


                        \usepackage[varqu]{zi4}
                        \renewcommand{\theFancyVerbLine}{
                            \fontfamily{zi4} \textcolor[rgb]{0.5,0.5,1.0}
                            {\small\oldstylenums{\arabic{FancyVerbLine}}}
                        }

                        \begin{document}
                            
                        \begin{center} \bf{File: """

latex_template2=     r"""} \end{center}

                        \inputminted
                        [
                        frame=single,
                        numbersep=5pt,
                        frame=lines,
                        framesep=2mm,
                        xleftmargin=10pt,
                        linenos,
                        stepnumber=1,
                        breaklines=true,
                        fontfamily=zi4,
                        breaklines=true
                        ]
                        {"""

latex_template3=        r"""}
                        {"""
latex_template4=        r"""}
                        \end{document}
                        """


save_to_dir =  os.path.join(args.output_folder , datetime.now().strftime("_%Y_%b_%d_%a_%I_%M_%S_%p"))
Path(save_to_dir).mkdir(parents=True, exist_ok=True)

list_pdf_files = []

for root, dirs, files in os.walk(args.source_folder, topdown = False):
   for fname in files:
       if fname.endswith(args.file_extension):
            path_file = os.path.join(root, fname)
            save_file = os.path.join(save_to_dir, fname)

            print(path_file)
            
            tex_file = os.path.join(save_to_dir,fname)[:-1*len(args.file_extension)]+ 'tex'

            if not os.path.exists(tex_file):
                with open(tex_file, "w") as tex_file_p:
                    tex_file_p.write(latex_template1 + path_file.replace('_', r'\_') +latex_template2 + args.syntax_language + latex_template3 + path_file + latex_template4)

                print(tex_file)

                cmd = 'pdflatex -synctex=1 -interaction=nonstopmode --shell-escape -output-directory '+save_to_dir+' '+ tex_file
                print('processing : ' + cmd )
                process= subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                process_output = process.communicate()[0].decode('utf-8', errors='replace')
                print(process_output)

                list_pdf_files.append(tex_file[:-3]+'pdf')
            else:
               print('Skip existing: '+ save_file)

                       
# combine all pdf 
final_pdf_path = os.path.join(save_to_dir, 'print.pdf')
cmd = 'pdfunite '+ ' '.join(list_pdf_files) + ' '+final_pdf_path
print('processing : ' + cmd )
process= subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
process_output = process.communicate()[0].decode('utf-8')
print(process_output)

# os.system('google-chrome  "'+ final_pdf_path+'"')

print("done")
print("Final PDF is generated at: "+ final_pdf_path)