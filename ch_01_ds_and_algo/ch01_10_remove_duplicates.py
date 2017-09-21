def dedupe(items):
  """
  If the values in the sequence are hashable, the problem can be easily
  solved using a set and a generator.
  :param items:
  :return: generator
  """
  seen = set()
  for item in items:
    if item not in seen:
      yield item
      seen.add(item)


def dedupe2(items, key=None):
  """
   If you are trying to eliminate duplicates in a sequence of unhashable
   types (such as dicts)
  :param items:
  :param key:
  :return:
  """
  seen = set()
  for item in items:
    val = item if key is None else key(item)
    if val not in seen:
      yield item
      seen.add(val)


if __name__ == "__main__":
  a = [1, 5, 2, 1, 9, 1, 5, 10]
  print(list(dedupe(a)))

  a2 = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
  print(list(dedupe2(a2, key=lambda d: (d['x'], d['y']))))
  print(list(dedupe2(a2, key=lambda d: d['x'])))
