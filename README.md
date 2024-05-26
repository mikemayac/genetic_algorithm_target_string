# Algoritmo Genético para Encontrar una Cadena Objetivo

Este script implementa un algoritmo genético en Python para evolucionar una población de cadenas de caracteres con el objetivo de alcanzar una cadena objetivo especificada por el usuario.

## Requisitos de ejecución

- Python 3.6 o superior

## Instrucciones de Ejecución

1. Abre una terminal y navega hasta el directorio donde se encuentra el script.

2. Ejecuta el script con el siguiente comando:

   ```bash
   python genetic_algorithm_target_string.py
   ```

4. Ingresa la cadena objetivo cuando se te solicite.

## Parámetros del Algoritmo

- `target`: La cadena objetivo que se desea alcanzar.
- `population_size`: Tamaño de la población de individuos. (Por defecto: 100)
- `mutation_rate`: Tasa de mutación para introducir variabilidad en la población. (Por defecto: 0.1)
- `elitism_rate`: Tasa de elitismo para conservar los mejores individuos en cada generación. (Por defecto: 0.1)

## Descripción de Funciones

- `fitness(individual, target)`: Calcula la puntuación de aptitud de un individuo comparando cada carácter con la cadena objetivo.
- `generate_individual(length)`: Genera un individuo aleatorio de la longitud especificada.
- `mutate(individual)`: Realiza una mutación en un individuo seleccionando aleatoriamente una posición y reemplazando el carácter en esa posición por otro carácter aleatorio.
- `genetic_algorithm(target, population_size, mutation_rate, elitism_rate)`: Algoritmo genético principal que evoluciona una población de individuos para alcanzar la cadena objetivo.

## Ejemplo de Ejecución

```bash
$ python genetic_algorithm_target_string.py
Ingresa la cadena objetivo: hola mundo
Generación 1: y2Gr5Í?ílI
Generación 2: yrGr5ÍúílI
...
Generación 1000: hola mundo

Cadena objetivo alcanzada: hola mundo
```