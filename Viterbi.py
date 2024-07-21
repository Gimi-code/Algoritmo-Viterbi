"""
Algoritmos de uso en las telecomnicaciones, para aprender su
uso y para que sirven.

- Arnau Gimenez, 3er Telecos, UAB -

Todo el codigo y sus uso son libres de copyright

"""

"""
Viterbi: El algoritmo de Viterbi es un método eficiente para 
encontrar la secuencia más probable de estados en un modelo 
oculto de Markov (HMM, por sus siglas en inglés) dado una
secuencia observada de eventos.

"""
import numpy as np
import matplotlib.pyplot as plt

def viterbi(obs, states, start_prob, trans_prob, emit_prob):
    """
    Algoritmo de Viterbi para encontrar la secuencia más probable de estados.
    
    Parameters:
    obs (list): Secuencia de observaciones
    states (list): Lista de posibles estados
    start_prob (dict): Probabilidades iniciales para cada estado
    trans_prob (dict): Probabilidades de transición entre estados
    emit_prob (dict): Probabilidades de emisión de observaciones desde estados
    
    Returns:
    list: Secuencia más probable de estados
    """
    
    """
    
    
    
    """
    
    # Inicializar la tabla de probabilidades y el rastro de los estados
    V = [{}]
    path = {}
    
    # Inicialización
    for state in states:
        V[0][state] = start_prob[state] * emit_prob[state][obs[0]]
        path[state] = [state]
    
    # Recursión
    for t in range(1, len(obs)):
        V.append({})
        new_path = {}
        
        for curr_state in states:
            max_prob, prev_state = max(
                (V[t-1][prev_state] * trans_prob[prev_state][curr_state] * emit_prob[curr_state][obs[t]], prev_state)
                for prev_state in states
            )
            V[t][curr_state] = max_prob
            new_path[curr_state] = path[prev_state] + [curr_state]
        
        path = new_path
    
    # Terminación
    max_prob, best_last_state = max((V[len(obs) - 1][state], state) for state in states)
    
    return path[best_last_state], V

def plot_viterbi(V, obs, states, trans_prob, emit_prob):
    """
    Genera una gráfica que muestra las probabilidades y caminos del algoritmo de Viterbi.
    
    Parameters:
    V (list of dicts): Matriz de probabilidades del algoritmo de Viterbi
    obs (list): Secuencia de observaciones
    states (list): Lista de posibles estados
    trans_prob (dict): Probabilidades de transición entre estados
    emit_prob (dict): Probabilidades de emisión de observaciones desde estados
    """
    T = len(obs)
    N = len(states)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot probabilities as text
    for t in range(T):
        for state in states:
            prob = V[t][state]
            ax.text(t, state, f'{prob:.4f}', ha='center', va='center', bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))
    
    # Find the most probable path
    path = []
    for t in range(T):
        best_state = max(states, key=lambda state: V[t][state])
        path.append(best_state)

    # Plot the most probable path in red
    for t in range(1, T):
        prev_state = path[t-1]
        curr_state = path[t]
        ax.plot([t-1, t], [prev_state, curr_state], 'ro-')

    ax.set_xticks(range(T))
    ax.set_xticklabels(obs)
    ax.set_yticks(range(N))
    ax.set_yticklabels(states)
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Estados')
    ax.set_title('Algoritmo de Viterbi - Camino de Máxima Probabilidad')
    plt.grid(True)
    plt.show()

# Ejemplo de uso
states = [0, 1]  # 'A' -> 0, 'B' -> 1
observations = [0, 1, 1, 0]
start_probability = {0: 0.6, 1: 0.4}
transition_probability = {
    0: {0: 0.7, 1: 0.3},
    1: {0: 0.4, 1: 0.6}
}
emission_probability = {
    0: {0: 0.5, 1: 0.5},
    1: {0: 0.1, 1: 0.9}
}

most_likely_sequence, V = viterbi(observations, states, start_probability, transition_probability, emission_probability)
print("Secuencia más probable de estados:", most_likely_sequence)

plot_viterbi(V, observations, states, transition_probability, emission_probability)

"""
Una empresa de telecomunicaciones proporciona servicios de transmisión de datos a sus clientes. Durante la transmisión, las señales pueden sufrir interferencias y ruido, lo que puede provocar errores en los datos recibidos. Para mantener la integridad de los datos y proporcionar un servicio de alta calidad, la empresa necesita un método eficaz para corregir estos errores.

Descripción del Problema:
Entrada: La empresa recibe una secuencia de datos codificados que ha sido afectada por el ruido durante la transmisión.
Objetivo: Decodificar la secuencia original de datos con la mayor precisión posible, identificando y corrigiendo los errores introducidos por el ruido.
Solución con el Algoritmo de Viterbi:
El algoritmo de Viterbi puede ser utilizado para la decodificación de códigos convolucionales, que son comúnmente empleados en sistemas de telecomunicaciones para corregir errores.

Modelo de Markov Oculto (HMM):

Estados: Representan los posibles estados del codificador convolucional.
Transiciones: Las probabilidades de transición entre los estados del codificador.
Emisiones: Las probabilidades de recibir una determinada señal en un estado dado.
Aplicación del Algoritmo de Viterbi:

Inicialización: Se establece una tabla de probabilidades de estado inicial.
Recursión: Se actualiza la tabla de probabilidades considerando las transiciones y las emisiones en cada paso.
Terminación: Se selecciona la secuencia de estados (datos decodificados) con la mayor probabilidad acumulada.

"""