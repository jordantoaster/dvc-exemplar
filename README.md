# Project Overview

This project gives a basic overview of how versioning for both data and models can be performed using DVC. 

Scripts are provided to simulate data preparation and training.

The core goal is to showcase how to merge data, code and models into a single retreivable snapshot using GIT.

In this project you can modify the data as you desire and generate a new model through running...

``python src/preprocessing.py data/data.csv``

then

``python src/train.py data``

which will take a given dataset, process the data and generate a new model from which you can play with the DVC workflow.

## Setup

1. Clone the repostory locally.

2. Setup a virtual environment by running the command ``make`` which kicks off the single Make command. This also packages our dependencies.

3. Ensure you have AWS credentials setup, to allow S3 to be used as a remote file store.

4. Given this repository has already setup DVC, you will not need to run ``dvc init`` or ``dvc remote add...``. For reference the remote used in this project is: ``dvc remote add -d s3remote s3://dvc-exemplar/artifact-versioning``

5. The data will not exist in your local workspace at this point, you will need to run ``dvc pull`` - this will put required files in the workspace.

## DVC Workflow

- When you have modified either a model or a data file, you will run ``dvc add [FILE|FOLDER]``. This command creates a .dvc file for each artifact you want to track and copies the file or folder to the DVC cache while also adding the file to the dvc .gitignore file to prevent it being added to GIT. Only the .dvc files need put into source control.

- When you want to push your artifact changes to a remote, you need to run ``dvc push``, which in this case, will put the data onto S3 with the rest of the data versions.

- For development ease, for each change in either your model or data its recommended to tag your GIT branch. 

e.g. ``git tag -a "v2.0" -m "model v2.0, 2000 images"``

This will enable you to do two things:

1. Restore a snapshot of the data, model and code associated with a tag:

``git checkout v1.0 dvc checkout``

2. Keep your current source code but load the data models associated with a tag:

``git checkout v1.0 data.dvc dvc checkout data.dvc``


## Development Use Cases

- In sandbox / EDA you will have several versions of a bulk dataset, from original to cleaned and others with other modifications. To this end, having a tagged history of the data in which you can pull the original dataset indepedent of code is valuable while avoiding any manual steps in getting data from a file store or even worse, putting data in a repository.

- In production, you will plan to train for new data. In this training process you can setup a either an automated or manual training process in which you use the latest data from a given source, then update the version history after the fact. 

e.g. New data -> file store -> pull new data into execution environment -> merge or replace data snf update Git history. This process is much more aligned to manual intervention process rather than automation.

- If something goes wrong in the deployed code, you can revert the git history to use both data and a model that is 'safe'.

- Model, code and data are connected to a single git history via the .dvc files and standard code source control.


## Notes

- Collaboration file conflicts are possible. For example if two developers change the same .dvc file, how do you resolve which one should be leveraged? It is possible to solve this by protecting the .dvc files and discussion in merge requests.

- It is also possible to take some of the heavy lifting from the user by combining DVC with Travis CI to version the data and models upon certain conditions. IE upon merge to a shared development branch.

## Resources

- DVC Official Documentation 
