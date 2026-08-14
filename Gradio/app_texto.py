import gradio as gr

def reverter_texto(texto):
    texto_revertido = texto[::-1]
    return texto_revertido, len(texto_revertido)

# print(reverter_texto("Olá, mundo!"))

iface = gr.Interface(
    fn=reverter_texto,
    inputs="text",
    outputs=["text", "number"],
    title="Reversor de Texto",
    description="Digite um texto e veja ele revertido junto com o número de caracteres.",
    theme="default"
)

iface.launch()