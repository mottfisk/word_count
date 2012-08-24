# Word Count
# Program will count the number of words and the number of occurences for each word.
# Author:  Mott Fisk

def count_words(text):
    return len(text.split())
        
    
if __name__ == '__main__':
    print count_words('i went to the store')

