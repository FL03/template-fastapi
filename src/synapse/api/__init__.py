from .index import router as api_router

__import__("synapse.api.routes", globals(), locals())
