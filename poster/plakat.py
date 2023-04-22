from pylatex.section import Subsection
from pylatex import Command, Document, Section, Figure, SubFigure, NoEscape, Itemize, Tabular, Package, Enumerate
import frontmatter

import os, subprocess


class MyDocument(Document):

    def markdownInputBlock(self, mdFile):
        md = frontmatter.load(mdFile)
        self.append(Command("begin", arguments=["block", md['title']]))
        self.append(NoEscape("\\begin{markdown}\n"+md.content+"\n\\end{markdown}"))
        
        #self.append(Command("markdownInput", arguments=[mdFile]))
        #self.append(Command("end", "markdown"))
        self.append(Command("end", "block"))

if __name__ == '__main__':
    doc = MyDocument(default_filepath='plakat')
    mdFilesDir = "../content/dokumentation/"
    doc.documentclass = Command(
        'documentclass',
        arguments = 'beamer'
    )

    doc.packages.append(Package("markdown"))
    doc.packages.append(Package("beamerposter", options = ['orientation = landscape', 'size = a3', 'scale = 1.0']))
    doc.packages.append(Package("inputenc", "utf8"))
    doc.packages.append(Package("fontenc","T1"))
    doc.packages.append(Package("libertine"))
    doc.packages.append(Package("newtxmath","libertine"))
    doc.packages.append(Package("inconsolata","scaled=.92"))
    doc.preamble.append(Command("usetheme", NoEscape("LLT-poster")))
    doc.preamble.append(Command("usecolortheme", NoEscape("ComingClean")))
    doc.preamble.append(Command("title","PuzzlePalooza"))

    doc.preamble.append(Command("author","Simon Flückiger \& Daniel Schmocker","info@swissmakers.ch"))
    doc.preamble.append(Command("institute","Swiss Makers"))

    doc.preamble.append(NoEscape("\\footimage{\\includegraphics[width=4cm]{IMG_1934.jpg}}"))

    doc.append(NoEscape("\\begin{columns}[T]"))

    args = ["column", NoEscape(".32\\textwidth")]
    doc.append(Command("begin", arguments = args))
    doc.markdownInputBlock(mdFilesDir + "DasSpiel.md")
    doc.markdownInputBlock(mdFilesDir + "Das-Spiel als Projekt.md")
    doc.append(Command("end", arguments = ["column"]))
    
    
    args = ["column", NoEscape(".32\\textwidth")]
    doc.append(Command("begin", arguments = args)) 
    doc.markdownInputBlock(mdFilesDir + "Das Projekt.md")
    doc.append(Command("end", arguments = ["column"]))

    args = ["column", NoEscape(".32\\textwidth")]
    doc.append(Command("begin", arguments = args)) 
    doc.markdownInputBlock(mdFilesDir + "Das Projekt.md")
    doc.append(Command("end", arguments = ["column"]))


    doc.append(Command("end", "columns")) 

    print("compiling pdf")
    doc.generate_tex()
    doc.generate_pdf(clean_tex=False, compiler="pdflatex", compiler_args = ["--shell-escape"])

    #subprocess.run("open plakat.pdf", shell=True, check=True)