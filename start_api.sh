#!/usr/bin/env bash
export APP_MODULE=endpoints.api.app:app

API_HOST=${API_HOST:-0.0.0.0}
API_PORT=${API_PORT:-8001}
LOG_LEVEL=${LOG_LEVEL:-info}

exec uvicorn --reload --reload-dir ${PWD} --host $API_HOST --port $API_PORT --log-level $LOG_LEVEL "$APP_MODULE" --access-log
