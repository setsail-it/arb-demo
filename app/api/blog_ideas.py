import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.data import get_clients, get_blog_ideas, get_blog_idea_html as get_blog_idea_html_data, get_blog_post_artifact
from app.schemas.models import BlogIdeaRead, BlogIdeaUpdate, BlogPostArtifactRead
from app.utils import create_sse_stream, delay_response, get_current_timestamp

router = APIRouter()


@router.get("", response_model=list[BlogIdeaRead])
async def list_blog_ideas(client_id: int):
    """List all blog ideas for a client."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    return get_blog_ideas(client_id)


@router.post("/generate", response_model=list[BlogIdeaRead])
async def generate_blog_ideas(client_id: int):
    """Generate blog ideas from keyword sets (stub, wait 5s)."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    await delay_response(5)
    
    return get_blog_ideas(client_id)


@router.put("/{blog_idea_id}", response_model=BlogIdeaRead)
async def update_blog_idea(
    client_id: int,
    blog_idea_id: int,
    blog_idea_update: BlogIdeaUpdate,
):
    """Update a blog idea (stub)."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    # Verify the blog idea belongs to the client
    blog_ideas = get_blog_ideas(client_id)
    blog_idea = next((b for b in blog_ideas if b.id == blog_idea_id), None)
    if not blog_idea:
        raise HTTPException(status_code=404, detail="Blog idea not found")

    # Merge updates
    update_data = blog_idea_update.model_dump(exclude_unset=True)
    blog_idea_dict = blog_idea.model_dump()
    blog_idea_dict.update(update_data)
    blog_idea_dict["updated_at"] = get_current_timestamp()
    
    return BlogIdeaRead(**blog_idea_dict)


@router.post("/{blog_idea_id}/queue", response_model=BlogIdeaRead)
async def queue_blog_idea(
    client_id: int, blog_idea_id: int
):
    """Queue a blog idea for processing (stub)."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    # Verify the blog idea belongs to the client
    blog_ideas = get_blog_ideas(client_id)
    blog_idea = next((b for b in blog_ideas if b.id == blog_idea_id), None)
    if not blog_idea:
        raise HTTPException(status_code=404, detail="Blog idea not found")

    # Update state to queued
    blog_idea_dict = blog_idea.model_dump()
    blog_idea_dict["state"] = "queued"
    blog_idea_dict["updated_at"] = get_current_timestamp()
    
    return BlogIdeaRead(**blog_idea_dict)


@router.post("/process-queued")
async def process_queued_blog_ideas(
    client_id: int
):
    """Move all queued blog ideas directly to 'complete' state (stub, wait 5s)."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    # Simulate processing delay
    await delay_response(5)

    # Get queued blog ideas
    blog_ideas = get_blog_ideas(client_id)
    queued_ideas = [b for b in blog_ideas if b.state == "queued"]

    results = []
    for blog_idea in queued_ideas:
        results.append({
            "blog_idea_id": blog_idea.id,
            "state": "complete",
        })

    return results


@router.get("/{blog_idea_id}/process-stream")
async def stream_blog_idea_processing(
    client_id: int,
    blog_idea_id: int,
):
    """Stream progress events for processing a single blog idea (stub)."""
    # Verify client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    # Verify blog idea exists and belongs to client
    blog_ideas = get_blog_ideas(client_id)
    blog_idea = next((b for b in blog_ideas if b.id == blog_idea_id), None)
    if not blog_idea:
        raise HTTPException(status_code=404, detail="Blog idea not found")
    
    # Verify blog idea is in progress
    if blog_idea.state != "in_progress":
        raise HTTPException(
            status_code=400,
            detail=f"Blog idea is in '{blog_idea.state}' state, must be 'in_progress' to stream processing"
        )
    
    # Create progress messages
    progress_messages = [
        "Initializing blog post generation...",
        "Creating content brief...",
        "Generating initial draft...",
        "Optimizing for SEO...",
        "Finalizing blog post...",
    ]
    
    # Prepare final data
    final_data = {
        "blog_idea_id": blog_idea_id,
        "state": "complete",
        "final_version_number": 1,
    }
    
    async def event_generator():
        async for event in create_sse_stream(progress_messages, final_data):
            yield event
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@router.get("/{blog_idea_id}/html")
async def get_blog_idea_html(
    client_id: int,
    blog_idea_id: int,
    version_number: int | None = None,
):
    """Get HTML for a blog idea."""
    # Verify client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    # Verify blog idea exists and belongs to client
    blog_ideas = get_blog_ideas(client_id)
    blog_idea = next((b for b in blog_ideas if b.id == blog_idea_id), None)
    if not blog_idea:
        raise HTTPException(status_code=404, detail="Blog idea not found")
    
    # Get HTML (pass client_id to help identify which client this belongs to)
    html_data = get_blog_idea_html_data(blog_idea_id, version_number, client_id)
    if not html_data:
        raise HTTPException(
            status_code=404,
            detail="HTML artifact not found for this blog idea",
        )
    
    return html_data


@router.delete("/{blog_idea_id}", status_code=204)
async def delete_blog_idea(
    client_id: int, blog_idea_id: int
):
    """Delete a blog idea (stub)."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    # Verify the blog idea belongs to the client
    blog_ideas = get_blog_ideas(client_id)
    blog_idea = next((b for b in blog_ideas if b.id == blog_idea_id), None)
    if not blog_idea:
        raise HTTPException(status_code=404, detail="Blog idea not found")
    
    return None


@router.get("/{blog_idea_id}/debug")
async def debug_blog_idea(
    client_id: int, blog_idea_id: int
):
    """Debug endpoint to inspect the ABS state for a single blog idea."""
    # Query for the BlogIdea
    blog_ideas = get_blog_ideas(client_id)
    blog_idea = next((b for b in blog_ideas if b.id == blog_idea_id), None)
    if not blog_idea:
        raise HTTPException(status_code=404, detail="BlogIdea not found")

    # Load associated BlogPostArtifact if any
    final_post = get_blog_post_artifact(blog_idea_id)

    return {
        "blog_idea": blog_idea.model_dump(),
        "brief": blog_idea.brief_json,
        "latest_sq_report": blog_idea.latest_sq_report,
        "draft_html": blog_idea.draft_html,
        "final_post": final_post.model_dump() if final_post else None,
    }

