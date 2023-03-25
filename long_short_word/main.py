# Trouver le mot le plus court et le plus long dans une phrase

def get_min_and_max_words(sentence):
  list_words = sentence.split(" ")
  min_word = min(list_words, key=len)
  max_word = max(list_words, key=len)
  return min_word, max_word

def get_min_and_max_words_sorted(sentence):
  list_words = sentence.split(" ")
  min_word, max_word = get_min_and_max_words(sentence)

  all_min = [w for w in list_words if len(w) == len(min_word)]
  all_max = [w for w in list_words if len(w) == len(max_word)]

  all_min.sort()
  all_max.sort()

  return all_min[0], all_max[0]

def get_min_and_max_words_sorted2(sentence):
  list_words = sentence.split(" ")
  list_words.sort()
  min_word = min(list_words, key=len)
  max_word = max(list_words, key=len)
  return min_word, max_word

s = "Un chasseur sachant chasser sait chasser sans son chien"

min_word, max_word = get_min_and_max_words_sorted2(s)

print(f"Mot le plus petit: {min_word}")
print(f"Mot le plus grand: {max_word}")