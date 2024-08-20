from typing import Any, Dict, List

import openai
from openai import OpenAI

from repoinsight.utils import get_openai_api_key


def generate_readme(conversation_history: List[Dict[str, str]]) -> str:
    """
    Generate a README.md file for a Python project based on previous analysis.

    This function uses OpenAI's GPT model to generate a comprehensive README
    file based on the conversation history of a previous code analysis.

    Args:
        conversation_history: A list of dictionaries representing the conversation
                              history from the previous code analysis.

    Returns:
        A string containing the generated README.md content in Markdown format.
    """
    # Set the OpenAI API key
    openai.api_key = get_openai_api_key()
    client = OpenAI()
    # Define the user message for README generation
    user_message: str = """
    Based on the previous analysis, create a README.md file for this Python project.

    The README should include:
    1. Project Overview
    2. Installation and Setup
    3. Usage Instructions
    4. Project Structure
    5. Key Components
    6. Potential Improvements
    7. Contributing Guidelines
    8. License (Assume MIT License)

    Format the README in Markdown.
    """

    # Add the new user message to the conversation history
    conversation_history.append({"role": "user", "content": user_message})

    # Make the API call to OpenAI
    response: Any = client.chat.completions.create(
        model="gpt-4o-mini", messages=conversation_history
    )

    # Extract and return the generated README content
    return response.choices[0].message.content
