print 'Welcome to the Pig Latin Translator!'
print
# Start coding here!
print '=====some rules================'
print "Word doesn't containt a numbers"
print '==============================='
print
original = raw_input("Enter a word: ")
if len(original) > 0 and original.isalpha() is True:
   pyg = 'ay'
   word = original.lower()
   first = word[0]
   new_word = word + first + pyg
   new_word = new_word[1:len(new_word)];
   print 
   print 'you word is: ', new_word;
else:
   print 'you entered empty word or word with a number';