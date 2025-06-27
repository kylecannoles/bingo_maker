import random
import os

#settings
num_squares = 16
squares_per_line = 4
num_pages = 50
project_name = "schedule_bingo"
title = "My Schedule Bingo"
dialogA = "What time do you get up?"
underline = ["get up", "6:00", "clean my room", "clean your room", "4:00"]
dialogB = "I get up at 6:00." 
bold = ["my", "your"]
dialogA2 = "What time do you clean your room?"
dialogB2 = "I clean my room at 4:00."
file_name = project_name
graphics_path_list = ["images/","images/characters"]

word_list = True


for s in underline:
    dialogA = dialogA.replace(s, "\\underline{"+s+"}")
    dialogB = dialogB.replace(s, "\\underline{"+s+"}")

for s in underline:
    dialogA2 = dialogA2.replace(s, "\\underline{"+s+"}")
    dialogB2 = dialogB2.replace(s, "\\underline{"+s+"}")

for s in bold:
    dialogA2 = dialogA2.replace(s, "\\textbf{"+s+"}")
    dialogB2 = dialogB2.replace(s, "\\textbf{"+s+"}")

graphics_path_string = ""
for path in graphics_path_list:
    graphics_path_string += "{" + path + "}"

images = [os.path.splitext(f)[0] for f in os.listdir(f"./{project_name}/images") if f.endswith((".png", ".jpg", ".jpeg", ".gif"))]

word_table = r"""
\medskip
\def\arraystretch{1.5}%  1 is the default, change whatever you need
\begin{footnotesize}
\begin{tabular}{ccccc}
"""

for i,img in enumerate(sorted(images)):
    word_table += img.replace("_", " ")
    if i < len(images) and i % 5 != 4:
        word_table += " & "
    else:
        word_table += r" \\" + "\n"

word_table += r"""\end{tabular}
\end{footnotesize}
\medskip
"""

setup = r"""\documentclass[12pt, a4paper]{article}
\usepackage[
a4paper, 
margin=1cm,
includehead,
headheight=32pt,
nomarginpar,% We don't want any margin paragraphs
]{geometry}
\usepackage{fancyhdr} % headers
\usepackage[normalem]{ulem} % underlining

\usepackage{graphicx} % Required for inserting images
\graphicspath{""" + graphics_path_string + r"""}

\usepackage{tikz}
\usetikzlibrary{positioning,shapes.callouts} % for speech bubbles

\usepackage{array} % for '\newcolumntype' macro
\usepackage{verbatimbox}

\usepackage{fontspec} % custom fonts
\setmainfont{MitsuEHandwriting}[
    Path=../MitsuEHandwriting/,
    Extension = .otf,
    UprightFont=*-R,
    BoldFont=*-B,
    ItalicFont=*Italic-R,
    BoldItalicFont=*Italic-B
    ]
\setmonofont{MitsuEHandwriting4lines}[
    Path=../MitsuEHandwriting/,
    Extension = .otf,
    UprightFont=*-R,
    BoldFont=*-B,
    ItalicFont=*Italic-R,
    BoldItalicFont=*Italic-B
    ]

\newcolumntype{C}[1]{>{\centering\arraybackslash}m{#1}} % centered version of 'm' col. type

\begin{document}
% Set the page style to "fancy"...
\pagestyle{fancy}
\fancyhf{} % clear existing header/footer entries
\fancyhfinit{\bfseries\ttfamily}
% We don't need to specify the O coordinate
\fancyhead[L]{\Huge{Name:||||||||||||||}}
\fancyhead[R]{\Huge{Date:|||||||}}
\renewcommand{\headrulewidth}{0pt}
"""

end = r"""
\end{document}"""

page_start = r"""
\centering
\begin{Huge}
\textbf{""" + f"{title}" + r"""}
\end{Huge}%
\medskip

\begin{tikzpicture}
  \node at (-9, 0) (charA) {\includegraphics[width=3cm,height=3cm]{charA}};
  \node [inner sep=8pt, thick, draw, align=center,
         rectangle callout, rounded corners, callout relative pointer={(-1.5,-1.0)},
         above right = 0 and -2 cm of charA.north east]
    {""" + f"{dialogA}" + r"""};
  \node [inner sep=8pt, thick, draw, align=center,
         rectangle callout, rounded corners, callout relative pointer={(-1,0)},
         above right = -2 and 0 cm of charA.north east]
    {""" + f"{dialogA2}" + r"""};
  \node at (6, 0) (charB) {\includegraphics[width=3cm,height=3cm]{charB}};
  \node [inner sep=8pt, thick, draw, align=center,
         rectangle callout, rounded corners, callout relative pointer={(2,-1)},
         above left = -0.5 and 0 cm of charB.north west]
    {""" + f"{dialogB}" + r"""};
  \node [inner sep=8pt, thick, draw, align=center,
         rectangle callout, rounded corners, callout relative pointer={(2,0.5)},
         above left = -3.5 and 0 cm of charB.north west]
    {""" + f"{dialogB2}" + r"""};
\end{tikzpicture}

"""
page_begin_table = r"""
\def\arraystretch{1.5}%  1 is the default, change whatever you need
\medskip
\begin{tabular}{| C{4cm} | C{4cm} | C{4cm}| C{4cm}| }
\hline
"""
page_end_table = r"""
\end{tabular}
"""

with open(f"./{project_name}//{file_name}_p{num_pages}"+".tex", mode='w') as f:
    f.write(setup)
    for pg_num in range(1,num_pages+1):
        f.write(f"% pg {pg_num} start\n")
        f.write(page_start)
        if word_list:
            f.write(word_table)

        f.write(page_begin_table)
        random.shuffle(images)
        img_names = ""
        imgs = ""
        line_text = ""
        for i,img in enumerate(images):
            if i > num_squares-1:
                break
            line_text += img.replace("_", " ")
            line_text += " \\strut\n\n"
            line_text += "\\includegraphics[width=3.5cm,height=2.8cm,keepaspectratio]{"+f"{img}"+"}"

            img_names += img.replace("_", " ")
            imgs += "\\includegraphics[width=3cm,height=3cm,keepaspectratio]{"+f"{img}"+"}"
            if i % squares_per_line != squares_per_line-1:
                line_text += " & "
                img_names += " & "
                imgs += " & "
            else:
                f.write(line_text)
                #f.write(imgs)
                f.write(" \\\\\n")
                #f.write(img_names)
                #f.write(" \\\\\n")
                f.write("\\hline\n")
                line_text = ""
                img_names = ""
                imgs = ""
            i += 1

        f.write(page_end_table)
        f.write(f"% pg {pg_num} end\n")
        f.write("\\clearpage\n\n")
    f.write(end)
