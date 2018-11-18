import math as m
class LaplaceUnigramLanguageModel:

  sum_word=""
  word_uni = {}
  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    for sentence in corpus.corpus: # iterate over sentences in the corpus
      #print(sentence)
      for datum in sentence.data: # iterate over datums in the sentence
        if datum.word not in self.word_uni:
          self.word_uni[datum.word]=1
        else:
          self.word_uni[datum.word]=self.word_uni[datum.word]+1
    # self.word_uni['unk']=0
    # print(sum(self.word_uni.values()))
    # print(self.word_uni['<s>'])
    # print(self.word_uni['<s>']/sum(self.word_uni.values()))

    self.sum_word=sum(self.word_uni.values())+len(self.word_uni)
    pass

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    score = 0
    probability = 0
    for token in sentence:  # iterate over words in the sentence
       if token in self.word_uni:

         score+= m.log(self.word_uni[token]+1)
         score-=m.log(self.sum_word)
       else:
         #self.word_uni['unk'] = self.word_uni['unk'] + 1
         score+=m.log(1);
         score-=m.log(self.sum_word)

    return score
