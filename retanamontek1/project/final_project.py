'''
Description
The program will take in a csv file of participants who want to be in a speech data collection project.
The participants will be filtered based on certain attributes (language, nativeness, place they grew up, etc).
Then, the participants will be prioritized based on certain attributes (place they grew up, monolingualism, etc).
Using heaps, the participants will be sorted by priority.
Then, using graphs, the participants will be checked to see who knows who.
Using BFS, the participants will be allocated audio files to annotate, making sure that no participant annotates their own file or the file of someone they know.
The output will be a list of participants and the audio files they have been allocated to annotate.
Objectives
- Filter participants to check that they meet the criteria for the project
- Prioritize participants based on certain attributes using a max heap
- Create a graph to represent the relationships between participants
- Use BFS to traverse the graph and find participants who know each other, then allocate audio files for them to annotate.
'''

# Create a list of the participants with priority being first followed by their name.
# This is what will be read into the heap.
def heap_list(lst):
  to_heap = []

  for person in lst:
    to_heap.append((person['priority'], person['name']))

  return to_heap


# This creates the max heap. It's not a perfect binary max heap, the heap_sort function will do that.
# This is called within the heap_sort function.
def create_max_heap(index, heap, n):
    # index is the index of the current node
    while True:

      left_child = 2 * index + 1
      right_child = 2 * index + 2
      largest = index

      # Compare with left child
      # If left child is larger, update largest  
      if left_child < n and heap[left_child][0] < heap[largest][0]:
            largest = left_child

      # Compare with right child
      # If right child is larger, update largest
      if right_child < n and heap[right_child][0] < heap[largest][0]:
            largest = right_child

      if largest == index:
        break

      # Swap
      heap[index], heap[largest] = heap[largest], heap[index]

      index = largest

# This used the create_max_heap function to create a perfect binary max heap.
def heap_sort(to_heap):
    curNode = len(to_heap) // 2 - 1

    # start from the last non-leaf node
    while curNode >= 0:
        create_max_heap(curNode, to_heap, len(to_heap)) # call max heapify. 
        curNode = curNode - 1

    # One by one extract elements from heap
    curNode = len(to_heap) - 1
    while curNode > 0:
        # Swap numbers
        temp = to_heap[0]
        to_heap[0] = to_heap[curNode]
        to_heap[curNode] = temp

        # call max heapify again on the reduced heap
        create_max_heap(0, to_heap, curNode)
        curNode = curNode - 1


# Below are various classes and methods used to create the graph.
class Vertex:
  def __init__(self, vertex_label):
        self.label = vertex_label

  def __repr__(self):
        return f"Vertex({self.label})"

class Edge:
    def __init__(self, from_vertex, to_vertex):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex

    def __repr__(self):
        return f"({self.from_vertex.label}, {self.to_vertex.label})"

class Graph:
  def __init__(self):
    # dictionary of edges
    self.from_edges = dict()
    self.to_edges = dict()

  def get_edge_list(self):
    edges_set = []
    for edges in self.from_edges.values(): 
        edges_set.append(edges)            
    return edges_set


  def get_vertices(self):
    vertices = []
    for vertex in self.from_edges:
      vertices.append(vertex)
    return vertices

  # Not currently used, but I have it here if needed
  def get_vertex(self, vertex_label):
    for v in self.from_edges:
      if v.label == vertex_label:
        return v
    return None


  def add_vertex(self, new_vertex):
    vertex = Vertex(new_vertex)
    self.from_edges[vertex] = []
    self.to_edges[vertex] = []
    return vertex

  def has_edge(self, from_vertex, to_vertex):
    if from_vertex not in self.from_edges: # check if from_vertex exists in the edges at all
      return False

    edges = self.from_edges[from_vertex] # get all the edges outgoing from the from_vertex, loop through them
    for edge in edges:
      if edge.to_vertex == to_vertex: # check if the to_vertex matches what we're looking for
        return True
    return False

  # Since the graph is undirected, edges are added for both directions
  def add_edge(self, vertexA, vertexB):
    if self.has_edge(vertexA, vertexB):
      return None

    new_edge = Edge(vertexA, vertexB) # create new edge
    # add edge to from_edges and to_edges dictionaries
    self.from_edges[vertexA].append(new_edge)
    self.to_edges[vertexB].append(new_edge)

    self.from_edges[vertexB].append(new_edge)
    self.to_edges[vertexA].append(new_edge)

  # Create adjacency list from the graph
  def adjacency_list(self):
    adj_lst = {}

    # Loop through vertices using from_edges
    for vertex in self.from_edges:
        neighbors = []

        # go through edges from that specific vertex
        for edge in self.from_edges[vertex]:
          if edge.from_vertex == vertex:
            neighbor = edge.to_vertex  # get the neighbor vertex        
            neighbors.append(neighbor.label) # add neighbor label to the list for that specific vertex

        adj_lst[vertex.label] = neighbors # add to adjacency list dictionary

    return adj_lst

# BFS function goes through the graph and finds all vertices connected to the start vertex.
# In application, the start vertex is the annotator, and the discovered vertices are the people they know.
from collections import deque
def BFS(adj_list, start):
  discovered = set()
  q = deque()

  discovered.add(start)
  q.append(start)

  while q:
    vertex = q.popleft()

    for neighbor in adj_list[vertex]: # go through neighbors of the current vertex
      if neighbor not in discovered:
        discovered.add(neighbor)
        q.append(neighbor)

  return discovered

# This function takes in a list of participants, and creates a graph based on who knows who.
# The specific lists this uses are the basic lists of all participants for each language. So jpn_speakers and spn_speakers.
def create_graph(lst):

  # Create graph
  connections = Graph()

  # Add vertices
  for person in lst:
    name = person['name']
    connections.add_vertex(name)

  # Add edges
  # Some people listed multiple names, but python will read it as a string, so it has to be split
  for person in lst:
    annotator_vertex = connections.get_vertex(person['name'])
    friends_lst = person['do they know other participants (names)'].strip()
    friend_lst = friends_lst.split(",")

    # Put friends into a clean list, stripping whitespace to be sure there are no errors
    friends = []
    for people in friend_lst:
      friends.append(people.strip())

    # Loop through friends and add edges
    for friend in friends:
      friend_vertex = connections.get_vertex(friend)
      if friend_vertex is None: # if they didn' t list anyone they know, skip
        continue
      connections.add_edge(annotator_vertex, friend_vertex)

  # Create adjacency list
  adj_list = connections.adjacency_list()

  # The only thing we really need from here is the adjacency list, so that is returned.
  return adj_list


# This function takes in the total list of speakers, the annotators (from the heap), and the data to be annotated (also in heap format).
def allocate(total_speakers, annotators, data):
  # Create a dictionary to track files
  # Has who is tracking them.
  annotated_files = {audio[1]: [] for audio in data} # audio[1] is the name/ of the data file and the value is a list of annotators. 

  # Create a dictionary for the allocations
  allocated = {}

  # Loop through each annotator in the list and allocate files
  # Each annotator should get 2 files to annotate
  for person in annotators:

    person['annotating'] = [] # This is for the person's dictionary is the annotators list
    allocated[person['name']] = [] # This is for the allocation dictionary

    # This keeps track of how many files have been assigned to the annotator so it won't exceed 2
    assigned = 0

    for audio in data:

        # Break if already assigned 2 files
        if assigned >= 2:
          break

        # This gets the name of person whose audio the annotator would be annotating
        audio_name = audio[1]

        # Check if the audio file already has 2 annotators. 
        # There's not enough annotators to do more than 2 per file
        if len(annotated_files[audio_name]) >= 2:
          continue

        # Check if the annotator knows the person whose file it is or if it's their own file
        adj_lst = create_graph(total_speakers)

        # Skip if they know each other or if it's their own file
        if audio_name in BFS(adj_lst, person['name']):
          continue

        # Skip if it's their own file
        if audio_name == person['name']:
          continue

        # Allocate the file to the annotator
        person['annotating'].append(audio) # append to personal dictionary
        allocated[person['name']].append(audio_name) # append to allocation dictionary
        annotated_files[audio_name].append(person['name']) # append to the file's list of annotators
        assigned += 1 # Increment the assigned count

  return allocated    


# Asks for input file name
input_file = input("file")


def main(input_file):
  # imports
  import pandas as pd

  '''
  csv format will be
  name | age | gender | main language | other languages | proficiency | place they grew up | do they want to participate in round 2 | 'do they know other participants (names)'
  '''
  # read in csv
  df = pd.read_csv(input_file)

  # step 1 & 2 - group into japanese and spanish. check if japanese speakers are native and grew up speaking japanese. those who don't match, filter them out
  '''
  This will make two dictionaries. One for japanese speakers, and one for spanish speakers. 
  Since we're filtering by main language, the non-native speakers are automatically filtered out.
  '''

  # creates a list of dictionaries with this
  df = df.fillna('') # fill na with empty string to avoid errors, mostly for names of other participants
  df['name'] = df['name'].str.lower() # for ease of matching later
  df['do they know other participants (names)'] = df['do they know other participants (names)'].str.lower()
  speakers =  df.to_dict('records')

  # These lists will be the main participants lists that will be used later.
  jpn_speakers = []
  spn_speakers = []
  for person in speakers:
    if person['main language'].lower() == 'japanese':
      jpn_speakers.append(person)
    elif person['main language'].lower() == 'spanish':
      spn_speakers.append(person)

  # step 3
  '''
  Since different variaties of a language will have different prosodic happenings, I need to prioritize people from certain areas.
  Plus +2 priority for them.
  I also want to prioritize people who are monolingual in case their other languages affect their native language.
  *If* a participant were to be multilingual, let is be english.
  So priority order goes monolingual(+2) > english(+1) > other(0)
  Location priority for japanese speakers is tokyo (+2), for spanish speakers it's costa rica, mexico, colombia (+2).
  '''

  # check if they're from the ideal providence for japanese speakers. don't delete those who aren't but prioritize those who are.
  for person in jpn_speakers:
    if person["place where they grew up"].lower() == 'tokyo':
      person['priority'] = 2
    else:
      person['priority'] = 0

  # check if they're from the ideal country for spanish speakers. don't delete those who aren't but prioritize those who are
  for person in spn_speakers:
    if person["place where they grew up"].lower() in ['costa rica', 'mexico', 'colombia']:
      person['priority'] = 2
    else:
      person['priority'] = 0

  # step 3.9 - add priority for monolingual, bilingual with english, and then no additional priority for others
  for person in jpn_speakers:
    if str(person["other languages"]) == 'nan':
      person['priority'] += 2
    elif 'english' in person['other languages'].lower():
      person['priority'] +=1

  for person in spn_speakers:
    if str(person["other languages"]) == 'nan':
      person['priority'] += 2
    elif 'english' in person['other languages'].lower():
      person['priority'] +=1

  # step 4 - create max heap lists
  '''
  Using the priority numbers from before, create max heap. This is just for the files to be annotated. So for the data. Participant max heap is later
  This isn't the heaps just yet, just the lists to be read into the heaps.
  Can just be name/code and the priority number, it's not really necessary to store full info here
  '''
  spn_data_heap = heap_list(spn_speakers)
  jpn_data_heap = heap_list(jpn_speakers)

  # Step 5 - create max heaps
  '''
  This is what makes the lists into max heaps. 
  The function that creates the max heaps is called in heap_sort, which is why heap_sort is called here.
  Heap sort is O(N log N)
  '''
  heap_sort(jpn_data_heap)
  heap_sort(spn_data_heap)

  # step 6 - sort through the participants by who wants to do round 2, and put them into a list
  '''
  Create new dictionaries for subsets of participants
  '''
  round2_jpn = []
  round2_spn = []
  for person in jpn_speakers:
    if person['do they want to participate in round 2'] == 'yes':
      round2_jpn.append(person)

  for person in spn_speakers:
    if person['do they want to participate in round 2'] == 'yes':
      round2_spn.append(person)

  # step 7 - max heap part 2: annotator ver
  '''
  So basically the subset of annotators that want to participate, sorted by priority. Same system as the the data heaps.
  '''
  jpn_annotate_heap = heap_list(round2_jpn)
  spn_annotate_heap = heap_list(round2_spn)

  heap_sort(jpn_annotate_heap)
  heap_sort(spn_annotate_heap)

  # step 8 - find out how to mark who knows who
  '''
  Use a graph
  If two people are adjacent, then they can't work on each others' files. They obviously can't work on their own files
  Adjacency list is O(V + E) better for sparce graphs like friend circles where not everyone knows each other,
  and adjacency matrix is O(V^2), better for dense small graphs. So adjacency list is better here.
  This is all done through functions not called immediately here.
  '''

  # step 9 - allocate but they can't annotate their own stuff or files of people they know
  '''
  There's 4 heaps.
  Priority list for the data:
  jpn_data_heap
  spn_data_heap

  Priority list for just the people who agreed to do the annotation:
  jpn_annotate_heap
  spn_annotate_heap

  So everyone should have 2-3 files, ideally 2 or so people annotating each file
  Use max heap 1 with max heap 2 to get peak ideal match ups. Must check with graph to see if they know each other
  BFS. O(V + E). The graphs aren't very deep, so it's best to use BFS here.

  - Grab person from the annotate heap, then grab person from the data heap. 
  - If they are the same person or know each other, then skip to the next person in the data heap.
  - Store that info in a list connected to that annotator. Also make a list for each files to track how many people  are annotating it. Each one should only get 2 annotators
  '''

  jpn_participants = [{'priority': p, 'name': n, 'annotating': []} for p, n in jpn_annotate_heap]

  jpn_allocations = allocate(jpn_speakers,jpn_participants, jpn_data_heap)

  spn_participants = [{'priority': p, 'name': n, 'annotating': []} for p, n in spn_annotate_heap]

  spn_allocations = allocate(spn_speakers,spn_participants, spn_data_heap)

  # step 10 - output allocations
  print("Spanish annotation allocations:")
  for annotator, audios in spn_allocations.items():
      print(f"{annotator}: {audios}")

  print("\nJapanese annotation allocations:")
  for annotator, audios in jpn_allocations.items():
      print(f"{annotator}: {audios}")


main(input_file)