from .index import router as api_router

__import__('app.api.endpoints', globals(), locals())
