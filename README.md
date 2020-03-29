# Data Version Control - Example.

## Setup / Use

- Clone
- dvc init in terminal
- dvc add data/data.csv  this adds new data.
- dvc get can grab data from a dvc repo
- dvc add moves the actual data file to the cache directory 
- The dvc push command allows one to upload data to remote storage. It doesn't save any changes in the code or DVC-files
- run dvc pull to get the data from the remote.
- need to have aws configure setup with the credentials required.
- you can also treat a local directory as the remote if you want.
- using dvc import you get data from another source and keep its versioning information.
- DVC commands do not impact the code, this is for git.


## Notes

- If using Mac you need to ensure activation of the virtual environment occurs in the directory ``env/bin/activate`` whereas for Windows the directory is ``env/Scripts/activate``. The Makefile will need modified in this way to reflect your OS.

## Resources

- https://dvc.org/doc/tutorials/get-started/initialize


create a model pipeline stage to preprocess data, DVC its output and generate a dvc stage file.

dvc run -f preprocessing.dvc \
        -d src/preprocessing.py -d data/data.csv \
        -o data/preprocessed \
        python src/preprocessing.py data/data.csv