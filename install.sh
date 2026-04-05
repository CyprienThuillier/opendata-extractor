echo "[-] Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1
playwright install chromium > /dev/null 2>&1
echo "[-] Installation completed."