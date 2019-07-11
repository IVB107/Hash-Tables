

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.storage = [None for i in range(capacity)]
        self.capacity = capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, maximum):
    hash_num = 5381
    for char in string:
        hash_num = ((hash_num * 33) + hash_num) + ord(char)
    return hash_num % maximum

# '''
# Fill this in.
# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    bucket_index = hash(key, hash_table.capacity)

    new_pair = Pair(key, value)
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


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
