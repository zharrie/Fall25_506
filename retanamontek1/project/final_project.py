'''
Description
Assuming an already made CSV of initial participants in a study, this tool filters through them for people who meet the requirements to be included. 
It also creates a new subset of people who checked off that they wanted to be included in a future section of the study. Through that subset of people, 
annotators are allocated to files gathered in the first part of the study.

Objectives
- Filter for certain attributes
- Use graphs for checking which participants know each 

Uhh use graphs, dictionaries, lists, queues(??)
figure out if you should use BFS or DFS
'''

# Create a list of the participants with priority being first followed by their name
def heap_list(df):
  to_heap = []

  for person in df:
    to_heap.append((person['priority'], person['name']))

  return to_heap


def create_max_heap(index, heap, n):
    
    while True:
      left_child = 2 * index + 1
      right_child = 2 * index + 2
      largest = index
  
      if left_child < n and heap[left_child][0] < heap[largest][0]:
            largest = left_child

      if right_child < n and heap[right_child][0] < heap[largest][0]:
            largest = right_child

      if largest == index:
        break

      heap[index], heap[largest] = heap[largest], heap[index]

      index = largest


def heap_sort(to_heap):
    n = len(to_heap) // 2 - 1
    while n >= 0:
        create_max_heap(n, to_heap, len(to_heap))
        n = n - 1
                
    n = len(to_heap) - 1
    while n > 0:
        # Swap numbers[0] and numbers[i]
        temp = to_heap[0]
        to_heap[0] = to_heap[n]
        to_heap[n] = temp

        create_max_heap(0, to_heap, n)
        n = n - 1


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
    edges_set = set()
    for edges in self.from_edges.values(): 
        edges_set.update(edges)            
    return edges_set


  def get_vertices(self):
    vertices = []
    for vertex in self.from_edges:
      vertices.append(vertex)
    return vertices

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
    if from_vertex not in self.from_edges:
      return False

    edges = self.from_edges[from_vertex]
    for edge in edges:
      if edge.to_vertex == to_vertex:
        return True
    return False

  def add_edge(self, vertexA, vertexB):
    if self.has_edge(vertexA, vertexB):
      return None

    new_edge = Edge(vertexA, vertexB)

    self.from_edges[vertexA].append(new_edge)
    self.to_edges[vertexB].append(new_edge)

    self.from_edges[vertexB].append(new_edge)
    self.to_edges[vertexA].append(new_edge)

  def adjacency_list(self):
    adj_lst = {}

    for vertex in self.from_edges:
        neighbors = []

        for edge in self.from_edges[vertex]:
          if edge.from_vertex == vertex:
            neighbor = edge.to_vertex          
            neighbors.append(neighbor.label)

        adj_lst[vertex.label] = neighbors

    return adj_lst

def create_graph(lst):

  connections = Graph()

  for person in lst:
    name = person['name']
    connections.add_vertex(name)

  for person in lst:
    from_vertex = connections.get_vertex(person['name'])
    friends_lst = person['do they know other participants (names)'].strip()
    friend_lst = friends_lst.split(",")

    friends = []
    for people in friend_lst:
      friends.append(people.strip())

    for friend in friends:
      to_vertex = connections.get_vertex(friend)
      if to_vertex is None:
        continue
      connections.add_edge(from_vertex, to_vertex)

  adj_list = connections.adjacency_list()

  return adj_list


def allocate(total_speakers, annotators, data):
  annotated_files = {audio[1]: [] for audio in data}
  allocated = {}

  for person in annotators:
    person['annotating'] = []
    allocated[person['name']] = []

    assigned = 0
    
    for audio in data:
        if assigned >= 2:
          break
        audio_name = audio[1]

        if len(annotated_files[audio_name]) >= 2:
          continue

        adj_lst = create_graph(total_speakers)
        if audio_name in BFS(adj_lst, person['name']):
          continue

        if audio_name in person['annotating']:
          continue

        person['annotating'].append(audio)
        allocated[person['name']].append(audio_name)
        annotated_files[audio_name].append(person['name'])
        assigned += 1

  return allocated

from collections import deque
def BFS(adj_list, start):
  discovered = set()
  q = deque()

  discovered.add(start)
  q.append(start)

  while q:
    vertex = q.popleft()

    for neighbor in adj_list[vertex]:
      if neighbor not in discovered:
        discovered.add(neighbor)
        q.append(neighbor)

  return discovered    



input_file = input("file")
def main(input_file):
  # imports
  import pandas as pd

  '''
  Lets say csv format will be
  name | age | gender | main language | other languages | proficiency | place they grew up | do they want to participate in round 2 | 'do they know other participants (names)'
  '''
  df = pd.read_csv(input_file)

  # step 1 & 2 - group into japanese and spanish. check if japanese speakers are native and grew up speaking japanese. those who don't match, filter them out
  '''
  This will make two dictionaries. One for japanese speakers, and one for spanish speakers. Since I'm filtering by main language, the non-native speakers are automatically filtered out

  I'm not sure if a hash table would be better for this???
  '''
  # creates a list of dictionaries with this
  df = df.fillna('')
  df['name'] = df['name'].str.lower()
  df['do they know other participants (names)'] = df['do they know other participants (names)'].str.lower()
  speakers =  df.to_dict('records')

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
  Plus +2 priority for them

  I also want to prioritize people who are monolingual in case their other languages affect their native language.
  *If* a participant were to be multilingual, let is be english.
  So priority order goes monolingual(+2) > english(+1) > other(0)
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
  1
  Can just be name/code and the priority number, it's not really necessary to store full info here
  '''
  spn_data_heap = heap_list(spn_speakers)
  jpn_data_heap = heap_list(jpn_speakers)

  # Step 5 - create max heaps
  '''
  The left child of a node at index i is at 2*i + 1.
  The right child of a node at index i is at 2*i + 2.
  The parent of a node at index i is at (i-1) // 2
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
  So basically the subset of annotators that want to participate
  '''
  jpn_annotate_heap = heap_list(round2_jpn)
  spn_annotate_heap = heap_list(round2_spn)

  heap_sort(jpn_annotate_heap)
  heap_sort(spn_annotate_heap)

  # step 8 - find out how to mark who knows who
  '''
  Use a graph
  If two people are adjacent, then they can't work on each others' files. They obviously can't work on their own files

  Adjacency list is O(V + E) + better for sparce graphs like friend circles where not everyone knows each other,
  and adjacency matrix is O(V^2), better for dense small graphs. So adjacency list is better here.
  '''

  # step 9 - allocate but they can't annotate their own stuff or files of people they know
  '''
  There's 4 heaps.
  Priority list for the data
  jpn_data_heap
  spn_data_heap

  Priority list for just the people who agreed to do the annotation
  jpn_annotate_heap
  spn_annotate_heap

  So everyone should have 2-3 files, ideally 2 or so people annotating each file

  Use max heap 1 with max heap 2 to get peak ideal match ups. Must check with graph to see if they know each other

  BFS. O(V + E). The graphs aren't very deep, so it's best to use BFS here.
  '''
  # Grab person from the annotate heap, then grab person from the data heap. 
  # If they are the same person or know each other, then go to the next
  # store that info in a list connected to that annotator. Also make a list for each files to track how many people
  # are annotating it. Each one should only get 2 annotators

  jpn_participants = [{'priority': p, 'name': n, 'annotating': []} for p, n in jpn_annotate_heap]

  jpn_allocations = allocate(jpn_speakers,jpn_participants, jpn_data_heap)

  spn_participants = [{'priority': p, 'name': n, 'annotating': []} for p, n in spn_annotate_heap]

  spn_allocations = allocate(spn_speakers,spn_participants, spn_data_heap)

  print("Spanish annotation allocations:")
  for annotator, audios in spn_allocations.items():
      print(f"{annotator}: {audios}")

  print("\nJapanese annotation allocations:")
  for annotator, audios in jpn_allocations.items():
      print(f"{annotator}: {audios}")


main(input_file)