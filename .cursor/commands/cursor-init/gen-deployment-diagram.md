# Generate Deployment Diagram

Generate diagrams showing how your application is deployed across infrastructure.

## What This Does

Analyzes deployment configuration to create infrastructure visualizations:

1. Scans for deployment configs (Dockerfile, docker-compose.yml, k8s manifests, terraform)
2. Identifies infrastructure components (containers, VMs, serverless functions)
3. Maps network architecture and load balancing
4. Documents scaling and redundancy configuration
5. Generates Mermaid deployment diagram
6. Saves to `docs/deployment.md`

## Usage

```
/gen-deployment-diagram
```

## Example Output

```mermaid
graph TB
    subgraph Internet
        Users[Users]
        CDN[CloudFront CDN]
    end

    subgraph AWS
        subgraph Production
            ALB[Application Load Balancer]
            ECS1[ECS Task 1]
            ECS2[ECS Task 2]
            RDS[(RDS PostgreSQL)]
            S3[S3 Bucket]
        end

        subgraph Monitoring
            CloudWatch[CloudWatch]
            XRay[X-Ray]
        end
    end

    Users --> CDN
    CDN --> ALB
    ALB --> ECS1
    ALB --> ECS2
    ECS1 --> RDS
    ECS2 --> RDS
    ECS1 --> S3
    ECS2 --> S3
    ECS1 -.-> CloudWatch
    ECS2 -.-> CloudWatch
```

## Configuration

```yaml
documentation:
  infrastructure:
    deployment: true  # Set to false to disable

templates:
  deployment: "cloud_native"  # Options: cloud_native, containerized, serverless
```

---

**Output File**: `docs/deployment.md`
