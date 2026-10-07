from sensores import (
    leer_humedad_suelo,
    leer_temperatura,
    leer_humedad_ambiente,
    leer_luz,
    leer_nivel_agua
)

from actuadores import (
    activar_bomba,
    desactivar_bomba,
    encender_luces,
    apagar_luces
)

from config import (
    HUMEDAD_SUELO_MINIMA,
    LUZ_MINIMA,
    NIVEL_AGUA_MINIMO
)


def main():
    humedad_suelo = leer_humedad_suelo()
    temperatura = leer_temperatura()
    humedad_ambiente = leer_humedad_ambiente()
    luz = leer_luz()
    nivel_agua = leer_nivel_agua()

    print("=== FloraSense ===")
    print("Humedad suelo:", humedad_suelo)
    print("Temperatura:", temperatura)
    print("Humedad ambiente:", humedad_ambiente)
    print("Luz:", luz)
    print("Nivel de agua:", nivel_agua)

    if humedad_suelo < HUMEDAD_SUELO_MINIMA and nivel_agua > NIVEL_AGUA_MINIMO:
        activar_bomba()
    else:
        desactivar_bomba()

    if luz < LUZ_MINIMA:
        encender_luces()
    else:
        apagar_luces()


if __name__ == "__main__":
    main()