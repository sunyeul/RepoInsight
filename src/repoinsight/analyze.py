from typing import Any, Dict, List

import openai
from openai import OpenAI

from repoinsight.utils import get_openai_api_key


def analyze_code(code_index: List[str], code_text: str) -> List[Dict[str, str]]:
    """
    Analyze Python project code using OpenAI's GPT model.

    This function takes the index and content of Python files in a project,
    sends them to OpenAI's GPT model for analysis, and returns the conversation
    history including the model's response.

    Args:
        code_index: A list of strings representing the file paths in the project.
        code_text: A string containing the concatenated content of all project files.

    Returns:
        A list of dictionaries representing the conversation history, including
        the system message, user message, and assistant's response.
    """
    # Set the OpenAI API key
    openai.api_key = get_openai_api_key()
    client = OpenAI()

    # Define the system message for the AI assistant
    system_message = "You are a helpful assistant that analyzes Python projects."

    # Construct the user message with project details
    user_message = f"""
    Analyze the following Python project:

    File index:
    {code_index}

    Code content:
    {code_text}

    Provide a detailed analysis including:
    1. Overall project structure
    2. Main functionalities
    3. Key components and their interactions
    4. Potential improvements or issues

    Format the analysis as a dictionary with keys: 'structure', 'functionalities', 'components', 'improvements'.
    """

    # Prepare the messages for the API call
    messages: List[Dict[str, str]] = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]

    # Make the API call to OpenAI
    response: Any = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages
    )

    # Extract the assistant's response
    assistant_message: Dict[str, str] = {
        "role": "assistant",
        "content": response.choices[0].message.content,
    }

    # Return the full conversation history
    return messages + [assistant_message]
