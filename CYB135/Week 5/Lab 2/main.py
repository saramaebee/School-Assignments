import hashlib

def hash_function(password, salt, al):
  if al == 'md5':
    #md5
    hash = hashlib.md5(salt.encode() + password.encode())
    hash.update(password.encode('utf-8'))
    return hash.hexdigest() + ':' + salt
  elif (al == 'sha1'):
    #sha1  
    hash = hashlib.sha1()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest() + ':' + salt
  elif al == 'sha224':
    #sha224
    hash = hashlib.sha224()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest() + ':' + salt
  elif al == 'sha256':
    #sha256
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest() + ':' + salt
  elif al == 'blake2b':
    #blake2b512
    hash = hashlib.blake2b()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest() + ':' + salt
  else:
    print("Error: No Algorithm!")

if __name__ == "__main__":
  # TODO: create a list called hash_list that contains
  # the five hashing algorithsm as strings
  # md5, sha1, sha224, sha256, blake2b
  hash_list = ['md5', 'sha1', 'sha224', 'sha256', 'blake2b']

  # TODO: accept user input for a password to hash
  u_pass = input()

  # TODO: create a salt variable from 13 digits (4458585599393) and 
  # convert it to hex 
  salt = hex(4458585599393)

  # TODO: use a for loop to iterate through the hash_list.
  # Inside the loop create a new variable returned from a call to the hash_function
  # Display the info as described above.  (new line after last print)
  
  for h in hash_list:
      hashed = hash_function(u_pass, salt, h)
      print(f'Testing hash algorithm:  {h}')
      print(f'Hashed Password =  {hashed}')
      print('')
 
 
