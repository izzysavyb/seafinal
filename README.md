# SEAFinal

Software Engineering and Agile Assignment

## Instructions for running the project locally.

1. Unzip the file and open it in your IDE of choice (or open it from the repository)
2. Cd into the backend a create a virtual environment using the following command: python -m venv seavenv
3. Activate the venv with this command: seavenv\Scripts\activate
4. Install the dependencies for the backend with this command: pip install -r requirements.txt
5. Create a .env file in the backend folder and put the following inside:
   SECRET_KEY=<your generated key>
   ALGORITHM=HS256
   DATABASE_URL=sqlite:///./assets.db
6. Generate a secret key using the following command and paste it into the secret key variable in the .env file:
   python -c "import secrets; print(secrets.token_hex(32))"
7. Then run uvicorn app.main:app to start the backend
8. Docs can be found at: http://127.0.0.1:8000/docs
9. CD into the frontend and run npm i to install the dependencies
10. Then run npm run dev
11. Frontend can be found at this URL: http://localhost:5173
12. Log in with account: username - admin and password - Admin123 to access admin permissons or create your own account by registering!
