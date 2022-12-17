from .index import router as api_router

__import__("synapse.api.endpoints", globals(), locals())
