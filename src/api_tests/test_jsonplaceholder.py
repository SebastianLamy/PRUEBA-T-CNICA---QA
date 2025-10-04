import time
import requests
from utils.schemas import post_schema, user_schema, assert_schema

BASE = "https://jsonplaceholder.typicode.com"

def test_get_posts_schema_and_performance():
    start = time.time()
    r = requests.get(f"{BASE}/posts")
    elapsed = time.time() - start
    assert r.status_code == 200
    assert elapsed < 2.0, f"Response too slow: {elapsed}s"

    from typing import List, Dict, Any
    data: List[Dict[str, Any]] = r.json()
    assert isinstance(data, list)
    assert len(data) > 0

    # validar primer elemento contra esquema de post
    assert_schema(data[0], post_schema)


def test_post_put_delete_crud_flow():
    # POST
    payload: dict[str, str | int] = {"title": "foo", "body": "bar", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code in (201, 200)

    created = r.json()
    assert created.get("title") == "foo"

    # validar contra post_schema
    assert_schema(created, post_schema)

    post_id = created.get("id") or 101

    # PUT (update)
    update: dict[str, str | int] = {"id": post_id, "title": "foo2", "body": "bar2", "userId": 1}
    r2 = requests.put(f"{BASE}/posts/{post_id}", json=update)
    assert r2.status_code in (200, 201)
    assert r2.json().get("title") == "foo2"

    # DELETE
    r3 = requests.delete(f"{BASE}/posts/{post_id}")
    assert r3.status_code in (200, 204)


def test_post_comments_and_user_posts():
    # comentarios de un post
    r = requests.get(f"{BASE}/posts/1/comments")
    assert r.status_code == 200
    from typing import List, Dict, Any
    comments: List[Dict[str, Any]] = r.json()
    assert isinstance(comments, list)
    assert len(comments) > 0

    # posts de un usuario (algunas versiones usan /posts?userId=1)
    r2 = requests.get(f"{BASE}/users/1/posts")
    if r2.status_code == 404:
        r2 = requests.get(f"{BASE}/posts", params={"userId": 1})

    assert r2.status_code == 200
    from typing import List, Dict, Any
    user_posts: List[Dict[str, Any]] = r2.json()
    assert isinstance(user_posts, list)
    assert len(user_posts) > 0

    # validar primer post de usuario contra post_schema
    assert_schema(user_posts[0], post_schema)


def test_get_user_schema():
    # obtener un usuario
    r = requests.get(f"{BASE}/users/1")
    assert r.status_code == 200
    user = r.json()

    # validar contra esquema de usuario
    assert_schema(user, user_schema)


def test_negative_cases_invalid_id_and_method():
    # ID inexistente
    r = requests.get(f"{BASE}/posts/9999")
    assert r.status_code in (200, 404)

    # payload inválido
    r2 = requests.post(f"{BASE}/posts", data="not-json")
    assert r2.status_code in (400, 201, 200)

    # método no permitido
    r3 = requests.patch(f"{BASE}/nonexistent")
    assert r3.status_code in (404, 405)
    r4 = requests.put(f"{BASE}/posts/1", data="not-json")
    assert r4.status_code in (400, 200, 201)