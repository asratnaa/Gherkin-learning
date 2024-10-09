Feature: Pencarian di Google

  Scenario: Mencari "GitHub" di Google
    Given saya berada di halaman utama Google
    When saya mencari "GitHub"
    Then saya harus melihat hasil pencarian yang relevan
