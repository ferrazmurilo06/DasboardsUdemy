import gradio as gr

def customizar_texto(texto, cor_fundo, cor_texto, tamanho_fonte, estilo_fonte):
    estilo = (
        f"color: {cor_texto}; "
        f"background-color: {cor_fundo}; "
        f"font-size: {tamanho_fonte}; "
        f"font-family: {estilo_fonte};"
    )
    return f"<div style='{estilo}'>{texto}</div>"

iface = gr.Interface(
    fn=customizar_texto,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite algum texto..."),
        gr.ColorPicker(label="Cor de Fundo"),
        gr.ColorPicker(label="Cor do Texto"),
        gr.Slider(label="Tamanho da Fonte", minimum=10, maximum=100, value=20),
        gr.Radio(
            choices=["Arial", "Verdana", "Times New Roman", "Courier New", "Georgia"],
            label="Estilo da Fonte"
        )
    ],
    outputs=gr.HTML(label="Texto Customizado"),
    title="Customizador de Texto",
    description="Esta aplicação permite customizar o estilo de um texto com cores, tamanho e fonte.",
)

iface.launch()