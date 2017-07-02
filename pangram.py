import string

"""
Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
"""

def is_pangram(input_string, alphabet=string.ascii_lowercase):
	"""
	This function checks whether the given input string is pangram or not.
	"""
	alphaset = set(alphabet)
	return alphaset <= set(input_string.lower())

print is_pangram('The quick brown fox jumps over the lazy dog')
