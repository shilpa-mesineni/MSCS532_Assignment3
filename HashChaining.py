class HashTable:
    def __init__(self, size=10):
        self.size = size  # Number of buckets
        self.table = [[] for _ in range(self.size)]  # Initialize table with empty lists (chains)

    # Universal hash function: This hash function uses the built-in hash() function of Python and applies modulo operation
    def hash_function(self, key):
        return hash(key) % self.size

    # Insert key-value pair into the hash table
    def insert(self, key, value):
        hash_index = self.hash_function(key)
        bucket = self.table[hash_index]
        
        # Check if the key already exists, if so, update the value
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update the value
                return
        
        # If key doesn't exist, append the new key-value pair
        bucket.append((key, value))

    # Search for a value associated with a key
    def search(self, key):
        hash_index = self.hash_function(key)
        bucket = self.table[hash_index]
        
        # Look for the key in the appropriate bucket
        for k, v in bucket:
            if k == key:
                return v  # Return the value if key is found
        
        return None  # If key is not found

    # Delete a key-value pair from the hash table
    def delete(self, key):
        hash_index = self.hash_function(key)
        bucket = self.table[hash_index]
        
        # Find the key in the bucket and remove it
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Delete the key-value pair
                return True
        
        return False  # If key was not found

    # Utility function to display the contents of the hash table
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# Example usage
if __name__ == "__main__":
    # Create a hash table
    ht = HashTable(size=10)

    # Insert key-value pairs
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("orange", 3)
    ht.insert("grape", 4)

    # Display the hash table
    print("Hash Table after insertion:")
    ht.display()

    # Search for keys
    print("\nSearch results:")
    print("apple:", ht.search("apple"))  # Output: 1
    print("banana:", ht.search("banana"))  # Output: 2
    print("pear:", ht.search("pear"))  # Output: None

    # Delete a key-value pair
    print("\nDeleting 'banana'...")
    ht.delete("banana")

    # Display the hash table after deletion
    print("\nHash Table after deletion:")
    ht.display()

    # Try searching for the deleted key
    print("\nSearch for 'banana':", ht.search("banana"))  # Output: None
