filename=$(basename "$1")
extension="${filename##*.}"
filename="${filename%.*}"
#DIR=$(dirname "$1")
pandoc --toc --number-sections -V lang=finnish  --include-in-header=styles.css --filter pandoc-citeproc -f markdown+example_lists+superscript+subscript -s $filename.$extension -o $filename.html
#pandoc --toc --number-sections -V lang=finnish  --include-in-header=styles.css --filter pandoc-citeproc -f markdown+example_lists+superscript+subscript -s aspekti_menneen_ajan_verbimuodoilla.Rmd -o aspekti_menneen_ajan_verbimuodoilla.html
