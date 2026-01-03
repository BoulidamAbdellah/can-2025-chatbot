from flask import Flask, request, jsonify, make_response
from datetime import datetime
import logging
from ragService import *

# Configuration du logging DÉTAILLÉE
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    """Ajouter les headers CORS manuellement"""
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

# Gérer les requêtes OPTIONS (pre-flight CORS)
@app.route('/', methods=['OPTIONS'])
@app.route('/api/health', methods=['OPTIONS'])
@app.route('/api/chat', methods=['OPTIONS'])
def handle_options():
    """Gérer les requêtes OPTIONS pour CORS"""
    return '', 204

logger.info("Démarrage du serveur Flask...")
chatbot_instance = get_chatbot()
logger.info("Chatbot chargé avec succès")

@app.before_request
def log_request():
    """Logger TOUTES les requêtes"""
    logger.info("=" * 60)
    logger.info(f" {request.method} {request.path}")
    logger.info(f"   Origin: {request.headers.get('Origin', 'Direct')}")
    logger.info(f"   User-Agent: {request.headers.get('User-Agent', 'Unknown')[:50]}")
    logger.info("=" * 60)

@app.after_request
def log_response(response):
    """Logger TOUTES les réponses"""
    logger.info(f"Status: {response.status_code}")
    return response

@app.route('/')
def home():
    """Page d'accueil"""
    logger.info("Fonction home() appelée")
    return jsonify({
        "message": "Chatbot CAN 2025 API",
        "version": "1.0.0",
        "status": "En ligne",
        "endpoints": {
            "home": "GET /",
            "health": "GET /api/health",
            "chat": "POST /api/chat"
        }
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Vérifier l'état du serveur"""
    logger.info(" Health check appelé")
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "chatbot_loaded": chatbot_instance is not None
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint principal pour le chat"""
    try:
        logger.info(" Endpoint /api/chat appelé")
        
        data = request.get_json()
        logger.info(f" Données reçues: {data}")
        
        if not data:
            logger.error(" Aucune donnée JSON")
            return jsonify({"error": "Aucune donnée fournie"}), 400
        
        user_message = data.get('message', '').strip()
        
        if not user_message:
            logger.error("Message vide")
            return jsonify({"error": "Le message ne peut pas être vide"}), 400
        
        logger.info(f"Question: {user_message}")
        
        # Obtenir la réponse du chatbot
        bot_response = chatbot_instance.get_response(user_message)
        
        logger.info(f" Réponse: {bot_response[:50]}...")
        
        return jsonify({
            "response": bot_response,
            "timestamp": datetime.now().isoformat(),
            "status": "success"
        })
    
    except Exception as e:
        logger.error(f" ERREUR: {str(e)}", exc_info=True)
        return jsonify({
            "error": "Une erreur est survenue",
            "details": str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 - Route non trouvée: {request.path}")
    return jsonify({
        "error": "Endpoint non trouvé",
        "path": request.path
    }), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 - Erreur serveur: {error}")
    return jsonify({
        "error": "Erreur interne du serveur"
    }), 500

if __name__ == '__main__':
    logger.info("=" * 60)
    logger.info(" SERVEUR FLASK PRÊT")
    logger.info(" URL: http://localhost:5555")
    logger.info(" URL: http://127.0.0.1:5555")
    logger.info("=" * 60)
    
    app.run(
        host='0.0.0.0',
        port=5555,
        debug=True
    )