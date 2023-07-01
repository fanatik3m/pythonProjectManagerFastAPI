from fastapi import HTTPException


def check_len(result):
    if not len(result.all()):
        raise HTTPException(status_code=403, detail={
            'status': 'error',
            'details': {'msg': '403 Forbidden'},
            'data': {}
        })