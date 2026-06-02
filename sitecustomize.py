"""
Python startup hook (repo root).

Windows에서 asyncio 기본 루프가 ProactorEventLoop로 잡히면,
async mode psycopg(=SQLAlchemy async)가 동작하지 않아
`Psycopg cannot use the 'ProactorEventLoop' to run in async mode` 에러가 납니다.

uvicorn 실행 전 SelectorEventLoop로 강제합니다.
"""

from __future__ import annotations

import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

