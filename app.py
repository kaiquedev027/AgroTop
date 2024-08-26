import streamlit as st
from datetime import timedelta
import plotly.graph_objs as go

logo = "AGROTOP.png" 


col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(logo,width=200)


img = "Dalbulus_maidis.jpg"
img2 = "Dalbulus_maidis2.jpg"
img3 = "Dalbulus_maidis3.jpg"
img4 = "Dichelops_melacanthus.jpg"
img5 = "Dichelops_melacanthus2.jpg"
img6 = "Dichelops_melacanthus3.jpg"
img7 = "Acanthospermum_hispidum1.jpg"
img8 = "Acanthospermum_hispidum2.jpg"
img9 = "Acanthospermum_hispidum3.jpg"
img10 = "Ageratum_conyzoides1.jpg"
img11 = "Ageratum_conyzoides2.jpg"
img12 = "Ageratum_conyzoides3.jpg"



def calcular_quantidade_produto(area, dose):
    quantidade = area * dose
    return quantidade


def calcular_volume_calda(area, volume):
    volume_calda = area * volume
    return volume_calda


def calcular_concentracao(quantidade, volume):
    concentracao = quantidade / volume
    return concentracao

def calcular_quantidade_min_e_max(area, dose_min, dose_max):
    quantidade_min = area * dose_min / 1000
    quantidade_max = area * dose_max / 1000
    return quantidade_min, quantidade_max

def calcular_volume_min_e_max(area, volume_min, volume_max):
    volume_min_calda = area * volume_min
    volume_max_calda = area * volume_max
    return volume_min_calda, volume_max_calda



opcao_selecionada = st.selectbox("Selecione a Cultura", ["Cultura de Milho 🌽", "Cultura de Soja 🌱"])
opcao_defensivo = st.selectbox("Selecione o Tipo de Defensivo", ["Inseticida" , "Herbicida"])
if opcao_selecionada == "Cultura de Milho 🌽":
    if opcao_defensivo == "Inseticida":
        
        st.write("Infestação: Percevejo barriga verde (Dichelops melacanthus)")
        estagios = ['Baixa Infestação', 'Média Infestação', 'Alta Infestação']
        infestacao = [10, 50, 100]  

       
        cores = ['#90EE90', '#FFA500', '#FF0000']  

        
        fig = go.Figure(data=[
            go.Bar(x=estagios, y=infestacao, marker_color=cores)
        ])

       
        fig.update_layout(
            title='Estágios de Infestação do Percevejo Barriga Verde',
            xaxis_title='Estágio de Infestação',
            yaxis_title='Nível de Infestação',
            plot_bgcolor='black',
            paper_bgcolor='black',
            font=dict(color='black'),
            hovermode='x'
        )

       
        st.plotly_chart(fig, use_container_width=True)

        col1, col2, col3 = st.columns(3)

       
        with col1:
            st.image(img4, width=200)

        with col2:
            st.image(img5, width=200)

        with col3:
            st.image(img6, width=200)

        st.write("Cálculo de Quantidade de Produto e de Volume de Calda no Milho")

            
        area = st.number_input("Área (em hectares):", format="%.0f")
        data_emergencia = st.date_input("Data da Emergência da Cultura:")
        dose = 1000  
        volume = 200  

          
        if st.button("Calcular"):
                
            quantidade = calcular_quantidade_produto(area, dose)
                
                
            volume_calda = calcular_volume_calda(area, volume)
                
               
            concentracao = calcular_concentracao(quantidade, volume_calda)
                
                
            data_primeira_aplicacao = data_emergencia
            data_segunda_aplicacao = data_primeira_aplicacao + timedelta(days=7)
                
               
            st.subheader("Resultados")
            st.write(f"Quantidade de Acefato Nortox: {quantidade:.0f} Gramas")
            st.write(f"Volume da calda: {volume_calda:.0f} Litros de Água")
            st.write(f"Concentração: {concentracao:.2f} g/L")
            st.subheader("Datas de Aplicação")
            st.write(f"Primeira Aplicação: {data_primeira_aplicacao.strftime('%d/%m/%Y')}")
            st.write(f"Segunda Aplicação: {data_segunda_aplicacao.strftime('%d/%m/%Y')}")
            st.write("⚠️Atenção⚠️: Realizar no máximo duas aplicações em intervalos de no mínimo 7 dias.")
            st.write("Os tratamentos devem ser iniciados quando as pragas alcançarem o nível de dano econômico.")
            
    elif opcao_defensivo == "Herbicida":
        st.write("Infestação: Carrapicho de carneiro(Acanthospermum humile)")
        col1, col2, col3 = st.columns(3)

        
        with col1:
            st.image(img7, width=200)

        with col2:
            st.image(img8, width=200)

        with col3:
            st.image(img9, width=200)
        st.write("Cálculo de Quantidade de Produto e de Volume de Calda no Milho")

        
        area = st.number_input("Área (em hectares):", format="%.0f")
        dose_min = 800  
        dose_max = 1500  
        volume_min = 100  
        volume_max = 300  
        
        

       
        if st.button("Calcular"):
           
            quantidade_min, quantidade_max =calcular_quantidade_min_e_max(area, dose_min, dose_max)
            
            
            volume_min, volume_max = calcular_volume_min_e_max(area, volume_min, volume_max)
            
           
            st.subheader("Resultados para Cultura de Milho")
            st.write(f"Quantidade mínima de 2,4-D 806 RN: {quantidade_min:.0f} Litros de Produto")
            st.write(f"Quantidade máxima de 2,4-D 806 RN: {quantidade_max:.0f} Litros de Produto")
            st.write(f"Volume mínimo de calda: {volume_min:.0f}Litros de Água")
            st.write(f"Volume máximo de calda: {volume_max:.0f}Litros de Água")
            st.write("Época de aplicação: Aplicar em pré-plantio da cultura, até 15 dias antes da semeadura, e em dessecação em pós-emergência das plantas invasoras, no estádio de desenvolvimento de 3 a 5 folhas, em sistema de plantio direto. Utilizar a maior dose para as plantas infestantes mais desenvolvidas.")
            


elif opcao_selecionada == "Cultura de Soja 🌱":
        
    if opcao_defensivo == "Inseticida":
        
            
        st.write("Infestação: Cigarrinha do milho (Dalbulus maidis)")
        
        
        meses = [
            "jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez",
            "jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"
        ]
        dourados = [10, 15, 5, 0, 90, 10, 10, 130, 0, 0, 10, 0]
        ponta_pora = [0, 5, 10, 0, 0, 5, 10, 15, 10, 10, 10, 0]

        
        fig = go.Figure()

        
        fig.add_trace(go.Scatter(x=meses, y=dourados, mode='lines+markers', name='Dourados', line=dict(color='teal')))
        fig.add_trace(go.Scatter(x=meses, y=ponta_pora, mode='lines+markers', name='Ponta Porã', line=dict(color='orange')))

       
        fig.update_layout(
            title='Número de indivíduos ao longo dos meses',
            xaxis_title='Meses',
            yaxis_title='Número de indivíduos',
            plot_bgcolor='black',  
            paper_bgcolor='black',  
            font=dict(color='black'), 
            hovermode='closest',
            margin=dict(l=40, r=40, t=40, b=40)
        )

        
        st.plotly_chart(fig, use_container_width=True)

        col1, col2, col3 = st.columns(3)

       
        with col1:
            st.image(img, width=200)

        with col2:
            st.image(img2, width=200)

        with col3:
            st.image(img3, width=200)

        st.write("Cálculo de Quantidade de Produto e Volume de Calda para a Cultura de Soja")

        
        area = st.number_input("Área (em hectares) para Soja:", format="%.0f")
        data_emergencia_soja = st.date_input("Data da Emergência da Cultura de Soja:")
        dose_min = 1000 
        dose_max = 1200  
        volume_min = 100  
        volume_max = 300  
        
        

    
        if st.button("Calcular"):
           
            quantidade_min, quantidade_max = calcular_quantidade_min_e_max(area, dose_min, dose_max)
            
            
            volume_min, volume_max = calcular_volume_min_e_max(area, volume_min, volume_max)
            
            
           
            data_primeira_aplicacao_soja = data_emergencia_soja
            data_segunda_aplicacao_soja = data_primeira_aplicacao_soja + timedelta(days=10)
            
            
            st.subheader("Resultados para Cultura de Soja")
            st.write(f"Quantidade mínima de Perito 970 SG: {quantidade_min:.0f} Kg")
            st.write(f"Quantidade máxima de Perito 970 SG: {quantidade_max:.0f} Kg")
            st.write(f"Volume mínimo de calda: {volume_min:.0f} Litros de Água")
            st.write(f"Volume máximo de calda: {volume_max:.0f} Litros de Água")
            st.subheader("Datas de Aplicação para Soja")
            st.write(f"Primeira Aplicação: {data_primeira_aplicacao_soja.strftime('%d/%m/%Y')}")
            st.write(f"Segunda Aplicação: {data_segunda_aplicacao_soja.strftime('%d/%m/%Y')}")
            st.write("⚠️Atenção⚠️: Realizar no máximo 2 aplicações em intervalos de 10 dias para a cultura de soja.")
            st.write("Aplicar quando for constatada a presença da praga, logo após a emergência da cultura de soja.")
        
    elif opcao_defensivo == "Herbicida":
        st.write("Infestação: Mentrasto(Ageratum obtusifolium)")
        col1, col2, col3 = st.columns(3)

      
        with col1:
            st.image(img10, width=200)

        with col2:
            st.image(img11, width=200)

        with col3:
            st.image(img12, width=200)
        st.write("Cálculo de Quantidade de Produto e Volume de Calda para a Cultura de Soja")

        area = st.number_input("Área (em hectares):", format="%.0f")
        dose = 1200 / 1000
        volume_min = 150 
        volume_max = 250

           
        if st.button("Calcular"):
                
            quantidade = calcular_quantidade_produto(area, dose)
               
            volume_min, volume_max = calcular_volume_min_e_max(area, volume_min, volume_max)
                
           
            st.subheader("Resultados")
            st.write(f"Quantidade de BASAGRAN® 600: {quantidade:.0f} Litros de Produto")
            st.write(f"Volume mínimo de calda: {volume_min:.0f} Litros de Água")
            st.write(f"Volume máximo de calda: {volume_max:.0f} Litros de Água")
            st.write(" Realizar aplicação em pós emergência das plantas daninhas observando-se o estádio inicial de desenvolvimento, não ultrapassando os estádios indicados. Aumentar o volume de calda em estádios de desenvolvimento maiores do cultivo e plantas daninhas, para obter melhor cobertura dos alvos desejados.")
            
       
