import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
class RAGChatbot:
    def __init__(self):
        """Initialiser le chatbot RAG CAN 2025"""
        
        # Configurer l'API Google
        self.api_key = os.getenv("GOOGLE_API_KEY", os.getenv("api-key"))
        os.environ["GOOGLE_API_KEY"] = self.api_key
        
        # Charger les embeddings et le FAISS index
        print("🔄 Chargement du modèle d'embeddings...")
        self.embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        print("🔄 Chargement de la base vectorielle FAISS...")
        self.vector_db = FAISS.load_local(
            "faiss_index_can", 
            self.embeddings_model, 
            allow_dangerous_deserialization=True
        )
        
        # Créer le retriever
        self.retriever = self.vector_db.as_retriever(search_kwargs={"k": 10})
        
        # Créer le modèle Gemini
        print("🔄 Initialisation du modèle Gemini...")
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.1)
        
        # Définir le prompt
        template = """Tu es un assistant expert de la CAN 2025.
Utilise les extraits suivants pour répondre à la question.
Si tu ne connais pas la réponse avec ces infos, dis simplement que tu ne sais pas.
Sois précis sur les buteurs, les minutes de jeu et les clubs des joueurs.

Contexte:
{context}

Question: {question}

Réponse:"""
        
        self.prompt = ChatPromptTemplate.from_template(template)
        
        # Créer la chaîne RAG
        self.rag_chain = (
            {"context": self.retriever | self._format_docs, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
        
        print("✅ Chatbot RAG initialisé avec succès !")
    
    def _format_docs(self, docs):
        """Formater les documents récupérés"""
        return "\n\n".join(doc.page_content for doc in docs)
    
    def get_response(self, question: str) -> str:
        """Obtenir une réponse à partir d'une question"""
        try:
            response = self.rag_chain.invoke(question)
            return response
        except Exception as e:
            print(f"❌ Erreur lors de la génération de la réponse: {e}")
            return f"Désolé, une erreur est survenue: {str(e)}"

# Instance globale (chargée une seule fois au démarrage)
chatbot = None

def get_chatbot():
    """Obtenir l'instance du chatbot (singleton)"""
    global chatbot
    if chatbot is None:
        chatbot = RAGChatbot()
    return chatbot