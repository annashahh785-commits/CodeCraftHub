# CodeCraftHub – API Testing Documentation

## 1. Introduction

This document contains test cases for verifying the CodeCraftHub REST API.

The tests cover:
- Creating courses
- Retrieving all courses
- Retrieving a specific course
- Updating courses
- Deleting courses
- Testing invalid requests
- Verifying error handling

**Base URL:** `http://127.0.0.1:5000`

**Important:** Start the Flask server using `python app.py` before running these tests. Execute the commands in a second PowerShell terminal.

---

## 2. Successful API Tests

### Test 1: Create a course (POST)

**Endpoint:** `/api/courses`

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/courses" -Method POST -ContentType "application/json" -Body '{"course_name":"Python Basics","description":"Learn Python fundamentals","target_completion_date":"2026-12-15","status":"Not Started"}'
```

Expected:
- Course created successfully.
- Automatically generated ID.
- Creation timestamp returned.
- HTTP status: 201 Created.

### Test 2: Retrieve all courses (GET)

**Endpoint:** `/api/courses`

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/courses" -Method GET
```

Expected:
- Returns all stored courses.
- HTTP status: 200 OK.

### Test 3: Retrieve a specific course (GET)

**Endpoint:** `/api/courses/1`

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/courses/1" -Method GET
```

Expected:
- Returns the course with ID 1.
- HTTP status: 200 OK.

### Test 4: Update a course (PUT)

**Endpoint:** `/api/courses/1`

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/courses/1" -Method PUT -ContentType "application/json" -Body '{"course_name":"Python Basics","description":"Learn Python fundamentals","target_completion_date":"2026-12-15","status":"In Progress"}'
```

Expected:
- Course information updated.
- Status changes to In Progress.
- Original creation timestamp remains unchanged.
- HTTP status: 200 OK.

### Test 5: Delete a course (DELETE)

**Endpoint:** `/api/courses/1`

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/courses/1" -Method DELETE
```

Expected:
- Course deleted successfully.
- HTTP status: 200 OK.

### Test 6: Verify deletion (GET)

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/courses" -Method GET
```

Expected:
- Empty list if no other courses exist.

```json
[]
```

---

## 3. Error Handling Tests

### Test 7: Invalid course status

Try creating a course with an unsupported status.

```powershell
curl.exe -i -X POST "http://127.0.0.1:5000/api/courses" -H "Content-Type: application/json" -d '{"course_name":"Flask","description":"Learn Flask","target_completion_date":"2026-12-20","status":"Learning"}'
```

Expected:
- HTTP status: 400 Bad Request.
- Error: Invalid course status.

### Test 8: Missing required fields

```powershell
curl.exe -i -X POST "http://127.0.0.1:5000/api/courses" -H "Content-Type: application/json" -d '{"course_name":"Flask"}'
```

Expected:
- HTTP status: 400 Bad Request.
- Error indicating a missing required field.

### Test 9: Invalid date format

```powershell
curl.exe -i -X POST "http://127.0.0.1:5000/api/courses" -H "Content-Type: application/json" -d '{"course_name":"Flask","description":"Learn Flask","target_completion_date":"20-12-2026","status":"Not Started"}'
```

Expected:
- HTTP status: 400 Bad Request.
- Error: Date must be in YYYY-MM-DD format.

### Test 10: Course not found

```powershell
curl.exe -i "http://127.0.0.1:5000/api/courses/9999"
```

Expected:
- HTTP status: 404 Not Found.
- Error: Course not found.

### Test 11: Update a nonexistent course

```powershell
curl.exe -i -X PUT "http://127.0.0.1:5000/api/courses/9999" -H "Content-Type: application/json" -d '{"course_name":"Flask","description":"Learn Flask","target_completion_date":"2026-12-20","status":"In Progress"}'
```

Expected:
- HTTP status: 404 Not Found.
- Error: Course not found.

### Test 12: Delete a nonexistent course

```powershell
curl.exe -i -X DELETE "http://127.0.0.1:5000/api/courses/9999"
```

Expected:
- HTTP status: 404 Not Found.
- Error: Course not found.

---

## 4. Final Verification Checklist

- [ ] POST creates a course.
- [ ] GET retrieves all courses.
- [ ] GET retrieves a specific course.
- [ ] PUT updates a course.
