import numpy as np
from fiel1 import build_scoring_matrix, compute_alignment_matrix, compute_global_alignment

def get_edit_distance(seq_x, seq_y, scoring_matrix):
    '''
    compute the seq_x and seq_y global alignment with scoring matrix
    return the edit distance can be expressed in term of:
    |x| + |y| - score(x, y)
    '''
    alignment_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, True)
    score, align_x, align_y = compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    return len(seq_x) + len(seq_y) - score
    
def edit_distance_simple_test(diag_score, off_diag_score, dash_score):
    '''
    Insert: Repalce the string x + y by the string x + a + y
    Delete: Replace the string x + a + y by the string x + y
    Substitute: Replace the string x + a + y by the string x + b + y
    To find the optimal argument of scoring_matrix
    '''
    scoring_matrix = scoring_matrix = build_scoring_matrix({'x', 'a', 'y', 'b'}, diag_score, off_diag_score, dash_score)
    insert_score = get_edit_distance('xay', 'xaay', scoring_matrix)
    delete_score = get_edit_distance('xaay', 'xby', scoring_matrix)
    substitute_score = get_edit_distance('xaaay', 'xby', scoring_matrix)
    return insert_score, delete_score, substitute_score
    
def find_argument():
    '''
    To find the optimal argument of scoring_matrix
    the optimal argument found as:
    diag_score = 2 
    off_diag_score = 1 
    dash_score = 0
    '''
    optimal_result = np.array([1, 2, 3])
    for diag_score in range(10):
        for off_diag_score in range(-10, 5):
            for dash_score in range(-10, 5):
                result = np.array(edit_distance_simple_test(diag_score, off_diag_score, dash_score))
                diff = tuple(result - optimal_result)
                if diff == (0, 0, 0):
                    print("found the optimal argument. \ndiag_score: %s\noff_diag_score: %s\ndash_score: %s"\
                        %(diag_score, off_diag_score, dash_score))    
    return
    
def read_words(filename):
    '''
    read words from file named filename
    return list of words
    '''
    word_file = open(filename, 'r')
    words = word_file.read()
    word_file.close()
    words = words.split('\n')
    
    print("loaded a dictionary with %s words" %len(words))
    return words

def check_spelling(checked_word, dist, words):
    '''
    words is the list of correct spell word, dist is the edit distance
    Return the set of words that are with in dist of the string checked_word
    '''
    alphabet = set('qwertyuiopasdfghjklzxcvbnm')
    scoring_matrix = scoring_matrix = build_scoring_matrix(alphabet=alphabet, diag_score=2, off_diag_score=1, dash_score=0)
    
    answer = set([])
    for word in words:
        edit_distance = get_edit_distance(checked_word, word, scoring_matrix)
        if edit_distance <= dist:
            answer.add(word)
    return answer

if __name__ == '__main__':
    #find_argument()
    
    words = read_words('words.txt')
    humble_1 = check_spelling('humble', 1, words)
    firefly_2 = check_spelling('firefly', 2, words)
    print("words within an edit distance of one from the string 'humble' is: %s\nwords within an edit distance of two from the string 'firefly' is: %s"\
        %(humble_1, firefly_2))
    print humble_1
    print firefly_2
