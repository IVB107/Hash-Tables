

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.storage = [None for i in range(capacity)]
        self.capacity = capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, maximum):
    hash_num = 5381
    for char in string:
        hash_num = ((hash_num * 33) + hash_num) + ord(char)
    return hash_num % maximum


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    bucket_index = hash(key, hash_table.capacity)

    new_pair = LinkedPair(key, value)
    existing_pair = hash_table.storage[bucket_index]

    if existing_pair:
        last_pair = None
        while existing_pair:
            if existing_pair.key == key:
                # Found existing key, replace value
                existing_pair.value = value
                return
            last_pair = existing_pair
            existing_pair = existing_pair.next
        
        # Chain new_pair to end of bucket's linked-list
        last_pair.next = new_pair
    else:
        hash_table.storage[bucket_index] = new_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    bucket_index = hash(key, hash_table.capacity)

    existing_pair = hash_table.storage[bucket_index]
    if existing_pair:
        last_pair = None
        while existing_pair:
            if existing_pair.key == key:
                if last_pair:
                    last_pair.next = existing_pair.next
                else:
                    hash_table.storage[bucket_index] = existing_pair.next
            last_pair = existing_pair
            existing_pair = existing_pair.next


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    bucket_index = hash(key, hash_table.capacity)

    existing_pair = hash_table.storage[bucket_index]
    if existing_pair:
        while existing_pair:
            if existing_pair.key == key:
                return existing_pair.value
            existing_pair = existing_pair.next
    return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    resized = hash_table.capacity * 2
    new_hash_table = HashTable(resized)

    for i in hash_table.storage:
        current = hash_table.storage[i]
        while current is True:
            hash_table_insert(new_hash_table, hash_table.storage[i].key, hash_table.storage[i].value)
            current = current.next
    return new_hash_table

def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    # old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #     + " to " + str(new_capacity) + ".")


Testing()
