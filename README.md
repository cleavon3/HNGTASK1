# HNG Stage 0 Task - Public API

This is a simple public API that returns:
- My registered email address.
- The current datetime in ISO 8601 format.
- The GitHub URL of this project.

## API Endpoint
- URL: `https://your-app.onrender.com`
- Method: `GET`
- Response:
  ```json
  {
    "email": "your-email@example.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/your-repo"
  }