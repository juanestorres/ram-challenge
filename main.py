from fastapi import FastAPI
import src.ram_challenge_logic
app = FastAPI()


@app.get("/")
async def root():
    response = src.ram_challenge_logic.rick_and_morty_solution(False)
    print(type(response))
    return response