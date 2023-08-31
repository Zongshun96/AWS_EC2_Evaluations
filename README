In this repo we have the ploting methods for our LIBRA paper.
The paper ([DOI](https://doi.ieeecomputersociety.org/10.1109/IC2E52221.2021.00028)) was published at IC2E2021(Best Paper Award). And the source code is [here](https://github.com/Zongshun96/LIBRA).

Note: the data to generate plots in LIBRA paper is [here](https://drive.google.com/drive/folders/1ovbW6YLqee70_TPF0sdomK7BYdMJX9XT?usp=sharing).


Run:
1. Configure your [AWS crecidentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#interactive-configuration)
1. For each autoscaling group (potentially ran with different controller, i.e., LIBRA or SPOCK, or configurations), 
    1. Set the autoscaling group name at `__main__` in `VM_utils.py`
    1. Run `python3 VM_utils.py` to pull running time information of all VM instances in the specified autoscaling group.
1. Copy the corresponding request logs to same place as the VM logs.
1. Set the data pathnames in `main_script.py`. Notice that req log and vm logs have to be added separately.
1. Create and activate a python virtual environment (`python3 -m venv venv` and `source venv/bin/activate`) and install dependancies from `requirements.txt` (`python3 -m pip install -r requirements.txt`)
1. Run `main_script.py` and the figures will be generated in a folder, `figs/`, in the current working directory

`main_script.py`
The main script, it calls all other ploting and utility functions.

Utility Functions (`Hybrid_utils.py`, `SLS_utils.py`, `VM_utils.py`)
They are the entry point for cost plot and status plots.

Ploting Functions (`plot_bar.py`, `plot_cdf.py`)
Basically the original code from you. some small changed to the plt.figure.

`requirements.txt`
```
Dependancies for the scripts
```

