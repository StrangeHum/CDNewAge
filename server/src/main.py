# docker run --rm -p 15672:15672  rabbitmq:3.10.7-management
# docker run -d --name rabbitmq --hostname rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3.10.7-management
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/users")
async def make_order():
    return [{"id": 1, "name": ""}]


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")
