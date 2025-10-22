# COmanage Terms and Conditions Demo

A lightweight Flask web application that authenticates users via OpenID Connect (OIDC) and displays decoded ID token claims in a formatted web interface.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Skiddler233/COmanage-Terms-and-Conditions.git
cd COmanage-Terms-and-Conditions
````

### 2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux
# or
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env file
```bash
APP_SESSION_SECRET=Random String

CLIENT_ID=Supplied by OIDC Client
CLIENT_SECRET=Supplied when creating OIDC client
REDIRECT_URI=Set when creating OIDC client

TOKEN_ENDPOINT=
DISCOVERY_URL=

```
APP_SESSION_SECRET: A random string used by Flask for session encryption.

CLIENT_ID / CLIENT_SECRET: Provided when registering your application with your OIDC provider.

REDIRECT_URI: Must match the redirect URI registered with your OIDC client.

TOKEN_ENDPOINT / DISCOVERY_URL: Found in your OIDC provider’s metadata (e.g., /.well-known/openid-configuration).

