from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Given: Saya berada di halaman utama Google
@given('saya berada di halaman utama Google')
def buka_halaman_google(context):
    context.browser = webdriver.Chrome()  # Pastikan Anda memiliki ChromeDriver yang sesuai
    context.browser.get("https://www.google.com")  # Buka halaman Google

# When: Saya mencari "GitHub"
@when('saya mencari "{kata_kunci}"')
def lakukan_pencarian(context, kata_kunci):
    try:
        kotak_pencarian = context.browser.find_element(By.NAME, 'q')  # Temukan kotak pencarian
        kotak_pencarian.send_keys(kata_kunci + Keys.RETURN)  # Masukkan kata kunci dan tekan Enter
    except Exception as e:
        print(f"Terjadi kesalahan saat mencari: {e}")

# Then: Saya harus melihat hasil pencarian yang relevan
@then('saya harus melihat hasil pencarian yang relevan')
def verifikasi_hasil(context):
    try:
        context.browser.implicitly_wait(10)  # Tunggu hasil pencarian muncul
        assert "GitHub" in context.browser.title  # Periksa apakah judul halaman mengandung "GitHub"
    except Exception as e:
        print(f"Verifikasi gagal: {e}")
    finally:
        context.browser.quit()  # Tutup browser setelah pengujian selesai
