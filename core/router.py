from fastapi import APIRouter
from .views import register

router = APIRouter()

router.add_api_route("/register", endpoint=register, methods=["POST"])