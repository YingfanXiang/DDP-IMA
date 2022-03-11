#!/usr/bin/env python
# coding: utf-8

# In[5]:


def case_count(str1):
    case = {'Uppercase':0, 'Lowercase':0}
    for letter in str1:
        if letter.isupper():
            case['Uppercase'] += 1
        if letter.islower():
            case['Lowercase'] += 1
    print('Uppercase:', case['Uppercase'],',','Lowercase:', case['Lowercase'])
case_count("Hello World")


# In[ ]:





# In[3]:


def morse_code(text):
    code =  { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':' '}
    morse_code = " "
    
    for x in text:
        morse_code = morse_code + code[x.upper()]
    return morse_code
text = input("Enter text to convert to Morse Code: ")
print(morse_code(text))


# In[ ]:





# In[ ]:





# In[ ]:




