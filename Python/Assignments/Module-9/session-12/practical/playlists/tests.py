from django.test import TestCase

# Create your tests here.

class PlaylistsViewTests(TestCase):
    def test_music_home_view(self):
        """
        Tests that visiting the '/music/' URL yields a 200 status code
        and returns the correct welcome message string.
        """
        # Make a GET request to the path
        response = self.client.get('/music/')
        
        # Check that the response status is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check that the response contains the expected string
        self.assertContains(response, "Welcome to My Spotify Playlists! - Mithlesh")
