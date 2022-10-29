# Version management with Jupyter notebooks

## jupytext

Paired notebooks via jupyter notebook or jupyterlab extension, synchronise the two representations

```
jupytext --sync notebook.ipynb
```

Or enable it directly in jupyter notebook or jupyterlab.

`Percent format`: format with explicit cell delimiters (# %%) supported by many IDEs.
`Light format`: to see fewer cell markers.

Or use a configuration file to enable jupytext globally for all the notebooks or for a rootfolder, allowing to control the directory where the .py scripts will be saved too.

### Problems solved by jupytext
- Comparing git differences between versions locally and when doing PRs in Github (.py files are rendered correctly and can be compared in the web UI directly).
- Having instant synchronization enables the Data Scientist to take that script to start doing modifications to make it `production-ready`.

### Problems that doesn't solve
- Merging jupyter notebooks

## nbdime

Use to compare notebook differences and merging Jupyter notebooks.

- Has a nice interface to visualize the changes in the web browser and with github.
- Can be configured to use nbdime when `git diff` is used in notebooks.
- Has merger to avoid problems 

```
nbdime config-git --enable --global
```
### Problems solved by nbdime
- Merging jupyter notebooks effectively to avoid conflicts

## jupyterlab-git
Jupyterlab extension for version control using git.


