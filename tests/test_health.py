from http import HTTPStatus

from httpx2 import AsyncClient


async def test_health(client: AsyncClient) -> None:
    response = await client.get("/api/v1/health")

    body = response.json()

    assert response.status_code == HTTPStatus.OK, f"Ожидали статус 200, получили: {response.status_code}."
    assert body == {"status": "ok"}, f"Ожидали status: ok, получили: {body}."
