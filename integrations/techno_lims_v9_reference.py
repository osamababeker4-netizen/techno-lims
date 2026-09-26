# TECHNO LIMS integration reference
# Canonical integration notes for TECHNO Soil Lab only.
#
# Rules:
# 1. Keep TECHNO branding, URLs, API service names, and deployment paths isolated from other systems.
# 2. Use the TECHNO central database and current schema; do not create a parallel local production database.
# 3. Reuse the authenticated API and permission model already implemented in server.py.
# 4. New integrations must preserve auditability, realtime synchronization, and role-based access.
# 5. Production endpoints must target the TECHNO frontend and TECHNO API exclusively.

TECHNO_FRONTEND = "https://osamababeker4-netizen.github.io/techno-lims/"
TECHNO_API = "https://techno-lims-api.onrender.com"
TECHNO_RELEASE = "10.9.4-techno-data-sync"

def integration_summary():
    return {
        "product": "TECHNO LIMS",
        "frontend": TECHNO_FRONTEND,
        "api": TECHNO_API,
        "release": TECHNO_RELEASE,
        "isolation": "TECHNO-only",
    }
