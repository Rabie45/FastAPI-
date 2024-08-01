
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import (Products, supplier_pydantic,supplier_pydanticIn, Supplier,product_pydantic,product_pydanticIn)
from typing import List

from fastapi import BackgroundTasks, FastAPI
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse


app = FastAPI()



@app.get("/")
async def root():
    return {"Msg": "Hello world"}



@app.post("/supplier")
async def add_supplier(supplier_info: supplier_pydanticIn): # type: ignore
    supplier_obj = await Supplier.create(**supplier_info.model_dump(exclude_unset=True))
    response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
    return {"status":"ok","data":response}


@app.get("/supplier")
async def get_all_suppliers():
    response = await supplier_pydantic.from_queryset(Supplier.all())
    return {"status":"ok","data":response}
    
@app.get("/supplier/{supplier_id}") 
async def get_specific_supplier(supplier_id: int):
      response = await supplier_pydantic.from_queryset_single(Supplier.get(id=supplier_id))
      #response = await supplier_pydantic.from_tortoise_orm(response)
      return {"status":"ok","data":response}
      
      
@app.put("/supplier/{supplier_id}")
async def update_supplier(supplier_id: int, upadte_info: supplier_pydanticIn): # type: ignore
    product = await Supplier.get(id=supplier_id)
    upadte_info =upadte_info.model_dump(exclude_unset=True)
    product.name= upadte_info['name']
    product.company= upadte_info['company']
    product.email= upadte_info['email']
    product.phone_number= upadte_info['phone_number']
    await product.save()
    response = await supplier_pydantic.from_tortoise_orm(response)
    return {"status":"ok","data":response}
    
    

@app.delete('/supplier/{supplier_id}')
async def delete_supplier(supplier_id: int):
    await Supplier.get(id=supplier_id).delete()
    return {"status":"ok","data":f"Supplier with id {supplier_id} has been deleted"} 
   
        
@app.post("/product")
async def add_product(supplied_id:int,products_detail: product_pydanticIn): # type: ignore
    supplier = await Supplier.get(id=supplied_id)
    if not supplier:
        return {"status":"error","data":f"Supplier with id {supplied_id} not found"}
    
    products_detail=products_detail.model_dump(exclude_unset=True)
    products_detail['revenue']+=products_detail['quantity_sold'] * products_detail['unit_price'] 
    products_detail['supplied_by']= supplier  # add supplier relationship to the product
    product_obj = await Products.create(**products_detail)
    response = await product_pydantic.from_tortoise_orm(product_obj)
    return {"status":"ok","data":response}

@app.get("/product")
async def get_all_products():
    response = await product_pydantic.from_queryset(Products.all())
    return {"status":"ok","data":response}

@app.get("/product/{id}")
async def specific_product(id:int):
    response= await product_pydantic.from_queryset_single(Products.get(id=id))
    return {"status":"ok","data":response}

@app.put("/product/{id}")
async def update_product(id: int, update_info: product_pydanticIn): # type: ignore
    product = await Products.get(id=id)

    update_info = update_info.model_dump(exclude_unset=True)
    product.name = update_info['name']
    product.quantity_in_stock = update_info['quantity_in_stock']
    product.quantity_sold += update_info['quantity_sold']
    product.unit_price = update_info['unit_price']
    product.revenue += update_info['quantity_sold'] * update_info['unit_price']
    await product.save()
    response = await product_pydantic.from_tortoise_orm(product)
    return {"status": "ok", "data": response}


@app.delete('/product/{id}')
async def delete_product(id: int):
    await Products.get(id=id).delete()
    return {"status":"ok","data":f"Product with id {id} has been deleted"} 



register_tortoise(app,
                  db_url="sqlite://database.sqlite3",
                  modules={"models": ["models"]},
                  generate_schemas=True,
                  add_exception_handlers=True
)

