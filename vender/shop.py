from fastapi import APIRouter

router = APIRouter(prefix="/vendor")


@router.get('/')
def test():
    return {'msg': 'Test route Ok'}
