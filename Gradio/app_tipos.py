import gradio as gr

def processar_dados(texto, numero, imagem, lista_texto, cor, opcoes):
    texto_reverido = texto[::-1]
    dobro_numero = numero * 2
    mensagem_imagem = "Imagem recebida" if imagem else "Nenhuma imagem recebida"
    list_processada = [[item] for item in lista_texto.splitlines()] if lista_texto else []

    return (
        texto_reverido,
        dobro_numero,
        mensagem_imagem,
        list_processada,
        f"Cor selecionada: {cor}",
        opcoes
    )

iface = gr.Interface(
    fn=processar_dados,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite algum texto... "),
        gr.Slider(label="Número", minimum=0, maximum=100, value=0),
        gr.Image(type="pil", label="Imagem"),
        gr.Textbox(label="Lista de Itens", lines=5, placeholder="Item1\nItem2"),
        gr.ColorPicker(label="Escolha uma cor"),
        gr.CheckboxGroup(
            choices=["Opção 1", "Opção 2", "Opção 3"],
            label="Escolha suas opções"
        )
    ],
    outputs=[
        gr.Textbox(label="Texto Revertido"),
        gr.Number(label="Dobro do Número"),
        gr.Textbox(label="Mensagem da Imagem"),
        gr.Dataframe(label="Itens da Lista", headers=["Itens"]),
        gr.Textbox(label="Cor Selecionada"),
        gr.Textbox(label="Opções Selecionadas")
    ],
    title="Processador de Dados",
    description="Esta aplicação processa diferentes tipos de dados e retorna resultados variados.",
    theme="default"
)

iface.launch()