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


User / Code Guide

Step 0:
The program starts by the user giving the path to a csv when prompted. It's then read into the program through pandas. This is the only user interaction required.
The csv has the following columns:
  name | age | gender | main language | other languages | proficiency | place they grew up | do they want to participate in round 2 | do they know other participants (names)

______________________________________________________________________________________________________________________________________

Step 1-2: 
Group into Japanese and Spanish. Check if they're native speakers. Those who don't match, filter them out.
This step creates two lists of dictionaries, one for each language. They're created by initiating lists, then looping over rows in the csv, spliting them by what they put in the 'main langugae' (native language) question. Since there are only two possible dictionaries to be sorted in, anyone who didn't list Spanish or Japanese as their main language is automatically filtered out.

The dictionaries look like the follow:
{'name': 'genta',
  'age': 24,
  'gender': 'male',
  'main language': 'japanese',
  'other languages': 'mandarin',
  'place where they grew up': 'tokyo',
  'do they know other participants (names)': 'kyoko',
  'do they want to participate in round 2': 'no'},

_________________________________________________________________________________________________________________________________

Step 3:
A new key in the dictionaries is made, 'priority'. 
Priority order for languages spoken is monolingual(+2) > english(+1) > other(0).
Priority for target country/city is a flat +2 priority for Costa Rica, Mexico, and Colombia, and Tokyo.

The target attributes are found via if else statements searching for string matches, as well as searching for nan (monolingual) in the 'other languages' key.

__________________________________________________________________________________________________________________________________________

Step 4, Max heap lists:
Using the priority numbers from before, lists to be turned into max heaps are created.
The speaker lists are looped through, and a list of tuples is created. Index 0 stores the priority, and index 1 stores the name of the participant.

The output looks like this:
[(3, 'sofia'),
 (2, 'kris'),
 (3, 'sebastian')]

______________________________________________________________________________________________________________________________________

Step 5, Creating max heaps:
These max heaps refer to the data that is to be annotated.
The function create_max_heap() is reapeatedly called within the heap_sort() function to check and swap elements repeatedly and the heap_sort function goes through the list. It takes in 3 arguments:
- index
- heap (list)
- n (length)
It functions by looking at a given index's left and right children, and swapping with whichever one is larger. If the index is the largest, then it breaks.

The heap_sort() function takes in a single argument, the heap lists.
Both the heap_sort and create_max_heap() functions look at priority. This has a runtime of O(N log N).

Looks something like this:
 [(2, 'genta'),
 (1, 'masashi'),
 (1, 'kaoru'),
 (0, 'yuika')]

__________________________________________________________________________________________________________________

Step 6:
Participants are sorted into a list based on what they responded for the questioned that asked if they wanted to be annotators in the second part of the study. Same set up as step 1-2.

____________________________________________________________________________________________________________

Step 7, annotator max heap:
A second set of max heaps are created the same way they were for the data in step 5. These are specifically for the people who will be doing the annotations.

________________________________________________________________________________________________________________

Step 8, Graph creation:
This program comes with a built in class for graph creation. It has methods for getting lists of edges, getting a list of vertices, adding a vertex, checking if an edge exitsts, adding an edge, and creating an adjacency list. The adjacency list, O(V + E) runtime, was chosen over and adjacency matrix, O(V^2) runtime, due to it's better runtime and the fact that the graph utilized in this program is space. The matrix would not be as efficient, especially with all the zeros it would have.

The class is implemented in the function create_graph() that takes in the list of dictionaries created in step 6.
- A graph locally labeled as connections is initiated using Graph().
- The function loops through the list and creates vertices for everyone.
- Annotator is labeled as annotator_vertex
- In order to create the edges, the values from 'do they know other participants (names)' have to be stripped and split(by commas) because some people may list more than one person.
- The add_edge() method takes in self, and 2 vertexes. 
- In the create_graph() function, the friend/aquaintence is grabbed from the vertex list using the get_vertex() method and labaled as friend_vertext
- Annotator vertex and friend vertex create and edge.
- Since this is an undirected graph, edges are added for both directions 
    - both vertices are added to self.from_edges and self.to_edges.

- Within the create_graph() function, an adjacency list is also made by calling the adjacency_list() method.
    - The adjacency list is initiated by adj_lst = {}
    - Loops though vertexes from the self.from_edges
    - A neighbors list is created
    - for edge in self.from_edges[vertex] loops and neighbor is set to self.to_vertex
    - The neighbor is added to the neighbors list. The list is then added to the dictionary.

________________________________________________________________________________________________________________

Step 9, Allocating:
There are 4 heaps that are used for this:
- Data heaps:
    - jpn_data_heap
    - spn_data_heap
- Annotator heaps:
    - jpn_annotate_heap
    - spn_annotate_heap

Each annotator will annotate 2 audios, and each audio will be annotated by a max of 2 annotators. There are more data elements than annotators since not all participants agreed to be annotators.
Breath first search, runtime of O(V + E) is used. The graphs aren't very deep, so it's best to use BFS here.

The allocate() function takes in 3 arguments:
total_speakers: jpn_speakers , spn_speakers
annotators: annotators heaps
data: data heaps

- annotated_files = {audio[1]: [] for audio in data} --> dictionary of data and annotators
- allocated dictionary is created
- Loops over annotator
- lists for what the annotator is annotating, and who is annotating each file
    - person['annotating'] = []
    - allocated[person['name']] = []
- annotated = 0 counter is initiated

- Loops over the data
    - If annotator has been already given 2 files to annotate, break
    - if data has already been allocated twice, skip
    - adjacency list is grabbed
    - checks if data is in adjacency list with BFS. If it's in there, skip

BFS:
- Uses deque from collections
- Takes 2 arguments: the adjacency list, and a starting vertex (annotator)
- There is a discovered set, and queue.
- The starting is added to the queue and discovered set.
- Goes through vertexes in q through popleft() method
    - Loops through friends/neighbors in the adjacency list and adds them to discovered and to the queue if it's not already in discovered.
- Returns discovered

Once it finds a match, the function will append the audio allocation to the key 'annotating' in the annotator list/dictionary, and the allocated list. Assigned is also incremented by 1.

When every annotator has been allocated 2 files, it ends and returns the allocated dictionary.
Looks like:
{'subaru': ['shoji', 'keiko'],
 'yurika': ['shoji', 'ryoto'],
 'yoshiki': ['ryoto', 'subaru']}

_________________________________________________________________________________________________________________

Step 10:

The program will then print out the allocations for both the japanese speakers and the spanish speakers




