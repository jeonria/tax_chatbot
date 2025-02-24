from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Tax Assistant API"}

@app.get("/chat/{query}")
def chat(query: str):
    return {"response": f"Your tax-related query: {query}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
