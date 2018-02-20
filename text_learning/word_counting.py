



s = 'how many words will be removed when we remove stopwords from hi katie the machine learning class will be great best sebastian'

number_of_occurences = 0
for word in s.split():
  if word == 'the':
    number_of_occurences += 1
print number_of_occurences
