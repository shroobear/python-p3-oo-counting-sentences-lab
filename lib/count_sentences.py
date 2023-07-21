#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    self.value = value

  def get_value(self):
    print("Getting value")
    return self._value
  
  def set_value(self, value):
    if(type(value) == str):
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    if self.value.endswith("."):
      return True
    return False
  
  def is_question(self):
    if self.value.endswith("?"):
      return True
    return False

  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    return False

  def count_sentences(self):
    replaced_qmarks = self.value.replace("?", ".")
    replaced_punctuation = replaced_qmarks.replace("!", ".")
    sentence_list = replaced_punctuation.split(". ")
    print(sentence_list)
    if sentence_list == ['']:
      return 0
    return(len(sentence_list))

simple_string = MyString("one. two. three?")
empty_string = MyString()
complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
simple_string.count_sentences()
empty_string.count_sentences()
complex_string.count_sentences()