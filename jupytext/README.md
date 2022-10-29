## jupytext

Paired notebooks via jupyter notebook or jupyterlab extension, synchronise the two representations

```
jupytext --sync notebook.ipynb
```

Or enable it directly in jupyter notebook or jupyterlab.

`Percent format`: format with explicit cell delimiters (# %%) supported by many IDEs.
`Light format`: to see fewer cell markers.

## nbdime

Use to compare notebook differences and merging Jupyter notebooks.

- Has a nice interface to visualize the changes in the web browser and with github.
- Can be configured to use nbdime when `git diff` is used in notebooks.
- Has merger to avoid problems 

```
nbdime config-git --enable --global
```

## jupyterlab-git
Jupyterlab extension for version control using git


