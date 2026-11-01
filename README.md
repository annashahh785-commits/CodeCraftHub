# CodeCraftHub

CodeCraftHub is a beginner-friendly learning platform API built using Python and Flask. It allows users to manage their learning courses and track their progress.

## Features

- Create new courses
- Retrieve all courses
- Retrieve an individual course
- Update course information
- Delete courses
- Validate course information
- Handle API errors
- Store course data in a JSON file

## Technologies Used

- Python
- Flask
- REST API
- JSON
- PowerShell

## Project Structure

```text
CodeCraftHub/
├── app.py
├── courses.json
├── requirements.txt
├── test_commands.md
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project folder:

```bash
cd CodeCraftHub
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

The API runs at:

`http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/api/courses` | Retrieve all courses |
| GET | `/api/courses/<id>` | Retrieve a specific course |
| POST | `/api/courses` | Create a course |
| PUT | `/api/courses/<id>` | Update a course |
| DELETE | `/api/courses/<id>` | Delete a course |

## Course Statuses

- Not Started
- In Progress
- Completed

## Data Storage

Course information is stored locally in `courses.json`.

## Testing

Refer to `test_commands.md` for API test commands and expected responses.

## Project Status

Initial development version. Further improvements and verification are ongoing.