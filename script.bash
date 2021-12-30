for filename in *.ipynb; do mv $filename ${filename%.ipynb}.py; done
