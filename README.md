# Quickstart: Protect FastAPI web API with the Microsoft identity platform

In this quickstart, you download a Python FastAPI web API code sample, and review the way it restricts resource access to authorized accounts only. The sample supports authorization of personal Microsoft accounts and accounts in any Azure Active Directory (Azure AD) organization.

## Prerequisites

- Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/en-us/free/?WT.mc_id=A261C142F).
- [Azure Active Directory tenant](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-create-new-tenant)
- Python 3.8 or higher
- [Visual Studio Code](https://code.visualstudio.com/) (or equivalent)

## Step 1: Clone or download the sample

Clone the sample from your shell or command line:

```cmd
git clone https://github.com/TessFerrandez/fastapi_with_aad_auth.git
```

## Step 2: Register the web API Azure AD Applications

Register your web API in **App Registrations** in the Azure portal.

1. Sign in to the Azure Portal
1. If you have access to multiple tenants, use the **Directory + subscription** filter in the top menu to select the tenant in which you want to register an application.
1. Find and select **Azure Active Directory**.
1. Under **Manage**, select **App registrations > New registation**.
1. Enter a **Name** for your application, for example `TODO-API`. Users of your app might see this name and you can change it later.
1. For **Supported account types**, select **Accounts in any organizational directory**.
1. Select **Register** to create the application.
1. On the **Overview** page, look for the **Application (client) ID** value, and then record it for later use. You'll need it to configure the API (that is, `API_CLIENT_ID` in the *.env* file).
1. Under **Manage**, select **Expose an API > Add a scope**. Accept the proposed Application ID URI (api://{clientId}) by selecting **Save and continue**, and then enter the following information:
    - For **Scope name**, enter `access_as_user`
    - For **Who can consent**, ensure that the **Admins and users** option is selected.
    - In the **Admin consent display name** box, enter `Access TODO API as a user`.
    - In the **Admin consent description** box, enter `Access TODO API as a user`.
    - In the **User consent display name** box, enter `Access TODO API as a user`.
    - In the **User consent description** box, enter `Access TODO API as a user`.
    - For **State**, keep **Enabled**.
1. Select **Add scope**.

Add roles to the API App registration

1. Under **Manage**, select **App Roles** and **Create app role**
    - For **Display name**, enter `Admin`
    - For **Allowed member types**, select **Users/Groups**
    - For **Value**, enter `Admin`
    - For **Description**, enter `Administrator`
    - Ensure that the checkbox for **Do you want to enable this app role?** is checked
1. Repeat the same steps to create a `User` app role

Add a secret to the API App registration

1. Under **Manage**, select **Certificates & secrets** and **New client secret**
    - For **Description**, enter `API Client Secret`
    - For **Expires**, leave it at 6 months
1. Select **Add**
1. On the **Certificates & Secrets** page, save the secret **Value**. You'll need it to configure the API (that is `API_CLIENT_SECRET` in the *.env* file.).

> NOTE: You will not be able to access this value later so it is important that you save it. If you missed saving it, you can remove it and create a new secret.

Create an App registration for Swagger

1. Back at **App registrations**, select **New registration**
    - For **Name**, enter `TODO-API-SWAGGER`
    - For **Supported account types**, select **Accounts in any organizational directory**.
    - For **Redirect URI**, enter `http://localhost:8000/oauth2-redirect`
1. Select **Register** to create the application.
1. On the **Overview** page, look for the **Application (client) ID** value, and then record it for later use. You'll need it to configure the API (that is, `SWAGGER_UI_CLIENT_ID` in the *.env* file).

## Step 3: Assign users to roles

1. In Azure Portal, find and select **Azure Active Directory**
1. Under **Manage**, select **Enterprise applications**, and select the `TODO-API` application
1. Select **Assign users and groups** and then **Add user/group**
1. Under **Users**, select your own user, and select **Select** to make your choice.
1. Under **Select a role**, select either `Admin` or `User` and select **Select** to make your choice. Depending on which you choose, you will have access to different API endpoints
1. Select **Assign** to finish assigning the role to the user.

## Step 4: Configure the API

> TODO: install libraries + set up .env

## Step 5: Run the API locally

> TODO: running the API locally

## How the sample works

### The API

> TODO: brief overview of the endpoints

### Auth code and dependencies

> TODO: quick explanation of the auth code and the dependencies

### Protecting endpoints

> TODO: showing different ways of protecting endpoints

### Testing access

> TODO: maybe some unit tests etc. not sure if we need this, might be overkill

-----

Old stuff

## Configuring Azure AD Applications

## Configuring your dev environment

```cmd
python -m venv .venv
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

Fill out .env with ... coming soon
