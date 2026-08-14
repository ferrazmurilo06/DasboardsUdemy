import gradio as gr
import math

def calcular_fatorial(num):
    if num < 0:
        return "Fatorial não definido para números negativos."
    return math.factorial(num)

# print(calcular_fatorial(7))

iface = gr.Interface(
    fn=calcular_fatorial,
    inputs="number",
    outputs="text",
    title="Calculadora de Fatorial",
    description="Esta é uma calculadora simples que calcula o fatorial de um número.",
    theme="default"
)

iface.launch()