
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="Simple Python Calculator")


@app.get("/")
def home():
    return {"message": "Welcome to the Python Calculator API"}


@app.get("/calculate")
def calculate(first: float, operator: str, second: float):
    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot divide by zero"
            )
        result = first / second
    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid operator. Use +, -, *, or /."
        )

    return {
        "first": first,
        "operator": operator,
        "second": second,
        "result": result
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
