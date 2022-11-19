from requests import get

class BrBaQuotes:
	def __init__(self) -> None:
		self.api = "https://api.breakingbadquotes.xyz"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_random_quote(self) -> dict:
		return get(
			f"{self.api}/v1/quotes"
			headers=self.headers).json()

	def get_multiple_quotes(self, count: int) -> dict:
		return get(
			f"{self.api}/v1/quotes/{count}"
			headers=self.headers).json()	
