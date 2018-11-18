import math
import collections
class CustomLanguageModel:
  word_null={}
  word_uni = {}
  word_before = {}
  word_after = {}
  word_uni_uni={}
  word_bi = collections.defaultdict(list)
  sum_word=""

  # def __init__(self, corpus):
  #   """Initialize your data structures in the constructor."""
  #   # TODO your code here
  #   self.train(corpus)
  #
  # def train(self, corpus):
  #   """ Takes a corpus and trains your language model.
  #       Compute any counts or other corpus statistics in this function.
  #   """
  #   # TODO your code here
  #   for sentence in corpus.corpus: # iterate over sentences in the corpus
  #     #print(sentence)
  #     for datum in range(0,len(sentence.data)-1): # iterate over datums in the sentence
  #       word_1=sentence.data[datum].word
  #       word_2=sentence.data[datum+1].word
  #       if word_1 not in self.word_uni:
  #         self.word_uni[word_1]=1
  #       else:
  #         self.word_uni[word_1]=self.word_uni[word_1]+1
  #
  #       if word_1+" "+word_2 not in self.word_bi:
  #         temp=word_1+" "+word_2
  #         self.word_bi[word_1+" "+word_2].append(1)
  #         self.word_bi[temp].append(word_1)
  #         self.word_bi[temp].append(word_2)
  #       else:
  #           # print(self.word_bi[word_1+" "+word_2])
  #           self.word_bi[word_1+" "+word_2][0]=self.word_bi[word_1+" "+word_2][0]+1
  #
  #
  #
  #       if datum==len(sentence.data)-1:
  #         word_1 = sentence.data[datum+1].word
  #         if word_1 not in self.word_uni:
  #           self.word_uni[word_1] = 1
  #         else:
  #           self.word_uni[word_1] = self.word_uni[word_1] + 1
  #
  #   # self.word_uni['unk']=0
  #   # print(self.word_uni)
  #   # print(self.word_bi)
  #   self.context()
  #   pass
  #
  # def context(self):
  #   count=0
  #   index=1
  #   for word in self.word_uni:
  #     self.word_before[word]=0
  #     self.word_after[word]=0
  #   for word in self.word_before:
  #     for a in self.word_bi:
  #       if a[1]==word:
  #         self.word_before[word]=self.word_before[word]+1
  #   for word in self.word_after:
  #     for a in self.word_bi:
  #       if a[2]==word:
  #         self.word_before[word]=self.word_before[word]+1
  # def score(self, sentence):
  #   """ Takes a list of strings as argument and returns the log-probability of the
  #       sentence using your language model. Use whatever data you computed in train() here.
  #   """
  #   score =0;
  #   temp2=0;
  #   temp3=0;
  #   d=0.04
  #   # TODO your code here
  #   for datanum in range(0,len(sentence)-1):
  #     word_1=sentence[datanum]
  #     word_2=sentence[datanum+1]
  #     temp=word_1+" "+word_2
  #     # print(self.word_bi[temp])
  #     # print(self.word_bi[temp][0])
  #     # print(self.word_bi[temp][1])
  #     if temp in self.word_bi:
  #       temp2=(self.word_bi[temp][0]-d)/self.word_uni[self.word_bi[temp][1]]
  #
  #       # score+=math.log(self.word_bi[temp][0]+1)
  #       # score-=math.log(self.word_uni[self.word_bi[temp][1]]+len(self.word_bi))
  #       # print(score)
  #     else:
  #       temp2=0
  #
  #       # score += math.log(1)
  #       # if word_1 in self.word_uni:
  #       #   score -= math.log(self.word_uni[word_1] + len(self.word_bi))
  #       # else:
  #       #   score -= math.log(len(self.word_bi))
  #         # print(score)
  #     if word_1 not in self.word_uni or word_2 not in self.word_uni:
  #       temp3 = 0
  #       temp3 = 0
  #     else:
  #       temp3=d*self.word_before[word_1]/self.word_uni[word_1]
  #       temp3=temp3*self.word_after[word_2]/len(self.word_bi)
  #
  #     if temp3==0 and temp2==0:
  #       score
  #     else:
  #       score+=math.log(temp2+temp3)
  #   return score


  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model.
        Compute any counts or other corpus statistics in this function.
    """
    # TODO your code here
    for sentence in corpus.corpus:  # iterate over sentences in the corpus
      # print(sentence)
      for datum in range(0, len(sentence.data) - 2):  # iterate over datums in the sentence
        word_0=sentence.data[datum].word
        word_1 = sentence.data[datum].word+" "+sentence.data[datum+1].word
        word_2 = sentence.data[datum + 2].word
        if word_0 not in self.word_null:
          self.word_null[word_0]=1
        else:
          self.word_null[word_0]=self.word_null[word_0]+1

        if word_1 not in self.word_uni:
          self.word_uni[word_1] = 1
        else:
          self.word_uni[word_1] = self.word_uni[word_1] + 1

        if word_1 + " " + word_2 not in self.word_bi:
          temp = word_1 + " " + word_2
          self.word_bi[word_1 + " " + word_2].append(1)
          self.word_bi[temp].append(word_1)
        else:
          # print(self.word_bi[word_1+" "+word_2])
          self.word_bi[word_1 + " " + word_2][0] = self.word_bi[word_1 + " " + word_2][0] + 1


        if datum == len(sentence.data) - 3:
          for i in range(1,3):

            word_0=sentence.data[datum+i]
            if word_0 not in self.word_null:
              self.word_null[word_0]=1
            else:
              self.word_null[word_0]=self.word_null[word_0]+1
          word_1 = sentence.data[datum + 1].word + " " +sentence.data[datum+2].word
          if word_1 not in self.word_uni:
            self.word_uni[word_1] = 1
          else:
            self.word_uni[word_1] = self.word_uni[word_1] + 1


    self.sum_word=sum(self.word_null.values()) + len(self.word_null)
    # self.word_uni['unk']=0
    # print(self.word_uni)
    # print(self.word_bi)

    pass

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0;
    # TODO your code here
    for datanum in range(0, len(sentence) - 2):
      word_0=sentence[datanum]
      word_1 = sentence[datanum] +" "+ sentence[datanum +1]
      word_2 = sentence[datanum + 2]

      temp = word_1 + " " + word_2
      # print(temp)
      # print(self.word_bi[temp])
      # print(self.word_bi[temp][0])
      # print(self.word_bi[temp][1])
      if temp in self.word_bi:
        score += math.log(self.word_bi[temp][0]+1)
        score -=math.log (self.word_uni[self.word_bi[temp][1]]+len(self.word_uni))
      else:
        score += math.log(1)

        if word_1 in self.word_uni:
          score -= math.log(self.word_uni[word_1] + len(self.word_uni))
          # x=self.word_uni[word_1]
          # # x=x/(self.word_null[word_0])
          # x = x / (self.word_null[word_0]+len(self.word_null))
          # x=x*0.4
          # score+=math.log(x)
        # elif word_0 in self.word_null:
        else:
          score -=math.log (len(self.word_uni))
        # else: word_0 in self.word_null
        # x = 1
        # x = x / len(self.word_null)
        # # x=x/self.sum_word
        # x = x * 0.4
        # score += math.log(x)
          # x=self.word_null[word_0]

        # else:
        #   x = 1
        #   x = x / self.sum_word
        #   x = x * 0.4
        #   score += math.log(x)
        # score += math.log(1)
        # if word_1 in self.word_uni:
        #   score -= math.log(self.word_uni[word_1] + len(self.word_bi))
        # else:
        #   score -= math.log(len(self.word_bi))


    return score
