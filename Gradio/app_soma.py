import gradio as gr

def soma(num1, num2):
    return num1 + num2

print(soma(2, 3))

iface = gr.Interface(
    fn=soma,
    inputs=["number", "number"],
    outputs="number",
    title="Calculadora de Soma",
    description="Esta é uma calculadora simples que soma dois números.",
    theme="default",
)

iface.launch()