class CipherTest:
  
  def __init__(self, shift=0, direction='r', text = ''):
    self.shift = shift
    self.direction = direction
    self.text = text
    
  #Shift to right function
  def shift_to_right(self):
    encrypted_Text = ""
    for i in range(len(self.text)):
      c = self.text[i]
      #Encrypt upper case 
      if(c == ' '):
        encrypted_Text += ' '
      elif (c.isupper()):
        encrypted_Text += chr((ord(c) + self.shift-65) % 26 + 65)
      #Encrypt lower case
      else:
        encrypted_Text += chr((ord(c) + self.shift-97) % 26 + 97)

    return encrypted_Text
    
  #Shift to left function
  def shift_to_left(self):
    encrypted_Text = ""
    for i in range(len(self.text)):
      c = self.text[i]
      #Encrypt upper case 
      if(c == ' '):
        encrypted_Text += ' '
      elif (c.isupper()):
        encrypted_Text += chr((ord(c) - self.shift-65) % 26 + 65)
      #Encrypt lower case
      else:
        encrypted_Text += chr((ord(c) - self.shift-97) % 26 + 97)

    return encrypted_Text



if __name__ == "__main__":
    text = input()
    shift = int(input())
    direction = input().lower()
    
    # def __init__(self, shift=0, direction='r', text = ''):
    cipher = CipherTest(shift, direction, text)
  
    if cipher.direction == 'r':
        print(cipher.shift_to_right())
    elif cipher.direction == 'l':
        print(cipher.shift_to_left(), end='')
        
   

