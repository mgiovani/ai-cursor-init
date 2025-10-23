# Generate Security Diagram

Generate diagrams showing security architecture, authentication flows, and data protection.

## What This Does

Analyzes security implementation to create security architecture visualizations:

1. Identifies authentication/authorization mechanisms
2. Maps security boundaries and trust zones
3. Documents data flow with security controls
4. Visualizes encryption (in-transit, at-rest)
5. Shows access control patterns
6. Generates security architecture diagram
7. Saves to `docs/security.md`

## Usage

```
/gen-security-diagram
```

## Example Output

```mermaid
graph TB
    subgraph Internet [Internet - Untrusted]
        User[User/Browser]
    end

    subgraph DMZ [DMZ - Limited Trust]
        WAF[Web Application Firewall]
        LB[Load Balancer + TLS]
    end

    subgraph AppTier [Application Tier - Trusted]
        API[API Server]
        Auth[Auth Service]
    end

    subgraph DataTier [Data Tier - Highly Trusted]
        DB[(Encrypted Database)]
        Secrets[Secrets Manager]
    end

    User -->|HTTPS| WAF
    WAF -->|Filtered| LB
    LB -->|TLS 1.3| API

    API -->|JWT Validation| Auth
    Auth <-->|Encrypted| Secrets
    API <-->|Encrypted Connection| DB

    style Internet fill:#ff9999
    style DMZ fill:#ffff99
    style AppTier fill:#99ff99
    style DataTier fill:#9999ff
```

## Security Elements Documented

- Authentication flows (OAuth, JWT, session-based)
- Authorization patterns (RBAC, ABAC)
- Network security (firewalls, VPCs, security groups)
- Data encryption (TLS, encryption at rest)
- Secrets management
- API security (rate limiting, CORS, CSP)
- Audit logging

## Configuration

```yaml
documentation:
  infrastructure:
    security: true  # Set to false to disable
```

---

**Output File**: `docs/security.md`
