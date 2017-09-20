def drop_first_last(grades):
  first, *middle, last = grades
  return first, sum(middle)/len(middle), last

if __name__ == '__main__':
  print(drop_first_last([1, 2, 3, 4, 5, 6]))

  record = ('archie', 'artsiom.tkachou@gmail.com', 'email1', 'email2')
  name, email, *phones = record
  print(phones)