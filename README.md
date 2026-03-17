# my-first-repo
A backend service handling GitHub authentication and managing core application data for code review and documentation processes.

---

## Codebase Tour (Start Here)

1.  **`auth.py`**
    This file teaches you how users authenticate with GitHub and how the application fetches data from the GitHub API.
2.  **`models.py`**
    This file teaches you the core data structures and database schema used across the application.

## Architecture & Data Flow

This repository contains core logic for handling user authentication via GitHub OAuth and defining the data models for the application's domain. The `auth.py` file manages the OAuth flow, exchanging authorization codes for access tokens, fetching user details from GitHub, and issuing internal JWTs. It also provides functionality to retrieve a user's GitHub repositories. The `models.py` file defines the database schema for entities such as organizations, users, repositories, and various operational runs like documentation and code reviews.

`github_login()` in `auth.py` → `github_callback()` in `auth.py` (GitHub OAuth, JWT creation) → `get_repositories()` in `auth.py` (fetches GitHub data) → `models.py` (defines data structures for persistence)

## Key Entry Points

*   **`auth.github_login()` in `auth.py`**: Initiates the GitHub OAuth login flow by redirecting the user to GitHub's authorization page.
*   **`auth.github_callback()` in `auth.py`**: Handles the callback from GitHub after authorization, exchanging the code for an access token, fetching user details, and issuing a JWT.
*   **`auth.get_repositories()` in `auth.py`**: Fetches a list of repositories for the authenticated user from the GitHub API.

## Folder / File Walkthrough

### `auth.py`
**Owns:** This file is responsible for handling GitHub OAuth authentication, user data retrieval from GitHub, and the creation of internal JSON Web Tokens (JWTs).
**Key symbols:** `github_login`, `github_callback`, `get_repositories`
**Gotcha:** The `github_callback` function performs a multi-step process involving external API calls to GitHub for token exchange and user data, followed by internal JWT creation and a frontend redirect. The `get_repositories` function relies on a `verify_jwt` dependency to ensure the user is authenticated and their GitHub access token is available.

### `models.py`
**Owns:** This file defines the SQLAlchemy ORM models representing the application's database schema, including entities like organizations, users, repositories, and various operational runs (documentation, code review) and their findings.
**Key symbols:** `Organization`, `User`, `Repository`, `DocumentationRun`, `PullRequest`, `CodeReviewRun`, `ReviewFinding`
**Gotcha:** All models inherit from a `Base` class (not provided in evidence, but implied by usage) and define `__tablename__` and `Column` definitions, including `UUID` primary keys and `ForeignKey` relationships. Understanding these relationships is key to navigating the data model.

## How to Extend This Codebase

**Adding new endpoints / modules / agents / services**
*   **New authentication endpoints**: To add a new authentication flow or endpoint, you would typically create a new function in `auth.py` (or a similar module) that follows the pattern of `github_login` for initiating external redirects and `github_callback` for handling the response, token exchange, and JWT creation.
*   **New data models**: To introduce new entities or modify existing ones, define new classes in `models.py` that inherit from `Base` (implied). Ensure you specify a `__tablename__`, define `Column` types for all attributes, and correctly establish `ForeignKey` relationships to other models as needed.

**Common pitfalls**
*   In `auth.py`, when making requests to the GitHub API (e.g., in `github_callback` and `get_repositories`), it's critical to include the `User-Agent` header. Forgetting this can lead to API request failures or rate limiting.
*   When defining new models in `models.py`, ensure that `ForeignKey` relationships correctly reference the `__tablename__` and `id` column of the parent table (e.g., `organizations.id` for `organization_id`). Incorrect references will cause database schema issues.
*   Handling sensitive information like `GITHUB_CLIENT_SECRET` and `JWT_SECRET` in `auth.py` requires careful attention to security best practices, such as using environment variables and avoiding hardcoding.

**PR checklist**
> ⚠️ Not confirmed — check [specific path or symbol name].
*   > ⚠️ Not confirmed — verify that new database models in `models.py` have corresponding migrations generated.
*   > ⚠️ Not confirmed — ensure all new API calls in `auth.py` include appropriate error handling and logging.
*   > ⚠️ Not confirmed — confirm that all environment variables used are documented and configured for deployment.
*   > ⚠️ Not confirmed — verify that any changes to authentication flows are tested for security vulnerabilities.

## Project Overview

`my-first-repo` serves as a foundational backend component, primarily focused on integrating with GitHub for user authentication and managing the application's core data. It enables users to log in via GitHub OAuth, retrieves their repository information, and maintains a structured database of organizations, users, repositories, and various operational records related to documentation generation and code review processes. This repository likely underpins a larger application that leverages these capabilities for automated code analysis or documentation.

## Features

*   **GitHub OAuth Authentication**: Allows users to log in using their GitHub accounts, obtaining necessary access tokens.
*   **GitHub User & Repository Data Fetching**: Retrieves authenticated user profiles and lists of their repositories from the GitHub API.
*   **Internal JWT Generation**: Creates secure JSON Web Tokens for authenticated users to manage session state.
*   **Core Data Modeling**: Defines database schemas for:
    *   Organizations and Users.
    *   Repositories connected to the platform.
    *   `DocumentationRun` records, tracking documentation generation processes.
    *   `PullRequest` entities, representing GitHub pull requests.
    *   `CodeReviewRun` records, tracking automated code review processes.
    *   `ReviewFinding` entities, detailing specific issues found during code reviews.

## Tech Stack

*   **Python**: The primary programming language.
*   **requests**: Used for making HTTP requests to external APIs, specifically GitHub (seen in `auth.py`).
*   **uuid**: Used for generating UUIDs, particularly for primary keys in database models (seen in `models.py`).
*   **SQLAlchemy (implied)**: Used for Object-Relational Mapping (ORM) to interact with a database, as evidenced by `Base` inheritance, `Column` definitions, `__tablename__`, and `ForeignKey` in `models.py`.
*   **PyJWT (implied)**: Used for encoding JSON Web Tokens (seen in `jwt.encode` in `auth.py`).
*   **Web Framework (implied)**: A web framework is used for handling HTTP requests and responses, evidenced by `RedirectResponse`, `HTTPException`, and `Depends` in `auth.py`.

## Setup

> ⚠️ Not confirmed — verify before running.
No explicit setup commands (e.g., `pip install`, `docker-compose`) were found in the evidence.

**Environment Variables:**
*   `GITHUB_CLIENT_ID`: Used in `auth.py` for initiating GitHub OAuth. If missing, GitHub login will fail.
*   `GITHUB_CLIENT_SECRET`: Used in `auth.py` to exchange the authorization code for an access token. If missing, GitHub login will fail.
*   `JWT_SECRET`: Used in `auth.py` for signing internal JWTs. If missing, JWT creation will fail, preventing user sessions.
*   `JWT_ALGORITHM`: Used in `auth.py` to specify the algorithm for JWT signing. If missing, JWT creation will fail.
*   `JWT_EXPIRE_MINUTES`: Used in `auth.py` to set the expiration time for JWTs. If missing, JWT expiration will be undefined or default.

No explicit configuration files were found in the evidence.

## Usage

> ⚠️ Not confirmed — verify before running.
No explicit usage commands were found in the evidence.

The primary usage flow involves:
1.  A user initiating the GitHub login process, which is handled by `github_login()` in `auth.py`.
2.  Upon successful GitHub authorization, `github_callback()` in `auth.py` processes the response, authenticates the user, and issues an internal JWT.
3.  Authenticated users can then use their JWT to call endpoints like `get_repositories()` in `auth.py` to fetch their GitHub repository data.
4.  The application's data, as defined in `models.py`, would be persisted to a database, allowing for tracking of organizations, users, repositories, and various operational runs (documentation, code reviews) and their findings.