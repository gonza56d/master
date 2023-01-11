from fastapi import APIRouter

router = APIRouter()


@router.get('/', tags=['hello'])
async def root():
    return {'hello': 'world!'}
