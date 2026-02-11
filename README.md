# retail-sniper-starter

Starter deployment scaffold for UK RA/OA using Keepa API, PostgreSQL, Redis, and Python services:

- Data collector (Keepa offer listing + price history ingestion)
- Analyzer (ROI/profit filters + de-duplication)
- WhatsApp alert worker (dispatches signals via Twilio/WhatsApp Business API)
- Minimal web UI to view recent signals and service health

## Repository layout

```
retail-sniper-starter/
  docker-compose.yml
  docker-compose.workers.yml
  Dockerfile
  .env.example
  app/
    __init__.py
    web.py
    collector.py
    analyzer.py
    whatsapp_worker.py
    models.py
    keepa_client.py
    ui/
      index.html
      ui.js
```

## Deploy on a Linux VPS

1. Install Docker + Docker Compose plugin (or docker-compose).
2. Clone:
   ```bash
   git clone https://github.com/MISCHIEFMNGD/retail-sniper-starter.git
   cd retail-sniper-starter
   ```
3. Create your env file:
   ```bash
   cp .env.example .env
   ```
4. Bring up core stack (web + DB + Redis):
   ```bash
   docker compose up -d --build
   ```
5. Bring up workers (collector/analyzer/alerts):
   ```bash
   docker compose -f docker-compose.workers.yml up -d --build
   ```
6. Tail logs (example):
   ```bash
   docker compose logs -f app
   docker compose -f docker-compose.workers.yml logs -f collector analyzer alert-worker
   ```
7. Clean down:
   ```bash
   docker compose down
   docker compose -f docker-compose.workers.yml down
   ```

## Env vars

See `.env.example` for a starter set of variables (Keepa key, DB/Redis settings, WhatsApp/Twilio creds).

## Notes

- Keepa API is rate-limited and billable; keep calls conservative.
- The WhatsApp worker is a stub; wire it to Twilio/WhatsApp Cloud API and add retries/monitoring before you trust alerts.
