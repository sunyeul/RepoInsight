import os
from typing import Optional

from dotenv import load_dotenv


def get_openai_api_key() -> str:
    """
    Retrieve the OpenAI API key from environment variables.

    This function loads environment variables from a .env file (if present)
    and retrieves the OpenAI API key. If the API key is not found, it raises
    a ValueError.

    Returns:
        str: The OpenAI API key.

    Raises:
        ValueError: If the OPENAI_API_KEY is not found in the environment variables.

    Example:
        >>> api_key = get_openai_api_key()
        >>> print(api_key)
        'sk-...'
    """
    # Load environment variables from .env file (if it exists)
    load_dotenv()

    # Attempt to retrieve the API key from environment variables
    api_key: Optional[str] = os.getenv("OPENAI_API_KEY")

    # Check if the API key was successfully retrieved
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    return api_key
