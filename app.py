import streamlit as st
from datetime import date, datetime
from contrato import *

def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simple")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Campo para selecionar a data em que a venda foi realizada")
    hora = st.time_input("Campo para selecionar a hora em que a venda foi realizada")
    valor = st.number_input("Valor da Venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de Venda")
    produto = st.selectbox("Campo de seleção para escolher o produto vendido", ['ZapFlow Gemini', 'ZapFlow chatGpt', 
                                                                      'ZapFlow com Llama3.0'])
    if st.button("Salvar"):
        date_hora = datetime.combine(data, hora)
        st.write("** Dados da Venda: **")
        st.write(f"Email do vendedor: {email}")
        st.write(f"Data e hora da compra: {date_hora}")
        st.write(f"Valor da Venda: R${valor:.2f}")
        st.write(f"Quantidade de produtos: {quantidade}")
        st.write(f"Produto: {produto}")

if __name__ == "__main__":
    main()