import os
import subprocess
from pdf2image import convert_from_path
from PIL import Image

# Corrected LaTeX code for the monad diagram with accurate arrows
latex_code = r"""
\documentclass{standalone}
\usepackage{tikz}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[>=stealth, node distance=4cm, thick]
    % Black background
    \fill[black] (-2, -2) rectangle (6, 6);

    \node[green!30!black] (T) at (0, 0) {$\color{green!30!black} T$};
    \node[red] (TT1) at (4, 0) {$\color{red} T^2$};
    \node[red] (TT2) at (0, 4) {$\color{red} T^2$};
    \node[blue] (TTT) at (4, 4) {$\color{blue} T^3$};

    \draw[->, red] (TT1) to node [above, red] {$\mu$} (T);
    \draw[->, red] (TT2) to node [right, red] {$\mu$} (T);
    \draw[->, blue] (TTT) to node [left, blue] {$\mu T$} (TT1);
    \draw[->, blue] (TTT) to node [below, blue] {$T\mu$} (TT2);
\end{tikzpicture}
\end{document}
"""

# Save the LaTeX code to a .tex file
latex_file_path = "monad_diagram.tex"
with open(latex_file_path, "w") as f:
    f.write(latex_code)

# Compile the LaTeX file to PDF
subprocess.run(["pdflatex", latex_file_path], check=True)

# Convert the PDF to a PNG image
pdf_path = "monad_diagram.pdf"
png_path = "monad_diagram.png"
images = convert_from_path(pdf_path, dpi=300)
for image in images:
    image.save(png_path, "PNG")

# Resize the image to 1792x1792
img = Image.open(png_path)
img_resized = img.resize((1792, 1792), Image.LANCZOS)

# Convert the resized image to WEBP format
webp_path = "monad_diagram.webp"
img_resized.save(webp_path, "webp")

print("Conversion complete. Files saved as:")
print(f"PDF: {pdf_path}")
print(f"PNG: {png_path}")
print(f"WEBP: {webp_path}")
