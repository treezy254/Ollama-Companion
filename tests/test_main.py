import unittest
from unittest.mock import patch
from src.main import main

class TestMain(unittest.TestCase):
    @patch('src.main.install_dependencies')
    @patch('src.main.install_ollama')
    @patch('src.main.run_ollama')
    @patch('src.main.install_model')
    @patch('src.main.start_litellm_proxy')
    @patch('src.main.run_flask_app')
    def test_main(self, mock_run_flask_app, mock_start_litellm_proxy, mock_install_model, 
                  mock_run_ollama, mock_install_ollama, mock_install_dependencies):
        main()
        mock_install_dependencies.assert_called_once()
        mock_install_ollama.assert_called_once()
        mock_run_ollama.assert_called_once()
        mock_install_model.assert_called_once()
        mock_start_litellm_proxy.assert_called_once()
        mock_run_flask_app.assert_called_once()

if __name__ == '__main__':
    unittest.main()