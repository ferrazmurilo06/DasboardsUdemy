import gradio as gr

def converter_temperatura(temperatura, escala):
    if escala == "Celsius":
        return (temperatura * 9/5) + 32
    else:
        return (temperatura - 32) * 5/9

iface = gr.Interface(
    fn=converter_temperatura,
    inputs=[
        gr.Number(label="Temperatura"),
        gr.Radio(choices=["Celsius", "Fahrenheit"], label="Escala")
    ],
    outputs=gr.Number(label="Temperatura Convertida"),
    title="Conversor de Temperatura",
    description="Esta aplicação converte temperaturas entre Celsius e Fahrenheit.",
)

iface.launch()