# 🌱 Raiziomfix Core Engine – To be evolved into Raiziom
FROM python:3.11-slim AS backend
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY backend ./backend

FROM node:18 AS frontend
WORKDIR /frontend
COPY frontend ./frontend
RUN cd frontend && npm install && npm run build

FROM python:3.11-slim
WORKDIR /app
COPY --from=backend /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=backend /app/backend ./backend
COPY --from=frontend /frontend/frontend/build ./frontend/build
COPY requirements.txt .

ENV PORT=8000
EXPOSE 8000

# 🧠 Core logic: part of Raiziom engine
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
