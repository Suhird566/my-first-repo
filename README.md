```markdown
# --- route_handler:github_login ---
def github_login():
    github_url = (
        "https://github.com/login/oauth/authorize"
        f"?client_id={GITHUB_CLIENT_ID}"
        f"&redirect_uri=http://localhost:8000/auth/github/callback"
        f"&scope=repo read:user user:email"
    )
    return RedirectResponse(github_url)

# --- route_handler:github_callback ---
def github_callback(code: str):

    # 1️⃣ Exchange code for access token
    token_response = requests.post(
        "https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data={
            "client_id": GITHUB_CLIENT_ID,
            "client_secret": GITHUB_CLIENT_SECRET,
            "code": code
        }
    ).json()

    access_token = token_response.get("access_token")

    if not access_token:
        raise HTTPException(400, "GitHub access token not received")

    # 2️⃣ Fetch GitHub user
    user_response = requests.get(
        "https://api.github.com/user",
        headers={
            "Authorization": f"token {access_token}",  # ✅ FIX
            "User-Agent": "code-review-agent"
        }
    )

    user = user_response.json()

    # 3️⃣ Create JWT
    payload = {
        "github_id": user["id"],
        "username": user["login"],
        "github_access_token": access_token,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_MINUTES)
    }

    jwt_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    # 4️⃣ Redirect to frontend
    return RedirectResponse(
        f"http://localhost:5173/dashboard?token={jwt_token}"
    )

# --- route_handler:get_repositories ---
def get_repositories(user=Depends(verify_jwt)):

    access_token = user.get("github_access_token")

    if not access_token:
        raise HTTPException(401, "GitHub token missing in JWT")

    response = requests.get(
        "https://api.github.com/user/repos",
        headers={
            "Authorization": f"token {access_token}",  # ✅ CRITICAL FIX
            "Accept": "application/vnd.github+json",
            "User-Agent": "code-review-agent"
        },
        params={
            "per_page": 100,
            "sort": "updated"
        },
        timeout=10
    )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code,
            f"GitHub API error: {response.text}"
        )

    repos = response.json()

    return [
        {
            "id": repo["id"],
            "name": repo["name"],
            "full_name": repo["full_name"],
            "private": repo["private"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "language": repo["language"],
            "updated_at": repo["updated_at"]
        }
        for repo in repos
    ]

# --- function:github_login ---
def github_login():
    github_url = (
        "https://github.com/login/oauth/authorize"
        f"?client_id={GITHUB_CLIENT_ID}"
        "&redirect_uri=http://localhost:8000/auth/github/callback"
        "&scope=repo read:user user:email"
    )
    return RedirectResponse(github_url)

# --- function:github_callback ---
def github_callback(code: str):

    # 1️⃣ Exchange code for access token
    token_response = requests.post(
        "https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data={
            "client_id": GITHUB_CLIENT_ID,
            "client_secret": GITHUB_CLIENT_SECRET,
            "code": code
        }
    ).json()

    access_token = token_response.get("access_token")

    if not access_token:
        raise HTTPException(400, "GitHub access token not received")

    # 2️⃣ Fetch GitHub user
    user_response = requests.get(
        "https://api.github.com/user",
        headers={
            "Authorization": f"token {access_token}",  # ✅ FIX
            "User-Agent": "code-review-agent"
        }
    )

    user = user_response.json()

    # 3️⃣ Create JWT
    payload = {
        "github_id": user["id"],
        "username": user["login"],
        "github_access_token": access_token,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_MINUTES)
    }

    jwt_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    # 4️⃣ Redirect to frontend
    return RedirectResponse(
        f"http://localhost:5173/dashboard?token={jwt_token}"
    )

# --- function:get_repositories ---
def get_repositories(user=Depends(verify_jwt)):

    access_token = user.get("github_access_token")

    if not access_token:
        raise HTTPException(401, "GitHub token missing in JWT")

    response = requests.get(
        "https://api.github.com/user/repos",
        headers={
            "Authorization": f"token {access_token}",  # ✅ CRITICAL FIX
            "Accept": "application/vnd.github+json",
            "User-Agent": "code-review-agent"
        },
        params={
            "per_page": 100,
            "sort": "updated"
        },
        timeout=10
    )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code,
            f"GitHub API error: {response.text}"
        )

    repos = response.json()

    return [
        {
            "id": repo["id"],
            "name": repo["name"],
            "full_name": repo["full_name"],
            "private": repo["private"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "language": repo["language"],
            "updated_at": repo["updated_at"]
        }
        for repo in repos
    ]

# --- function:github_login ---
def github_login():
    github_url = (
        "https://github.com/login/oauth/authorize"
        f"?client_id={GITHUB_CLIENT_ID}"
        f"&redirect_uri=http://localhost:8000/auth/github/callback"
        f"&scope=repo read:user user:email"
    )
    return RedirectResponse(github_url)

# --- function:github_callback ---
def github_callback(code: str):

    # 1️⃣ Exchange code for access token
    token_response = requests.post(
        "https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data={
            "client_id": GITHUB_CLIENT_ID,
            "client_secret": GITHUB_CLIENT_SECRET,
            "code": code
        }
    ).json()

    access_token = token_response.get("access_token")

    if not access_token:
        raise HTTPException(400, "GitHub access token not received")

    # 2️⃣ Fetch GitHub user
    user_response = requests.get(
        "https://api.github.com/user",
        headers={
            "Authorization": f"token {access_token}",  # ✅ CRITICAL FIX
            "User-Agent": "code-review-agent"
        }
    )

    user = user_response.json()

    # 3️⃣ Create JWT
    payload = {
        "github_id": user["id"],
        "username": user["login"],
        "github_access_token": access_token,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_MINUTES)
    }

    jwt_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    # 4️⃣ Redirect to frontend
    return RedirectResponse(f"http://localhost:5173/dashboard?token={jwt_token}")

# --- function:get_repositories ---
def get_repositories(user=Depends(verify_jwt)):

    access_token = user.get("github_access_token")

    if not access_token:
        raise HTTPException(401, "GitHub token missing in JWT")

    response = requests.get(
        "https://api.github.com/user/repos",
        headers={
            "Authorization": f"token {access_token}",  # ✅ CRITICAL FIX
            "Accept": "application/vnd.github+json",
            "User-Agent": "code-review-agent"
        },
        params={
            "per_page": 100,
            "sort": "updated"
        },
        timeout=10
    )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code,
            f"GitHub API error: {response.text}"
        )

    repos = response.json()

    return [
        {
            "id": repo["id"],
            "name": repo["name"],
            "full_name": repo["full_name"],
            "private": repo["private"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "language": repo["language"],
            "updated_at": repo["updated_at"]
        }
        for repo in repos
    ]

```