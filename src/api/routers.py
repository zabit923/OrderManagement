from fastapi import APIRouter

from api.orders.router import router as order_router
from api.users.router import router as users_router

router = APIRouter(prefix="/api/v1")
router.include_router(users_router, tags=["users"])
router.include_router(order_router, tags=["orders"])
