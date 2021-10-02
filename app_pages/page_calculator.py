import streamlit as st

def calculator_body():
    st.write("---")
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        num1 = st.number_input(label='Enter number 1', step=1)
    with col2:
        num2 = st.number_input(label='Enter number 2', step=1)
    with col3:
        operation = st.selectbox(label="Select an operation",
                                options=['Add','Subract','Multiply','Division'])

    if st.button("Click here for the maths"):
        if num2 == 0 and operation == 'Division':
            st.error('The denominator should not be 0. Try again.')
        else:
            calculator_function(num1, num2, operation)


def calculator_function(num1, num2, operation):
    if operation == 'Add': result = num1 + num2
    elif operation == 'Subract': result = num1 - num2
    elif operation == 'Multiply': result = num1 * num2
    elif operation == 'Division': result = num1 / num2

    st.success(f"The result is:  **{result}**")