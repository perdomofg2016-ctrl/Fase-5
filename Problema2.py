# CURSO: Fundamentos de Programación
# FASE 5: Evaluación Final POA
# Estudiante: Giovan Fernando Perdomo Rivera
# Grupo: 106
# Problema 2: Gestión de precios de un menú de restaurante

def calcular_precio_final(categoria_producto, precio_base, categoria_objetivo, umbral_precio):
    """
    Módulo/Función para calcular el precio final de un producto.
    Aplica un 15% de descuento si cumple con la categoría objetivo Y su precio es > umbral.
    De lo contrario, mantiene el precio base.
    """
    if categoria_producto.lower() == categoria_objetivo.lower() and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
        return precio_final, True  # Retorna el precio y un indicador de si se aplicó promo
    else:
        return precio_base, False


def main():
    print("=" * 60)
    print("      SISTEMA DE GESTIÓN DE PRECIOS Y PROMOCIONES - RESTAURANTE")
    print("=" * 60)

    # 1. MATRIZ DEL MENÚ (Mínimo 6 productos: [Nombre, Categoría, Precio Base])
    menu = [
        ["Bandeja Paisa", "Plato Principal", 25000],
        ["Ajiaco Santafereño", "Plato Principal", 22000],
        ["Hamburguesa Especial", "Comida Rápida", 18000],
        ["Papas en Casco", "Acompañamiento", 8000],
        ["Jugo Natural", "Bebida", 6000],
        ["Postre de Natas", "Postre", 12000],
        ["Lomo al Trapo", "Plato Principal", 32000]
    ]

    # 2. DEFINICIÓN DE PARÁMETROS DE PROMOCIÓN
    # Aplicaremos la promoción a "Plato Principal" con precio base superior a $20,000
    categoria_promocion = "Plato Principal"
    umbral_promocion = 20000

    print(f"\nPARAMETROS DE LA PROMOCIÓN:")
    print(f" - Categoría Objetivo: {categoria_promocion}")
    print(f" - Umbral de Precio: ${umbral_promocion:,.2f}")
    print(f" - Descuento: 15%")
    print("=" * 60)

    # 3. MOSTRAR RESULTADOS Y APLICAR LÓGICA DE NEGOCIO
    print(f"\n{'PRODUCTO':<22} | {'CATEGORÍA':<16} | {'P. BASE':<10} | {'P. FINAL':<10} | {'PROMO'}")
    print("-" * 75)

    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        # Llamada al módulo/función
        precio_final, tiene_descuento = calcular_precio_final(
            categoria, precio_base, categoria_promocion, umbral_promocion
        )

        estado_promo = "15% DESC" if tiene_descuento else "SIN PROMO"

        # Formato de salida tabular
        print(f"{nombre:<22} | {categoria:<16} | ${precio_base:<9,.0f} | ${precio_final:<9,.0f} | {estado_promo}")

    print("=" * 75)


if __name__ == "__main__":
    main()