Description
There exists a CSV with participants responses from an initial part of a linguistic study. 
The first part of the study involved gathering speech data. The second part of the study is reaching out to a subset of those participants to have them used their native speaker
intuition to annotate data for prosodic events.

It's not realistic to completely exclude certain people with a small diverse corpus, however there are certain attributes one could wish to prioritize. This program prioritizes monolinguals and target language-engish bilunguals. It also prioritizes people from certain provinces and countries.

The end goal of this is to allocate data to willing participants based on priority. The output will be a list of participants and the audio files they have been allocated to annotate. Participants should not be annotating their own audio, as well as the audio of anyone they know.

Objectives
Output a useable list of annotation allocations for the people who signed up for the second part of the study.

The data structures used in the program are:
- Dictionaries/lists
- Max heaps
- Undirected graph

Algorithms used are:
- BFS
- Heap sort

Functions:
- Filter participants to check that they meet the criteria for the project
- Prioritize participants based on certain attributes using a max heap
- Create a graph to represent the relationships between participants
- Use BFS to traverse the graph and find participants who know each other, then allocate audio files for them to annotate.

Required python packages and imports:
- pandas
- collections (deque)

User guide:

The program starts by the user giving the path to a csv when prompted. It's then read into the program through pandas. This is the only user interaction required.
The csv has the following columns:
  name | age | gender | main language | other languages | proficiency | place they grew up | do they want to participate in round 2 | do they know other participants (names)

The output is the allocations in a list in the following format:
name: [file1, file2], name2: [file1, file2]
