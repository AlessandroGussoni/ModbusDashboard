from pymodbus.client import ModbusTcpClient
import streamlit as st
from streamlit import cli as stcli

def main():

    ip = "192.168.1.100"

    st.set_page_config(page_title="GusBus dashboard", layout="wide")
    st.subheader("Read your ModBus data thanks to Gustar8")

    connect = st.button('connect')
    connected = False

    if connect:

        client = ModbusTcpClient(ip)
        connected = client.connect()

    if not connected:

        st.write("You are not connected, try again !")
   
    else:

        register_type = st.radio("Select register Type:", ('input', 'holding'))

        slave_id = st.slider('Select slave id', 0, 25, 1)

        register_address = st.number_input('Address register')

        if register_type=='input':
            res = client.read_input_registers(address=int(register_address), slave=int(slave_id))
            try:
                results = str(res.registers[0])
            except:
                results = "Exception response"
            st.subheader("GusBus: ")
            st.write(results)

        elif register_type=='holding':
            res = client.read_holding_registers(address=int(register_address), slave=int(slave_id))
            try:
                results = str(res.registers[0])
            except:
                results = "Exception response"
            st.subheader("GusBus: ")
            st.write(results)

if __name__ == '__main__':
    main()