from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
def main():
 return("Hello from fight-nepal!")


if __name__ == "__main__":
    main()
