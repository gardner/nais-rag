import logging

from app.settings import init_settings
from app.workflow import create_workflow
from dotenv import load_dotenv
from llama_index.server import LlamaIndexServer, UIConfig

logger = logging.getLogger("uvicorn")

# A path to a directory where the customized UI code is stored
COMPONENT_DIR = "components"


def create_app():
    app = LlamaIndexServer(
        workflow_factory=create_workflow,  # A factory function that creates a new workflow for each request
        ui_config=UIConfig(
            component_dir=COMPONENT_DIR,
            app_title="Chat App",
            starter_questions=[
                "What is this document?",
                "When is the submission deadline for feedback?",
                "How can interested parties submit comments?",
                "What are Maximum Residue Levels (MRLs)?",
                "How are MRLs determined?",
                "How is dietary risk from residues assessed?",
                "How many agricultural compounds are affected by the proposed amendments?",
                "Why are the MRLs for methamidophos being changed?",
                "What are the changes proposed for glyphosate?",
                "Are any new agricultural compounds being added to the MRL notice?",
                "Do the proposed MRLs pose any health risks?",
                "How do the proposed MRLs compare to international standards?",
            ]
        ),
        logger=logger,
    )
    # You can also add custom FastAPI routes to app
    app.add_api_route("/api/health", lambda: {"message": "OK"}, status_code=200)
    return app


load_dotenv()
init_settings()
app = create_app()
