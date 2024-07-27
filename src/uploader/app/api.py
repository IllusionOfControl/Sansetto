from typing import Annotated

from fastapi import APIRouter, UploadFile, Form, File, Response, status, Depends

from app.dependencies import get_image_upload_service
from app.exceptions import InternalException
from app.services import ImageUploadService

router = APIRouter()

ImageUploadServiceDep = Annotated[ImageUploadService, Depends(get_image_upload_service)]


@router.post('/upload')
async def upload(
        image: Annotated[UploadFile, File()],
        meta: Annotated[str, Form(default="{}")],
        image_upload_service: ImageUploadServiceDep
):
    file_buff = await image.read()
    try:
        await image_upload_service.upload(
            image_buff=file_buff,
            meta_raw=meta,
        )
    except InternalException as exc:
        return {
            "success": True,
            "message": str(exc),
        }

    return Response(status_code=status.HTTP_201_CREATED)
