import random
  
punct = (".", ";", "!", "?", ",")
count = 0
new_word = ""
  
inputfile = input("Enter input file name:")
  
with open(inputfile, 'r') as fin:
    for line in fin.readlines():  # Read line by line in txt file
  
        for word in line.split():  # Read word by word in each line
  
            if len(word) > 3:  # If word length >3
  
                '''If word ends with punctuation
                      Remove firstletter, lastletter and punctuation
                      Shuffle the words
                      Add the removed letters (first letter)
                      Add the removed letters (last letter)
                      Add the removed letters (punctuation mark)'''
  
                if word.endswith(punct):
                    word1 = word[1:-2]
                    word1 = random.sample(word1, len(word1))
                    word1.insert(0, word[0])
                    word1.append(word[-2])
                    word1.append(word[-1])
  
                    '''If there is no punctuation mark 
                      Remove first letter and last letter
                      Shuffle the word
                      Add the removed letters (first letter)
                      Add the removed letters (last letter)
                      Append the word and " " to the previous words'''
  
                else:
                    word1 = word[1:-1]
                    word1 = random.sample(word1, len(word1))
                    word1.insert(0, word[0])
                    word1.append(word[-1])
                    new_word = new_word + ''.join(word1) + " "
  
            '''If word length <3
                  just append the word and " " to the previous words'''
  
        else:
            new_word = new_word + word + " "
  
        # "Append to <filename>Scrambled.txt"
  
with open((inputfile[:-4] + "Scrambled.txt"), 'a+') as fout:
    fout.write(new_word + "\n")
  
new_word = ""
