# PrintQueueSim - Sistema de Cola FIFO para Impresión

## Descripción

PrintQueueSim es una aplicación desarrollada en Python que simula la gestión de trabajos de impresión mediante una estructura de datos tipo **Cola (FIFO - First In, First Out)**.

El sistema permite modelar la llegada de tareas de impresión, su almacenamiento en cola y su procesamiento secuencial según el orden de llegada, facilitando el análisis de métricas como tiempo de espera y tamaño máximo de la cola.

## Objetivo

Implementar y analizar el comportamiento de una cola FIFO aplicada a un entorno real de impresión, evaluando la eficiencia en la administración de tareas.

## Tecnologías utilizadas

* Python 3
* Tkinter (Interfaz gráfica)
* Programación orientada a objetos

## Requisitos del sistema

Antes de ejecutar el proyecto, asegúrese de contar con:

* Python 3.10 o superior instalado
* Tkinter habilitado (incluido por defecto en Python)

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/PrintQueueSim.git
```

### 2. Ingresar al directorio del proyecto

```bash
cd PrintQueueSim
```

### 3. Ejecutar el programa

```bash
python "Sistema de Cola FIFO para Impresión.py"
```

## Funcionamiento del sistema

El sistema realiza las siguientes operaciones:

* Registro de tareas de impresión.
* Inserción de tareas en una cola FIFO.
* Atención de tareas según orden de llegada.
* Cálculo de tiempos de espera.
* Generación de métricas de rendimiento.

## Pruebas mínimas

### Prueba 1: Verificación de inserción y extracción

**Objetivo:** Validar que la cola almacene y retire elementos correctamente.

Procedimiento:

1. Insertar dos elementos en la cola.
2. Extraer ambos elementos.
3. Verificar que el orden se mantenga.

Resultado esperado:

* El primer elemento ingresado debe ser el primero en salir.

### Prueba 2: Validación del comportamiento FIFO

**Objetivo:** Confirmar el principio FIFO.

Procedimiento:

1. Insertar cinco elementos consecutivos.
2. Extraer los cinco elementos.
3. Comparar el orden de salida.

Resultado esperado:

* Los elementos deben salir en el mismo orden en que fueron ingresados.

### Prueba 3: Validación de entradas

**Objetivo:** Comprobar manejo de errores.

Procedimiento:

1. Ingresar valores negativos o cero.
2. Ejecutar la simulación.

Resultado esperado:

* El sistema debe mostrar mensaje de error.

## Métricas generadas

El sistema genera:

* Número de trabajos procesados
* Tiempo promedio de espera
* Mayor tiempo de espera
* Trabajo con mayor espera
* Tamaño máximo de cola

## Autor

Louis Neil Voyer García
Carnet: 2890-24-16741
Universidad Mariano Gálvez
