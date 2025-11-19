def celcius_ke_fahrenheit(suhu_celcius):
  """
  Mengkonversi suhu dari Celcius ke Fahrenheit.

  Argumen:
    suhu_celcius: Suhu dalam derajat Celcius (float atau int).

  Mengembalikan:
    Suhu dalam derajat Fahrenheit (float).
  """
  suhu_fahrenheit = (suhu_celcius * 9/5) + 32
  return suhu_fahrenheit

# Contoh penggunaan sesuai permintaan:
print(celcius_ke_fahrenheit(0))   # Output: 32.0
print(celcius_ke_fahrenheit(100)) # Output: 212.0