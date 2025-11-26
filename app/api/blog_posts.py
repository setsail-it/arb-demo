from fastapi import APIRouter, HTTPException

from app.data import get_blog_post_artifact
from app.schemas.models import BlogPostArtifactRead

router = APIRouter()


@router.get("/{blog_post_id}", response_model=BlogPostArtifactRead)
async def get_blog_post(blog_post_id: int):
    """Get a blog post artifact by ID."""
    blog_post = get_blog_post_artifact(blog_post_id)
    if not blog_post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return blog_post


@router.get("/{blog_post_id}/xml")
async def get_blog_post_xml(blog_post_id: int):
    """Get the XML content of a blog post artifact."""
    blog_post = get_blog_post_artifact(blog_post_id)
    if not blog_post:
        raise HTTPException(status_code=404, detail="Blog post not found")

    xml_content = blog_post.xml if blog_post.xml else "<!-- XML not available -->"
    return {"xml": xml_content}

