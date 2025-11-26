import asyncio
import json
from datetime import datetime, timezone
from typing import AsyncGenerator


async def delay_response(seconds: int = 5):
    """Wait for the specified number of seconds."""
    await asyncio.sleep(seconds)


async def create_sse_stream(
    progress_messages: list[str],
    final_data: dict,
    delay_per_message: float = 1.0,
) -> AsyncGenerator[str, None]:
    """
    Create an SSE stream with progress messages and final data.
    
    Args:
        progress_messages: List of progress messages to send
        final_data: Final data to send in completion event
        delay_per_message: Delay between messages in seconds
    """
    step = 0
    
    # Send progress messages
    for message in progress_messages:
        step += 1
        event_data = json.dumps({
            "type": "progress",
            "message": message,
            "step": step,
        })
        yield f"data: {event_data}\n\n"
        await asyncio.sleep(delay_per_message)
    
    # Send final completion event
    final_event = json.dumps({
        "type": "complete",
        "data": final_data,
    })
    yield f"data: {final_event}\n\n"


def get_current_timestamp() -> datetime:
    """Get current UTC timestamp."""
    return datetime.now(timezone.utc)

