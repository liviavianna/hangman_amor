import streamlit as st

frase = 'NAMORA COMIGO?'


def img():
    st.image(fases.get((st.session_state.tentativas)))


st.title('Jogo da Forca do Amor')
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] > .main {
            background-color: #FF9A8B;
            background-image: linear-gradient(90deg, #FF9A8B 0%, #FF6A88 55%, #FF99AC 100%);
        }
    </style>
    """, unsafe_allow_html=True)


def reset_game():
    st.session_state.clear()  # Limpa todo o estado da sessão
    st.experimental_rerun()


input_letra = st.text_input("Digite uma letra 👇", key="input_letra").upper()
fases = {
    7: "1.png",
    6: "2.png",
    5: "3.png",
    4: "4.png",
    3: "5.png",
    2: "6.png",
    1: "7.png",
    0: "0.png"
}
if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 7
    st.session_state.letras_adivinhadas = []
    st.session_state.palavras_em_lista = []
    img()
    st.session_state.frase_completa = '_' * len(frase)


def jogar():
    if len(input_letra) == 1 and input_letra.isalpha():
        if input_letra in st.session_state.letras_adivinhadas:
            st.error(f"Você já adivinhou a letra {input_letra}")
        elif input_letra not in frase:
            st.error(f"{input_letra} não está na palavra.")
            st.session_state.tentativas -= 1
            st.session_state.letras_adivinhadas.append(input_letra)
        else:
            st.success(f"Parabéns, {input_letra} está na frase!")
            index = [i for i, letra in enumerate(
                frase) if letra == input_letra]
            frase_completa_lista = list(st.session_state.frase_completa)
            for i in index:
                frase_completa_lista[i] = input_letra
            st.session_state.frase_completa = "".join(frase_completa_lista)
            st.session_state.letras_adivinhadas.append(input_letra)

        img()

    if all(c in st.session_state.letras_adivinhadas or c in [' ', '?'] for c in frase):
        st.balloons()
        st.success('Parabéns! Você acertou a frase completa!')

    elif len(input_letra) > 1:
        st.warning("Escreva apenas uma letra.")
    elif input_letra and not input_letra.isalpha():
        st.warning('Digito inválido.')

    if st.session_state.tentativas <= 0:

        st.error('Você perdeu!')
        button_key = f"tentar_novamente_btn{st.session_state.tentativas}"
        if st.button("Tentar novamente", key=button_key):
            reset_game()

    columns = st.columns(len(frase))

    for i, col in enumerate(columns):
        with col:
            if i == 6:
                st.subheader(' ')
            elif i == 13:
                st.subheader('?')
            else:
                st.subheader(st.session_state.frase_completa[i])


jogar()

print(st.session_state.tentativas)
