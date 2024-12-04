# Deep Dive into Hashing: Custom HashMap and HashSet Implementations

This repository features a custom implementation of **HashMaps** and **HashSets**, built from scratch with robust collision handling and dynamic resizing capabilities.

---

## Features

1. **Collision Resolution Methods**:
   - **Chaining**: Uses linked lists for handling collisions.
   - **Linear Probing**: Resolves collisions by probing sequentially.
   - **Double Hashing**: Utilizes a secondary hash function for probing.

2. **Dynamic Resizing**:
   - Automatically resizes when the load factor exceeds a predefined threshold.
   - Employs prime-based resizing for optimal performance.

3. **Configurable Parameters**:
   - Allows customization of hashing methods, including double hashing parameters.

4. **Modular Structure**:
   - `HashTable`: Implements core HashMap and HashSet functionality.
   - `DynamicHashSet`: Adds dynamic resizing and rehashing capabilities.

---
