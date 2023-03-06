
#############################################################################################################################
#   filename:pySoundLike.py                                                       
#   created: 2023-03-06                                                              
#   import your librarys below                                                    
#############################################################################################################################

import pronouncing
import random

def rhyme(word):

    phonetic_sounds = pronouncing.phones_for_word(word)
    rhymes = pronouncing.rhymes(word)

    if len(rhymes) > 0:
        rhyme_suggestion = rhymes[random.randint(0, len(rhymes) - 1)]
        return f"A rhyme for {word} is {rhyme_suggestion}"
    else:
        return f"No rhymes found for{word}"


    