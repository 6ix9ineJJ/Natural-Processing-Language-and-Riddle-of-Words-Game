# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wApWzgB3-xfA5VmC5Lzy6JKn49gzSNY1
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd drive/MyDrive

# Commented out IPython magic to ensure Python compatibility.
# %ls
# %cd NLP

!pip install openai

api_key = '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'

import openai
openai.api_key = api_key

def gpt_3(prompt,engine = 'text-davinci-002',temp = 0.7, top_p = 1.0, tokens = 400, freq_pen = 0.0, pres_pen = 0.0, stop = '[<<END>>]'):
  prompt = prompt.encode(encoding = 'ASCII').decode()
  
  response = openai.Completion.create(
      engine = engine,
      prompt = prompt,
      temperature = temp,
      top_p = top_p,
      max_tokens = tokens,
      frequency_penalty = freq_pen,
      presence_penalty = pres_pen,
      stop = stop
    )
  text = response['choices'][0]['text'].strip()
  return text

def main():
  conversation = ["this is a word riddles game. This game has two player guessers and a presenter. Note all the guessing and presenting are about(actors, cricketers, police, the army, and famous people) from Pakistan.",
                """Example:
                presenter = He is famous, he is Cricketer and a politician
                guesser = Imran Khan
                
                presenter = He is famous, he is a singer and songwriter. he also works in Bollywood
                guesser =  Atif Aslam"""]
  # prompt = """this is a word riddles game. This game has two player guessers and a presenter. Note all the guessing and presenting are about(actors, cricketers, police, the army, and famous people) from Pakistan.
  #             Example: 
  #               presenter = He is famous, he is Cricketer and a politician
  #               guesser = Imran Khan"""
  # response2 = gpt_3(prompt)
  #print(response2)
  print("________________This is riddle game______________________________________")
  point_guesser = 0
  point_presenter = 0
  while True:
    x = input("Select 1 from presenter and 2 from guesser:  ")
    if "1" == x: 
      prompt = "Now You are Guesser and I am presenter"
      conversation.append( prompt)
      user_input = input("Write your riddle about actors, cricketers, police, the army, and famous people:  ")
      conversation.append("Presenter: %s" %user_input)
      text_block = "\n".join(conversation)
      prompt = text_block  + '\nGuesser'
      response2 = gpt_3(prompt)
      print(response2)
      conversation.append("Guesser: %s" %response2)
      y = input("if guess is Correct press one else 2")
      if y == '1':
        point_presenter = point_presenter + 1
        print("Points:\nPresenter:%s\nGuesser:%s",point_presenter,point_guesser)
      elif y == '2':
        point_guesser = point_guesser + 1
        print("Points:\nPresenter:%s\nGuesser:%s",point_presenter,point_guesser)

    elif "2" == x:
      prompt = "Now You are presenter and I am Guesser"
      conversation.append( prompt)
      text_block = "\n".join(conversation)
      prompt = text_block  + '\n/presenter'
      response2 = gpt_3(prompt)
      lines = response2.split('\n')
      print(lines)
      y = input("if guess is Correct press one else 2")
      if y == '1':
        point_guesser = point_guesser + 1
        print("Points:\nPresenter:%s\nGuesser:%s",point_presenter,point_guesser)
      elif y == '2':
        point_presenter = point_presenter + 1
        print("Points:\nPresenter:%s\nGuesser:%s",point_presenter,point_guesser)

   
main()

conversation = ["this is a word riddles game. This game has two player guessers and a presenter. Note all the guessing and presenting are about(actors, cricketers, police, the army, and famous people) from Pakistan.",
                """Example: 
presenter = He is famous, he is Cricketer and a politician
guesser = Imran Khan

presenter = He is famous, he is a singer and songwriter. he also works in Bollywood
guesser =  Atif Aslam"""]
text_block = "\n".join(conversation)
print(text_block)

string = "This is a\nmulti-line\nstring."
lines = string.split('\n')
print(lines)









