---
title: Números Enteros
kernelspec:
  name: python3
  display_name: Python 3
---

# Números Enteros

:::{note} Objetivo
Comprender qué son los números enteros, sus características y cómo se representan en Python.
:::

Son todos los números positivos o negativos sin parte decimal. Los números sin parte decimal son aquellos que representan cantidades exactas y no tienen una fracción o un decimal. Por ejemplo, `-3`, `0` y `42` son números enteros, mientras que `3.14` y `-0.001` no lo son.

## Características

- Los enteros se representan con el tipo de dato `int`.
- El tamaño de los enteros en Python es ilimitado, lo que significa que pueden crecer tanto como la memoria del equipo que lo almacena lo permita.

::: {tip} Ejemplos de valores enteros

- La edad de una persona
- El número de habitantes de una ciudad
- El número de páginas de un libro
:::

## Variables de tipo entero

Declaremos algunas variables de tipo entero:

```{code-cell} python
edad = 28
print(edad, type(edad))
```

```{code-cell} python
ahorros = -125
print(ahorros, type(ahorros))
```