import json

class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize statistics."""
		self.settings = ai_game.settings
		self.reset_stats()
		# Start Alien Invasion in an inactive state.
		self.game_active = False

		# High score should never be reset.
		filename = 'ai_game_high_score.json'
		with open(filename) as f:
			self.high_score = json.load(f)

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

	def save_high_score(self):
		filename = 'ai_game_high_score.json'
		with open(filename, 'w') as f:
			json.dump(self.high_score, f)
