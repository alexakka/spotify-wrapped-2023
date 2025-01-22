import base64
import json
import requests


class SpotifyClient():
    """A client for interacting with the Spotify Web API."""

    urls = {
            "get_track": "https://api.spotify.com/v1/tracks/",
            "get_artist": "https://api.spotify.com/v1/artists/"
    }

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the SpotifyClient instance with client credentials."""

        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self._get_access_token()

    def _get_access_token(self) -> str:
        """The access token to be used in subsequent API requests."""

        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": f"Basic {auth_base64}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}

        result = requests.post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result["access_token"]

        return token

    def _get_auth_header(self) -> dict[str, str]:
        """Generate the authorization header for API requests."""

        return {"Authorization": f"Bearer {self.token}"}

    def get_track(self, track_id: str):
        """Retrieve information about a specific track."""

        url = f"{self.urls["get_track"]}{track_id}"

        headers = self._get_auth_header()

        result = requests.get(url, headers=headers)

        json_result = json.loads(result.content)
        return json_result

    def get_artist(self, artist_id):
        """Retrieve information about a specific artist."""

        url = f"{self.urls["get_artist"]}{artist_id}"

        headers = self._get_auth_header()

        result = requests.get(url, headers=headers)

        json_result = json.loads(result.content)
        return json_result
