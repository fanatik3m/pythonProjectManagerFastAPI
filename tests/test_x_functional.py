from httpx import AsyncClient


async def test_create_project(ac: AsyncClient):
    response = await ac.post('/projects', cookies={
        'user_cookie': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODgzMjI0MDd9.p9xNbRfEPdRqf0aWF44r2Mz9uGkStOzHwR6M5oiXrjk'},
        json={
            'title': 'restful api',
            'description': 'make restful api using fastapi'
        }
    )

    assert response.status_code == 200, 'got wrong status code'
    assert response.json().get('status') == 'ok', 'status is not ok'


async def test_check_self_projects(ac: AsyncClient):
    response = await ac.get('/projects', params={
        'page': 1
    },
        cookies={
        'user_cookie': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODgzMjI0MDd9.p9xNbRfEPdRqf0aWF44r2Mz9uGkStOzHwR6M5oiXrjk'},
    )

    assert response.status_code == 200, 'got wrong status code'
    assert response.json().get('status') == 'ok', 'got not ok status'
    assert len(response.json().get('data')), 'got no data'


async def test_check_all_projects(ac: AsyncClient):
    response = await ac.get('/projects/all', params={
        'page': 1
    })

    assert response.status_code == 200, 'got wrong status code'
    assert response.json().get('status') == 'ok', 'got not ok status'
    assert len(response.json().get('data')), 'got no data'


async def test_add_user_to_project(ac: AsyncClient):
    response = await ac.post('/projects/1/1', cookies={
        'user_cookie': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODgzMjI0MDd9.p9xNbRfEPdRqf0aWF44r2Mz9uGkStOzHwR6M5oiXrjk'},
    )

    assert response.status_code == 200, 'got wrong status code'
    assert response.json().get('status') == 'ok', 'got not ok status'


async def test_add_task(ac: AsyncClient):
    response = await ac.post('/projects/tasks', cookies={
        'user_cookie': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODgzMjI0MDd9.p9xNbRfEPdRqf0aWF44r2Mz9uGkStOzHwR6M5oiXrjk'},
        json={
            'title': 'make security',
            'description': 'make security app - add auth and registration using fastapi-users',
            'executor_id': 1,
            'project_id': 1
        }
    )

    assert response.status_code == 200, 'got wrong status code'
    assert response.json().get('status') == 'ok', 'got not ok status'


async def test_check_tasks(ac: AsyncClient):
    response = await ac.get('/projects/tasks', cookies={
        'user_cookie': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODgzMjI0MDd9.p9xNbRfEPdRqf0aWF44r2Mz9uGkStOzHwR6M5oiXrjk'},
        params={
            'page': 1
        }
    )

    assert response.status_code == 200, 'got wrong status code'
    assert response.json().get('status') == 'ok', 'got wrong status'
    assert len(response.json().get('data')), 'got no tasks'


async def test_mark_task_as_completed(ac: AsyncClient):
    response = await ac.put('/projects/tasks/1', cookies={
        'user_cookie': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODgzMjI0MDd9.p9xNbRfEPdRqf0aWF44r2Mz9uGkStOzHwR6M5oiXrjk'},
    )

    assert response.status_code == 200, 'got wrong status code'
    assert response.json().get('status') == 'ok', 'got not ok status'


async def test_check_self_completed_tasks(ac: AsyncClient):
    response = await ac.get('/projects/tasks/completed', cookies={
        'user_cookie': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODgzMjI0MDd9.p9xNbRfEPdRqf0aWF44r2Mz9uGkStOzHwR6M5oiXrjk'},
        params={
            'page': 1
        }
    )

    assert response.status_code == 200, 'got wrong status code'
    assert response.json().get('status') == 'ok', 'got wrong status'
    assert len(response.json().get('data')), 'got no data'


async def test_check_self_uncompleted_tasks(ac: AsyncClient):
    response = await ac.get('/projects/tasks/uncompleted', cookies={
        'user_cookie': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODgzMjI0MDd9.p9xNbRfEPdRqf0aWF44r2Mz9uGkStOzHwR6M5oiXrjk'},
        params={
            'page': 1
        }
    )

    assert response.status_code == 200, 'got wrong status code'
    assert response.json().get('status') == 'ok', 'got wrong status'
    assert not len(response.json().get('data')), 'got no data'


async def test_delete_user_from_project(ac: AsyncClient):
    response = await ac.delete('/projects/1/1', cookies={
        'user_cookie': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODgzMjI0MDd9.p9xNbRfEPdRqf0aWF44r2Mz9uGkStOzHwR6M5oiXrjk'},
    )

    assert response.status_code == 200, 'got wrong status code'
    assert response.json().get('status') == 'ok', 'got not ok status'


