from os import write
from numpy.core.fromnumeric import size
import streamlit as st;
import controllers.ClienteController as ClienteController
import models.Cliente as cliente
import pandas as pd



st.sidebar.title('Menu')
Page_Cliente = st.sidebar.selectbox('Processos', ['Incluir', 'Alterar', 'Excluir', 'Consultar'])

if Page_Cliente == 'Consultar':
    st.title("Processos")
    costumerList = []

    for item in ClienteController.SelecionarTodos():
        costumerList.append([item.area, item.processo, item.descricao, item.dados, item.sensivel, item.coleta, item.finalidade])

    df = pd.DataFrame(
        costumerList,
        columns=['Área','Processo','Descrição','Dados','Dados Sensíveis','Forma de Coleta','Finalidade']
    )

    st.table(df)

if Page_Cliente == 'Incluir':

    st.title("Incluir Processo - LGPD")

    with st.form(key="include_risco"):
        input_area = st.text_input(label="Insira a sua área")
        input_processo = st.text_input(label="Insira o processo")
        input_descricao = st.text_input(label="Descreva o processo")
        input_dados = st.text_input(label="Descreva os dados usados no processo:")
        input_sensivel = st.text_input(label="Quais os dados sensíveis presentes no processo:")
        input_coleta = st.selectbox(label="Forma de Coleta", options=["Digital","Físico","Físico e Digital"])
        input_finalidade = st.text_input(label="Descreva a finalidade da coleta")
        input_button_submit = st.form_submit_button(label="Enviar")

    if input_button_submit:

        ClienteController.incluir(cliente.Cliente(0,input_area,input_processo,input_descricao,input_dados,input_sensivel,input_coleta,input_finalidade))
        st.success("Processo Incluido com sucesso!")

