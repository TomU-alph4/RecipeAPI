# 🧾 SmartRecipe API — Development Checklist

A FastAPI-based backend that scans grocery receipts, extracts purchased ingredients using OCR + NLP, stores them in PostgreSQL, and recommends recipes the user can cook with what they already have.

---

## 🏗️ Phase 1 – Project Setup
- [x] Create public GitHub repo **`recipeAPI`**
- [x] Initialize `README.md` with project overview & setup instructions
- [x] Create virtual environment (`venv` or `poetry`)
- [x] Install base dependencies: `fastapi`, `uvicorn`, `pydantic`, `python-dotenv`
- [x] Setup `.gitignore` for Python, venv, and local files
- [x] Create folder structure:
app/
├── api/
├── core/
├── models/
├── services/
├── tests/

---

## ⚙️ Phase 2 – Core App & Config
- [x] Create `main.py` with FastAPI instance and root `/health` endpoint
- [x] Add configuration using `pydantic.BaseSettings` (load `.env` variables)
- [x] Implement basic logging setup in `core/logging.py`
- [x] Add automatic CORS middleware setup
- [x] Add a basic dependency-injection pattern (`Depends`)

---

## 🧠 Phase 3 – Database & Models
- [x] Install and run **PostgreSQL** (via Docker)
- [ ] Install ORM tools: `sqlmodel`, `psycopg2-binary`
- [ ] Create `core/db.py` with SQLModel engine and session logic
- [ ] Define `User`, `Receipt`, and `Ingredient` models
- [ ] Add Alembic migrations
- [ ] Create `init_db.py` to bootstrap initial tables
- [ ] Test database connection with `/db-check` endpoint

---

## 📸 Phase 4 – OCR Receipt Upload
- [ ] Add `python-multipart` and `pillow` for file uploads
- [ ] Implement `/receipts/upload` endpoint to accept `.jpg` or `.png`
- [ ] Use `pytesseract` or `easyocr` to extract text from receipt image
- [ ] Parse text lines into structured product names + quantities
- [ ] Store parsed receipt + items in the database
- [ ] Log extraction success/failure per upload

---

## 🍎 Phase 5 – Ingredient Management
- [ ] Create `/ingredients` CRUD endpoints
- [ ] When a receipt is processed, auto-populate user’s ingredient list
- [ ] Add optional expiry dates or “used up” flags
- [ ] Implement filtering for “available” ingredients only

---

## 🥘 Phase 6 – Recipe Generation
- [ ] Integrate AI/ML or rule-based matching for recipe suggestions
- [ ] Simple version: use Edamam or Spoonacular API
- [ ] Advanced: build own matching logic from recipe dataset
- [ ] Add `/recipes/suggest` endpoint that:
- [ ] Takes current ingredients
- [ ] Returns ranked list of possible recipes
- [ ] Add `/recipes/{id}` to fetch full recipe details
- [ ] Cache results (e.g., with Redis)

---

## 🔒 Phase 7 – Authentication (optional but realistic)
- [ ] Add JWT-based auth with `fastapi-users` or custom logic
- [ ] Require user auth for uploading receipts & managing ingredients

---

## ☁️ Phase 8 – Cloud & Deployment
- [ ] Add `Dockerfile` and `docker-compose.yml` (FastAPI + Postgres)
- [ ] Setup environment variables securely via `.env`
- [ ] Prepare production-ready `uvicorn` command
- [ ] Deploy to Render / Railway / Fly.io for public demo

---

## 🧪 Phase 9 – Testing & Docs
- [ ] Add unit tests for OCR parsing, ingredient matching, and recipe suggestions
- [ ] Use `pytest` + `httpx` for integration tests
- [ ] Generate API docs via `/docs` (FastAPI auto)
- [ ] Add Postman collection or OpenAPI export
- [ ] Write comprehensive `README.md` with setup, usage, and screenshots

---

## 🌟 Phase 10 – Enhancements (Optional)
- [ ] Add AI-powered ingredient normalizer (e.g., map “tomatoes” → “tomato”)
- [ ] Add food waste tracker (“expiring soon” alerts)
- [ ] Add front-end demo using React or Vue
- [ ] Add user preference filtering (vegan, gluten-free, etc.)
- [ ] Add analytics (most-used ingredients, recipe success rates)

---

## ✅ Progress Tracking
- [ ] **Phase 1** – Setup complete
- [ ] **Phase 2** – Core app running
- [ ] **Phase 3** – Database integrated
- [ ] **Phase 4** – OCR upload works
- [ ] **Phase 5** – Ingredient CRUD done
- [ ] **Phase 6** – Recipe generation functional
- [ ] **Phase 7–10** – Enhancements, testing, deployment