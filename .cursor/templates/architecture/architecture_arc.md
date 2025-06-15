### {{PROJECT_NAME}} - Architecture Documentation (Arc42)

**Version:** {{VERSION}}
**Date:** {{DATE}}
**Authors:** {{AUTHORS}}
**Status:** {{STATUS}}

---

## 1. Introduction and Goals

{{INTRODUCTION_AND_GOALS}}

### 1.1 Requirements Overview

{{REQUIREMENTS_OVERVIEW}}

[Short description of the functional requirements, driving forces, extract (or abstract) of requirements. Link to (hopefully existing) requirements documents (with version number and information where to find it).]

#### Key Functional Requirements

{{FUNCTIONAL_REQUIREMENTS}}

- **{{REQ_1}}**: {{REQ_1_DESCRIPTION}}
- **{{REQ_2}}**: {{REQ_2_DESCRIPTION}}
- **{{REQ_3}}**: {{REQ_3_DESCRIPTION}}

### 1.2 Quality Goals

{{QUALITY_GOALS}}

[The top three (max five) quality goals for the architecture whose fulfillment is of highest importance to the major stakeholders. We really mean quality goals for the architecture. Don't confuse them with project goals.]

| Priority | Quality Goal | Motivation |
|----------|--------------|------------|
| 1 | {{QUALITY_GOAL_1}} | {{MOTIVATION_1}} |
| 2 | {{QUALITY_GOAL_2}} | {{MOTIVATION_2}} |
| 3 | {{QUALITY_GOAL_3}} | {{MOTIVATION_3}} |

### 1.3 Stakeholders

{{STAKEHOLDERS}}

[Explicit overview of stakeholders of the system, i.e. all person, roles or organizations that should know the architecture, have to be convinced of the architecture, have to work with the architecture or have to come up with decisions about the system and its development.]

| Role/Name | Contact | Expectations |
|-----------|---------|--------------|
| {{STAKEHOLDER_1}} | {{CONTACT_1}} | {{EXPECTATIONS_1}} |
| {{STAKEHOLDER_2}} | {{CONTACT_2}} | {{EXPECTATIONS_2}} |
| {{STAKEHOLDER_3}} | {{CONTACT_3}} | {{EXPECTATIONS_3}} |

## 2. Architecture Constraints

{{ARCHITECTURE_CONSTRAINTS}}

[Any requirement that constrains software architects in their freedom of design and implementation decisions or decision about the development process. These constraints sometimes go beyond individual systems and are valid for whole organizations and companies.]

### 2.1 Technical Constraints

{{TECHNICAL_CONSTRAINTS}}

| Constraint | Background/motivation |
|------------|----------------------|
| {{TECH_CONSTRAINT_1}} | {{TECH_CONSTRAINT_1_REASON}} |
| {{TECH_CONSTRAINT_2}} | {{TECH_CONSTRAINT_2_REASON}} |

### 2.2 Organizational Constraints

{{ORGANIZATIONAL_CONSTRAINTS}}

| Constraint | Background/motivation |
|------------|----------------------|
| {{ORG_CONSTRAINT_1}} | {{ORG_CONSTRAINT_1_REASON}} |
| {{ORG_CONSTRAINT_2}} | {{ORG_CONSTRAINT_2_REASON}} |

### 2.3 Conventions

{{CONVENTIONS}}

[Coding or documentation guidelines, company standards]

## 3. System Scope and Context

{{SYSTEM_SCOPE_CONTEXT}}

[System scope and context delimits your system from its (external) communication partners (neighboring systems and users). It thereby specifies the external interfaces.]

### 3.1 Business Context

{{BUSINESS_CONTEXT}}

[Specification of all communication partners (users, IT-systems, ...) with explanations of domain specific inputs and outputs or interfaces. Optionally you can add domain specific formats or communication protocols.]

#### Business Context Diagram

{{BUSINESS_CONTEXT_DIAGRAM}}

[Insert diagram showing business context]

#### Communication Partners

| Partner | Input | Output |
|---------|-------|--------|
| {{PARTNER_1}} | {{INPUT_1}} | {{OUTPUT_1}} |
| {{PARTNER_2}} | {{INPUT_2}} | {{OUTPUT_2}} |

### 3.2 Technical Context

{{TECHNICAL_CONTEXT}}

[Technical interfaces (channels and transmission media) linking your system to its environment. In addition a mapping of domain specific input/output to the channels, i.e. an explanation with I/O uses which channel.]

#### Technical Context Diagram

{{TECHNICAL_CONTEXT_DIAGRAM}}

[Insert diagram showing technical context]

## 4. Solution Strategy

{{SOLUTION_STRATEGY}}

[A short summary and explanation of the fundamental decisions and solution strategies, that shape the system's architecture. These include technology decisions, decisions about the top-level decomposition of the system, approaches to fulfill the most important quality goals as well as relevant organizational decisions.]

### 4.1 Technology Decisions

{{TECHNOLOGY_DECISIONS}}

| Technology | Decision | Rationale |
|------------|----------|-----------|
| {{TECH_1}} | {{DECISION_1}} | {{RATIONALE_1}} |
| {{TECH_2}} | {{DECISION_2}} | {{RATIONALE_2}} |

### 4.2 Top-level Decomposition

{{TOP_LEVEL_DECOMPOSITION}}

[How does the overall system break down into building blocks? Which modules or packages are there?]

### 4.3 Quality Goals Achievement

{{QUALITY_GOALS_ACHIEVEMENT}}

[How are the quality goals achieved? Which architectural approaches are used?]

## 5. Building Block View

{{BUILDING_BLOCK_VIEW}}

[The building block view shows the static decomposition of the system into building blocks (modules, components, subsystems, classes, interfaces, packages, libraries, frameworks, layers, partitions, tiers, functions, macros, operations, datas structures, ...) as well as their dependencies (relationships, associations)]

### 5.1 Whitebox Overall System

{{WHITEBOX_OVERALL_SYSTEM}}

[Here you describe the decomposition of the overall system using the following white box template. It contains up to 15 building blocks with their responsibilities, interfaces and (opaque) implemented requirements.]

#### Overview Diagram

{{OVERVIEW_DIAGRAM}}

[Insert system overview diagram]

#### Contained Building Blocks

| Building Block | Responsibility |
|----------------|----------------|
| {{BLOCK_1}} | {{RESPONSIBILITY_1}} |
| {{BLOCK_2}} | {{RESPONSIBILITY_2}} |
| {{BLOCK_3}} | {{RESPONSIBILITY_3}} |

#### Important Interfaces

{{IMPORTANT_INTERFACES}}

[Description of important interfaces]

### 5.2 Level 2 - Building Blocks

{{LEVEL_2_BUILDING_BLOCKS}}

#### 5.2.1 {{SUBSYSTEM_1}} (Whitebox)

{{SUBSYSTEM_1_DESCRIPTION}}

**Purpose/Responsibility:**
{{SUBSYSTEM_1_PURPOSE}}

**Interface(s):**
{{SUBSYSTEM_1_INTERFACES}}

**Implemented Requirements:**
{{SUBSYSTEM_1_REQUIREMENTS}}

#### 5.2.2 {{SUBSYSTEM_2}} (Whitebox)

{{SUBSYSTEM_2_DESCRIPTION}}

**Purpose/Responsibility:**
{{SUBSYSTEM_2_PURPOSE}}

**Interface(s):**
{{SUBSYSTEM_2_INTERFACES}}

**Implemented Requirements:**
{{SUBSYSTEM_2_REQUIREMENTS}}

## 6. Runtime View

{{RUNTIME_VIEW}}

[The runtime view describes concrete behavior and interactions of the system's building blocks in form of scenarios from the following areas: important use cases or features, interactions at critical external interfaces, operation and administration plus error and exception scenarios.]

### 6.1 Runtime Scenario 1: {{SCENARIO_1_NAME}}

{{SCENARIO_1_DESCRIPTION}}

#### Scenario Description

{{SCENARIO_1_DETAILED}}

[Step-by-step description of the scenario]

1. {{SCENARIO_1_STEP_1}}
2. {{SCENARIO_1_STEP_2}}
3. {{SCENARIO_1_STEP_3}}

### 6.2 Runtime Scenario 2: {{SCENARIO_2_NAME}}

{{SCENARIO_2_DESCRIPTION}}

#### Scenario Description

{{SCENARIO_2_DETAILED}}

[Step-by-step description of the scenario]

1. {{SCENARIO_2_STEP_1}}
2. {{SCENARIO_2_STEP_2}}
3. {{SCENARIO_2_STEP_3}}

## 7. Deployment View

{{DEPLOYMENT_VIEW}}

[The deployment view describes the environment in which the system is executed. It describes the geographic distribution of the system or the structure of the hardware components that execute the software.]

### 7.1 Infrastructure Level 1

{{INFRASTRUCTURE_LEVEL_1}}

#### Deployment Diagram

{{DEPLOYMENT_DIAGRAM}}

[Insert deployment diagram]

#### Node Descriptions

| Node | Description | Responsibility |
|------|-------------|----------------|
| {{NODE_1}} | {{NODE_1_DESC}} | {{NODE_1_RESP}} |
| {{NODE_2}} | {{NODE_2_DESC}} | {{NODE_2_RESP}} |

### 7.2 Infrastructure Level 2

{{INFRASTRUCTURE_LEVEL_2}}

[More detailed view of specific nodes if needed]

## 8. Cross-cutting Concepts

{{CROSS_CUTTING_CONCEPTS}}

[This section describes overall, principal regulations and solution ideas that are relevant in multiple parts (→ cross-cutting) of your system.]

### 8.1 Domain Model

{{DOMAIN_MODEL}}

[Description of domain model and core domain concepts]

### 8.2 Architecture Patterns

{{ARCHITECTURE_PATTERNS}}

[Which architectural patterns are applied? Which design patterns are used?]

### 8.3 Programming Model

{{PROGRAMMING_MODEL}}

[Which programming paradigms are used? How are domain concepts mapped to code?]

### 8.4 Exception/Error Handling

{{EXCEPTION_ERROR_HANDLING}}

[How are exceptions and errors handled? Which exceptions are checked, which are unchecked?]

### 8.5 Logging, Tracing

{{LOGGING_TRACING}}

[How does the system log important events? How can you trace the execution of use cases?]

### 8.6 Transaction Handling

{{TRANSACTION_HANDLING}}

[How are transactions handled? Are there distributed transactions?]

### 8.7 Session Handling

{{SESSION_HANDLING}}

[How are user sessions managed? How is session state handled?]

### 8.8 Security

{{SECURITY}}

[How is the system secured? Which security mechanisms are in place?]

#### Authentication

{{AUTHENTICATION}}

[How are users authenticated?]

#### Authorization

{{AUTHORIZATION}}

[How is access control implemented?]

#### Data Protection

{{DATA_PROTECTION}}

[How is sensitive data protected?]

### 8.9 Safety

{{SAFETY}}

[If relevant: How does the system ensure safety requirements?]

### 8.10 Communications

{{COMMUNICATIONS}}

[How do building blocks communicate with each other? Which protocols are used?]

### 8.11 Plausibility Checks

{{PLAUSIBILITY_CHECKS}}

[How does the system validate input data?]

### 8.12 Business Rules

{{BUSINESS_RULES}}

[Where and how are business rules implemented?]

### 8.13 Configurability

{{CONFIGURABILITY}}

[How is the system configured? Which parameters can be changed at runtime?]

### 8.14 Parallelization and Threading

{{PARALLELIZATION_THREADING}}

[How does the system handle concurrent access? Which threading models are used?]

### 8.15 Internationalization

{{INTERNATIONALIZATION}}

[How does the system support multiple languages and locales?]

### 8.16 Migration

{{MIGRATION}}

[How is data migrated between system versions?]

### 8.17 Testability

{{TESTABILITY}}

[How is the system designed for testability? Which testing strategies are used?]

### 8.18 Scaling

{{SCALING}}

[How does the system scale? Which scaling strategies are implemented?]

### 8.19 High Availability

{{HIGH_AVAILABILITY}}

[How does the system ensure high availability?]

### 8.20 Code Generation

{{CODE_GENERATION}}

[If relevant: Which parts of the system are generated? Which tools are used?]

### 8.21 Build Management

{{BUILD_MANAGEMENT}}

[How is the system built and deployed? Which build tools are used?]

## 9. Design Decisions

{{DESIGN_DECISIONS}}

[Important, expensive, risky, critical or unusual design decisions including rationales.]

### 9.1 Decision 1: {{DECISION_1_TITLE}}

**Status:** {{DECISION_1_STATUS}}
**Date:** {{DECISION_1_DATE}}

**Problem:** {{DECISION_1_PROBLEM}}

**Decision:** {{DECISION_1_DECISION}}

**Rationale:** {{DECISION_1_RATIONALE}}

**Consequences:** {{DECISION_1_CONSEQUENCES}}

### 9.2 Decision 2: {{DECISION_2_TITLE}}

**Status:** {{DECISION_2_STATUS}}
**Date:** {{DECISION_2_DATE}}

**Problem:** {{DECISION_2_PROBLEM}}

**Decision:** {{DECISION_2_DECISION}}

**Rationale:** {{DECISION_2_RATIONALE}}

**Consequences:** {{DECISION_2_CONSEQUENCES}}

## 10. Quality Requirements

{{QUALITY_REQUIREMENTS}}

[This section contains all quality requirements as quality tree with scenarios. The most important ones have already been described in section 1.2. (quality goals).]

### 10.1 Quality Tree

{{QUALITY_TREE}}

[Quality tree with quality/evaluation scenarios as leafs.]

### 10.2 Quality Scenarios

{{QUALITY_SCENARIOS}}

#### Performance

| Scenario | Response Measure |
|----------|------------------|
| {{PERF_SCENARIO_1}} | {{PERF_MEASURE_1}} |
| {{PERF_SCENARIO_2}} | {{PERF_MEASURE_2}} |

#### Availability

| Scenario | Response Measure |
|----------|------------------|
| {{AVAIL_SCENARIO_1}} | {{AVAIL_MEASURE_1}} |
| {{AVAIL_SCENARIO_2}} | {{AVAIL_MEASURE_2}} |

#### Security

| Scenario | Response Measure |
|----------|------------------|
| {{SEC_SCENARIO_1}} | {{SEC_MEASURE_1}} |
| {{SEC_SCENARIO_2}} | {{SEC_MEASURE_2}} |

## 11. Risks and Technical Debts

{{RISKS_TECHNICAL_DEBTS}}

[A list of identified technical risks or technical debts, ordered by priority]

| Risk/Debt | Probability | Impact | Action |
|-----------|-------------|--------|--------|
| {{RISK_1}} | {{PROB_1}} | {{IMPACT_1}} | {{ACTION_1}} |
| {{RISK_2}} | {{PROB_2}} | {{IMPACT_2}} | {{ACTION_2}} |

## 12. Glossary

{{GLOSSARY}}

[The most important domain and technical terms that your stakeholders use when discussing the system.]

| Term | Definition |
|------|------------|
| {{TERM_1}} | {{DEFINITION_1}} |
| {{TERM_2}} | {{DEFINITION_2}} |
| {{TERM_3}} | {{DEFINITION_3}} |

---

*This document follows the Arc42 template for architecture communication. More information: <https://arc42.org>*
