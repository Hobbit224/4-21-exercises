####EXERCISE 1####
print('Exercise 1\n')

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print phonebook_dict['Elizabeth']

phonebook_dict.update({'Kareem': '938-489-1234'})

del phonebook_dict['Alice']

phonebook_dict['Bob'] = '968-345-2345'

print "Bob, Elizabeth, and Kareem's numbers are " + phonebook_dict['Bob'] + ", " + phonebook_dict['Elizabeth'] + ", and " + phonebook_dict['Kareem'] + ".\n"


####EXERCISE 2####
print('Exercise 2\n')
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print ramit['email']
print ramit['interests'][0]
print ramit['friends'][0]['email']
print ramit['friends'][1]['interests'][1]
print '\n'

####Letter Summary####
print('Letter Summary\n')


def letter_histogram(word):
	letter_summary = {}
	for characters in word:
		if characters in letter_summary:
			letter_summary[characters] += 1
		else:
			letter_summary[characters] = 1
	print letter_summary


letter_histogram('Antidisestablishmentarianism')
print '\n'


####Word Summary####
print 'Word Summary\n'

def word_histogram(paragraph):
	word_list = paragraph.split(' ')
	word_summary = {}
	for piece in word_list:
		if piece in word_summary:
			word_summary[piece] += 1
		else:
			word_summary[piece] = 1
	print word_summary

word_histogram('to be or not to be')






















	