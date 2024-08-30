import streamlit as st
import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Check for HTTP request errors
        ip = response.json()['ip']
        return ip
    except requests.exceptions.RequestException as e:
        return f"Error getting IP address: {e}"
    
ip_address = get_public_ip()

st.write(ip_address)
