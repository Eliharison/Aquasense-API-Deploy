from flask import Flask
from routes.routes import routes
from database.db import initialize_db
from extensions.extensions import Extensions
from config import Config

app = Flask(__name__)

# Configurações
app.config.from_object(Config)

# Inicializações
initialize_db(app)
Extensions.initialize_jwt(app)
Extensions.initialize_marsh(app)
Extensions.initialize_bcript(app)

# Registro de rotas
app.register_blueprint(routes)
