import logging
import sys

from fastapi import FastAPI

from app.api import blog_ideas, blog_posts, client, client_context, keywords

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

# Set log levels for our modules
logging.getLogger("app").setLevel(logging.INFO)

app = FastAPI()

# Include routers
app.include_router(client.router, prefix="/clients", tags=["clients"])
app.include_router(
    client_context.router,
    prefix="/clients/{client_id}/context",
    tags=["client-context"],
)
app.include_router(
    keywords.router, prefix="/clients/{client_id}/keywords", tags=["keywords"]
)
app.include_router(
    blog_ideas.router,
    prefix="/clients/{client_id}/blog-ideas",
    tags=["blog-ideas"],
)
app.include_router(blog_posts.router, prefix="/blog-posts", tags=["blog-posts"])


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/health")
async def health():
    return {"status": "healthy"}

