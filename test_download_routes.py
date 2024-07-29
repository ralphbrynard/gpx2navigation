import os
import unittest
from unittest.mock import patch

# Import the script to test
import download_routes

class TestDownloadRoutes(unittest.TestCase):
    @patch('download_routes.get_access_token')
    @patch('download_routes.fetch_routes')
    @patch('download_routes.download_gpx')
    @patch('download_routes.save_gpx_file')
    @patch('download_routes.load_cache')
    @patch('download_routes.save_cache')
    def test_main(self, mock_save_cache, mock_load_cache, mock_save_gpx_file, mock_download_gpx, mock_fetch_routes, mock_get_access_token):
        # Mock the return values for each function
        mock_get_access_token.return_value = 'mock_access_token'
        mock_fetch_routes.return_value = [{'id': 123, 'name': 'Test Route', 'distance': 10}]
        mock_download_gpx.return_value = b'mock gpx content'
        mock_save_gpx_file.return_value = '/mock/path/Test Route.gpx'
        mock_load_cache.return_value = []

        # Run the main function
        download_routes.main()

        # Check that each function was called with expected arguments
        mock_get_access_token.assert_called_once()
        mock_fetch_routes.assert_called_once_with('mock_access_token')
        mock_download_gpx.assert_called_once_with(123, 'mock_access_token')
        mock_save_gpx_file.assert_called_once_with({'id': 123, 'name': 'Test Route', 'distance': 10}, b'mock gpx content')
        mock_load_cache.assert_called_once()
        mock_save_cache.assert_called_once_with([{'id': 123, 'name': 'Test Route', 'distance': 10, 'number_of_rides': 0}])

if __name__ == '__main__':
    # Set environment variables for the test
    os.environ['clientID'] = 'mock_client_id'
    os.environ['clientSecret'] = 'mock_client_secret'
    os.environ['refreshToken'] = 'mock_refresh_token'
    
    unittest.main()
