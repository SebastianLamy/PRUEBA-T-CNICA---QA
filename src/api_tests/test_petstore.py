import requests


BASE = "https://petstore.swagger.io/v2"




def test_find_pets_by_status():
    r = requests.get(f"{BASE}/pet/findByStatus", params={"status": "available"})
    assert r.status_code == 200
    assert isinstance(r.json(), list)




def test_basic_pet_crud():
    pet: dict[str, object] = {"id": 999999, "name": "pytest-pet", "photoUrls": [], "status": "available"}
    # create
    r = requests.post(f"{BASE}/pet", json=pet)
    assert r.status_code in (200, 201)


    # get
    r2 = requests.get(f"{BASE}/pet/999999")
    assert r2.status_code == 200
    assert r2.json().get("name") == "pytest-pet"


    # delete
    r3 = requests.delete(f"{BASE}/pet/999999")
    assert r3.status_code in (200, 204)