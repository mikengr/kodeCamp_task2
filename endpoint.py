from fastapi import FastAPI

app = FastAPI()

@app.get('/query_param/')
def query_param(query_id: int):
    return {"query_id" : query_id}


@app.get("/path_param/{path_param_id}")
def path_param(path_param_id: int):
    return {"param_id" : path_param_id}
