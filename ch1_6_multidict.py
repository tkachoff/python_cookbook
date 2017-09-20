"""
Use a list if you want to preserve the insertion order of the items.
Use a set if you want to eliminate duplicates (and don’t care about the order)
"""
import collections
import pprint

if __name__ == "__main__":
  # Using list
  d_list = collections.defaultdict(list)
  d_list['a'].append(1)
  d_list['a'].append(2)
  d_list['b'].append(4)
  pprint.pprint(dict(d_list))

  # Using set
  d_set = collections.defaultdict(set)
  d_set['a'].add(1)
  d_set['a'].add(2)
  d_set['b'].add(4)
  pprint.pprint(dict(d_set))

  # Using regular dict and list
  d = {}
  d.setdefault('a', []).append(1)
  d.setdefault('a', []).append(2)
  d.setdefault('b', []).append(4)
  pprint.pprint(dict(d))

  # Using regular dict and set
  d2 = {}
  d2.setdefault('a', set()).add(1)
  d2.setdefault('a', set()).add(2)
  d2.setdefault('b', set()).add(4)
  pprint.pprint(dict(d2))
