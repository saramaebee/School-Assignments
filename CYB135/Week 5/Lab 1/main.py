#Caesar Cipher Encryption function
def caesar_cipher_encrypt(text, key, a):
  text = text.upper()
  encrypted_Text = ""
  for i in text:
    if i in a:
      index = (a.find(i) + key) % len(a)
      encrypted_Text = encrypted_Text + a[index]
    else:
      encrypted_Text = encrypted_Text + i
  return encrypted_Text

#Caesar Cipher Decrypt function
def caesar_cipher_decrypt(text, key, a):
    text = text.upper()
    decrypted_Text = ""
    for i in text:
        if i in a: 
            index = (a.find(i) - key) % len(a)
            decrypted_Text = decrypted_Text + a[index]
        else:
            decrypted_Text = decrypted_Text + i
    return decrypted_Text

# TODO Create a function called caesar_hack( text, a, check ) that takes a Caesar Cipher encrypted message, an alphabet list, and the original message in main.
# This function will attempt to hack an encrypted message.  Use a nested for loop to find the key between 0 & 25.
# Check where the letter is found in the alphabet list based on the encrypted text letter sent to this function.
# Check if the decrypted message is the same as the original message.
# If a key is found , return the key value and the decrypted message.
# If not found return 99 as the key and "Error: Key not found!" as the message. 

def caesar_hack(text, a, check):
  solved = False
  for i in range(len(a)):
      d = caesar_cipher_decrypt(text, i, a)
      if d == check.upper():
          return i, d
          solved = True
  if not solved:
      return 99, 'Error: Key not found!'
   

if __name__ == "__main__":
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  text = "This is a secret message"
  shift = int(input()) #Number between 1 & 25  
  encrypted_data =  caesar_cipher_encrypt(text, shift, alphabet)
  print('Brute Force Hack Attempt: ')
  print ('Encrypted Message: ', encrypted_data)
  
  # TODO: Add a call to caesar_hack (encrypted_data, alphabet, text) return it to two variables k (key) & h (hacked message)
  k, h = caesar_hack(encrypted_data, alphabet, text)
  # TODO: If k == 99 print the returned message
  # Else - print 'Successful Attempt found! Key =' k variable
  # Add a print 'Secret message:' h variable 
  if k == 99:
      print(h)
  else:
      print(f'Successful Attempt found! Key = {k}')
      print(f'Secret message: {h}')
