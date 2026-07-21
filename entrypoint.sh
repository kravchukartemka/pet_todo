#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! python -c "
import asyncio
import asyncpg

async def main():
    try:
        conn = await asyncpg.connect(
            user='postgres',
            password='postgres',
            database='tasks_db',
            host='db'
        )
        await conn.close()
    except Exception:
        raise

asyncio.run(main())
" >/dev/null 2>&1
do
    sleep 2
done

echo "PostgreSQL is ready."

echo "Running migrations..."

alembic upgrade head

echo "Starting FastAPI..."

exec uvicorn main:app --host 0.0.0.0 --port 8000