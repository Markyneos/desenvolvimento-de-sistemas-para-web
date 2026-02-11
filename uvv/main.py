from my_webserver import MyWebServer
from http.server import SimpleHTTPRequestHandler
import os

PORT = int(os.getenv("PORT", 3001)) # Porta padrão 3001
