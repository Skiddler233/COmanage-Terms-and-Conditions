# COmanage Terms and Conditions Demo

A lightweight Flask web application that authenticates users via OpenID Connect (OIDC) and displays decoded ID token claims in a formatted web interface.

---

### 1. Clone the repository
```bash
git clone https://github.com/Skiddler233/COmanage-Terms-and-Conditions.git
cd COmanage-Terms-and-Conditions
````

### 2. Install Dependencies  
    pip install -r requirements.txt

### 3. Create `.env` File  
In the root directory, create a `.env` file with the following configuration:

#### Local Session Token  
    APP_SESSION_SECRET=<any random secret, only stored here>

### API User Creation
Create a API user and CORE API in the registry.\
Setup instructions please see "https://spaces.at.internet2.edu/spaces/COmanage/pages/25860703/CoPerson+API"\
Add the details to the `.env`. Example below. 

#### OIDC Client Configuration  
You can store multiple client configurations in the `.env` file.  
Comment out any unused configuration and ensure only **one** is active.  

Example:  
```
# OIDC Client CONFIG (Template)
# CLIENT_ID=<Provided by the OIDC Client upon creation>
# CLIENT_SECRET=<Provided by the OIDC Client upon creation>
# REDIRECT_URI=<Callback URL configured in the OIDC client>
# TOKEN_ENDPOINT=https://<your client URL>/oauth2/token
# DISCOVERY_URL=https://<your client URL>/.well-known/openid-configuration

# Active OIDC Client CONFIG
CLIENT_ID=<Provided by the OIDC Client upon creation>
CLIENT_SECRET=<Provided by the OIDC Client upon creation>
REDIRECT_URI=<Callback URL configured in the OIDC client>
TOKEN_ENDPOINT=https://<your client URL>/oauth2/token
DISCOVERY_URL=https://<your client URL>/.well-known/openid-configuration

# API User config
URL_BASE="https://<your client url>/registry"
API_USER="<your API user username>"
API_KEY="<your API user key>"
TERMS_URL="https://<you client url>/registry/CoTermsAndConditions/display/<your terms version number e.g. 5>"

```

#### Standard App Configuration  
```
FLASK_APP=oidc_reflector
FLASK_RUN_PORT=5000
FLASK_RUN_HOST=0.0.0.0
```

### 4. Run the Application  
    python main.py

### 5. Access the App  
Open your browser and navigate to:  

    http://localhost:5000

### 6. Authenticate  
- Follow the login steps.  
- Authenticate with your OIDC provider.  
- If you have NOT accepted the Terms and Conditions in the registry, the terms will be displayed.
- Accepting the Terms will make an API call to update the registry.
- The token details will be reflected back in the app.  

---

## Notes  
- Keep your `.env` file secure.  
- Never commit secrets (Client IDs, Secrets, Tokens) to version control.