from prime_generator import get_next_size
class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.collision_type = collision_type
        if collision_type == "Double":
            self.z1 = params[0]
            self.z2 = params[1]
            self.c2 = params[2]
            self.size = params[3]
        else:
            self.z = params[0]
            self.size = params[1]


        self.hash = [None] * self.size
        self.elements = 0

    def get_element_count(self):
        """Return the number of elements currently in the hash table"""
        return self.elements

    def hash_function(self,z,key,extra=None):

        ans = 0
        for i in range(len(key)):
            if key[i].islower():
                p=ord(key[i])-ord("a")
            else:
                p=ord(key[i])-ord("A")+26
            ans+= p*pow(z,i)
        if extra!=None:
            return ans
        return ans % self.size

    def insert(self, x):
        # Check if the table is already full before attempting insertion


        slot = self.get_slot(x) if isinstance(x, str) else self.get_slot(x[0])

        if self.collision_type == "Chain":
            # Handle insertion for chaining
            if self.hash[slot] is None:
                self.hash[slot] = [x]
                self.elements += 1
            else:
                # Check if the item already exists in the chain
                flag = False
                if isinstance(x, tuple):
                    for index, value in enumerate(self.hash[slot]):
                        if value[0] == x[0]:
                            flag = True
                            self.hash[slot][index] = x
                            break
                else:
                    for index, value in enumerate(self.hash[slot]):
                        if value == x:
                            flag = True
                            break
                if not flag:
                    self.hash[slot].append(x)
                    self.elements += 1
        else:
            # Handle linear or double hashing insertion
            if self.elements >= self.size:
                raise Exception("Hash table full")
            flag = False
            if self.hash[slot] is not None:
                if isinstance(x, tuple):
                    if x[0] == self.hash[slot][0]:
                        flag = True
                        self.hash[slot] = x
                else:
                    if x == self.hash[slot]:
                        flag = True
                        self.hash[slot] = x
            if not flag:
                self.hash[slot] = x
                self.elements += 1

    def find(self, key):
        """Find an element in the hash table"""
        slot = self.get_slot(key)

        if self.collision_type == "Chain":
            if self.hash[slot] is not None:
                for item in self.hash[slot]:
                    if isinstance(item, tuple):
                        if item[0] == key:
                            return True
                    elif item == key:
                        return True
                return False
            return False

        else:  # Linear or Double
            current_slot = slot
            if self.hash[current_slot] is not None:
                if isinstance(self.hash[current_slot], tuple):
                    return self.hash[current_slot][0] == key
                return self.hash[current_slot] == key
            return False

    def get_slot(self, key):

        if self.collision_type == "Chain":
            initial_slot = self.hash_function(self.z,key)
            return initial_slot

        elif self.collision_type == "Linear":
            slot = self.hash_function(self.z, key)

            while self.hash[slot] is not None:

                if isinstance(self.hash[slot],tuple):
                    if self.hash[slot][0]==key:
                        return slot
                else:
                    if self.hash[slot]==key:
                        return slot

                slot = (slot + 1) % self.size  # Use self.size instead of self.hash

            return slot

        elif self.collision_type == "Double":
            initial_slot = self.hash_function(self.z1, key)
            step_size = self.c2 - (self.hash_function(self.z2,key,1)%self.c2)
            slot = initial_slot
            i=0

            while self.hash[slot] is not None:
                if i>self.size:
                    raise Exception("Table is full")
                if isinstance(self.hash[slot],tuple):
                    if self.hash[slot][0]==key:
                        return slot
                else:
                    if self.hash[slot]==key:
                        return slot
                slot = (initial_slot + i * step_size) % self.size
                i+=1

            return slot

    def get_load(self):
        return self.elements/self.size

    def __str__(self):
        result = []

        if self.collision_type == "Chain":
            for index, value in enumerate(self.hash):
                if value is not None:

                    if isinstance(value[0],str):
                        temp=""
                        for i in value:
                            temp=temp+i+" ; "
                        temp=temp[:-3]
                        result.append(temp)
                    else:
                        temp=""
                        for i in value:
                            temp= temp+"("+i[0]+","+str(i[1])+")"+" ; "
                        temp=temp[:-3]
                        result.append(temp)

                else:
                    result.append("<EMPTY>")

        else:  # For Linear Probing and Double Hashing
            for index, value in enumerate(self.hash):
                if value is not None:
                    if isinstance(value,tuple):
                        i, j = value[0], value[1]
                        temp = "(" + i + "," + j + ")"
                        result.append(temp)
                    else:
                        result.append(str(value))
                else:
                    result.append("<EMPTY>")

        # Join all parts of the result list with '|'
        return " | ".join(result)

    def print_library(self):
        if self.collision_type == "Chain":
            for i in self.hash:
                if i!=None:
                    for j in i:
                        print(f"{j[0]}: {str(j[1])}")



    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass

# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF,
# YOU WOULD NOT NEED TO WRITE IT TWICE

class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def insert(self, key):
        super().insert(key)

    def find(self, key):
        return super().find(key)

    def get_slot(self, key):
        return super().get_slot(key)

    def get_load(self):
        return super().get_load()

    def get_element_count(self):
        return super().get_element_count()

    def get_words(self):
        """Return a list of all distinct words in the set"""
        words = []
        if self.collision_type == "Chain":
            for bucket in self.hash:
                if bucket is not None:
                    for word in bucket:
                        if isinstance(word, str):  # Only add string items (words)
                            words.append(word)
        else:  # Linear or Double
            for item in self.hash:
                if item is not None and isinstance(item, str):
                    words.append(item)
        return words

    def __str__(self):
        return super().__str__()

    def rehash(self):
        pass


class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def insert(self, x):
        # x = (key, value)
        super().insert(x)

    def find(self, key):
        slot = self.get_slot(key)
        if slot is None:
            return None

        if self.collision_type == "Chain":
            if self.hash[slot] is not None:
                for item in self.hash[slot]:
                    if isinstance(item, tuple) and item[0] == key:
                        return item[1]
            return None
        else:  # Linear or Double
            item = self.hash[slot]
            if item is not None and isinstance(item, tuple) and item[0] == key:
                return item[1]
            return None

    def get_slot(self, key):
        return super().get_slot(key)

    def get_load(self):
        return super().get_load()

    def __str__(self):
        return super().__str__()

    def print_library(self):
        if self.collision_type == "Chain":
            for bucket in self.hash:
                if bucket is not None:
                    for item in bucket:
                        if isinstance(item, tuple):
                            print(f"{item[0]}: {item[1]}")
        else:
            for element in self.hash:
                if element is not None:
                    print(f"{element[0]}: {element[1]}")