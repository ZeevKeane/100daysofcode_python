# Write your code below: 
from contextlib import contextmanager

@contextmanager
def generic(card_type, sender, recipient):
  generic_card = open(card_type, "r")
  # *CM27052022
  ordered_card = open(f"{sender}_generic.txt", "w")
  try:
    ordered_card.write(f"Dear {recipient}")
    ordered_card.write(generic_card.read())
    ordered_card.write(f"\nSincerely {sender}")
    yield ordered_card
  finally:
    generic_card.close()
    ordered_card.close()


# with generic("thankyou_card.txt", "Mwenda", "Amanda"):
#   print("Card Generated!")

# with open("Mwenda_generic.txt", "r") as card:
#   print(card.read())
    


# class based personalized card making machine!:
class Personalized:
  def __init__(self, sender, recipient):
    self.sender = sender
    self.recipient = recipient
    # this is something new, but i applied what i learned above *CM27052022
    self.card = open(f"{sender}_personalized.txt", "w")

  def __enter__(self):
    self.card.write(f"Dear {self.recipient}\n")
    return self.card

  def __exit__(self, *exc):
    self.card.write(f"Sincerely, {self.sender}")
    self.card.close()


with Personalized("John", "Michael") as p_card:
 p_card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")





