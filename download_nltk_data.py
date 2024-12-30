import nltk
import os

# Set the path for NLTK data (use /tmp for temporary files in Heroku)
nltk_data_dir = '/tmp/nltk_data'

# Append the directory path for NLTK data
nltk.data.path.append(nltk_data_dir)

# Check if 'punkt' is available, if not, download it
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=nltk_data_dir)

