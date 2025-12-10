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

# imports
import pandas as pd

# Just gonna put placeholder for csv to start doing stuff
'''
Lets say csv format will be
name | age | gender | main language | other languages | proficiency | place they grew up | do they want to participate in round 2 | do you know anyone else who is doing this
'''
df = pd.read_csv("/content/drive/MyDrive/data structures/pretend csv.csv")

###########################################################################################################

# step 1 & 2 - group into japanese and spanish. check if japanese speakers are native and grew up speaking japanese. those who don't match, filter them out
'''
This will make two dictionaries. One for japanese speakers, and one for spanish speakers. Since I'm filtering by main language, the non-native speakers are automatically filtered out

I'm not sure if a hash table would be better for this???
'''
# creates a list of dictionaries with this
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

# tbh this can be left for latet
# step ? create code names for anonimity
'''
language + gender + age
if there is more than one of them with that code, add a number
'''

# step 4 - create max heap
'''
Using the priority numbers from before, create max heap. This is just for the files to be annotated. So for the data. Participant max heap is later

Can just be name/code and the priority number, it's not really necessary to store full info here
'''
jpn_to_heap = []
spn_to_heap = []
for person in jpn_speakers:
    jpn_to_heap.append((person['name'], person['priority']))

for person in spn_speakers:
  spn_to_heap.append((person['name'], person['priority']))

import heapq

jpn_heap1 = heapq.heapify(jpn_to_heap)

# Step 5 - create max heaps
'''
The left child of a node at index i is at 2*i + 1.
The right child of a node at index i is at 2*i + 2.
The parent of a node at index i is at (i-1) // 2
'''

def max_heapifier(i, to_heap, n):
  child = 2 * i + 1
  val = to_heap[i]

  while child < n:
    max_val = val
    max_index = -1
    z = 0

    while z < 2 and z + child < n:
      if to_heap[z + child] > max_val:
        max_val = to_heap[z + child]
        max_index = z + child
      z += 1

    if max_val == val:
      return

    temp = to_heap[i]
    to_heap[i] = to_heap[max_index]
    to_heap[max_index] = temp

    i = max_index
    child = 2*i + 1
  return to_heap


def create_max_heap(to_heap):
  i = len(to_heap) // 2 - 1

  while i >= 0:
    max_heapifier(i, to_heap, len(to_heap))
    i -= 1

  return to_heap

# Now we gotta make the max heaps for the japanese speakers and the spanish speakers

jpn_spk_heap = create_max_heap(jpn_to_heap)
spn_spk_heap = create_max_heap(spn_to_heap)


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

.... I need to automate this into a function.....
'''
jpn_to_heap2 = []
spn_to_heap2 = []
for person in round2_jpn:
    jpn_to_heap2.append((person['priority'], person['name']))

for person in round2_spn:
  spn_to_heap2.append((person['priority'], person['name']))

round2_jpn_heap = create_max_heap(jpn_to_heap2)
round2_spn_heap = create_max_heap(spn_to_heap2)

# step 8 - find out how to mark who knows who
'''
Use a graph
If two people are adjacent, then they can't work on each others' files. They obviously can't work on their own files
'''

# step 9 - allocate but they can't annotate their own stuff or files of people they know
'''
So everyone should have 2-3 files, ideally 2 or so people annotating each file

Use max heap 1 with max heap 2 to get peak ideal match ups. Must cheap with graph to see if they know each other

Maybe use a queue?? Like sort the array that is the heap, and then match? but is that even necessary?
'''

