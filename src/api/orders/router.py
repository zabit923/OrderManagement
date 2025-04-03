from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from starlette.requests import Request

from api.orders.schemas import OrderCreate, OrderRead
from api.orders.service import OrderService, order_service_factory

router = APIRouter(prefix="/orders")


@router.post("", status_code=status.HTTP_201_CREATED, response_model=OrderRead)
async def create_order(
    order_data: OrderCreate,
    request: Request,
    order_service: OrderService = Depends(order_service_factory),
):
    if not request.user.is_authenticated:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    new_user = await order_service.create_order(order_data)
    return new_user
