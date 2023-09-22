import streamlit as st
import random
import matplotlib.pyplot as plt 
import numpy as np
x=['가위','보','바위']

if 'stage' not in st.session_state:
    st.session_state.stage=1
if 'num' not in st.session_state:
    st.session_state.num=0
def butt():
    st.session_state.num+=1

if st.session_state.stage == 1:
    text_input = st.text_input(label="너의 이름은?")
    if text_input:
        st.write("안녕",text_input)
        st.session_state.text1 = text_input  
        st.session_state.stage += 1

if st.session_state.stage == 2:
    text2 = st.text_input("너에게는 3가지의 선택권이 있어. A,B,C중에 골라봐")
    if text2=="A":
        st.write(text2,"은 꽝이야", "(잘가", st.session_state.text1,")")
    if text2=="B":
        st.write("나랑 가위바위보를 하자")
        
        ai_choice=random.choice(x)
        
        game_input=st.text_input(label='가위바위보중에 하나 골라')
        
        if ai_choice==game_input:
            st.write("비겻다")
        elif (ai_choice=='가위') and (game_input=='보'):
            st.write('졋다')
        elif (ai_choice=='보') and (game_input=='바위'):
            st.write('졋다')
        elif (ai_choice=='바위') and (game_input=='가위'):
            st.write('졋어')
        else:
            st.write('이겼어')
        
    if text2=="C":
        st.write("버튼을 눌러봐")

        while True:
            st.button('눌러봐',on_click=butt)
            st.write(st.session_state.num)
            
            fig, ax= plt.subplots(1,2)
            person=['Elon_musk','Trump','obama','betts']
            counts=[10,3,1,1]
            bar_color=['tab:blue','tab:red','tab:blue','tab:orange']
            
            ax[0].bar(person,counts,color=bar_color)
            ax[0].set_ylabel('Good')
            ax[0].set_title('wow')
            ax[0].legend()
            
            x = np.linspace(0, 10, 100)
            x = np.linspace(0, 10, 100)
            y = np.sin(x)
            ax[1].plot(x,y)
            ax[1].set_title('Sine Wave')

            st.pyplot(plt)


        






        
    



 










    
      
