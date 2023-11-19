# Progress Report

> Each project team is required to submit a short progress report by the Nov 19, 2023 listing the progress made, remaining tasks, any challenges/issues being faced, etc. It will be graded based on completion with respect to addressing the following points: (1) Progress made thus far, (2) Remaining tasks, (3) Any challenges/issues being faced.

## Project Member(s)

Solo project (sole member and i.e. captain):

- Full name: **Swarup Ghosh**
- Net ID: **swarupg2**

## Progress

> (1) Progress made thus far

As per the sub-tasks presented in the project proposal, the following tasks have been now completed:

1. Data collection: Collection of data from GitHub in the form of *.sh, *.bat, .Dockerfile, etc.
2. Constructing/determining useful keywords for each OS category

For 1. data collection was done using Google Big Query which hosts public data containing code contents from all public GitHub repositories. Constructed different BigQuery SQL queries to collect Linux Shell Scripts, Windows Batch Files, Dockerfiles and stored them as CSVs. My current dataset consists of 15626 linux shell scripts, 2204 windows batch scripts and 1413 Dockerfile(s).

For 2. labelling based on operating systems was performed. Windows batch files collected were directly labelled as Windows OS, this was relatively easy step. For debian/ubuntu like OS, keywords like "debian", "ubuntu", "apt", "apt-get" etc. were used to determine OS base. Similarly, for "rhel", "fedora", "centos" and the "dnf", "yum" keywords were found helpful. 

4. Data pre-processing and indexing

For 4. currently, I'm half-way done as pre-processing have been done. The contents of Dockerfile(s) with RUN, CMD were extracted, for shell scripts empty lines were removed and keywords are tokenized. Yet, to proceed with indexing in later stage.


## Remaining

> (2) Remaining tasks

3. Creating rules for better filtering the different Operating Systems from raw data

For 3. it doesn't seem to be a mandatory required step at this time as in 2. I am performing data labelling directly and the same will be used later in the classifier. If needed, IR can be used in later display of results which is already part of 5.

5. Ranking the items in the database based upon evaluation from keyword search
6. Preparing data for a classifier based upon ranked data
7. Creating a small UI (either GUI or CLI) with the classifier

For 5., 6., 7. these are yet to taken upon. For classification I'm planning to experiment with basic ML classifiers like SVM, Logistic Regression, etc. Scikit-learn in python should be useful.

## Challenges and Issues

> (3) Any challenges/issues being faced.

Based upon initial data cleaning completion and dataset evaluation hold out set split, it can be possible that data doesn't train well on any classifier. At that step more data collection could be required, but this should be straight-forward as during the initial data collection from Big Query I'm using a subset dataset, which I can increase from there and re-collect, would need to run my clean scripts again in that case again which should work. Basis of how rankining and classification performance, if results are in the poor regime will reach out to course instructors upon need basis. No other challenge is anticipated as of now.
