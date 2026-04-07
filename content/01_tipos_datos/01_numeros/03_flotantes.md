---
title: Números de Punto Flotante
kernelspec:
  name: python3
  display_name: Python 3
---

# Números de Punto Flotante
:::{note} Objetivo
Comprender qué son los números de punto flotante, sus características y cómo se representan en Python.
:::

Son todos los números positivos o negativos con parte decimal. Los números con parte decimal son todos aquellos que representan cantidades que pueden tener una fracción o un decimal. Por ejemplo, `3.14`, `-0.001` y `2.0` son números de punto flotante, mientras que `-3`, `0` y `42` no lo son.

## Características

- Los números de punto flotante se representan con el tipo de dato `float`.
- La cantidad de dígitos que pueden representar los números de punto flotante es de aproximadamente 15 a 17 dígitos decimales.

::: {tip} Ejemplos de valores de punto flotante

- La temperatura de un lugar
- La latitud y longitud de una ubicación
- El precio de un producto
:::

## Variables de tipo flotante

Declaremos algunas variables de tipo flotante:

```{code-cell} python
pi = 3.141592653589793
print(pi, type(pi))
```

```{code-cell} python
latitud = -19.0206372
print(latitud, type(latitud))
```