import random

images = [
    "bag",
    "bat",
    "bed",
    "bicycle",
    "board_game",
    "book",
    "video_games",
    "hat",
    "piano",
    "pillow",
    "plushie",
    "racket",
    "shoes",
    "soccer_ball",
    "sweater",
    "Nintendo_Switch",
    "toys",
    "trampoline",
    "wallet",
    "watch"
]

# settings
setup = r"""\documentclass[12pt, a4paper]{article}
\usepackage[
a4paper, 
margin=1cm,
includehead,
headheight=16pt,
nomarginpar,% We don't want any margin paragraphs
]{geometry}
\usepackage{fancyhdr} % headers
\usepackage[normalem]{ulem} % underlining

\usepackage{graphicx} % Required for inserting images
\graphicspath{{images/}}

\usepackage{fontspec} % custom fonts
\setmainfont{MitsuEHandwriting}[
    Path=../MitsuEHandwriting/,
    Extension = .otf,
    UprightFont=*-R,
    BoldFont=*-B,
    ItalicFont=*Italic-R,
    BoldItalicFont=*Italic-B
    ]

\begin{document}
% Set the page style to "fancy"...
\pagestyle{fancy}
\fancyhf{} % clear existing header/footer entries
% We don't need to specify the O coordinate
\fancyhead[L]{Name:\uline{\hspace{13em}}}
\fancyhead[R]{Class:\uline{\hspace{2em}--\hspace{2em}}\hspace{2em} Number:\uline{\hspace{3em}}\hspace{2em}Date:  \uline{\hspace{2em}/\hspace{2em}}}
\renewcommand{\headrulewidth}{0pt}
"""

end = r"""
\end{document}"""

page_start = r"""
\centering
\begin{Huge}
\textbf{Birthday Present Bingo}
\end{Huge}%

\def\arraystretch{2}
\begin{tabular}{l}
    A: What do you want for your birthday? \\
    B: I want \underline{a new bicycle}. \\
\end{tabular}

\begin{center}
"""
page_begin_table = r"""
\def\arraystretch{1.5}
\begin{tabular}{|c|c|c|c|}
\hline
"""
page_end_table = r"""
\end{tabular}
\end{center}
"""

num_squares = 16
squares_per_line = 4
num_pages = 35
file_name = "birthday_gifts_bingo"
with open(f"./{file_name}//{file_name}"+".tex", mode='w') as f:
    f.write(setup)
    for pg_num in range(1,num_pages+1):
        f.write(f"% pg {pg_num} start\n")
        f.write(page_start)
        f.write(page_begin_table)

        random.shuffle(images)
        img_names = ""
        imgs = ""
        for i,img in enumerate(images):
            if i > num_squares-1:
                break
            img_names += img.replace("_", " ")
            imgs += "\\includegraphics[width=4cm,height=4cm,keepaspectratio]{"+f"{img}"+"}"
            #f.write("\\includegraphics[width=4cm,height=4cm,keepaspectratio]{"+f"{img}"+"}")
            if i % squares_per_line != squares_per_line-1:
                img_names += " & "
                imgs += " & "
                #f.write(" & ")
            else:
                f.write(imgs)
                f.write(" \\\\\n")
                f.write(img_names)
                f.write(" \\\\\n")
                f.write("\\hline\n")
                img_names = ""
                imgs = ""
            i += 1

        f.write(page_end_table)
        f.write(f"% pg {pg_num} end\n")
        f.write("\\clearpage\n\n")
    f.write(end)