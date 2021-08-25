from random import choice
import words
import unidecode

def generate_word():
	category = choice(list(words.dic.keys()))
	return (category, choice(words.dic[category]))

def evaluate(word, hidden, guess):
	word = unidecode.unidecode(word)
	if (guess in word) and (guess not in hidden):
		return True
	return False

def update(word, hidden, guess):
	word = unidecode.unidecode(word)
	word_to_check = word.lower()
	new_hidden = hidden

	if guess == word_to_check:
		new_hidden = word
	else:
		for i in range(len(word_to_check)):
			if guess == word_to_check[i]:
				new_hidden = new_hidden[:i] + word[i] + new_hidden[i+1:]

	return new_hidden

def generate_html(category, hidden):
	html = f"""
	<!DOCTYPE html>
	<html>
		<head>
			<title>Hangman!</title>
		</head>
		<body>
			<h1>Categoria</h1>
			<p>{category}</p>
			<h1>Palavra</h1>
			<p>{hidden}</p>
		</body>
	</html>
	"""
