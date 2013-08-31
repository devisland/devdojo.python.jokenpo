import unittest

def enum(**enums):
    return type('Enum', (), enums)

Jokenpo = enum(ROCK=3, PAPER=1, SCISSORS=2)

def judge(play1, play2):
	if play1 == play2:
		return 'draw'

	PAPER_WINS_ROCK = not (play1 + play2) % 2

	return Jokenpo.PAPER if PAPER_WINS_ROCK else max(play1, play2)

class JokenpoTests(unittest.TestCase):
	
	def test_Player1_is_Rock_and_Player2_is_Rock_Must_be_Draw(self):
		self.assertEqual(judge(Jokenpo.ROCK, Jokenpo.ROCK), "draw")

	def test_Player1_is_Paper_and_Player2_is_Paper_Must_be_Draw(self):
		self.assertEqual(judge(Jokenpo.PAPER, Jokenpo.PAPER), "draw")

	def test_Player1_is_Scissors_and_Player2_is_Scissors_Must_be_Draw(self):
		self.assertEqual(judge(Jokenpo.SCISSORS, Jokenpo.SCISSORS), "draw")

	def test_Player1_is_Rock_and_Player2_is_Scissors_Must_be_Rock(self):
		self.assertEqual(judge(Jokenpo.ROCK, Jokenpo.SCISSORS), Jokenpo.ROCK)

	def test_Player1_is_Scissors_and_Player2_is_Paper_Must_be_Scissors(self):
		self.assertEqual(judge(Jokenpo.SCISSORS, Jokenpo.PAPER), Jokenpo.SCISSORS)

	def test_Player1_is_Paper_and_Player2_is_Rock_Must_be_Paper(self):
		self.assertEqual(judge(Jokenpo.PAPER, Jokenpo.ROCK), Jokenpo.PAPER)

	def test_Player2_is_Rock_and_Player1_is_Scissors_Must_be_Rock(self):
		self.assertEqual(judge(Jokenpo.SCISSORS, Jokenpo.ROCK), Jokenpo.ROCK)

	def test_Player2_is_Scissors_and_Player1_is_Paper_Must_be_Scissors(self):
		self.assertEqual(judge(Jokenpo.PAPER, Jokenpo.SCISSORS), Jokenpo.SCISSORS)

	def test_Player2_is_Paper_and_Player1_is_Rock_Must_be_Paper(self):
		self.assertEqual(judge(Jokenpo.ROCK, Jokenpo.PAPER), Jokenpo.PAPER)


if __name__ == '__main__':
	unittest.main()