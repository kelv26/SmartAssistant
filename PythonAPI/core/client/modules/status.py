import re


PRIORITY = 8

def handle(text, Mic, Agent):
  """
  Abilities:
  - report the status of the Smart Assistant (will soon be deprecated
    for AI to reply)
  """
  Mic.say("Everything is copacetic!")


def isValid(text):
  # check if text is valid
  return (
    (
      bool(re.search(r'\bhow |how\'s |what |what\'s \b', text, re.IGNORECASE)) and \
      bool(re.search(r'\b going| doing\b', text, re.IGNORECASE))
    ) or \
    bool(re.search(r'\bstatus\b', text, re.IGNORECASE))
  )




if __name__ == '__main__':
  print(isValid("How is eveything going?"))
