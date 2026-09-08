# automated-deploy-platform

Production-grade automated deployment platform built as a DevOps portfolio project.

## Stack
- **CI/CD** — GitHub Actions
- **Containerization** — Docker
- **Registry** — AWS ECR
- **Deployment** — Ansible
- **Server** — AWS EC2 (Ubuntu 24.04, ap-northeast-3)
- **App** — Python Flask + Pytest
- **Proxy** — Nginx

## CI/CD Flow
```
Push to main
      ↓
GitHub Actions runs Pytest
      ↓
Docker image built + pushed to ECR
      ↓
Ansible deploys to EC2
      ↓
Health check verifies deployment
      ↓
Auto rollback if failed
```

## Project Structure
```
automated-deploy-platform/
├── .github/workflows/
│   ├── ci.yml
│   └── deploy.yml
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── tests/
│       └── test_app.py
├── ansible/
│   ├── playbooks/
│   │   ├── deploy.yml
│   │   └── rollback.yml
│   └── roles/
├── nginx/
│   └── nginx.conf
└── docker-compose.yml
```

## Phases
✅ Phase 1 — Flask app + Pytest
✅ Phase 2 — Docker + AWS ECR
✅ Phase 3 — GitHub Actions CI pipeline
✅ Phase 4 — Ansible deployment + auto rollback
⬜ Phase 5 — Failure scenarios + troubleshooting