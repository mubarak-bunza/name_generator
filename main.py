import random

def is_vowel(letters):
  vowels = 'aioue'
  result = set()
  for i in range(len(letters)):
    result.add(letters[i].lower() in vowels)
  
  if False not in result:
    return True
  else:
    return False
  

# v = is_vowel('qqqq')
# print(v)


def name_generator(vowels, consonant):
  fname = ''
  lname = ''
  try:
    assert len(vowels) >= 3 and len(consonant) >= 3
  except:
    return "Vowels and Consonants can not be less than 3 characters"
  else:
    if is_vowel(vowels):
      fname = ''.join(random.choice(vowels) for _ in vowels)
    else:
      return 'This param accepts vowels only'

    if not is_vowel(consonant):
      lname = ''.join(random.choice(consonant) for _ in consonant)
    else:
      return'This param accepts consonants only'

    fullname = fname +" "+lname
    return {
      'Firstname':fname,
      'Lastname':lname,
      'Fullname':fullname
    }

# for i in range(5):
# print(name_generator('iae','afghj'))

