# FastAPI-Learning 
- simple FastAPI application that demonstrates how to create an API for managing product suppliers.

## How to use 
- First install FastAPI ```pip install fastapi uvicorn```
- Then install tortoise ORM ```pip install tortoise-orm```
- Clone the repo ``` git clone https://github.com/Rabie45/FastAPI-.git```
- Use the terminal to run the server
- ```uvicorn main:app --reload```
## End points
- @app.post("/supplier")
  - async def add_supplier(supplier_info: supplier_pydanticIn) --> used to add supplier
- @app.get("/supplier")
  - async def get_all_suppliers() --> to return all supplier int the data base
- @app.get("/supplier/{supplier_id}") 
  - async def get_specific_supplier(supplier_id: int) return supplier with id 
- @app.put("/supplier/{supplier_id}")
  - async def update_supplier(supplier_id: int, upadte_info: supplier_pydanticIn) --> update supplier data
- @app.delete('/supplier/{supplier_id}')
  - async def delete_supplier(supplier_id: int) --> delete supplier
- @app.post("/product")
  - async def add_product(supplied_id:int,products_detail: product_pydanticIn) -->add product 
- @app.get("/product")
  - async def get_all_products() --> return all products
- @app.get("/product/{id}"
  - async def specific_product(id:int) --> return spacific product with supplier id
- @app.put("/product/{id}")
  - async def update_product(id: int, update_info: product_pydanticIn) --> update spacific product with supplier id
- @app.delete('/product/{id}')
  - async def delete_product(id: int) --> delete spacific product with supplier id
- ![Screenshot from 2024-08-01 15-51-30](https://github.com/user-attachments/assets/41b64ac4-1a38-4f4b-b733-3a8cb491150d)
