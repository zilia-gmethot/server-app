from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World!"}


@app.get("/healthcheck")
def read_healthcheck():
    return Response(status_code=200)
