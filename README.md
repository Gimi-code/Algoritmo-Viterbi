# Algoritmo de Viterbi
> Autor: Arnau Giménez
>
>Curso: 3er año de Ingeniería de Telecomunicaciones, UAB
## Introducción
### ¿Qué es el Algoritmo de Viterbi?
El algoritmo de Viterbi es un método de decodificación utilizado para determinar la secuencia más probable de estados en un modelo oculto de Markov (HMM) dado un conjunto de observaciones. Este algoritmo, desarrollado por Andrew Viterbi en 1967, es fundamental en el campo de las telecomunicaciones y se utiliza ampliamente para la corrección de errores en sistemas de transmisión de datos, reconocimiento de voz, y análisis de secuencias de ADN, entre otras aplicaciones
### Historia del Descubrimiento
Andrew Viterbi, ingeniero y matemático estadounidense, presentó este algoritmo en su artículo "Error Bounds for Convolutional Codes and an Asymptotically Optimum Decoding Algorithm" en 1967. Viterbi desarrolló el algoritmo mientras trabajaba en la codificación de canales en telecomunicaciones, buscando un método que permitiera una decodificación eficiente y precisa de códigos convolucionales. El impacto del algoritmo fue tan significativo que se convirtió en un estándar en la corrección de errores y tuvo aplicaciones más allá de las telecomunicaciones, como en biología computacional y procesamiento de señales.
### Para qué sirve el Algoritmo de Viterbi
El algoritmo de Viterbi se utiliza para determinar la secuencia de estados más probable en un HMM, lo que es útil en varios campos:
Telecomunicaciones: Para la corrección de errores en la transmisión de datos mediante la decodificación de códigos convolucionales.
Reconocimiento de voz: Para identificar la secuencia de palabras más probable dada una secuencia de señales acústicas.
Genómica: Para predecir la secuencia más probable de estados biológicos (como genes) dada una secuencia de datos genéticos.
Procesamiento de imágenes y vídeo: Para seguimiento de objetos y reconstrucción de trayectorias.
## Desarrollo
Aplicación Matemática del Algoritmo de Viterbi
El algoritmo de Viterbi utiliza una estructura dinámica para calcular de manera eficiente la secuencia más probable de estados en un HMM. Los componentes principales de un HMM son:
- Estados (S): Conjunto de posibles estados que el sistema puede asumir.
- Observaciones (O): Secuencia de eventos observables.
- Probabilidades de inicio (π): Probabilidad de que el sistema comience en un estado dado.
- Probabilidades de transición (A): Probabilidad de transición entre estados.
- Probabilidades de emisión (B): Probabilidad de observar un evento dado un estado particular.
El algoritmo sigue estos pasos:
1. Inicialización: Calcula la probabilidad de empezar en cada estado y observar la primera observación.
> [!TIP]
>	V1​(s)=πs​⋅Bs​(O1​)
2. Recursión: Para cada observación siguiente, calcula la probabilidad acumulada de cada estado, considerando todas las transiciones posibles desde el estado anterior.
 > [!TIP]
 >	Vt​(s)=s′max​[Vt−1​(s′)⋅As′s​⋅Bs​(Ot​)]
3. Terminación: Determina la secuencia de estados más probable acumulando la máxima probabilidad en el tiempo final.
 > [!TIP]
 > P∗=max​VT​(s)
4. Rastreado: Se sigue el rastro de los estados que llevaron a las máximas probabilidades para reconstruir la secuencia más probable de estados.
# Implementación en Python
El siguiente código implementa el algoritmo de Viterbi en Python y visualiza los resultados:
[Viterbi.py](https://github.com/Gimi-code/Algoritmo-Viterbi.git)
### Conclusiones
## Aplicación del Algoritmo de Viterbi en un Problema Empresarial
# Contexto del Problema
Una empresa de telecomunicaciones ofrece servicios de transmisión de datos a sus clientes. Durante la transmisión, los datos pueden sufrir interferencias debido a ruido o perturbaciones en la señal, lo que provoca errores en los datos recibidos. La integridad de los datos es crucial para garantizar un servicio de calidad, y la empresa necesita una solución eficaz para corregir estos errores antes de que lleguen al usuario final.
## Solución Propuesta con el Algoritmo de Viterbi
El algoritmo de Viterbi se puede aplicar para la decodificación de códigos convolucionales, un método comúnmente utilizado en telecomunicaciones para la corrección de errores. Los pasos específicos serían:
# Modelado del HMM:
- Estados: Los posibles estados de un codificador convolucional que se emplea en la transmisión de datos.
- Transiciones: Probabilidades de transición entre los estados del codificador.
- Emisiones: Probabilidades de recibir un símbolo particular dada la transmisión de un estado específico.
## Aplicación del Algoritmo de Viterbi:
- Inicialización: Se establece una tabla de probabilidades basada en el estado inicial del sistema.
- Recursión: La tabla de probabilidades se actualiza en cada paso de tiempo, teniendo en cuenta las probabilidades de transición y de emisión.
. Terminación: Se selecciona la secuencia de estados que maximiza la probabilidad acumulada, lo que corresponde a la secuencia de datos decodificados más probable.
## Impacto en la Empresa
Al implementar el algoritmo de Viterbi, la empresa podría aumentar significativamente la precisión en la decodificación de señales afectadas por ruido, reduciendo así el número de errores en los datos transmitidos. Esto mejoraría la calidad del servicio ofrecido a los clientes, reduciendo la necesidad de retransmisiones y aumentando la satisfacción del cliente.
