from fastapi import APIRouter
from models import MsgBody, MsgPayload

router = APIRouter()

messages_list: dict[int, MsgPayload] = {}

@router.post("/messages")
def add_msg(msg: MsgBody) -> dict[str, MsgPayload]:
    msg_id = max(messages_list.keys()) + 1 if messages_list else 0
    messages_list[msg_id] = MsgPayload(msg_id=msg_id, msg_name=msg.msg_name)
    return {"message": messages_list[msg_id]}

@router.get("/messages")
def message_items() -> dict[str, dict[int, MsgPayload]]:
    return {"messages:": messages_list}