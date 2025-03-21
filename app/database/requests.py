from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import BigInteger

engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3")

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    email = mapped_column()
    password = mapped_column()
    phone_number = mapped_column()
    username = mapped_column()
    first_name = mapped_column()
    last_name = mapped_column()
    date_of_birth = mapped_column()

    