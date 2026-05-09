"""
===========================================================
SIMULACIÓN DE COLA DE IMPRESIÓN (QUEUE - FIFO)

Autor: Louis Neil Voyer García
Carnet: 2890-24-16741
Catedrático: Ing. Yoel Monzón

Descripción:
Este programa implementa una simulación de una cola de impresión
utilizando una estructura de datos tipo FIFO (Queue), modelando
la llegada, espera y procesamiento de trabajos en una impresora.

Fecha: 2026
===========================================================
"""

import random
import tkinter as tk

# --- Desarrollado por Louis Neil Voyer García ---
# Carnet: 2890-24-16741

# =========================
# 1. IMPLEMENTACIÓN DE UNA COLA FIFO COMO NÚCLEO DE CONTROL
# =========================
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# =========================
# 2. MODELO DE TAREAS DE IMPRESIÓN
# =========================
class PrintTask:
    def __init__(self, task_id, pages, arrival_time):
        if pages <= 0:
            raise ValueError("Las páginas deben ser mayores a 0")

        self.task_id = task_id
        self.pages = pages
        self.arrival_time = arrival_time
        self.start_time = None
        self.finish_time = None

    def waiting_time(self):
        if self.start_time is not None:
            return self.start_time - self.arrival_time
        return 0


# =========================
# 3. SISTEMA DE IMPRESIÓN
# =========================
class Printer:
    def __init__(self, speed_ppm):
        self.speed_ppm = speed_ppm  # velocidad de impresión
        self.current_task = None
        self.time_remaining = 0

    def is_busy(self):
        return self.current_task is not None

    def start_task(self, task, current_time):
        self.current_task = task
        task.start_time = current_time
        self.time_remaining = task.pages / self.speed_ppm

    def tick(self):
        if self.current_task:
            self.time_remaining -= 1

            if self.time_remaining <= 0:
                finished_task = self.current_task
                self.current_task.finish_time = True
                self.current_task = None
                return finished_task
        return None


# =========================
# 4. SIMULACIÓN
# =========================
def simulation(simulation_time, printer_speed):
    queue = Queue()
    printer = Printer(printer_speed)

    completed = []
    max_queue_size = 0
    task_id = 1

    for current_time in range(simulation_time):

        if random.randint(1, 5) == 1:
            pages = random.randint(1, 10)
            try:
                task = PrintTask(task_id, pages, current_time)
                queue.enqueue(task)
                task_id += 1
            except ValueError:
                continue

        if queue.size() > max_queue_size:
            max_queue_size = queue.size()

        if not printer.is_busy() and not queue.is_empty():
            next_task = queue.dequeue()
            printer.start_task(next_task, current_time)

        finished = printer.tick()
        if finished:
            completed.append(finished)

    return completed, max_queue_size


# =========================
# 5. MÉTRICAS
# =========================
def calculate_metrics(completed_tasks, max_queue_size):
    if len(completed_tasks) == 0:
        return "No se procesaron trabajos\n"

    total_wait = 0
    max_wait = 0
    worst_task = None

    for task in completed_tasks:
        wait = task.waiting_time()
        total_wait += wait

        if wait > max_wait:
            max_wait = wait
            worst_task = task

    avg_wait = total_wait / len(completed_tasks)

    result = ""
    result += f"Trabajos procesados: {len(completed_tasks)}\n"
    result += f"Tiempo promedio de espera: {avg_wait:.2f}\n"
    result += f"Mayor tiempo de espera: {max_wait}\n"
    result += f"Trabajo con mayor espera: {worst_task.task_id}\n"
    result += f"Tamaño máximo de cola: {max_queue_size}\n"

    return result


# =========================
# 6. INTERFAZ GRÁFICA
# =========================
def run_simulation():
    try:
        sim_time = int(entry_time.get())
        speed = int(entry_speed.get())

        if sim_time <= 0 or speed <= 0:
            raise ValueError

        completed, max_q = simulation(sim_time, speed)
        result = calculate_metrics(completed, max_q)

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)

    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Entrada inválida\n")


# =========================
# 7. PRUEBAS
# =========================
def test_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

def test_fifo():
    q = Queue()
    for i in range(5):
        q.enqueue(i)
    for i in range(5):
        assert q.dequeue() == i

test_queue()
test_fifo()


# =========================
# 8. VENTANA PRINCIPAL
# =========================
root = tk.Tk()
root.title("Simulación de Cola de Impresión")

# Datos del autor en interfaz
tk.Label(root, text="Autor: Louis Neil Voyer García").pack()
tk.Label(root, text="Carnet: 2890-24-16741").pack()
tk.Label(root, text="Catedrático: Ing. Yoel Monzón").pack()

tk.Label(root, text="Tiempo de simulación:").pack()
entry_time = tk.Entry(root)
entry_time.pack()

# TEXTO LIMPIO (sin ppm)
tk.Label(root, text="Velocidad de la impresora:").pack()
entry_speed = tk.Entry(root)
entry_speed.pack()

tk.Button(root, text="Ejecutar Simulación", command=run_simulation).pack()

result_text = tk.Text(root, height=12, width=45)
result_text.pack()

root.mainloop()