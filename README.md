# Lab 2 README

## Reproduce Python

### Open Python Environment
Clone the reposetory using 
```
git clone https://github.com/accrawfish/lab2.git
```
With the environment.yml folder readily available, use Conda to set the python environment

```
conda env create -f environment.yml
conda activate lab2
jupyter lab
``` 
Open notebook in `script/PyNotebook.ipynb`  
Select Kernel → Restart Kernel and Run All Cells to run the notebook from beginning to end.

The rendered output is svaved as `PyNoteRendered.html`  

## Reproduce R 

### Open R Environment
Open note book in `script//RNotebook.Rmd` in R Studio  
Hit run -> Restart R and run all chunks

The rendered output is saved as `RNoteRendered.pdf`
```
#If having issues, use the bellow 
renv::restore(prompt = FALSE)
```

### Other Files
`AI_USAGE` describe my involvemnt of AI in resolving coding errors. The `environment.yml` and `renv.lock` is to help with reproducibility of the scripts. The `data` folder contains only the code to obtain the biostatistics/cilical data. These codes are included within both the R and Python scripts. Look at the bootom of the script for the question responses for the graduate addendum.
