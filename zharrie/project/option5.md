Allocating Annotation Assignments for Participants

Description
There exists a CSV with participants responses from an initial part of a linguistic study. 
The first part of the study involved gathering speech data. The second part of the study is reaching out to a subset of those participants to have them used their native speaker
intuition to annotate data for prosodic events.

It's not realistic to completely exclude certain people with a small diverse corpus, however there are certain attributes one could wish to prioritize. This program prioritizes monolinguals and target language-engish bilunguals. It also prioritizes people from certain provinces and countries.

The end goal of this is to allocate data to willing participants based on priority. The output will be a list of participants and the audio files they have been allocated to annotate. Participants should not be annotating their own audio, as well as the audio of anyone they know.

Objectives
- Filter participants to check that they meet the criteria for the project
- Prioritize participants based on certain attributes using a max heap
- Create a graph to represent the relationships between participants
- Use BFS to traverse the graph and find participants who know each other, then allocate audio files for them to annotate.

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

Sample Interactions:
The user interaction is very simple. The only thing the user needs to input is a CSV in the proper format:
  name | age | gender | main language | other languages | proficiency | place they grew up | do they want to participate in round 2 | do they know other participants (names)

The program will then output allocations for both spanish and japanese speakers.
