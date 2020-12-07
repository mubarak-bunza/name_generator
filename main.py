import random

def is_vowel(letters):
  if len(letters) >= 3:
    vowels = 'aioue'
    result = set()
    for i in range(len(letters)):
      result.add(letters[i].lower() in vowels)
    
    if False not in result:
      return True
    else:
      return False
  else:
    print('Parameters can not be less than 3 characters')
  

v = is_vowel('aqioue')
print(v)


def name_generator(vowels, consonant):
  fname = ''
  lname = ''
  if is_vowel(vowels):
    fname = ''.join(random.choice(vowels) for _ in vowels)
  else:
    print('This param accepts vowels only')
    return

  if not is_vowel(consonant):
    lname = ''.join(random.choice(consonant) for _ in consonant)
  else:
    print('This param accepts consonants only')
    return

  fullname = fname +" "+lname
  return {
    'Firstname':fname,
    'Lastname':lname,
    'Fullname':fullname
  }

# for i in range(5):
print(name_generator('ia','cdsdds'))

