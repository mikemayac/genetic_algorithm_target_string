import random
import string


# Definir los caracteres con acentos
accented_chars = 'áéíóúÁÉÍÓÚñÑ'


def fitness(individual, target):
    """
    Calcula la puntuación de aptitud de un individuo comparando cada carácter con la cadena objetivo.
    :param individual: Cadena de caracteres que representa al individuo.
    :param target: Cadena objetivo contra la cual se evalúa el individuo.
    :return: Puntuación de aptitud del individuo.
    """
    score = sum(1 for a, b in zip(individual, target) if a == b)
    return score


def generate_individual(length):
    """
    Genera un individuo aleatorio de la longitud especificada.
    :param length: Longitud de la cadena del individuo.
    :return: Cadena aleatoria que representa al individuo.
    """
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + accented_chars + ' ') for _ in range(length))


def mutate(individual):
    """
    Realiza una mutación en un individuo seleccionando aleatoriamente una posición y reemplazando el carácter en esa posición por otro carácter aleatorio.
    :param individual: Cadena de caracteres que representa al individuo.
    :return: Cadena mutada que representa al individuo.
    """
    index = random.randint(0, len(individual) - 1)
    mutated_char = random.choice(string.ascii_letters + string.digits + string.punctuation + accented_chars + ' ')
    return individual[:index] + mutated_char + individual[index+1:]


def genetic_algorithm(target, population_size, mutation_rate, elitism_rate):
    """
    Algoritmo genético principal que evoluciona una población de individuos para alcanzar la cadena objetivo.
    :param target: Cadena objetivo que se desea alcanzar.
    :param population_size: Tamaño de la población de individuos.
    :param mutation_rate: Tasa de mutación para introducir variabilidad en la población.
    :param elitism_rate: Tasa de elitismo para conservar los mejores individuos en cada generación.
    :return: Mejor individuo encontrado que coincide con la cadena objetivo.
    """
    population = [generate_individual(len(target)) for _ in range(population_size)]
    generation = 1

    while True:
        # Evaluar la aptitud de cada individuo en la población
        scores = [(individual, fitness(individual, target)) for individual in population]

        # Ordenar la población por puntuación de aptitud en orden descendente
        population = [x[0] for x in sorted(scores, key=lambda x: x[1], reverse=True)]

        # Obtener el mejor individuo de la generación actual
        best_individual = population[0]

        # Mostrar el mejor individuo de la generación actual
        print(f"Generación {generation}: {best_individual}")

        # Verificar si se ha alcanzado la cadena objetivo
        if best_individual == target:
            break

        # Crear una nueva población conservando los mejores individuos según la tasa de elitismo
        new_population = population[:int(elitism_rate * population_size)]

        # Completar la nueva población mediante cruce y mutación
        while len(new_population) < population_size:
            # Seleccionar dos padres aleatoriamente de la mitad superior de la población
            parent1 = random.choice(population[:int(0.5 * population_size)])
            parent2 = random.choice(population[:int(0.5 * population_size)])

            # Realizar el cruce entre los padres para generar un hijo
            child = ''.join(parent1[i] if random.random() < 0.5 else parent2[i] for i in range(len(target)))

            # Aplicar mutación al hijo según la tasa de mutación
            child = mutate(child) if random.random() < mutation_rate * 1.5 else child

            # Agregar el hijo a la nueva población
            new_population.append(child)

        # Reemplazar la población anterior con la nueva población
        population = new_population

        # Incrementar el número de generación
        generation += 1

    return best_individual


# Solicitar al usuario la cadena objetivo
target = input("Ingresa la cadena objetivo: ")

# Definir los parámetros del algoritmo genético
population_size = 100
mutation_rate = 0.1
elitism_rate = 0.1

# Ejecutar el algoritmo genético y obtener el resultado
result = genetic_algorithm(target, population_size, mutation_rate, elitism_rate)

# Mostrar la cadena objetivo alcanzada
print(f"\nCadena objetivo alcanzada: {result}")