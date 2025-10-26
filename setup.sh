mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"alee65056@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
base=\"light\"\n\
primaryColor=\"white\"\n\
" > ~/.streamlit/config.toml
