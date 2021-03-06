import  collections,math
class LaplaceBigramLanguageModel:

  word_uni = {}
  word_bi = collections.defaultdict(list)


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
      for datum in range(0,len(sentence.data)-1): # iterate over datums in the sentence
        word_1=sentence.data[datum].word
        word_2=sentence.data[datum+1].word
        if word_1 not in self.word_uni:
          self.word_uni[word_1]=1
        else:
          self.word_uni[word_1]=self.word_uni[word_1]+1

        if word_1+" "+word_2 not in self.word_bi:
          temp=word_1+" "+word_2
          self.word_bi[word_1+" "+word_2].append(1)
          self.word_bi[temp].append(word_1)
        else:
            # print(self.word_bi[word_1+" "+word_2])
            self.word_bi[word_1+" "+word_2][0]=self.word_bi[word_1+" "+word_2][0]+1



        if datum==len(sentence.data)-2:
          word_1 = sentence.data[datum+1].word
          if word_1 not in self.word_uni:
            self.word_uni[word_1] = 1
          else:
            self.word_uni[word_1] = self.word_uni[word_1] + 1

    # self.word_uni['unk']=0
    # print(self.word_uni)
    # print(self.word_bi)

    pass

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score =0;
    # TODO your code here
    for datanum in range(0,len(sentence)-1):
      word_1=sentence[datanum]
      word_2=sentence[datanum+1]
      temp=word_1+" "+word_2
      # print(self.word_bi[temp])
      # print(self.word_bi[temp][0])
      # print(self.word_bi[temp][1])
      if temp in self.word_bi:
        score+=math.log(self.word_bi[temp][0]+1)
        score-=math.log(self.word_uni[self.word_bi[temp][1]]+len(self.word_bi))
        # print(score)
      else:
        score += math.log(1)
        if word_1 in self.word_uni:
          score -= math.log(self.word_uni[word_1] + len(self.word_bi))
        else:
          score -= math.log(len(self.word_bi))
          # print(score)

    return score
