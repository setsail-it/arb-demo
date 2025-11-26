import json
from datetime import datetime
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.data import get_clients, get_client_context as get_client_context_data
from app.schemas.models import ClientContextRead, ClientContextUpdate
from app.utils import create_sse_stream, delay_response

router = APIRouter()


class FetchRequest(BaseModel):
    domain: str | None = None


@router.get("", response_model=ClientContextRead)
async def get_client_context(client_id: int):
    """Get the client context for a given client."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    context = get_client_context_data(client_id)
    if not context:
        raise HTTPException(status_code=404, detail="Client context not found")
    return context


@router.put("", response_model=ClientContextRead)
async def upsert_client_context(
    client_id: int,
    context_update: ClientContextUpdate,
):
    """Create or update the client context (stub)."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    # Get existing context or create new
    context = get_client_context_data(client_id)
    if not context:
        # Create new context
        if not context_update.domain:
            raise HTTPException(
                status_code=400, detail="domain is required for new context"
            )
        from app.utils import get_current_timestamp
        now = get_current_timestamp()
        context = ClientContextRead(
            id=client_id,
            client_id=client_id,
            domain=context_update.domain or "",
            call_to_action=None,
            about=None,
            competitors=None,
            brand_pov=None,
            ideal_target_market=None,
            brand_safety=None,
            author_tone=None,
            author_rules=None,
            logos=None,
            colors=None,
            fonts=None,
            images_used=None,
            social_links=None,
            company_details=None,
            questionnaire=None,
            existing_blog_titles=None,
            ready=False,
            created_at=now,
            updated_at=now,
        )
    
    # Merge updates
    update_data = context_update.model_dump(exclude_unset=True)
    context_dict = context.model_dump()
    context_dict.update(update_data)
    
    return ClientContextRead(**context_dict)


@router.post("/fetch", response_model=ClientContextRead)
async def fetch_client_context(
    client_id: int, request: FetchRequest | None = None
):
    """Fetch and build client context (stub, wait 5s)."""
    # Check if client exists
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    await delay_response(5)
    
    context = get_client_context_data(client_id)
    if not context:
        raise HTTPException(status_code=404, detail="Client context not found")
    return context


@router.post("/fetch-stream")
async def fetch_client_context_stream(
    client_id: int, request: FetchRequest | None = None
):
    """Fetch and build client context with SSE progress updates (stub)."""
    try:
        # Check if client exists
        clients = get_clients()
        client = next((c for c in clients if c.id == client_id), None)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        
        context = get_client_context_data(client_id)
        if not context:
            raise HTTPException(status_code=404, detail="Client context not found")
        
        # Create progress messages
        progress_messages = [
            "Initializing context fetch...",
            "Scraping website content...",
            "Analyzing brand elements...",
            "Extracting company information...",
            "Finalizing context data...",
        ]
        
        # Prepare final data - use model_dump with mode='json' to ensure proper serialization
        try:
            context_dict = context.model_dump(mode='json')
        except Exception as e:
            # Fallback: manual serialization
            context_dict = context.model_dump()
            # Convert datetime objects to ISO format strings
            for key in ["created_at", "updated_at"]:
                if key in context_dict and isinstance(context_dict[key], datetime):
                    context_dict[key] = context_dict[key].isoformat()
        
        async def event_generator():
            async for event in create_sse_stream(progress_messages, context_dict):
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
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        print(f"Error in fetch_client_context_stream: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

