import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.data import (
    get_clients,
    get_keyword_ideas,
    get_keyword_clusters,
    get_keyword_sets,
    get_best_alternates,
)
from app.schemas.models import (
    KeywordIdeaRead,
    KeywordClusterRead,
    KeywordSetRead,
    BestAlternateRead,
)
from app.utils import create_sse_stream, delay_response

router = APIRouter()


class GenerateIdeasRequest(BaseModel):
    min_sv: int | None = None
    max_kd: int | None = None


class BestAlternateRequest(BaseModel):
    keyword_id: int
    sim_threshold: float | None = None
    limit_per_seed: int | None = None


class DevelopSetsRequest(BaseModel):
    keyword_ids: list[int]
    min_sv: int | None = None


@router.post("/generate-ideas")
async def generate_ideas(
    client_id: int,
    request: GenerateIdeasRequest | None = None,
):
    """Generate keyword ideas with SSE progress updates (stub)."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    ideas = get_keyword_ideas(client_id)
    
    # Create progress messages
    progress_messages = [
        "Initializing keyword generation...",
        "Fetching seed keywords...",
        "Analyzing search volumes...",
        "Calculating keyword difficulty...",
        "Finalizing keyword ideas...",
    ]
    
    # Prepare final data
    final_data = [idea.model_dump(mode='json') for idea in ideas]
    
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


@router.get("/ideas", response_model=list[KeywordIdeaRead])
async def list_ideas(client_id: int):
    """List all keyword ideas for a client."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    return get_keyword_ideas(client_id)


@router.post("/best-alternate", response_model=BestAlternateRead)
async def best_alternate(request: BestAlternateRequest):
    """Find the best alternate keyword (stub, wait 5s)."""
    await delay_response(5)
    
    # Find the keyword idea to get client_id
    all_ideas = []
    for client_id in [1, 2]:
        all_ideas.extend(get_keyword_ideas(client_id))
    
    keyword_idea = next((k for k in all_ideas if k.id == request.keyword_id), None)
    if not keyword_idea:
        raise HTTPException(status_code=404, detail="Keyword idea not found")
    
    # Get best alternate for this client
    alternates = get_best_alternates(keyword_idea.client_id)
    alternate = next(
        (a for a in alternates if a.original_keyword_id == request.keyword_id),
        None
    )
    
    if not alternate:
        # Return a stub alternate
        return BestAlternateRead(
            id=1,
            client_id=keyword_idea.client_id,
            original_keyword_id=request.keyword_id,
            keyword=keyword_idea.keyword,
            search_volume=keyword_idea.search_volume,
            keyword_difficulty=keyword_idea.keyword_difficulty,
            is_original=True,
            created_at=keyword_idea.created_at,
            updated_at=keyword_idea.created_at,
        )
    
    return alternate


@router.get("/best-alternates", response_model=list[BestAlternateRead])
async def list_best_alternates(client_id: int):
    """List all best alternates for a client."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    return get_best_alternates(client_id)


@router.get("/clusters", response_model=list[KeywordClusterRead])
async def list_clusters(client_id: int):
    """List all keyword clusters for a client."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    return get_keyword_clusters(client_id)


@router.post("/develop-sets", response_model=list[KeywordSetRead])
async def develop_sets(
    client_id: int,
    request: DevelopSetsRequest,
):
    """Develop keyword sets (stub, wait 5s)."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    # Validate request
    if not request.keyword_ids:
        raise HTTPException(status_code=400, detail="keyword_ids cannot be empty")
    
    await delay_response(5)
    
    return get_keyword_sets(client_id)


@router.get("/sets", response_model=list[KeywordSetRead])
async def list_sets(client_id: int):
    """List all keyword sets for a client."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    return get_keyword_sets(client_id)

