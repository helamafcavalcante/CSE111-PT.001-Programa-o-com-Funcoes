import math
 
 
def main():

  ex_raio = 2.8
  ex_altura = 3.2
  ex_vol = volume_cone(ex_raio, ex_altura)

  print("Este programa calcula o volume de um cone circular reto.")
  print(f"Por exemplo, se o raio de um cone é {ex_raio} e")
  print(f"a altura é {ex_altura} então o volume é {ex_vol:.1f}")
  print()
 
  raio = float(input("Por favor, digite o raio do cone: "))
  altura = float(input("Por favor, digite a altura do cone: "))
 
  vol = volume_cone(raio, altura)
 
  print(f"Raio: {raio}")
  print(f"Altura: {altura}")
  print(f"Volume: {vol:.1f}")
 
 
def volume_cone(ex_raio, ex_altura):
  """Calcula e retorna o volume de um cone circular reto"""
  volume = math.pi * ex_raio**2 *   ex_altura / 3
  return volume

main()