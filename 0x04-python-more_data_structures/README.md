**Sets:**
A set is an unordered collection of unique elements. It is defined by enclosing the elements in curly braces ({}) or by using the `set()` function. Here's how you can work with sets:

1. **Creating a Set:**
   `````python
   my_set = {1, 2, 3, 4, 5}
   ```

2. **Adding and Removing Elements:**
   Sets support adding and removing elements.
   ````python
   my_set.add(6)       # Add an element to the set
   my_set.remove(3)    # Remove an element from the set
   ```

3. **Set Operations:**
   Sets have built-in operations like union, intersection, difference, and more.
   ````python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}
   union_set = set1.union(set2)           # Union of two sets
   intersection_set = set1.intersection(set2)   # Intersection of two sets
   difference_set = set1.difference(set2)   # Set difference
   ```

4. **Iterating over a Set:**
   You can use loops to iterate over the elements in a set.
   ````python
   for item in my_set:
       print(item)
   ```

**Dictionaries:**
A dictionary is an unordered collection of key-value pairs. It is defined using curly braces ({}) and consists of keys and their corresponding values separated by colons (:). Here's how you can work with dictionaries:

1. **Creating a Dictionary:**
   ````python
   my_dict = {'name': 'John', 'age': 25, 'country': 'USA'}
   ```

2. **Accessing Values:**
   You can access values in a dictionary using their keys.
   ````python
   print(my_dict['name'])      # Output: 'John'
   print(my_dict['age'])       # Output: 25
   ```

3. **Modifying and Adding Elements:**
   Dictionaries are mutable, so you can modify the value of existing keys or add new key-value pairs.
   ````python
   my_dict['age'] = 30                 # Modifying a value
   my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
   ```

4. **Dictionary Operations:**
   Dictionaries have various built-in operations, such as getting keys or values, checking for the presence of a key, and more.
   ````python
   keys = my_dict.keys()             # Get all keys
   values = my_dict.values()         # Get all values
   is_present = 'country' in my_dict  # Check if a key is present
   ```

5. **Iterating over a Dictionary:**
   You can iterate over the keys or values of a dictionary using loops.
   ````python
   for key in my_dict:
       print(key, my_dict[key])      # Output: key value pairs

   for value in my_dict.values():
       print(value)                  # Output: values
   ```

Dictionaries are useful for mapping one value to another and are commonly used for data representation and lookup operations.

Remember, sets are useful when you need to store unique elements, and dictionaries are ideal for key-value pair mappings.