from app.database.models import async_session, init_db
from app.database.models import User, Energy_values
from sqlalchemy import select, update


async def start_user(tg_id: int, first_name: str, last_name: str, username: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            user = User(
                tg_id=tg_id,
                first_name=first_name,
                last_name=last_name,
                username=username,
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)

        return user
