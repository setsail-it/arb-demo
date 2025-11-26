from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.data import get_clients
from app.schemas.models import ClientCreate, ClientRead, ClientUpdate
from app.utils import get_current_timestamp

router = APIRouter()


class RenameClientRequest(BaseModel):
    name: str


@router.get("", response_model=list[ClientRead])
async def list_clients():
    """List all clients."""
    return get_clients()


@router.post("", response_model=ClientRead, status_code=status.HTTP_201_CREATED)
async def create_client(client: ClientCreate):
    """Create a new client (stub)."""
    clients = get_clients()
    max_id = max(c.id for c in clients) if clients else 0
    now = get_current_timestamp()
    return ClientRead(
        id=max_id + 1,
        name=client.name,
        slug=client.slug,
        notes=None,
        created_at=now,
        updated_at=now,
    )


@router.get("/{client_id}", response_model=ClientRead)
async def get_client(client_id: int):
    """Get a single client by ID."""
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@router.patch("/{client_id}/rename", response_model=ClientRead)
async def rename_client(client_id: int, request: RenameClientRequest):
    """Rename a client (stub)."""
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    if not request.name or not request.name.strip():
        raise HTTPException(status_code=400, detail="Client name cannot be empty")
    
    # Return updated client
    return ClientRead(
        id=client.id,
        name=request.name.strip(),
        slug=client.slug,
        notes=client.notes,
        created_at=client.created_at,
        updated_at=get_current_timestamp(),
    )


@router.put("/{client_id}", response_model=ClientRead)
async def update_client(client_id: int, client_update: ClientUpdate):
    """Update a client (stub)."""
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    # Merge updates
    update_data = client_update.model_dump(exclude_unset=True)
    return ClientRead(
        id=client.id,
        name=update_data.get("name", client.name),
        slug=update_data.get("slug", client.slug),
        notes=update_data.get("notes", client.notes),
        created_at=client.created_at,
        updated_at=get_current_timestamp(),
    )


@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(client_id: int):
    """Delete a client (stub)."""
    clients = get_clients()
    client = next((c for c in clients if c.id == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return None

