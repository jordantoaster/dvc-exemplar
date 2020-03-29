# Project Overview

This project gives a basic overview of how versioning for both data and models can be performed using DVC. 

Scripts are provided to simulate data preparation and training.

The core goal is to showcase how to merge data, code and models into a single retreivable snapshot using GIT.

## Setup

1. Clone the repostory locally.

2. Setup a virtual environment by running the command ``make`` which kicks off the single Make command. This also packages our dependencies.

3. Ensure you have AWS credentials setup, to allow S3 to be used as a remote file store.

4. Given this repository has already setup DVC, you will not need to run ``dvc init`` or ``dvc remote add...``. For reference the remote used in this project is: ``dvc remote add -d s3remote s3://dvc-exemplar/artifact-versioning``

5. The data will not exist in your local workspace at this point, you will need to run ````

## DVC Workflow




## Notes



## Resources



dvc add [file or folder] - this puts the data in the cache

dvc push - pushes to remote and links the md5 hash locally with it.

Each thing added gets a dvc file to enable a local ref.

IF a data file is modified, you run dvc add, which modifies the .dvc file, you then version this in git. If you change verion of branch you can retrieve the older version of the data.

using git tag to make data and model snapshots easy to find is possible 
git tag -a "v1.0" -m "model v1.0, 1000 images"

Then you can run
git checkout v1.0
dvc checkout
to get the code and the data associated together, single versioned snapshapt.

On the other hand, if we want to keep the current code, but go back to the previous dataset version, we can do something like this:
git checkout v1.0 data.dvc
dvc checkout data.dvc
When we run git checkout we restore pointers (DVC-files) first. Then, when we run dvc checkout, we use these pointers to put the right data in the right place.
for experimental work, using new code on old data.

get some intermediate data.
python src/preprocessing.py data/data.csv

get a new model version
python src/train.py data

Need to add info on how to pull the data when it is cloned.