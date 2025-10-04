import pytest
from playwright.sync_api import Page, expect
from pathlib import Path

BASE = "https://the-internet.herokuapp.com"


@pytest.mark.e2e
def test_login_and_logout(page: Page):
    page.goto(f"{BASE}/login")

    # Login con credenciales correctas
    page.fill('input[name="username"]', 'tomsmith')
    page.fill('input[name="password"]', 'SuperSecretPassword!')
    page.click('button[type="submit"]')

    flash = page.locator('#flash')
    expect(flash).to_contain_text("You logged into a secure area!")

    # Logout
    page.click('a[href="/logout"]')
    expect(page.locator('#flash')).to_contain_text("You logged out")

@pytest.mark.e2e
def test_file_upload_and_verify(page: Page, tmp_path: Path):
    # Crear archivo temporal
    f = tmp_path / "upload_test.txt"
    f.write_text("hello from playwright")
    f.write_text("hello from playwright")

    page.goto(f"{BASE}/upload")
    page.set_input_files('input[type="file"]', str(f))
    page.click('input[type="submit"]')

    expect(page.locator('h3')).to_have_text("File Uploaded!")


@pytest.mark.e2e
def test_dynamic_controls_and_loading(page: Page):
    # Sección de Dynamic Controls
    page.goto(f"{BASE}/dynamic_controls")
    page.click('button[onclick="swapCheckbox()"]')
    message = page.locator('#message')
    expect(message).to_contain_text("It's gone!")

    # Sección de Dynamic Loading
    page.goto(f"{BASE}/dynamic_loading/1")
    page.click('div#start button')
    page.wait_for_selector('#finish')
    expect(page.locator('#finish')).to_have_text("Hello World!")


@pytest.mark.e2e
def test_drag_and_drop(page: Page):
    page.goto(f"{BASE}/drag_and_drop")
    box_a = page.locator('#column-a')
    box_b = page.locator('#column-b')

    # drag_and_drop puede fallar en algunos navegadores, lo reforzamos
    box_a.drag_to(box_b)

    # Verificar que el intercambio ocurrió
    text_a = box_a.inner_text().strip()
    text_b = box_b.inner_text().strip()
    assert text_a != text_b, "Los elementos no se intercambiaron correctamente"
    assert text_a == "B", f"Se esperaba 'B' en la columna A, pero se obtuvo '{text_a}'"
    assert text_b == "A", f"Se esperaba 'A' en la columna B, pero se obtuvo '{text_b}'"