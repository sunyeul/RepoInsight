import fnmatch
import os
from typing import List, Tuple


def should_ignore(path: str, ignore_patterns: List[str]) -> bool:
    """
    Check if the given path should be ignored based on the ignore patterns.

    Args:
        path: A string representing the path to check.
        ignore_patterns: A list of string patterns to match against.

    Returns:
        A boolean indicating whether the path should be ignored (True) or not (False).
    """
    return any(fnmatch.fnmatch(path, pattern) for pattern in ignore_patterns)


def extract_code(repo_dir: str, ignore_patterns: List[str]) -> Tuple[List[str], str]:
    """
    Extract Python code files from a repository directory.

    This function walks through the repository directory, ignoring specified patterns,
    and extracts the content of Python files.

    Args:
        repo_dir: A string path to the repository directory.
        ignore_patterns: A list of string patterns for files/directories to ignore.

    Returns:
        A tuple containing:
        - A list of strings representing relative paths to the extracted Python files.
        - A string containing the concatenated content of all extracted Python files.

    Raises:
        UnicodeDecodeError: If a file cannot be decoded as UTF-8.
        Exception: For any other error occurring during file reading.
    """
    code_index: List[str] = []
    code_text: str = ""

    for root, dirs, files in os.walk(repo_dir):
        # Filter out ignored directories
        dirs[:] = [
            d
            for d in dirs
            if not should_ignore(
                os.path.relpath(os.path.join(root, d), repo_dir), ignore_patterns
            )
        ]

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, repo_dir)

                if should_ignore(relative_path, ignore_patterns):
                    continue

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        if content.strip():  # Only add non-empty files
                            code_index.append(relative_path)
                            # Add file separator and content to code_text
                            code_text += f"---- File: {relative_path} ----\n"
                            code_text += content
                except UnicodeDecodeError:
                    # Log error for files that can't be decoded as UTF-8
                    print(
                        f"Error: Unable to decode {relative_path} as UTF-8. Skipping."
                    )
                except Exception as e:
                    # Log any other errors encountered during file reading
                    print(f"Error reading file {relative_path}: {str(e)}")

    return code_index, code_text
