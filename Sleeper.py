import requests


def request(url):
	response = requests.get(url)
	response.raise_for_status()
	return response.json()


class User:
	def __init__(self, user_identifier):
		self._root_url = "https://api.sleeper.app/v1/user"
		self.user = request(f'{self._root_url}/{user_identifier}')
		self.user_id = self.user["user_id"]
		self.username = self.user["username"]
		self._root_url = f'{self._root_url}/{self.user_id}'

	def get_user(self):
		return self.user

	def get_all_leagues(self, season="2020"):
		return request(f'{self._root_url}/leagues/nfl/{season}')

	def get_all_drafts(self, season="2020"):
		return request(f'{self._root_url}/drafts/nfl/{season}')


class League:
	def __init__(self, league_id):
		self.league_id = league_id
		self._root_url = f'https://api.sleeper.app/v1/league/{self.league_id}'
		self.league = request(self._root_url)

	def get_league(self, refresh=False):
		if refresh:
			self.league = request(self._root_url)
		return self.league

	def get_rosters(self):
		return request(f'{self._root_url}/rosters')

	def get_users(self):
		return request(f'{self._root_url}/users')

	def get_matchups(self, week=1):
		return request(f'{self._root_url}/matchups/{week}')

	def get_winners_bracket(self):
		return request(f'{self._root_url}/winners_bracket')

	def get_losers_bracket(self):
		return request(f'{self._root_url}/losers_bracket')

	def get_transactions(self, week=1):
		return request(f'{self._root_url}/transactions/{week}')

	def get_traded_picks(self):
		return request(f'{self._root_url}/traded_picks')

	def get_drafts(self):
		return request(f'{self._root_url}/drafts')


class Draft:
	def __init__(self, draft_id):
		self.draft_id = draft_id
		self._root_url = f'https://api.sleeper.app/v1/draft/{self.draft_id}'
		self.draft = request(self._root_url)

	def get_draft(self):
		return self.draft

	def get_picks(self):
		return request(f'{self._root_url}/picks')

	def get_traded_picks(self):
		return request(f'{self._root_url}/traded_picks')


class Players:
	def __init__(self):
		self._root_url = 'https://api.sleeper.app/v1/players/nfl'
		self._players = request(self._root_url)

	def get_players(self):
		return self._players

	def get_trending_players(self, type="add", hours=24, limit=25):
		return request(f'{self._root_url}/trending/{type}?lookback_hours={hours}&limit={limit}')

	def get_trending_down_players(self, hours=24, limit=25):
		return self.get_trending_players("drop", hours, limit)
