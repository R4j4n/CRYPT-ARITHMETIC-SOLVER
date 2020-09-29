
import webbrowser
import streamlit as st
import itertools


def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def solve2(equation):
    x = ''
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('+')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    if len(letters) < 10 : 
        digits = range(10)
        for perm in itertools.permutations(digits, len(letters)):
            sol = dict(zip(letters, perm))


            if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            
                x = ' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol)
            
        st.success(x)
    else:
        st.warning("VOCAB SIZE EXCEED.")

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
def main():
    st.title("🤖 CRYPT-ARITHMETIC-SOLVER 🤖")
    left = st.text_input(label="FIRST WORD",max_chars = 15 )
    left = left.upper()
    st.title("+")
    right = st.text_input(label="SECOND WORD" , max_chars = 15 )
    right = right.upper()
    st.write(" ** ------------------------------------------------------------------------------------------------------------ **")
    st.title("=")
    result = st.text_input(label="", max_chars = 15)
    result= result.upper()

    if st.button(" SOLVE "):
        check = left+right+result
        con1 = hasNumbers(check)
        if con1 == False:
            x = str(left+ "+" +right+ "=" +result)
            st.write(left+"+"+right+"="+result)
            with st.spinner("Working..."):
                solve2(x)
        else:
            st.warning("PLEASE INPUT VALID CHARACTER")

    url = 'https://r4j4n.github.io/'
    st.sidebar.title("FIND ME 👇👇")
    if st.sidebar.button('HERE 😎'):
        webbrowser.open_new_tab(url)
        
if __name__ == "__main__":
    main()