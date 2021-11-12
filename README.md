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
1. Under **Manage**, select **App registrations > New registration**.
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
    - For **Redirect URI**, select **Single-page application (SPA)** and enter `http://localhost:8000/oauth2-redirect`
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

Configure environment variables

1. Copy the `.env.sample` file and rename to `.env`
1. Set the `API_CLIENT_ID`, `API_CLIENT_SECRET` and `SWAGGER_UI_CLIENT_ID` to the values you gathered above
1. Set the `AAD_TENANT_ID` to your Azure Tenant ID

Install required libraries

1. Open a command prompt and navigate to the directory where you cloned the repository
1. Create a new virtual environment to install your python libraries

    ```cmd
    python -m venv .venv
    ```

1. Activate your virtual environment

    ```cmd
    .\.venv\Scripts\activate    # Windows
    source .venv/Scripts/activate   # Linux
    ```

1. Upgrade pip to the latest version

    ```cmd
    python -m pip install --upgrade pip
    ```

1. Install the required libraries `pip install -r requirements.txt`

    ```cmd
    pip install -r requirements.txt
    ```

Open Visual Studio Code and set the interpreter

1. In the terminal window, in the project directory, launch visual studio code

    ```cmd
    code .
    ```

1. Visual Studio Code may recognize that there is a virtual environment and ask you if you want to activate it. If this does not happen, use **View->Command Palette->Python:Select Interpreter** and select the `.venv:venv` interpreter (in rare cases you may need to manually select the `.\.venv\Scripts\python.exe` if Visual Studio Code does not recommend it).
1. Close down any open terminals and start a new one from **Terminal->New Terminal**. This ensures that any commands you run will be using the new interpreter.

## Step 5: Run the API locally

Run the API from Visual Studio Code

1. Open the file `app/main.py`
1. Press **F5** to run under a debugger (or **CTRL+F5** to run without a debugger)
1. Under **Debug Configuration** select **Python File**

This will serve the api locally on your machine.

> NOTE: The output suggests for you to browse to [http://localhost:8000](http://localhost:8000) - if you browse there you will see {"detail": "Not Found"}, this is normal as we don't have a default endpoint for our API.

1. Browse to [http://localhost:8000/health](http://localhost:8000/health) to reach the health endpoint. If all is working correctly, you should be greeted with "OK"
1. Browse to [http://localhost:8000/docs](http://localhost:8000/docs) to see the Swagger UI and the available endpoints.
1. Try an endpoint - for example **[GET]/todoitems->Try it out->Execute**. This should result in a `401:Unauthorized`

Log in to use the API

1. Log in using the **Authorize** button at the top right of the page.
    - **client_id:** should be pre-filled, leave it as is
    - **client_secret:** should be empty, leave it as is
    - **scopes:** select the `Access API as user` scope
    - Select **Authorize** to log in
1. Follow the prompts to log in with your account.
1. In the **Permissions requested** dialog box, check the box to **Consent on behalf of your organization** and select **Accept** - you will only need to consent once for the API.
1. In the **Available authorizations** dialog box, select **Close**

Access the **[POST]/todoitems**

1. Select the **[POST]/todoitems** endpoint
1. Select **Try it out**. You can change the request body, and give it another name than "Walk the dog" if you want
1. Select **Execute**
1. Verify that you receive a **201** result, and the resulting json for the created item.

## How the sample works

### The API

You can find the code for the available routes in `/app/api/routes/api.py`

| Endpoint | Request Method | Description | Authentication | Auth method |
| -- | -- | -- | -- | -- |
| /health | GET | Get health status | No authentication |
| /todoitems | GET | Get my todo items | User | Depends(get_user) |
| /todoitems | POST | Create todo item | User | Depends(get_user) |
| /todoitems | DELETE | Delete all todo items | Admin | Depends(get_admin_user) |
| /todoitems/{id} | GET | Get todo item | User (owner of item or admin) | Depends(get_todo_item_by_id_from_path) |
| /todoitems/{id} | DELETE | Delete todo item | User (owner of item or admin) | Depends(get_todo_item_by_id_from_path) |

### Auth code and dependencies

FastAPI has a powerful [**Dependency Injection**](https://fastapi.tiangolo.com/tutorial/dependencies/) system, that allows us to enforce security, authentication, role requirements etc.

In our case, we have created a simple dependency function in `/app/api/dependencies/auth.py` to ensure that the user is logged in for the `GET /todoitems` endpoint for example.

```python
def get_user(user: User = Depends(authorize)) -> User:
    return user
```

This, in turn, depends on **authorize**, defined in `app/services/AzureADAuthorization.py`. **authorize** is an instance of the **AzureADAuthorization**, that when called (through the `__call__` method) validates and decodes the authentication token against the Azure AD App and required scopes, and further generates a **User** instance based on the contents of the token.

If the token is invalid, or can't be processed, the **AzureADAuthorization** class returns a **401 UNAUTHORIZED** HTTP status.

Because the **AzureADAuthorization** class derives from **OAuth2AuthorizationCodeBearer**, FastAPI (and Swagger) understands that the endpoint requires authentication, and displays the padlock in the Swagger UI.

### Protecting endpoints

There are multiple ways to protect the endpoints, and the various endpoints implemented in this sample, show some of these varieties.

#### Require user to be authenticated

By passing in `user = Depends(get_user)` as a parameter to our endpoint function, we require the user to be authenticated and also get the user info, so that we can filter the todo items that belong to the user.

```python
@router.get('/todoitems', status_code=status.HTTP_200_OK, name="Get My Todos [Admin or Owner of todo]")
async def get_my_todos(user: User = Depends(get_user)) -> TodoItemsInList:
    items: List[TodoItem] = todo_repository.get_items_for_user(user)
    return TodoItemsInList(items=items)
```

#### Require the user to have the admin role

We can create more specialized dependency functions, that both validates that the user is authenticated, and validates that the user has the correct role.

```python
def get_admin_user(user: User = Depends(authorize)) -> User:
    if 'Admin' in user.roles:
        return user
    raise ForbiddenAccess('Admin privileges required')
```

We can then use the **get_admin_user** dependency function exactly as the **get_user** function.

The example below shows this usage with a slight modification. If you don't need to use the returned **user** for further processing, you can simply add the dependency to the router decorator.

```python
@router.delete('/todoitems', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(get_admin_user)], name="Delete all Todos [Admin]")
async def delete_all_todo_items() -> None:
    todo_repository.delete_all_items()
```

##### Create a dependency that retrieves a todo item if the user can access it

We can also create more intricate dependencies, that don't only validate authorization, but also validate access to items.

```python
def get_todo_item_by_id_from_path(id: int = Path(...), user: User = Depends(get_user)):
    try:
        todo: TodoItem = todo_repository.get_item(id)
    except EntityNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item does not exist')

    if 'Admin' in user.roles or todo.owner_id == user.id:
        return todo
    raise HTTPException(status.HTTP_403_FORBIDDEN, detail='User is not allowed to access the item')
```

Because **get_user** indirectly depends on **OAuth2AuthorizationCodeBearer**, and **get_todo_item_by_id_from_path** depends on **get_user**, FastAPI and the Swagger UI will still understand that authorization is required.

```python
@router.get('/todoitems/{id}', status_code=status.HTTP_200_OK, name="Get Todo by Id [Admin or Owner of todo]")
async def get_todo_by_id(id: int, todo: TodoItem = Depends(get_todo_item_by_id_from_path)) -> TodoItemInResponse:
    return TodoItemInResponse(item=todo)
```
