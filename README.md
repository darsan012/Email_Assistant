# Email Assistant with AI using Flask

This project is an **AI-powered Email Assistant** built with Python Flask. 
It helps users efficiently manage their emails, generate intelligent responses,
and perform automated tasks.
The project also incorporates Continuous Integration (CI) and Continuous Deployment (CD)
using GitHub Actions.

---

## Features

- **AI-powered email analysis** for generating intelligent suggestions.
- User-friendly web interface for managing emails.
- Secure handling of sensitive data with environment variables.
- Docker support for containerized deployment.
- GitHub Actions for automated testing and deployment.

---

## Prerequisites

To run the application and tests locally, you will need:

- **Python 3.9 or higher**
- **Flask** framework
- **pip** (Python package manager)
- **Docker** (optional, for containerization)


---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Rakshya64/Email_Assistant.git
cd Email_Assistant
```
### 2. Set up a Virtual Environment on Windows
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set Up Environment Variables
FLASK_APP=app.py
FLASK_ENV=development

### 3. Install Dependencies
```bash
python app.py
```
---

## Contributing Rules

We welcome contributions to the **Email Assistant with AI** project!
Please follow these rules to maintain consistency and ensure a smooth workflow:

---

### 1. Always Pull Before Starting
- Pull the latest changes from the `main` branch before starting any new work:
  ```bash
  git pull origin main
  ```

---

### 2. Create a New Branch for Each Feature
- Use the following naming convention for branches:  
  ```
  <your-initials><FeatureName><MonthAbbreviation><Day>
  ```
  Example:
  - For "Rakshya Niraula" adding email filtering on December 6th:
    ```
    rnAddEmailFilterDec06
    ```

---

### 3. Resolve Conflicts Locally
- Handle any merge conflicts on your local machine rather than on GitHub's web interface.

---

### 4. Never Commit Directly to `main`
- The `main` branch is protected. Always work on a separate branch and submit a pull request (PR) for review.

---

### 5. Managing Dependencies with `pip freeze`
- If you install a new package, make sure to update the `requirements.txt` file to reflect the changes:
  ```bash
  pip freeze > requirements.txt
  ```
- This ensures that all contributors can install the same dependencies by running:
  ```bash
  pip install -r requirements.txt
  ```
- Always check in the updated `requirements.txt` as part of your commit.

---


### 6. Naming Conventions
- **File Names**: Use **PascalCasing** (e.g., `EmailHandler.py`).  
- **Template & Static Files**: Use **snake_case** (e.g., `user_profile.html`, `email_styles.css`).  
- **Variables and Functions**: Use **snake_case** (e.g., `process_email()`).

---

### 7. Testing and Debugging
- Before submitting a pull request:
  - Test your code locally using `pytest` or Flask's test client.
  - Debug any issues to ensure your changes work as expected.
  - Avoid pushing broken or half-completed code.

---

### 8. Submit a Pull Request
- Submit a PR to the `main` branch with a clear title and description of your changes.
- Tag a team member for review.

---

By following these rules, we can ensure that our project stays clean, efficient, and collaborative. Thank you for contributing! 😊

---




