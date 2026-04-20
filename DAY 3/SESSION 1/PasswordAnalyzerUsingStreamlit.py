import streamlit as st
from PIL import Image

st.title("Password Checker")
st.write("Check your password strength")
img = Image.open("streamlit.png") # Open the image file
st.image(img, width=200)


def has_min_length(password,min_len=8):
    return len(password)>=min_len

def has_uppercase(password):
    for ch in password:
        if ch.isupper():
            return True
        
    return False

def has_lowercase(password):
    for ch in password:
        if ch.islower():
            return True
        
    return False


def has_digit(password):
    for ch in password:
        if ch.isdigit():
            return True
        
    return False

def has_sepcial_char(password,special='!@#$%^&*'):
    for ch in password:
        if ch in special:
            return True
        
    return False


def analyze_password(password):
    strength=0
    failed=[]

    if has_min_length(password):
        strength+=1
    else:
        failed.append("Minimum Length Required")
    
    if has_uppercase(password):
        strength+=1
    else:
        failed.append("Required Uppercase")
    
    if has_lowercase(password):
        strength+=1
    else:
        failed.append("Required Lowercase")
    
    if has_digit(password):
        strength+=1
    else:
        failed.append("Required a Digit")
    
    if has_sepcial_char(password):
        strength+=1
    else:
        failed.append("Required Special Character")

    
    
    if strength<=2:
        flag="Week"
    if strength==3:
        flag="Moderate"
    if strength==4:
        flag="Strong enough"
    elif strength>4:
        flag="Strong max"
    
    return flag,strength,failed





password=st.text_input("Enter the password",type="password")

if st.button("Analyze Password"):
    if password=="":
        st.warning("Please enter a password")
    else:
        flag,strength,failed=analyze_password(password)

        st.subheader("Result Ater checking")
        st.success(f"Strength: {strength}")
        st.info(f"Flag: {flag}")

        if failed:
            st.error("Failed Checks")

            for i in failed:
                st.write(i)
            else:
                st.success("All check pass")