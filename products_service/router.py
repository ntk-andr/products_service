from fastapi import APIRouter, Depends, Request
from sqlmodel import Session
from .db import get_session
from .dao import ProductsDAO
from .schemas import SchemaProduct, SchemaGetProduct, SchemaProductGetArgs
from .models import Product

router = APIRouter(
    prefix='/products',
    tags=['Товары в магазине']
)

@router.get('/')
def all_products(
    session: Session = Depends(get_session),
    ) -> list[SchemaGetProduct]:
    return ProductsDAO.find_all(
        session=session
        )
    

@router.get("/{product_id}")
def one_product_by_id(
    product_id: int,
    session: Session = Depends(get_session),
    ) -> SchemaGetProduct: 
    return ProductsDAO.find_by_id(session=session,model_id=product_id)
    
@router.post('/')
def create_product(
    product: SchemaProduct,
    session: Session = Depends(get_session),
    ):
    return ProductsDAO.add(session=session, data=product.model_dump())

@router.put('/{product_id}')
def update_product(
    product_id: int,
    product: SchemaProduct,
    session: Session = Depends(get_session),
    ):
    # return product
    return ProductsDAO.update(session=session, model_id=product_id, data=product.model_dump())

@router.delete('/{product_id}')
def delete_products(
    product_id:int, 
    product: SchemaProduct,
    session: Session = Depends(get_session),
    ):
    return ProductsDAO.delete(session=session,model_id=product_id,data=product.model_dump())
