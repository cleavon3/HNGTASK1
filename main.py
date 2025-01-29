from fastapi import FastAPI
from starlette import status
from datetime import datetime
from pydantic import BaseModel, Field
app = FastAPI()

# class AppRequest(BaseModel):
#     Email: str = Field(min_length=2)
#     Github_url: str = Field (min_lenght=2)
#
#     model_config = {
#         "json_schema_extra": {
#             "example": {
#                 "mail": "cleavon_design@gmail.com",
#                 "github_url": "https://github.com/yourusername/your-repo",
#             }
#         }
#     }



@app.get("/", status_code=status.HTTP_200_OK)
async def get_info():
    return {
        "email" : "cleavon_design@gmail.com",
        "current_datetime" : datetime.utcnow().isoformat() + "Z",
        "Github_url": "https://github.com/yourusername/your-repo"
    }
