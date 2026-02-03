```markdown
# Project Overview

This repository contains a basic implementation of a GitHub API integration for a code review agent. It focuses on a simplified authentication flow and a core functionality to retrieve repositories.

## Features

*   **GitHub Login:** Handles authentication with GitHub using the provided `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET`, and `GITHUB_ACCESS_TOKEN`.
*   **GitHub User Retrieval:** Fetches user details from the GitHub API.
*   **Repository Retrieval:**  Retrieves a list of repositories.
*   **JWT (JSON Web Token) Management:**  Uses JWT for secure token management.
*   **Basic Error Handling:** Includes robust error handling for API requests.

## Tech Stack

*   **Python:** The primary programming language.
*   **requests:** For making HTTP requests to the GitHub API.
*   **UUID:** For generating unique identifiers.
*   **datetime:** For timestamp handling.
*   **JWT (JSON Web Token):** For authentication and authorization.
*   **`requests`:** For fetching the Github user.

## Setup

1.  **Clone the Repository:**
    ```bash
    git clone <your_repo_here>
    cd <your_repo_here>
    ```
2.  **Install Dependencies:**
    ```bash
    pip install requests
    ```
3.  **Configure `.env` File (see code):**  Edit the `.env` file to store sensitive information like `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET`, and `GITHUB_ACCESS_TOKEN`.  **DO NOT commit this file to your repository.**
4.  **Set `JWT_SECRET`:**  Modify the `JWT_SECRET` variable in the `.env` file to a strong, randomly generated secret.
5.  **Set `JWT_EXPIRE_MINUTES`:** Configure `JWT_EXPIRE_MINUTES` to control the expiry time of the JWT.

## Usage

1.  **Run the Script:** Execute the script with the necessary arguments.
    ```bash
    python your_script.py
    ```
2.  **Verify Authentication:**  The script will return a redirect to the GitHub login page.
3.  **Retrieve Repositories:**
    ```bash
    python your_script.py --get_repositories
    ```
4.  **Access User Details:**
    ```bash
    python your_script.py --get_repositories --user <your_github_username>
    ```
    (Replace `<your_github_username>` with your GitHub username.)

**Important Note:** The script uses the GitHub API v3.  Verify the latest documentation for this API.  The URL and parameters may need to be updated.
```