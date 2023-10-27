> In your proposal, please answer the following questions:

# Project Proposal
> What are the names and NetIDs of all your team members? Who is the captain? The captain will have more administrative duties than team members.

## Project Member(s)

Solo project (sole member and i.e. captain):

- Full name: **Swarup Ghosh**
- Net ID: **swarupg2**

> What is your free topic? Please give a detailed description. What is the task? Why is it important or interesting? What is your planned approach? What tools, systems or datasets are involved? What is the expected outcome? How are you going to evaluate your work?

## Topic and Detailed Description

- Topic: **Infer operating system from commands/packages**
    - Description: Given a single keyword or a set of keywords from a line of shell script, the system will infer the probability of the Operating System where the command/package would be relevant to.
    - User input: either a single keyword or a line from a shell script
    - Output: visualize the probability of the OS where the command should be run. Classify amongst: Debian-based OSes, Fedora/RH-like OSes, Windows, MacOS, etc.
- Significance/interest: In the area of source code data mining there are various projects and tools that work quite well for full code search. However, there aren't enough tools that allow beginners to the world of software development to proactively pickup shell scripting as their are various challenges. In the project, the aim is to solve a small challenge where beginners starting with shell scripts could use source lines/keywords from the code snippets to identify relevant operating systems for the scripts to work properly. The project goal is to utilize text information retrieval techniques to open source code data available.
- Approach:
    1. Data collection: Collection of data from GitHub in the form of *.sh, *.bat, .Dockerfile, etc.
    2. Constructing/determining useful keywords for each OS category
    3. Creating rules for better filtering the different Operating Systems from raw data
    4. Data pre-processing and indexing
    5. Ranking the items in the database based upon evaluation from keyword search
    6. Preparing data for a classifier based upon ranked data
    7. Creating a small UI (either GUI or CLI) with the classifier
- (probable) tools, systems, datasets: 
- Expected outcome:
    - User input of either command keywords or exact shell script line would classify which is the most likely OS where the queried command/package would be run/available
    - Display the data in the form of probability distribution with highest probability first
- Self-evaluation goal:
    - The data collection step should involve indexing data larger than system memory i.e. ensure collected data is processed batch-wise
    - System should be able to infer OS for basic inputs like: `apt install ...` to be debian, `dnf installl ...` to be rh-like OS, etc. etc. for atleast 20 queries in hold out set
    - Perform ranking as well as classification, retrieval ranking for pulling data while classification to infer final results
    - UI developed either as GUI or CLI that can help users use the program by directly consuming from source code

> Which programming language do you plan to use?

## Programming Language

The primary implementation would be based in Python (other programming languages can be used on need basis). However, the source code collected would be constituting primarily Dockerfile(s) and Bash shell scripts.

> Please justify that the workload of your topic is at least 20*N hours, N being the total number of students in your team. You may list the main tasks to be completed, and the estimated time cost for each task.

## Workload

As per sub-bullets in Approach from previous section the following would be the proposed workload hours.

```
[
    1. would require approx 3-5 hours;
    2.,3. would require 2-3 hours;
    4.,5. would require 4-6 hours for retrieval ranking and comparing/improving diff techniques;
    6. would require 3-5 hours for preparing a classifier and comparing/improving;
    7. would require 2-3 hours
]
```