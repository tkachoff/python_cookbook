"""
An OrderedDict internally maintains a doubly linked list that orders the
keys according to insertion order. When a new item is first inserted,
it is placed at the end of this list. Subsequent reassignment of an existing
key doesn’t change the order.
"""
import collections

if __name__ == "__main__":
  d = collections.OrderedDict()
  d['foo'] = 1
  d['bar'] = 2
  d['spam'] = 3
  d['grok'] = 4

  for key in d:
    print(key, d[key])
