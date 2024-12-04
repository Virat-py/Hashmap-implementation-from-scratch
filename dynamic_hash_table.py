from hash_table import HashSet, HashMap
from prime_generator import get_next_size


class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def rehash(self):
        new_size = get_next_size()
        temp_params = None
        if self.collision_type == "Double":
            temp_params = (self.z1, self.z2, self.c2, new_size)
        else:
            temp_params = (self.z, new_size)
        temp_table = HashSet(self.collision_type, temp_params)

        # Re-insert elements from the old hash table
        if self.collision_type == "Chain":
            for bucket in self.hash:
                if bucket is not None:
                    for item in bucket:
                        temp_table.insert(item)
        else:
            for item in self.hash:
                if item is not None:
                    temp_table.insert(item)

        self.hash = temp_table.hash
        self.size = temp_table.size

    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)


        if self.get_load() >= 0.5:
            self.rehash()

    def get_load(self):
        return self.elements / self.size

class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def rehash(self):
        new_size = get_next_size()
        temp_params = None
        if self.collision_type == "Double":
            temp_params = (self.z1, self.z2, self.c2, new_size)
        else:
            temp_params = (self.z, new_size)
        temp_table = HashSet(self.collision_type, temp_params)

        # Re-insert elements from the old hash table
        if self.collision_type == "Chain":
            for bucket in self.hash:
                if bucket is not None:
                    for item in bucket:
                        temp_table.insert(item)
        else:
            for item in self.hash:
                if item is not None:
                    temp_table.insert(item)

        self.hash = temp_table.hash
        self.size = temp_table.size

    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)

        if self.get_load() >= 0.5:
            self.rehash()

    def get_load(self):
        return self.elements / self.size  # Use updated size for accurate load calculation