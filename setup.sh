mkdir -p ~/.streamlit/

echo "[theme]
base="light"
primaryColor="#4d9e85"
secondaryBackgroundColor="#efba95"
textColor="#6f244c"
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
