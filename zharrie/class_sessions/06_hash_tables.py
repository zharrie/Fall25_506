# Part 1: The Map Abstract Data Type
"""
Let's start with a fundamental question: what data strucutre woud you use if you need to store data where you want to look things up by some kind of identifier or key?
Think about a phone book. You have a person's name, and you want to find their phone number. Or think about a student database, you have a student ID, and you want to retrieve all that student's information. 
Or even something as simple as a dictionary, where you have a word and you want its definition.

This pattern comes up everywhere in computer science, and we formalize it with something called the Map Abstract Data Type. 
A map—sometimes called a dictionary or associative array—is an ADT that creates associations between keys and values. 
The fundamental idea is simple: you give me a key, I give you back the associated value.

Now, there's an important constraint here. Each key in a map must be distinct. 
You can't have duplicate keys. This makes sense if you think about it, if you could have the same key pointing to multiple values, which one would I return when you ask for it? 
So the rule is: one key maps to exactly one value. Of course, the same value can be associated with different keys, but each key is unique.

The map has three fundamental operations:
"""
# Map ADT Interface
def insert(key, value):
    # If key does not exist: insert key-value pair
    # If key exists: update the value
    pass

def get(key):
    # Return value associated with key
    # Return None if key does not exist
    pass

def remove(key):
    # Remove key-value pair
    # Return success/failure
    pass

# Notice the insert behavior: if the key already exists, we update its value rather than creating a duplicate. 
# This maintains the uniqueness constraint on keys.

# Part 2: A Limited Map Implementation
"""
So let's think about how we might implement a map. 
Let me start with a really simple scenario. 
Suppose I tell you that all your keys are going to be integers in the range from zero to nine. 
Just ten possible keys. How would you implement a map for this?

Well, this is almost trivially easy, right? 
You'd just use an array with ten elements. 
If someone wants to insert key 5 with some value, you just do array[5] = value. 
If they want to get the value for key 5, you return array[5]. 
If they want to remove key 5, you set array[5] to null. 
Done. This is incredibly fast—every operation is O(1), constant time. Perfect.
"""

class SimpleLimitedMap:
    def __init__(self):
        self.array = [None] * 10
    
    def insert(self, key, value):
        self.array[key] = value
    
    def get(self, key):
        return self.array[key]
    
    def remove(self, key):
        self.array[key] = None
        
# This works perfectly for our limited case. Every operation is O(1)—just one array access.

"""
This approach has two massive problems that make it impractical for most real applications.

- First, what if your keys aren't integers? 
What if they're strings, like people's names? 
Or what if they're more complex objects, like student records or coordinates or anything else? 
You can't use a string as an array index directly. Arrays need integer indices.

- The second problem is even more fundamental. 
Even if all your keys are integers, you almost certainly can't allocate an array large enough to hold all possible integers. 
Think about it: a 32-bit integer can be anything from negative two billion to positive two billion. 
Are you going to allocate an array with four billion elements? 
Of course not. Even if you could allocate that much memory, most of it would be wasted space. 
If you only have a hundred actual keys that you care about, you've wasted 99.9999% of your array.

So we need a solution that supports any key type—not just integers—and that uses a reasonable amount of memory even when the range of possible keys is enormous. 
This is exactly what hash tables give us.
"""

# Hash Table Overview
"""
The fundamental insight behind hash tables is this: what if we could somehow convert any key—whether it's a string, an object, whatever—into an integer, and then use that integer to index into a reasonably-sized array? 
That's the entire idea.
A hash table is a data structure that stores unordered items by mapping (or hashing) each item to a location in an array. 
Each hash table array element is called a bucket.
A hash map is an implementation of a map ADT using a hash table.
"""
# Part 3: Hash Codes and Hash Functions
# 3.1 Solving Problem 1: Hash Codes
"""
A hash code is simply a fixed-size, non-negative integer that represents a key. 
It's an attempt to uniquely identify that key with a number. And a hash function is the function that computes this hash code from a given key.
Now, hash functions are usually specific to the data type you're working with. 
For integers, the hash function might just return the integer itself. 
For strings, the hash function might do something more complex, like adding up the ASCII values of all the characters, or using some mathematical formula based on those characters.
"""

def hash_function(key):
    if isinstance(key, int):
        return key  # Integer keys hash to themselves
    elif isinstance(key, str):
        # String hash: sum of character ASCII values (simple version)
        hash_code = 0
        for char in key:
            hash_code += ord(char)
        return hash_code
    else:
        return abs(hash(key))  # Use built-in hash

# Examples:
print(hash_function(42))        # 42
print(hash_function("Alice"))   # 65+108+105+99+101 = 478
# Now we can convert any key type to an integer.

# 3.2 Solving Problem 2: The Modulo Operation
"""
So now we can convert any key into an integer—that's our hash code. But we still have the second problem: that integer might be huge. 
The hash code could be millions or billions. We can't create an array that big. This is where the clever part comes in.

A hash table is simply an array of a manageable size—let's say ten elements, or a hundred, or a thousand—whatever fits in memory and makes sense for your application. We call each element of this array a bucket. Now here's the trick: we take our potentially huge hash code and use the modulo operation to squeeze it down into a valid array index.
Step one: compute hashCode equals Hash(key). 
Step two: compute bucketIndex equals hashCode mod arraySize. 
That modulo operation is the magic. If your array has ten buckets, then hashCode mod 10 will always give you a number from zero to nine. 
If your array has a hundred buckets, hashCode mod 100 gives you zero to ninety-nine. No matter how big the hash code is, the modulo operation squeezes it into the range of valid array indices.

A concrete example. 
Suppose you have a string key, "Alice," and your hash function converts this to the integer 65,219. 
Your array has ten buckets. So bucketIndex equals 65,219 mod 10, which equals 9. 
So you'd store Alice's data in bucket 9 of your array.

This is beautiful, right? We've solved both problems. We can handle any key type because we have hash functions. 
And we can use a small array because we use modulo to compress large hash codes.
The key insight: use the modulo operator to map any hash code to a valid bucket index:
Step 1: hashCode = Hash(key)
Step 2: bucketIndex = hashCode % arrayAllocationSize
Step 2 solves the second problem. The array's allocation size doesn't need to support any integer index. 
The expression hashCode % arrayAllocationSize always yields an index in range for the array.
"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def _compute_bucket_index(self, key):
        hash_code = hash_function(key)
        bucket_index = hash_code % self.size
        return bucket_index

# Examples:
ht = HashTable(size=10)
print(ht._compute_bucket_index("Alice"))   # 478 % 10 = 8
print(ht._compute_bucket_index("Bob"))     # 275 % 10 = 5
print(ht._compute_bucket_index(86))        # 86 % 10 = 6
print(ht._compute_bucket_index(16))        # 16 % 10 = 6  ← Collision!

"""
we've introduced a new problem. This is called the collision problem, and it's fundamental to hash tables.
Think about what happens if we have two different keys that produce the same bucket index. 
For example, the integer key 86: 86 mod 10 equals 6, so it goes in bucket 6. But then we try to insert key 16: 16 mod 10 also equals 6. Collision! 
Both keys want to go in bucket 6, but bucket 6 already has something in it.

Now, can we completely avoid collisions? Let me ask you this: if we have a thousand possible keys but only ten buckets, can we avoid collisions? 
No, of course not. This is the pigeonhole principle from mathematics. If you have more items than containers, at least one container must hold multiple items. 
Collisions are mathematically inevitable when the number of possible keys exceeds the number of buckets—which is almost always the case.
So we can't avoid collisions. 
What we need instead is a strategy for handling them. 
This brings us to collision resolution techniques, and we're going to look at two major approaches: chaining and open addressing.
"""

# Chaining
"""
5.1 Chaining Overview
Chaining handles hash table collisions by using a list for each bucket, where each list stores the items that map to that bucket.

Visual representation after insertions:
Bucket 0: None
Bucket 1: None
Bucket 6: [(86, "Alice")] → [(16, "Bob")] → None
Bucket 7: [(27, "Charlie")] → None
Bucket 8: None
Bucket 9: None
The get, insert, and remove operations each start by using the item's key to determine the bucket. Each operation then searches that bucket's linked list for the key.

5.2 Chaining Operations
Get Operation:
Return the value corresponding to the key, or null if not found.

Insert Operation:
If the search finds a node, update that node's value.
If not, append a new node with the inserted key and value to the bucket's linked list.

Remove Operation:
If the search finds a node, remove that node from the bucket's linked list.

5.3 Implementation
The item structure needs three fields:
"""
class ChainItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Pointer to next item

# HashInsert function:
def HashInsert(hashTable, key, value):
    # Hash the key to get the bucket index
    bucketIndex = Hash(key) % len(hashTable)
    
    # Traverse the linked list, searching for the key. If the key exists in
    # an item, the value is replaced. Otherwise a new item is appended.
    currentItem = hashTable[bucketIndex]
    previousItem = None
    
    while currentItem != None:
        if key == currentItem.key:
            currentItem.value = value
            return True
        
        previousItem = currentItem
        currentItem = currentItem.next
    
    # Allocate new item
    newItem = ChainItem(key, value)
    
    # Append item to the linked list
    if hashTable[bucketIndex] == None:
        hashTable[bucketIndex] = newItem
    else:
        previousItem.next = newItem
    
    return True

# Notice the traversal pattern: we maintain both currentItem and previousItem. 
# The previousItem is necessary for appending the new node to the end of the list.

# HashGet function:
def HashGet(hashTable, key):
    # Hash the key to get the bucket index
    bucketIndex = Hash(key) % len(hashTable)
    
    # Search the bucket's linked list for the key
    item = hashTable[bucketIndex]
    while item != None:
        if key == item.key:
            return item.value
        item = item.next
    
    return None  # Key not found
# Straightforward traversal: we walk the linked list comparing keys until we find a match or reach the end.

# HashRemove function:
def HashRemove(hashTable, key):
    # Hash the key to get the bucket index
    bucketIndex = Hash(key) % len(hashTable)
    
    # Search the bucket's linked list for the key
    currentItem = hashTable[bucketIndex]
    previousItem = None
    
    while currentItem != None:
        if key == currentItem.key:
            if previousItem == None:
                # Remove linked list's first item
                hashTable[bucketIndex] = currentItem.next
            else:
                previousItem.next = currentItem.next
            
            return True
        
        previousItem = currentItem
        currentItem = currentItem.next
    
    return False  # Key not found

# The remove operation has two cases: removing the first item (update the bucket pointer) or removing a subsequent item (update the previous item's next pointer).

"""
Now let's talk about performance. 
In the best case, when items are distributed evenly across buckets and each bucket has very few items, get, insert, and remove are all essentially constant time—O(1). 
We compute the hash, compute the modulo, and then traverse a very short list.

The average case performance depends on something called the load factor. 
The load factor, usually denoted by the Greek letter alpha, is n divided by m, where n is the number of items in the hash table and m is the number of buckets. 
It represents the average number of items per bucket. If the load factor is 1, you have one item per bucket on average. If it's 2, you have two items per bucket on average. 
For good performance, we want the load factor to be relatively small—less than 1 or 2.

But what about the worst case? 
Well, imagine a terrible hash function that maps every single key to the same bucket. 
Then one bucket has a list with all n items, and the other buckets are empty. Now when you search, you're traversing a list of length n, which is O(n). 
So the worst-case performance is linear, not constant. This is why choosing a good hash function is so critical.
"""
# Part 6: Linear Probing
"""
6.1 Linear Probing Overview
A hash table with linear probing handles a collision by starting at the key's mapped bucket, and then linearly searches subsequent buckets until an empty bucket is found.

Example sequence:

Insert(86): 
  bucketIndex = 86 % 10 = 6
  → Store at bucket 6

Insert(16):
  bucketIndex = 16 % 10 = 6  ← Collision!
  → Bucket 6 occupied, try bucket 7
  → Bucket 7 empty, store there

Insert(26):
  bucketIndex = 26 % 10 = 6  ← Collision!
  → Bucket 6 occupied, try bucket 7
  → Bucket 7 occupied, try bucket 8
  → Bucket 8 empty, store there

Result:
[6] (86, value)  [7] (16, value)  [8] (26, value)
6.2 Empty Bucket Types, Search, and Removal

Linear probing distinguishes two types of empty buckets:

Empty-since-start: Has been empty since the hash table was created
Empty-after-removal: Had an item removed that caused the bucket to now be empty
The distinction is important during searches, since searching only stops for empty-since-start, not for empty-after-removal.

Why this distinction matters:
Initial state:
[6] (16, "Alice")  [7] (26, "Bob")  [8] EMPTY_SINCE_START

Search for "Bob":
  Start at bucket 6 (where 26 hashes)
  → Key 16 ≠ 26, continue
  → Check bucket 7, found "Bob" ✓

Now remove key 16:
[6] ?????  [7] (26, "Bob")  [8] EMPTY_SINCE_START

Search for "Bob" again:
  Start at bucket 6
  → If bucket 6 is EMPTY_SINCE_START: stop searching, "Bob not found" ✗ WRONG!
  → If bucket 6 is EMPTY_AFTER_REMOVAL: continue searching, find "Bob" ✓ CORRECT!
The search algorithm uses the sought item's key to determine the initial bucket. Then buckets are linearly probed (checked) until either:
- A matching key is found
- An empty-since-start bucket is found
- All buckets have been probed
Encountering an empty-since-start bucket or probing all buckets means that the key does not exist in the table.

The remove algorithm first searches for the key. If found, the remove algorithm then removes the key and marks the bucket as empty-after-removal (not empty-since-start).
"""

# 6.3 HashRemove Implementation
def HashRemove(hashTable, key):
    # Get the key's hash code
    hashCode = Hash(key)
    
    for i in range(len(hashTable)):
        bucketIndex = (hashCode + i) % len(hashTable)
        
        # An empty-since-start bucket implies the key is not in the table
        if hashTable[bucketIndex] is EMPTY_SINCE_START:
            return False
        
        if hashTable[bucketIndex] is not EMPTY_AFTER_REMOVAL:
            # Check if the non-empty bucket has the key
            if key == hashTable[bucketIndex].key:
                # Remove by assigning the bucket with empty-after-removal
                hashTable[bucketIndex] = EMPTY_AFTER_REMOVAL
                return True
    
    return False  # key not found

# The critical line is hashTable[bucketIndex] = EMPTY_AFTER_REMOVAL. 
# We must mark it as empty-after-removal to preserve the search paths for other items.
"""
6.4 Insertion Using Linear Probing
The insert algorithm first searches for the key to insert. 
If found, the corresponding value is updated. If not found, the probing sequence starts over and the key is inserted into the first empty bucket found.
"""
def HashInsert(hashTable, key, value):
    # Get the key's hash code
    hashCode = Hash(key)
    
    # First search for the key in the table. If found, update bucket's value.
    foundEmptySinceStart = False
    for i in range(len(hashTable)):
        bucketIndex = (hashCode + i) % len(hashTable)
        
        # An empty-since-start bucket implies the key is not in the table
        if hashTable[bucketIndex] is EMPTY_SINCE_START:
            foundEmptySinceStart = True
            break
        elif hashTable[bucketIndex] is not EMPTY_AFTER_REMOVAL:
            # Check if the non-empty bucket has the key
            if key == hashTable[bucketIndex].key:
                # Update the value
                hashTable[bucketIndex].value = value
                return True
    
    # The key is not in the table, so insert into first empty bucket
    for i in range(len(hashTable)):
        bucketIndex = (hashCode + i) % len(hashTable)
        if hashTable[bucketIndex] is EMPTY_SINCE_START or \
           hashTable[bucketIndex] is EMPTY_AFTER_REMOVAL:
            newItem = BucketItem(key, value)
            hashTable[bucketIndex] = newItem
            return True
    
    return False  # no empty bucket found
# The two-phase approach: first search for existing key (phase 1), then insert into first empty bucket (phase 2). This ensures we don't create duplicates and correctly handle updates.

# Part 7: Common Hash Functions
"""
Now let's talk about hash functions themselves. 
We've been treating the hash function as a black box that magically converts keys to integers, but the choice of hash function is absolutely critical to hash table performance. 
A good hash function can make your hash table blazingly fast. 
A poor hash function can make it slower than just using a linked list.

So what makes a hash function good? 
The fundamental goal is to minimize collisions by distributing items uniformly across all available buckets. 
Think of it like distributing students randomly into classrooms. 
You don't want all students ending up in one classroom and the others empty. You want them spread out evenly.

Let me describe three categories of hash functions. 
At the top, you have the perfect hash function. This is a hash function that produces zero collisions. 
Every key maps to a unique bucket. If you can achieve this, your operations are guaranteed O(1) in all cases—best case, average case, and worst case. 
But there's a catch: you can only create a perfect hash function if you know all possible keys in advance. 
In practice, this is rare. Maybe you're creating a hash table for a fixed set of reserved keywords in a programming language, and you can design a perfect hash function for those specific words. 
But for general-purpose hash tables where keys can be anything, perfect hashing isn't possible.

The second category is what we call a good hash function. 
This distributes keys uniformly across buckets, minimizes clustering, and achieves O(1) average-case performance. 
The worst case is still O(n)—if every key happens to hash to the same bucket—but that's statistically unlikely with a good hash function.

The third category is a poor hash function, which causes many collisions and non-uniform distribution. 
This degrades your hash table to essentially a list with extra overhead.

Here's an important point: a hash function's quality depends on both the hash table size and the distribution of expected keys. 
Let me give you an example of why this matters. 
Suppose your hash function is just key mod 10, and your keys happen to be 10, 20, 30, 40, up to 100. 
What happens? Every single key maps to bucket 0 because they're all divisible by 10. 
You've got ten buckets, but you're only using one. 
That's a terrible hash function for this particular set of keys, even though it might work fine for other keys.


7.1 A Good Hash Function Minimizes Collisions
Hash table operations are fast if the hash function minimizes collisions.
A perfect hash function maps items to buckets with no collisions. 
A perfect hash function can be created if the number of items and all possible item keys are known beforehand. 
The runtime for insert, search, and remove is O(1) with a perfect hash function.
A good hash function should uniformly distribute items into buckets. 
With chaining, a good hash function results in short bucket lists and thus fast inserts, searches, and removes. 
With linear probing, a good hash function will avoid hashing multiple items to consecutive buckets and thus minimize the average linear probing length to achieve fast inserts, searches, and removes. 
On average, a good hash function will achieve O(1) inserts, searches, and removes, but in the worst-case may require O(N).
A hash function's performance depends on the hash table size and knowledge of the expected keys.

"""
# Example of a poor hash function:
# Hash function: key % 10
# Hash table size: 10

keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for k in keys:
    print(f"{k} % 10 = {k % 10}")

# Output: All hash to bucket 0!
# 10 % 10 = 0
# 20 % 10 = 0
# 30 % 10 = 0
# ...
# All collisions at bucket 0!
# This shows why the hash function key % 10 performs poorly if the expected keys are all multiples of 10.

# 7.2 Modulo Hash Function
# A modulo hash uses the remainder from division of the key by the hash table size N.
def HashRemainder(key, N):
    return key % N
# Simple and fast, but sensitive to patterns in the data.

# 7.3 Mid-Square Hash Function
"""
A more sophisticated approach is the mid-square hash function. Here's how it works. 
You take your key and square it. Then you extract some digits from the middle of the result. 
Finally, you return those middle digits modulo your table size.

Let me give you a decimal example first, even though in practice you'd use binary. 
Suppose your key is 453. You square it: 453 times 453 equals 205,209. 
Now you extract the middle two digits, which are 52. That's your hash code—well, then you'd still modulo it by your table size.

Why does this work? 
The key insight is that when you square a number, the middle digits depend on all the digits of the original number. 
It mixes them together. This means even if your keys have patterns, the squared values tend to be more randomly distributed.
"""

# Binary implementation (more efficient):
def HashMidSquare(key, N):
    R = 24
    squaredKey = key * key
    
    lowBitsToRemove = (32 - R) // 2
    extractedBits = squaredKey >> lowBitsToRemove
    extractedBits = extractedBits & (0xFFFFFFFF >> (32 - R))
    
    return extractedBits % N

# The mid-square hash function is typically implemented using binary (base 2), not decimal, because a binary implementation is faster. A binary implementation only requires a few shift and bitwise AND operations.
# A binary mid-square hash function extracts the middle R bits and returns the remainder of the middle bits divided by hash table size N, where R ≥ log₂(N).

# 7.4 Multiplicative String Hash Function
"""
Now let's talk about hashing strings, because strings are one of the most common key types. 
You can't just use modulo or mid-square on a string—you need to convert the string to an integer first. 
A popular approach is the multiplicative string hash function.

The idea is to build up a hash value by repeatedly multiplying and adding. 
You start with some initial value—let's call it stringHash. 
For each character in the string, you multiply stringHash by some constant multiplier, then add the character's ASCII value. 
After processing all characters, you return stringHash modulo your table size.

One of the most famous versions of this was created by Daniel Bernstein, and it's called djb2. 
It uses an initial value of 5,381 and a multiplier of 33. 
These numbers weren't chosen randomly—Bernstein tested many values empirically and found these work exceptionally well for short English strings, which are common in many applications like symbol tables in compilers or dictionaries in interpreters.

Why 33 specifically? 
Well, 33 is 32 plus 1, and 32 is a power of 2. 
This means multiplying by 33 can be optimized: instead of a multiplication, you can do a left shift by 5 bits and add. 
This makes it very fast while still providing good distribution.

The key property of a good string hash function is that different strings produce different hash codes—not always, because you have more possible strings than possible hash codes, but usually. 
And even similar strings should produce different hash codes. "Alice" and "alice" and "Alicf" should all hash to different values.
"""
# A multiplicative string hash repeatedly multiplies the hash value and adds the ASCII (or Unicode) value of each character in the string.
def HashMultiplicative(key, N, InitialValue=5381, HashMultiplier=33):
    stringHash = InitialValue
    
    for strChar in key:
        stringHash = (stringHash * HashMultiplier) + ord(strChar)
    
    return stringHash % N

# Daniel J. Bernstein created a popular version (djb2) that uses an initial value of 5381 and a multiplier of 33. Bernstein's hash function performs well for hashing short English strings.
"""
Tracing through "Hi":

Initial: stringHash = 5381

Character 'H' (ASCII 72):
  stringHash = 5381 * 33 + 72
  stringHash = 177,573 + 72 = 177,645

Character 'i' (ASCII 105):
  stringHash = 177,645 * 33 + 105
  stringHash = 5,862,285 + 105 = 5,862,390

Return: 5,862,390 % N
The multiplication makes character order significant, so "abc", "bca", and "cab" all produce different hash codes.
"""

# Part 8: Direct Hashing
"""
Direct hashing. This is when you use the key itself directly as the array index. 
You don't compute a hash code, you don't use modulo—you just use key as the index. 
A hash table implemented this way is called a direct access table.

The structure is simple: an array of pointers to values. 
If array[key] is null, that key doesn't exist. If it's not null, it points to the value for that key.
The operations are trivial. 
Get(key)? Just return array[key]. 
Insert(key, value)? Just do array[key] equals value. 
Remove(key)? Just set array[key] to null. 
Everything is literally one array access. Perfect O(1) performance, guaranteed.

So why don't we always use this? 
Two reasons, and they're both severe limitations.
- First, your keys must be non-negative integers. You can't use direct hashing with strings or objects or anything else. The key has to be a valid array index.
- Second, and this is usually the dealbreaker, your array size must equal your largest key value plus one. If your keys can range from 0 to a million, you need an array with a million and one elements. 
If you only have a hundred actual items, you're wasting enormous amounts of memory. Most of that array is just sitting there empty.

So direct access tables are only useful in very specific scenarios. 
The key range has to be small and ideally dense. For example, if your keys are student IDs from 1000 to 9999, an array of 10,000 elements might be acceptable if you have thousands of students. 
But for general-purpose use, direct hashing just isn't practical.
"""

def HashGet(directAccessTable, key):
    return directAccessTable[key]

def HashInsert(directAccessTable, key, value):
    directAccessTable[key] = value

def HashRemove(directAccessTable, key):
    if directAccessTable[key] != None:
        directAccessTable[key] = None
        return True
    return False

# Part 9: Cryptography and Password Hashing
"""
Now let's briefly touch on a related but distinct topic: cryptographic hashing. 
This is different from hash tables, but it uses similar terminology, so I want to make sure you understand the difference.

When we've been talking about hash functions, we've been talking about functions designed to distribute data across array buckets. 
But hash functions are also used in a completely different context: cryptography and security.

Cryptography is the study of secure communication and data protection. 
In cryptography, you often need to encrypt data—transform it so that unauthorized parties can't understand it—and then decrypt it to recover the original. 
Hash functions play a role here, but in a different way than they do in hash tables.

A cryptographic hash function is designed with different goals. 
- First, it needs to be a one-way function. That means if I give you a hash value, you should not be able to reconstruct the original input. This is completely different from hash table hash functions, where we don't care about reversibility.
- Second, it needs to be collision-resistant. It should be computationally infeasible to find two different inputs that produce the same hash value. Again, this is much stronger than what we need for hash tables.
- Third, it should have the avalanche effect: changing even one bit of the input should change approximately half the bits of the output. The hash should look completely different.

A common cryptographic hash function you've probably heard of is SHA-256. 
It takes any input—could be a file, a string, whatever—and produces a 256-bit hash value. 
This hash is useful for verifying data integrity. If you download a file and someone provides the SHA-256 hash, you can compute the hash of what you downloaded and compare. 
If they match, you know the file wasn't corrupted or tampered with.

Password hashing. This is incredibly important in modern software systems.
Here's the problem: many online services need to verify passwords, but storing passwords in a database is risky. 
If the database is breached—and unfortunately, breaches happen all the time—attackers would have everyone's passwords. 
Those users probably use the same passwords on other sites, so the damage spreads.

The solution is to store password hashes instead of passwords. When a user creates an account with password "MySecurePass123," the system doesn't store that string. 
Instead, it computes a cryptographic hash—let's say SHA-256("MySecurePass123")—and stores the hash value. Let's say that hash is "a3f2b4c8..."—some long hexadecimal string.
When the user logs in later, they enter their password. The system computes the hash of what they entered and compares it to the stored hash. If they match, the password is correct. If they don't match, it's wrong.
The good part is that even if attackers steal the database, they only get the hashes. Because cryptographic hash functions are one-way, they can't reverse the hash to get the original password. The users' passwords remain protected.

The term "hash function" is used in two different contexts. 
In data structures, it's about distributing data across buckets. 
In cryptography, it's about security properties like one-way-ness and collision resistance. 
The underlying concept—computing a fixed-size value from arbitrary input—is the same, but the design goals are completely different.
"""

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Example usage:
password = "MySecurePass123"
password_hash = hash_password(password)

print(f"Password: {password}")
print(f"Hash: {password_hash}")
# Hash: 9b871512327a3a7b8e6d42f0b9e8c4d3a5f1e2c8b7a6d5c4b3a2f1e0d9c8b7a6
# When the user attempts a login, the supplied password is hashed, and the hash is compared against the database's hash value. Because the passwords are not stored, if a database with password hashes is breached, attackers may still have a difficult time determining a user's password.
class UserDatabase:
    def __init__(self):
        self.users = {}  # username -> password_hash
    
    def register(self, username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = password_hash
    
    def login(self, username, password):
        if username not in self.users:
            return False
        
        entered_hash = hashlib.sha256(password.encode()).hexdigest()
        return entered_hash == self.users[username]

# Usage:
db = UserDatabase()
db.register("alice", "MySecurePass123")
print(db.login("alice", "WrongPassword"))    # False
print(db.login("alice", "MySecurePass123"))  # True


# Summary and Key Takeaways
"""
Let's pull everything together. 
We've covered a lot of ground today, so let me recap the key ideas and show you how they fit together.
We started with the map abstract data type, which is fundamentally about associations between keys and values. 
The operations—insert, get, remove—are simple to describe but challenging to implement efficiently.

Hash tables are our solution. 
The core insight is this two-step mapping: convert any key to an integer hash code, then use modulo to map that hash code to a bucket index in a reasonably-sized array. 
This gives us fast operations with modest memory usage.

But this mapping introduces collisions—different keys mapping to the same bucket. 
We looked at two fundamentally different approaches to handling collisions.
Chaining uses linked lists at each bucket. It's conceptually simple and works well even when the table gets quite full. 
The performance degrades gracefully as the load factor increases. The downside is the memory overhead of storing pointers and the potential for poor cache performance.
Open addressing, particularly linear probing, stores one item per bucket and probes for alternative locations when collisions occur. 
It has better cache performance because everything is in one array. But it requires careful handling of empty bucket types—empty-since-start versus empty-after-removal—and it suffers from clustering. 
You need to keep the load factor lower than with chaining.

The performance of any hash table critically depends on the hash function. 
A good hash function distributes keys uniformly, minimizing collisions. 
We looked at several: the simple modulo method, the mid-square method, and multiplicative string hashing like Bernstein's djb2. 
Each has its place depending on your key types and distribution.

In terms of complexity, hash tables give us remarkable performance. 
Best case and average case, all operations—insert, search, remove—are O(1), constant time. 
This is as good as it gets. The worst case is O(n), which happens when all keys collide into one bucket, but with a good hash function and reasonable load factor, this is extremely unlikely.

The load factor α, which is the number of items divided by the number of buckets, is your key performance metric. 
Keep it below 0.75 or so for open addressing, and you can go a bit higher—maybe 1 or 2—for chaining. 
When the load factor gets too high, you resize the table, which involves creating a larger array and rehashing all existing items.

When should you use a hash table? 
Whenever you need fast key-value lookups and you don't care about maintaining any order. 
Hash tables don't keep items sorted. If you need to iterate through items in order, you want a different data structure, like a balanced binary search tree. 
But for pure lookup performance, hash tables are unbeatable.

Real-world applications are everywhere. 
- Databases use hash tables for indexing. 
- Compilers use them for symbol tables—looking up variable names and their types. 
- Web browsers and content delivery networks use them for caching. 
- Programming languages provide them as built-in data structures: Python's dict, Java's HashMap, C++'s unordered_map. They're all hash tables under the hood.

Let me leave you with some questions to think about. 
- Why can't we always use a perfect hash function? 
- When would you choose chaining over linear probing or vice versa? 
"""