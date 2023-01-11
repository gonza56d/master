from fastapi import APIRouter

hello = APIRouter()


@hello.get('/hello/', tags=['hello'])
async def root():
    return {'hello': 'world!'}
