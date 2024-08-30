import streamlit as st
import requests

def get_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json()['ip']
        return ip
    except Exception as e:
        st.error(f"Error getting IP address: {e}")
        return None
    
ip_address = get_ip()

st.write(ip_address)