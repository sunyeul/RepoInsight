import tempfile

from git import Repo


def clone_code(repo_url: str) -> str:
    """
    Clone a git repository to a temporary directory.

    This function creates a temporary directory and clones the specified
    git repository into it.

    Args:
        repo_url: A string representing the URL of the git repository to clone.

    Returns:
        A string path to the temporary directory containing the cloned repository.

    Raises:
        git.exc.GitCommandError: If there's an error during the cloning process.
    """
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Clone the repository into the temporary directory
    Repo.clone_from(repo_url, temp_dir)

    # Return the path to the cloned repository
    return temp_dir
