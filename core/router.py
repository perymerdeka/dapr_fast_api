from fastapi import APIRouter
from .views import register, email_verification

router = APIRouter()

router.add_api_route("/register", endpoint=register, methods=["POST"])
router.add_api_route("/verification", endpoint=email_verification, methods=["GET"])