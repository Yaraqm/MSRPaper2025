# MSR-2025

# Leveraging LLM Enhanced Commit Messages to Improve Machine Learning Based Test Case Prioritization

**Conference Submission:** [Mining Software Repositories (MSR), 2025]

## Overview
This repository contains the codebase for the paper titled **"Leveraging LLM Enhanced Commit Messages to Improve Machine Learning Based Test Case Prioritization
"** submitted to **MSR2025**. This code is designed to assist in reproducing the experiments and results presented in the paper.

## Repository Structure
- `Fine_tuning_model.ipynb`: This file contains the code to fine tune the base llama model and create an adapter model.
- `Merge-models.ipynb`: This file allows you to merge the base model and adapter model you create to then use.
- `Count Vectorization.py`: Contains code to be added to TCP-ML model to properly proccess and vectorize commit messages using the count vectorization technique.
- `TF-IDF.py`: Contains code to be added to TCP-ML model to properly proccess and vectorize commit messages using the TF-IDF technique.
- `Durations.py`: Contains code to be added to TCP-ML model in order to record duration metric for prioritized tests.

## Requirements
- In order to run both ipynb files you will need an environment with a GPU.

## Usage
**Reference TCP-ML Model:** icst24 /HP Tuning SOTA 2023.ipynb
- this is file contained within a public github repository named icst24.

**Fine Tuning LLM:** In order to fine tune the LLM you will need a training set that contains a set of code diffs and corresponding examples of good commit messages. A small sample can be viewed here: https://zenodo.org/records/14060468. This link contains a subset of the training set we used to fine tune our model, due to size and organizational limitations we cannot publish the whole set, however, this sample can be used to indicate the format and structure needed. Once you have a training set, first go through the code in the Fine_tuning_model.ipynb, this will result in an adapter model. Once you have this adapter model you can go through the code in the Merge-models.ipynb file, this should result in a final usable fine-tuned model. 

Within the file there is a sample of the code used to enhance the commit messages as well as the engineered prompt, this can be used to enhance your set of commit messages.

**Implementing Messages as a Feature:** Once you have obtained your desired enhanced commit messages you will then need the above reference TCP-ML model. You can select which vectorization technique you would like to test (Count Vectorization or TF-IDF) and download the code from its corresponding python file. This code will need to be added to the reference TCP-ML model within the calcualte_afp_value(_) function. 

Next you will need to take the durations code and add it within the same function in the corresponding area. Then you can run the model and obtain the apfd and duration values that are printed out. If you would like to get the base values as well simply do not include the commit messages as a feature.

To run the TCP-ML model you will need a dataset that includes these columns 'Test_Identifier', 'Execution_Count', 'Test_Total', 'Failure_Count', 'Failure_Rate', 'Last_Failure_Age', 'Last_Failure', 'Last_Transition', 'Transition_Count', '#Files_Changed', '#Lines_Inserted', '#Lines_Deleted'.

## License
This code is licensed under the [MIT License](LICENSE).
