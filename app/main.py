from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from core.database import Base, engine, get_db
from user.models import User
from product.models import Product, ProductImage
from category.models import Category, CategoryImage





app = FastAPI()



# midleware
app.add_middleware(
    
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# database:
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup():
    db = get_db()
    try:
        yield db
    finally:
        db.close()





@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)



