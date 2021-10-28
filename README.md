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

> TODO: Rewrite the below to fit this project

Register your web API in **App Registrations** in the Azure portal.

1. Sign in to the Azure Portal
1. If you have access to multiple tenants, use the **Directory + subscription** filter in the top menu to select the tenant in which you want to register an application.
1. Find and select **Azure Active Directory**.
1. Under **Manage**, select **App registrations > New registation**.
1. Enter a **Name** for your application, for example `AppModelv2-NativeClient-DotNet-TodoListService`. Users of your app might see this name and you can change it later.
1. For **Supported account types**, select **Accounts in any organizational directory**.
1. Select **Register** to create the application.
1. On the **Overview** page, look for the **Application (client) ID** value, and then record it for later use. You'll need it to configure the configuration file for this project (that is, `ClientId` in the *TodoListService\Web.config* file).
1. Under **Manage**, select **Expose an API > Add a scope**. Accept the proposed Application ID URI (api://{clientId}) by selecting **Save and continue**, and then enter the following information:
    - For **Scope name**, enter `access_as_user`
    - For **Who can consent**, ensure that the **Admins and users** option is selected.
    - In the **Admin consent display name** box, enter `Access TodoListService as a user`.
    - In the **Admin consent description** box, enter `Access TodoListService web API as a user`.
    - In the **User consent display name** box, enter `Access TodoListService as a user`.
    - In the **User consent description** box, enter `Access TodoListService web API as a user`.
    - For **State**, keep **Enabled**.
1. Select **Add scope**.

> TODO: how to register the necessary AAD apps for API + Swagger

## Step 3: Configure the API and Swagger

> TODO: install libraries + set up .env

## Step 4: Run the API locally

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
