"""
To find out what the two dictionaries have in common, simply perform common set
operations using the keys() or items() methods.
"""

if __name__ == "__main__":
  a = {
    'x': 1,
    'y': 2,
    'z': 3
  }

  b = {
    'w': 10,
    'x': 11,
    'y': 2
  }

  print(a.keys() & b.keys())  # Find keys in common
  print(a.keys() | b.keys())  # Find all keys in both dicts
  print(a.keys() ^ b.keys())  # Find keys present only in one dict
  print(a.keys() - b.keys())  # Find keys in a that are not in b
  print(a.items() & b.items())  # Find (key,value) pairs in common
