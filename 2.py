from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
  pass

ordered_counter = OrderedCounter()

with open('2.txt', 'r') as data_file:
    for line in data_file:
        for c in line.rstrip():
            ordered_counter[c] += 1

frequencies = ordered_counter.values()
average_freq = sum(frequencies) / len(frequencies)

rares = ''.join([letter for letter, freq in ordered_counter.iteritems() if freq < average_freq])
