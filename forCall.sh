#!/bin/bash
clear
for (( i = 0; i < 10000; i++ )); do
    #python  examples/http3_client_modified.py --ca-certs tests/pycacert.pem wss://192.168.1.2:4433/ws
    python  examples/http3_client_modified.py --ca-certs tests/pycacert.pem wss://192.168.1.4:4433/ws
    #python  examples/http3_client_modified.py --ca-certs tests/pycacert.pem wss://localhost:4433/ws
done