from fastapi import APIRouter

router = APIRouter(prefix="/vendor2")


@router.get('/')
def test():
    return {'msg': 'Test from init route Ok'}
