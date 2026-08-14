**# HexLoyal — Reward & Customer Loyalty Platform**

\> A scalable, multi-tenant SaaS platform for local businesses that
\> rewards customers for verified in-store visits and provides a controlled
\> reward-claim workflow with configurable optional/required engagement tasks.

![Status]\(https\://img.shields.io/badge/status-in%20development-orange)
![Architecture]\(https\://img.shields.io/badge/architecture-multi--tenant-blue)
![Frontend]\(https\://img.shields.io/badge/frontend-Next.js%20%2B%20TypeScript-black)
![Backend]\(https\://img.shields.io/badge/backend-NestJS-red)
![Database]\(https\://img.shields.io/badge/database-PostgreSQL-blue)
![Theme]\(https\://img.shields.io/badge/theme-Beige%20%7C%20Brown%20%7C%20Gold-amber)
![License]\(https\://img.shields.io/badge/license-MIT-green.svg)

**\*\*HexLoyal (Rewards.io)\*\*** is an enterprise-grade, multi-tenant Smart Reward and Item Confirmation platform designed to bridge the gap between business operations and customer loyalty. Featuring a warm luxury design system (**\*\*Beige, Brown, and Gold\*\***), dynamic reward calculations, real-time item tracker verifications, electronic signature vouchers, seamless Google OAuth integration, and instant push notifications, HexLoyal modernizes customer engagement for businesses of all scales.

\---

**## 🎨 Theme & Color Palette**

HexLoyal uses a **\*\*Warm Luxury\*\*** aesthetic built around three core colors, each with multiple shades:

\| Color | Shade | Hex Value | Usage |
\| :---- | :---- | :-------- | :---- |
\| **\*\*Beige\*\*** | Light | \`#FAF5EE\` | Page backgrounds & clean canvas |
\| **\*\*Beige\*\*** | Base | \`#E6D7C3\` | Container cards & panel backgrounds |
\| **\*\*Beige\*\*** | Dark | \`#D4C4A8\` | Subtle elevation & hover states |
\| **\*\*Brown\*\*** | Light | \`#8C6246\` | Secondary text & structural borders |
\| **\*\*Brown\*\*** | Base | \`#5C3D2E\` | Sub-headers & primary text |
\| **\*\*Brown\*\*** | Dark | \`#23120C\` | Deep contrast panels & dark mode backdrops |
\| **\*\*Gold\*\*** | Light | \`#F7E59D\` | Highlight glows & soft accents |
\| **\*\*Gold\*\*** | Base | \`#D4AF37\` | Primary CTA buttons & active badges |
\| **\*\*Gold\*\*** | Dark | \`#B59021\` | Reward point indicators & pressed states |

\---

**## 📋 Table of Contents**

1\.  [Project Overview](#-project-overview)
2\.  [Product Vision](#-product-vision)
3\.  [Core Principles](#-core-principles)
4\.  [User Roles & Access Control](#-user-roles--access-control)
5\.  [System Modules](#-system-modules)
6\.  [Reward System](#-reward-system)
7\.  [Reward Claim Workflow](#-reward-claim-workflow)
8\.  [Business QR & Check-In System](#-business-qr--check-in-system)
9\.  [Reward Tasks](#-reward-tasks)
10\. [Tracker / Confirmation System](#-tracker--confirmation-system)
11\. [Authentication](#-authentication)
12\. [Multi-Tenant Architecture](#-multi-tenant-architecture)
13\. [System Architecture](#-system-architecture)
14\. [Technology Stack](#-technology-stack)
15\. [Project Structure](#-project-structure)
16\. [Getting Started](#-getting-started)
17\. [Environment Variables](#-environment-variables)
18\. [Database Design](#-database-design)
19\. [API Design](#-api-design)
20\. [Frontend Architecture](#-frontend-architecture)
21\. [Notification Architecture](#-notification-architecture)
22\. [Security & Compliance](#-security--compliance)
23\. [Error Handling](#-error-handling)
24\. [Testing Strategy](#-testing-strategy)
25\. [Performance & Scalability](#-performance--scalability)
26\. [Development Workflow](#-development-workflow)
27\. [Deployment](#-deployment)
28\. [CI/CD](#-cicd)
29\. [Development Roadmap](#-development-roadmap)
30\. [MVP Scope](#-mvp-scope)
31\. [Future Roadmap](#-future-roadmap)
32\. [Troubleshooting](#-troubleshooting)
33\. [License](#-license)

\---

**## 💡 Project Overview**

HexLoyal is a web-based customer loyalty and reward management platform designed for local businesses.

The platform has three primary actors:

\- **\*\*Customer\*\*** — End-user earning loyalty points through verified visits, completing optional/required reward tasks, and claiming rewards
\- **\*\*Shop Owner (Business Manager)\*\*** — Primary business operator with full control over loyalty rules, check-in settings, rewards, and reward tasks
\- **\*\*Platform Administrator\*\*** — Central administrator governing system health and global configurations

The system allows businesses to configure a loyalty program that awards loyalty points primarily for **\*\*verified in-store visits/presence\*\***. Customers check in by scanning a business QR code, signing in, and passing a backend geolocation check. A successful verified visit can award one loyalty point for the configured visit period (normally one point per customer per day).

**### What Customers Can Do**

- Sign in with Google
- Manage their own profile
- Join/participate in a business loyalty program
- Scan a business QR code to initiate a store check-in
- Grant location permission and complete geolocation verification
- Earn loyalty points for verified visits
- View loyalty points, visit history, available rewards, and reward history
- View current visit streak/consistency progress
- View reward tasks and their optional/required status
- Complete required tasks before claiming rewards when configured by the Shop Owner
- Complete optional tasks without being blocked from claiming a reward
- Submit proof for tasks when required
- Request a reward claim & view claim status
- Receive real-time push notifications and web alerts
- View special business offers
- Review and accept incoming item tracker confirmation requests

**### What Shop Owners Can Do**

- Manage their business profile and settings
- Configure loyalty visit rules and check-in settings
- Configure the business geofence/radius used for visit verification
- Generate and manage business check-in QR codes
- View customers and verified visit history
- Configure loyalty thresholds and create rewards
- Configure reward tasks and set each task as **\*\*OPTIONAL\*\*** or **\*\*REQUIRED\*\***
- Decide whether a required task must be completed before a reward can be claimed
- Review task submissions/proof when verification is required
- Approve or reject reward claims & view reward history
- Issue item tracker requests and manage offers
- View business-specific loyalty analytics and reports

**### What Platform Administrators Can Do**

\- Manage businesses and platform users
\- Manage subscriptions and monitor system activity
\- View system-wide analytics and configure platform settings
\- Review audit logs and handle platform support

\> **\*\*Note:\*\*** There is intentionally **\*\*no employee role\*\*** in the current system. All business-side operations are managed by the Shop Owner.

\---

**## 🔭 Product Vision**

HexLoyal is not built as a single-shop application. It is built as a **\*\*multi-tenant SaaS platform\*\*** capable of supporting many independent businesses from the same application.

\`\`\`
                         HEXLOYAL
                            |
          +-----------------+-----------------+
          |                 |                 |
          v                 v                 v
      CUSTOMER         SHOP OWNER        ADMINISTRATOR
      PLATFORM          PLATFORM           PLATFORM
          |                 |                 |
          +-----------------+-----------------+
                            |
                            v
                      CORE SERVICES
                            |
       +--------------------+--------------------+
       |          |          |          |        |
       v          v          v          v        v
    Auth      Rewards    Transactions Notifications Audit
                            |
                            v
                        PostgreSQL
\`\`\`

\---

**## 🏛️ Core Principles**

The following principles are **\*\*mandatory\*\*** and must never be violated.

**### 1. Verified Store Presence**

The primary loyalty event is a verified customer visit. A customer can earn a loyalty point only after the backend confirms that the customer is authenticated, the business check-in QR is valid, and the customer is physically within the configured business geofence.

**### 2. Customer Owns Their Account**

Customers manage their own account and Google authentication. The Shop Owner can view loyalty information but does not manage customer credentials.

**### 3. Shop Owner Controls the Loyalty Program**

The Shop Owner controls visit rules, reward thresholds, reward items, check-in settings, geofence radius, and reward-task requirements for their business.

**### 4. Strict Tenant Isolation**

A business can only access its own business data.

**### 5. Ledger-Based Rewards**

The current point balance must be derived from an auditable reward ledger. Every point change needs a reason, such as a verified visit or reward redemption.

**### 6. Idempotency / Duplicate Check-In Protection**

The same customer must not receive multiple loyalty points for repeated scans during the same configured visit period. Check-ins must be safely deduplicated on the backend.

**### 7. Backend Authorization**

Security must be enforced on the backend. Hiding frontend buttons is not authorization.

**### 8. QR + Geolocation Verification**

A business QR scan starts a check-in attempt but does not automatically award points. The backend must verify the authenticated customer, business/branch QR, geolocation, check-in eligibility, and duplicate-check-in rules before creating a loyalty point.

**### 9. Group Visit Rewards**

Every authenticated customer who independently completes a verified check-in can earn the visit point. The person who pays does not receive exclusive loyalty credit.

Example: four people visit a café together. All four scan the business QR and pass verification, so all four receive one loyalty point.

**### 10. Configurable Reward Tasks**

A Shop Owner may create tasks associated with rewards. Each task must be configurable as either **\*\*OPTIONAL\*\*** or **\*\*REQUIRED\*\***. Required tasks become conditions for claiming the associated reward; optional tasks never block the reward claim.

**### 11. Loyalty Rewards Focus on Consistency**

The primary objective is to reward customers for repeatedly visiting a business. The Shop Owner defines the number of verified visit points required and the special item/reward unlocked at that threshold.

**## 👥 User Roles & Access Control**

**### 🛡️ Platform Administrator**

Central administrator governing system health, business onboarding, and global configurations.

\| Can | Cannot |
\| :-- | :----- |
\| Manage businesses & platform users | Bypass audit logging |
\| Manage subscriptions | — |
\| Monitor system activity & view system-wide analytics | — |
\| Configure platform settings | — |
\| Review audit logs | — |
\| Handle platform support & maintenance | — |

**### 💼 Business Manager (Shop Owner)**

Primary business operator with full operational control over their business instance.

\| Can | Cannot |
\| :-- | :----- |
\| Manage business profile & settings | Access another business |
\| Configure reward rules & manage rewards | Access Administrator-only functionality |
\| View business customers & verified transactions | Change customer authentication credentials |
\| Approve / reject reward claims | Bypass reward ledger rules |
\| View reward history & customer balances | Create points without a valid transaction |
\| Issue tracker requests & manage offers | — |
\| View analytics & send notifications | — |

**### 👤 Customer (User)**

End-user earning rewards and confirming transactions/items.

\| Can | Cannot |
\| :-- | :----- |
\| Google Sign-In & manage profile | Add points manually |
\| View own rewards, transactions & history | Modify verified transactions |
\| Request eligible rewards & view claim status | Approve claims |
\| Receive notifications & view offers | Access another customer's data |
\| Access permanent QR & accept tracker requests | Access Owner or Admin dashboards |

\---

**## 🧩 System Modules**

```
                         ┌─────────────────────────────────────────┐
                         │          HexLoyal Core Platform        │
                         └────────────────────┬────────────────────┘
                                              │
       ┌──────────────────┬───────────────────┼───────────────────┬───────────────────┐
       ▼                  ▼                   ▼                   ▼                   ▼
 ┌───────────┐      ┌───────────┐      ┌────────────┐      ┌───────────┐      ┌───────────┐
 │ Auth &    │      │ Visit /   │      │ Reward     │      │ Push &    │      │ Admin &   │
 │ Identity  │      │ Check-In  │      │ Engine     │      │ Socket    │      │ Analytics │
 └───────────┘      └───────────┘      └────────────┘      └───────────┘      └───────────┘
                         │                   │
                         └──────────┬────────┘
                                    ▼
                              PostgreSQL / Redis
```

| # | Module | Key Capabilities |
| :- | :----- | :-------------- |
| 1 | **\*\*Authentication\*\*** | Google OAuth, session/token management, role assignment, account linking, logout |
| 2 | **\*\*Business Management\*\*** | Registration, profile, branches, status, settings, subscription |
| 3 | **\*\*Customer Management\*\*** | Profile, business/customer relationship, lookup, loyalty summary |
| 4 | **\*\*Visit / Check-In Management\*\*** | Business QR, geolocation verification, geofence, attendance, duplicate protection |
| 5 | **\*\*Reward Engine\*\*** | Visit-based rules, point calculation, ledger, eligibility, balance |
| 6 | **\*\*Reward Management\*\*** | Creation, availability, thresholds, activation/deactivation |
| 7 | **\*\*Reward Tasks\*\*** | Task creation, OPTIONAL/REQUIRED configuration, proof submission, verification |
| 8 | **\*\*Reward Claims\*\*** | Claim request, task eligibility, owner approval/rejection, redemption, history |
| 9 | **\*\*Business QR System\*\*** | Secure check-in QR, business/branch binding, rotation, validation |
| 10 | **\*\*Notification System\*\*** | Visit, reward, task, claim, and tracker notifications |
| 11 | **\*\*Tracker / Confirmation\*\*** | Business item requests, user review & acceptance, confirmation storage |
| 12 | **\*\*Analytics\*\*** | Visits, returning customers, streaks, points issued, rewards claimed, retention |
| 13 | **\*\*Audit\*\*** | Check-ins, geolocation verification, reward changes, task decisions, claim events |

\---

**## 🎁 Reward System**

### Loyalty Model

HexLoyal rewards **customer consistency and verified visits**, not payment amount. The primary earning event is a successful store check-in.

```
Customer visits business
        ↓
Scans business QR
        ↓
Authenticates
        ↓
Geolocation verified
        ↓
Visit accepted
        ↓
+1 Loyalty Point
```

### Visit Reward Rule

The Shop Owner defines the visit rule. The default MVP behavior is:

```
1 verified visit = 1 loyalty point
```

The system should prevent multiple points from repeated scans during the same configured visit period. By default, this is **one point per customer per business day**, unless the business configures another supported period.

### Reward Threshold

The Shop Owner defines how many loyalty points are required to unlock a reward. Example:

```
10 verified visits = 1 special reward item
```

### Group Visits

Points are tied to verified customer presence, not the payer. If four customers visit a café and all four independently complete a verified check-in, all four receive one loyalty point.

### Reward Ledger

Never rely only on a mutable `points` column without a transaction history.

```
+----------------------+--------+--------------------------+
| Event                | Points | Reference                |
+----------------------+--------+--------------------------+
| Verified Store Visit | +1     | VISIT-10001              |
| Verified Store Visit | +1     | VISIT-10002              |
| Reward Redemption    | -10    | CLAIM-20001              |
+----------------------+--------+--------------------------+

Current Balance = 0
```

Every entry must include: business, customer, points, entry type, reference, timestamp, and actor/system source.

### Reward Rule Model

Recommended fields:

```
rule_type, points_per_visit, visit_period,
minimum_visits, maximum_points_per_period, active,
start_at, end_at
```

Future rule types can be added later without changing the core visit-based MVP. Purchase/order-based loyalty is intentionally **not part of the current reward model** and can be reconsidered separately in the future.

**## 🔄 Reward Claim Workflow**

```mermaid
sequenceDiagram
    autonumber
    actor Cust as Customer
    participant Sys as HexLoyal Backend
    actor BM as Shop Owner

    Cust->>Sys: Request Reward
    Sys->>Sys: Authenticate customer
    Sys->>Sys: Confirm business membership
    Sys->>Sys: Check loyalty-point eligibility
    Sys->>Sys: Load associated reward tasks
    alt Required task incomplete
        Sys-->>Cust: Reward blocked until required task is completed
    else Eligible
        Sys->>Sys: Create claim (prevent duplicates)
        Sys->>BM: Notification — "Pending Reward Claim"
        BM->>Sys: Approve or Reject
        alt Approved
            Sys->>Sys: Verify claim still pending
            Sys->>Sys: Lock & atomically update
            Sys->>Sys: Deduct points & create ledger entry
            Sys->>Sys: Mark claim as CLAIMED
            Sys->>Cust: Notification — "Reward Approved"
            Sys->>Sys: Create audit log
        else Rejected
            Sys->>Sys: Mark claim as REJECTED
            Sys->>Cust: Notification — "Reward Rejected"
        end
    end
```

### Claim State Machine

```
AVAILABLE → TASK_PENDING → REQUESTED → APPROVED → CLAIMED
                  │                         ↘ REJECTED
                  └── Optional tasks do not block REQUESTED
```

**## 📱 Business QR & Check-In System**

Each business/branch has a secure check-in QR code. The QR identifies the business or branch and starts the customer attendance flow. It is **not** a permanent customer QR and must not contain sensitive customer information.

### Check-In Flow

```mermaid
flowchart TD
    A[Customer enters business] --> B[Scan Business QR]
    B --> C[Open HexLoyal Check-In Page]
    C --> D[Authenticate Customer]
    D --> E[Request Geolocation]
    E --> F{Inside Configured Geofence?}
    F -->|No| G[Reject Check-In]
    F -->|Yes| H{Already Checked In for Period?}
    H -->|Yes| I[Show Existing Visit]
    H -->|No| J[Record Verified Visit]
    J --> K[Create +1 Ledger Entry]
    K --> L[Update Loyalty Balance]
```

### Geolocation Rules

- Customer must grant browser location permission for check-in.
- Backend validates the submitted location against the business/branch coordinates.
- Shop Owner can configure the allowed geofence radius.
- A check-in outside the geofence is rejected.
- The QR must be associated with the correct business/branch.
- Location data should be minimized and retained according to the platform's privacy policy.
- Geolocation is a verification signal, not a replacement for authentication.

### Duplicate Check-In Protection

```
Scan 1 → Location verified → +1 point
Scan 2 → Same visit period → No additional point
Scan 20 → Same visit period → No additional point
```

The backend must enforce uniqueness for the customer/business/visit-period combination.

### Group Visit Example

```
4 customers enter café
        ↓
Each customer scans the business QR
        ↓
Each customer's location is verified
        ↓
Customer A → +1
Customer B → +1
Customer C → +1
Customer D → +1
```

The payment payer does not receive exclusive points. Every verified participant can earn their own visit point.

### QR Security

- QR payload must use an opaque business/branch identifier or signed token.
- Do not place customer email, phone, balance, or other sensitive information inside the QR.
- QR tokens should be revocable/rotatable if required.
- Rate-limit check-in attempts.
- Log successful and rejected check-in attempts for audit and abuse investigation.

**## 📝 Reward Tasks**

Reward tasks allow a Shop Owner to attach an activity to a reward. The owner decides whether each task is optional or required.

### Task Requirement Types

| Requirement | Customer Behavior | Reward Impact |
| :--- | :--- | :--- |
| **OPTIONAL** | Customer may complete the task or skip it | Does not block reward claim |
| **REQUIRED** | Customer must complete the task | Blocks reward claim until satisfied |

### Example Tasks

- Leave a business review
- Complete a feedback form
- Follow the business on Instagram
- Create/share a social-media post
- Submit another owner-defined engagement action

The exact task types and verification methods can be expanded later.

### Owner Configuration

When creating a task, the Shop Owner configures:

```
task_name
description
task_type
requirement: OPTIONAL | REQUIRED
proof_required
verification_method
active
start_at
end_at
```

### Required Task Flow

```
Customer reaches reward threshold
        ↓
Required task is displayed
        ↓
Customer completes task
        ↓
Customer submits proof if required
        ↓
System/Owner verifies task
        ↓
Reward becomes claimable
```

### Optional Task Flow

```
Customer reaches reward threshold
        ↓
Optional task is displayed
        ↓
Customer may complete it
        ↓
Reward remains claimable either way
```

A task does not automatically generate loyalty points. Points remain tied to verified visits.

**## 📦 Tracker / Confirmation System**

The Tracker module is intentionally simple. The goal is to record: *\*"Business sent N items, and the user confirmed receiving N items."\**

\`\`\`mermaid
sequenceDiagram
    autonumber
    actor BM as Business Manager
    participant Sys as HexLoyal Backend
    actor Cust as Customer

    BM->>Sys: Create Request (Item Name, Quantity, Remarks)
    Sys->>Cust: Dispatch Notification ("Tracker Request Received")
    Cust->>Sys: Open Dashboard & Review Request
    Cust->>Sys: Click "Accept"
    Sys->>Sys: Save Confirmation permanently (Immutable log)
    Sys-->>BM: Dispatch Confirmation Notification ("Request Accepted")
\`\`\`

**\*\*Tracker Data Model:\*\***

\`\`\`
id, business\_id, sender\_user\_id, receiver\_user\_id,
item\_name, quantity, remarks, status,
created\_at, accepted\_at, accepted\_by
\`\`\`

Status values: \`PENDING\`, \`ACCEPTED\`

\---

**## 🔑 Authentication**

Google Sign-In is the primary customer authentication method.

\`\`\`
Browser → Google Sign-In → Identity Provider → Backend Token Verification
→ Find/Create User → Determine Role → Authorize Dashboard
\`\`\`

\- **\*\*Authentication\*\*** answers: *\*Who are you?\**
\- **\*\*Authorization\*\*** answers: *\*What are you allowed to do?\**

Both are required.

\---

**## 🏢 Multi-Tenant Architecture**

HexLoyal is a multi-tenant SaaS application. A **\*\*tenant\*\*** represents a **\*\*business\*\***.

All business-owned records must be associated with a tenant:

\`\`\`
businesses, customers/business\_customers, transactions, reward\_rules,
rewards, reward\_ledger, reward\_claims, offers, tracker\_requests, notifications
\`\`\`

**### Tenant Isolation Rule**

Every business query **\*\*must\*\*** include the authenticated business context.

\`\`\`sql
*-- ❌ Bad*
SELECT \* FROM reward\_claims WHERE id = $1;

*-- ✅ Good*
SELECT \* FROM reward\_claims WHERE id = $1 AND business\_id = $2;
\`\`\`

Never trust a \`business\_id\` sent by the browser without validating that the authenticated Shop Owner actually belongs to that business.

\---

**## 🏗️ System Architecture**

```
                         Client Applications
                                  |
              +-------------------+-------------------+
              |                                       |
              v                                       v
       Customer Web App                         Owner/Admin Web App
              |                                       |
              +-------------------+-------------------+
                                  |
                                  v
                           API / BFF Layer
                                  |
                           Authentication
                                  |
              +-----------------+-----------------+
              |                 |                 |
              v                 v                 v
        User Service      Check-In Service   Reward Service
              |                 |                 |
              |                 |                 +-------- Reward Tasks
              |                 |
              |                 +-------- Geolocation / Geofence
              |
              +-----------------+-----------------+
                                |
                     +----------+----------+
                     |                     |
                     v                     v
                 PostgreSQL              Redis
                     |
                     v
             Notification Service
                     |
               +-----+-----+
               |           |
               v           v
             Push        Email
```

> For the MVP, these services can exist as modules inside one backend application. Do not create unnecessary microservices too early.

\---

**## 💻 Technology Stack**

\| Layer | Technology | Rationale |
\| :--- | :--- | :--- |
\| **\*\*Frontend Framework\*\*** | **\*\*Next.js 14+ / React 18\*\*** | SSR/SSG capabilities, optimal SEO, fast routing, app directory |
\| **\*\*Language\*\*** | **\*\*TypeScript\*\*** | Strict type safety across client and server contracts |
\| **\*\*Styling\*\*** | **\*\*Tailwind CSS\*\*** | Utility-first CSS for rapid UI development and modern aesthetic |
\| **\*\*Form Handling\*\*** | **\*\*React Hook Form + Zod\*\*** | Performant forms with schema-based validation |
\| **\*\*Data Fetching\*\*** | **\*\*TanStack Query\*\*** | Server state management with caching and auto-refresh |
\| **\*\*Backend Framework\*\*** | **\*\*Node.js + NestJS\*\*** | Enterprise modular architecture, built-in dependency injection |
\| **\*\*Database\*\*** | **\*\*PostgreSQL\*\*** | Relational integrity, JSONB support, transactional reliability |
\| **\*\*ORM\*\*** | **\*\*Prisma / TypeORM\*\*** | Type-safe query generation and migration management |
\| **\*\*Authentication\*\*** | **\*\*Firebase Auth & Google OAuth\*\*** | Industry-standard identity management and seamless SSO |
\| **\*\*Cache / Queue\*\*** | **\*\*Redis + BullMQ\*\*** | In-memory caching and reliable job queue processing |
\| **\*\*Notifications\*\*** | **\*\*Firebase Cloud Messaging (FCM)\*\*** | Cross-platform web and mobile push delivery |
\| **\*\*Real-Time\*\*** | **\*\*Socket.IO / WebSocket\*\*** | Bi-directional low-latency event messaging for dashboards |
\| **\*\*Storage\*\*** | **\*\*S3-compatible object storage\*\*** | Scalable file and asset storage |
\| **\*\*Containerization\*\*** | **\*\*Docker & Docker Compose\*\*** | Reproducible builds across development, staging, and production |
\| **\*\*Reverse Proxy\*\*** | **\*\*Nginx\*\*** | Load balancing, SSL termination, and static asset caching |
\| **\*\*Observability\*\*** | **\*\*Sentry, Prometheus, Grafana\*\*** | Error tracking, metrics, and centralized structured logs |
\| **\*\*Deployment\*\*** | **\*\*AWS / Azure / DigitalOcean / VPS\*\*** | Scalable infrastructure with automated CI/CD pipelines |

\---

**## 📁 Project Structure**

\`\`\`
HexLoyal/
├── apps/
│   ├── web/                         # Next.js Frontend Application
│   │   ├── src/
│   │   │   ├── app/                 # Next.js App Router (pages & layouts)
│   │   │   │   ├── (admin)/         # Platform Administrator Dashboard
│   │   │   │   ├── (business)/      # Business Manager Portal
│   │   │   │   └── (customer)/      # Customer Portal
│   │   │   ├── components/          # Reusable UI Components
│   │   │   ├── features/            # Feature-based modules
│   │   │   │   ├── auth/
│   │   │   │   ├── customer/
│   │   │   │   ├── owner/
│   │   │   │   ├── rewards/
│   │   │   │   ├── claims/
│   │   │   │   ├── transactions/
│   │   │   │   ├── tracker/
│   │   │   │   ├── notifications/
│   │   │   │   └── analytics/
│   │   │   ├── hooks/               # Custom React Hooks
│   │   │   ├── lib/                 # Shared utilities
│   │   │   ├── services/            # API Client Services
│   │   │   └── styles/              # Global Styles & Tailwind Config
│   │   ├── public/                  # Static Assets
│   │   └── middleware.ts
│   │
│   └── api/                         # NestJS Backend API Service
│       ├── src/
│       │   ├── modules/
│       │   │   ├── auth/            # OAuth, Firebase & JWT Module
│       │   │   ├── users/           # User Management Module
│       │   │   ├── businesses/      # Business Management Module
│       │   │   ├── customers/       # Customer Management Module
│       │   │   ├── transactions/    # Transaction Processing Module
│       │   │   ├── rewards/         # Reward Engine & Claim Module
│       │   │   ├── tracker/         # Item Confirmation Module
│       │   │   ├── notifications/   # FCM & Socket.IO Gateway Module
│       │   │   ├── analytics/       # Analytics Module
│       │   │   ├── audit/           # Audit Logging Module
│       │   │   └── admin/           # Platform Administration Module
│       │   ├── common/              # Guards, Interceptors, Filters, Pipes
│       │   └── database/            # Prisma/TypeORM Schema & Migrations
│       └── test/                    # End-to-End & Integration Tests
│
├── packages/
│   ├── ui/                          # Shared UI component library
│   ├── config/                      # Shared configuration
│   ├── types/                       # Shared TypeScript types
│   ├── validation/                  # Shared validation schemas
│   └── eslint-config/               # Shared linting configuration
│
├── prisma/
│   ├── schema.prisma
│   ├── migrations/
│   └── seed.ts
│
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── database/
│   ├── security/
│   └── product/
│
├── docker/                          # Docker Configuration & Nginx Specs
│   ├── Dockerfile.web
│   ├── Dockerfile.api
│   └── nginx.conf
│
├── scripts/
├── .github/workflows/
├── .env.example
├── docker-compose.yml
├── package.json
├── pnpm-workspace.yaml
├── turbo.json
└── README.md
\`\`\`

\---

**## 🚀 Getting Started**

**### Prerequisites**

Ensure you have the following installed:

\- **\*\*Node.js\*\***: \`v18.x\` or \`v20.x\` (LTS)
\- **\*\*pnpm\*\***: \`v9.x\` (preferred) or npm
\- **\*\*PostgreSQL\*\***: \`v15+\`
\- **\*\*Redis\*\***
\- **\*\*Docker & Docker Compose\*\*** (optional, for containerized execution)
\- **\*\*Git\*\***

**### Installation & Local Setup**

1\. **\*\*Clone the Repository\*\***
   \`\`\`bash
   git clone https\://github.com/Gyrobird/Reqards.io.git
   cd Reqards.io
   \`\`\`

2\. **\*\*Install Dependencies\*\***
   \`\`\`bash
   pnpm install
   \`\`\`

3\. **\*\*Start Local Infrastructure\*\***
   \`\`\`bash
   docker compose up -d
   \`\`\`

4\. **\*\*Run Database Migrations\*\***
   \`\`\`bash
   pnpm db\:migrate
   \`\`\`

5\. **\*\*Seed Development Data\*\***
   \`\`\`bash
   pnpm db\:seed
   \`\`\`

6\. **\*\*Start Development Servers\*\***
   \`\`\`bash
   pnpm dev
   \`\`\`
   - Frontend: \`http\://localhost:3000\`
   - Backend API: \`http\://localhost:4000\`
   - API Documentation (Swagger): \`http\://localhost:4000/api/docs\`

**### Docker Setup**

To launch the full stack environment (PostgreSQL, Backend API, Frontend Web, Nginx):

\`\`\`bash
docker-compose up -d --build
\`\`\`

\---

**## 🔐 Environment Variables**

Create \`.env\` from \`.env.example\`. **\*\*Never commit\*\*** \`.env\`, private keys, OAuth secrets, database passwords, API keys, or service-account credentials.

**### Backend (**\`apps/api/.env\`**)**

\`\`\`env
PORT=4000
NODE\_ENV=development

DATABASE\_URL="postgresql://postgres\:postgres\@localhost:5432/hexloyal\_db?schema=public"
REDIS\_URL=

\# JWT Configuration
JWT\_SECRET=your\_super\_secret\_jwt\_key
JWT\_EXPIRES\_IN=7d

\# Google OAuth
GOOGLE\_CLIENT\_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE\_CLIENT\_SECRET=your-google-client-secret
AUTH\_SECRET=

\# Firebase Credentials
FIREBASE\_PROJECT\_ID=hexloyal-prod
FIREBASE\_CLIENT\_EMAIL=firebase-adminsdk\@hexloyal-prod.iam.gserviceaccount.com
FIREBASE\_PRIVATE\_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----"

\# Storage
STORAGE\_BUCKET=
STORAGE\_REGION=
STORAGE\_ACCESS\_KEY=
STORAGE\_SECRET\_KEY=

\# CORS
CORS\_ORIGIN=http\://localhost:3000

\# Observability
SENTRY\_DSN=
\`\`\`

**### Frontend (**\`apps/web/.env.local\`**)**

\`\`\`env
NEXT\_PUBLIC\_APP\_URL=http\://localhost:3000
NEXT\_PUBLIC\_API\_BASE\_URL=http\://localhost:4000/api/v1
NEXT\_PUBLIC\_SOCKET\_URL=http\://localhost:4000
NEXT\_PUBLIC\_FIREBASE\_API\_KEY=your-firebase-api-key
NEXT\_PUBLIC\_FIREBASE\_AUTH\_DOMAIN=hexloyal-prod.firebaseapp.com
NEXT\_PUBLIC\_FIREBASE\_PROJECT\_ID=hexloyal-prod
NEXT\_PUBLIC\_GOOGLE\_CLIENT\_ID=your-google-client-id.apps.googleusercontent.com
\`\`\`

\---

**## 🗃️ Database Design**

**### Core Entities**

```
User, Business, BusinessBranch, BusinessCustomer, CheckInQR, Visit,
RewardRule, Reward, RewardTask, RewardTaskSubmission, RewardLedger,
RewardClaim, TrackerRequest, Notification, AuditLog, Subscription
```

**### Entity Relationship Diagram**

```
User
 |
 +--------------------+
 |                    |
 v                    v
Business Owner     Customer
 |                    |
 v                    |
Business <---- BusinessCustomer
 |
 +-------- BusinessBranch
 |              |
 |              +-------- CheckInQR
 |              |
 |              +-------- Visit -------- Customer
 |
 +-------- RewardRule
 |
 +-------- Reward ---- RewardTask ---- RewardTaskSubmission ---- Customer
 |
 +-------- RewardClaim ---- Customer
 |
 +-------- RewardLedger
 |
 +-------- TrackerRequest
 |
 +-------- Notification
 |
 +-------- AuditLog
```

**### Table Schemas**

<details>
<summary><strong>users</strong></summary>

```
id, google\_subject, email, name, avatar\_url, role, status, created\_at, updated\_at
```
`google\_subject` uniquely identifies the authenticated Google identity.
</details>

<details>
<summary><strong>businesses</strong></summary>

```
id, owner\_user\_id, name, slug, status, created\_at, updated\_at
```
</details>

<details>
<summary><strong>business\_customers</strong></summary>

```
id, business\_id, customer\_user\_id, customer\_code, status, joined\_at, created\_at, updated\_at
```
Unique constraint: `(business\_id, customer\_user\_id)`
</details>

<details>
<summary><strong>business\_branches</strong></summary>

```
id, business\_id, name, latitude, longitude, geofence\_radius\_meters,
status, created\_at, updated\_at
```
</details>

<details>
<summary><strong>check\_in\_qrs</strong></summary>

```
id, business\_id, branch\_id, token\_hash, active, created\_at, updated\_at, rotated\_at
```
</details>

<details>
<summary><strong>visits</strong></summary>

```
id, business\_id, branch\_id, customer\_id, qr\_id,
checked\_in\_at, latitude, longitude, distance\_meters,
verification\_status, visit\_period\_key, created\_at
```
Unique constraint: `(business\_id, customer\_id, visit\_period\_key)`
</details>

<details>
<summary><strong>transactions</strong></summary>

```
id, business\_id, customer\_id, external\_reference, amount, currency,
payment\_status, verified\_at, created\_at, updated\_at
```
Payment transactions are retained as an operational/future integration concept; they are **not the current trigger for loyalty points**.

Unique constraint: `(business\_id, external\_reference)`
</details>

<details>
<summary><strong>reward\_rules</strong></summary>

```
id, business\_id, rule\_type, points\_per\_visit, visit\_period,
maximum\_points\_per\_period, active, start\_at, end\_at, created\_at, updated\_at
```
</details>

<details>
<summary><strong>rewards</strong></summary>

```
id, business\_id, name, description, points\_required, reward\_type,
reward\_value, active, created\_at, updated\_at
```
</details>

<details>
<summary><strong>reward\_tasks</strong></summary>

```
id, business\_id, reward\_id, name, description, task\_type,
requirement, proof\_required, verification\_method, active, start\_at, end\_at,
created\_at, updated\_at
```
`requirement` is either `OPTIONAL` or `REQUIRED`.
</details>

<details>
<summary><strong>reward\_task\_submissions</strong></summary>

```
id, business\_id, task\_id, reward\_claim\_id, customer\_id,
proof\_url, status, submitted\_at, reviewed\_at, reviewed\_by, review\_notes
```
Status values: `PENDING`, `APPROVED`, `REJECTED`.
</details>

<details>
<summary><strong>reward\_ledger</strong></summary>

```
id, business\_id, customer\_id, visit\_id, claim\_id, points,
entry\_type, description, created\_at
```
Use a signed `points` value or separate debit/credit fields consistently.
</details>

<details>
<summary><strong>reward\_claims</strong></summary>

```
id, business\_id, customer\_id, reward\_id, status, requested\_at,
approved\_at, approved\_by, rejected\_at, rejection\_reason, created\_at, updated\_at
```
</details>

<details>
<summary><strong>tracker\_requests</strong></summary>

```
id, business\_id, sender\_user\_id, receiver\_user\_id, item\_name,
quantity, remarks, status, created\_at, accepted\_at, accepted\_by
```
</details>

<details>
<summary><strong>notifications</strong></summary>

```
id, recipient\_user\_id, business\_id, type, title, message, read\_at, created\_at
```
</details>

<details>
<summary><strong>audit\_logs</strong></summary>

```
id, business\_id, actor\_user\_id, action, entity\_type, entity\_id, metadata, created\_at
```
</details>

**### Recommended Indexes**

```
users:                    google\_subject, email
businesses:               owner\_user\_id, slug
business\_customers:      business\_id, customer\_user\_id, customer\_code
business\_branches:       business\_id, status
check\_in\_qrs:            business\_id, branch\_id, active
visits:                   business\_id, customer\_id, branch\_id, checked\_in\_at, visit\_period\_key
transactions:              business\_id, customer\_id, external\_reference, created\_at
reward\_ledger:            business\_id, customer\_id, visit\_id, claim\_id
reward\_tasks:             business\_id, reward\_id, requirement, active
reward\_task\_submissions: business\_id, task\_id, customer\_id, status
reward\_claims:             business\_id, customer\_id, status
tracker\_requests:         business\_id, receiver\_user\_id, status
notifications:              recipient\_user\_id, created\_at
```

\---

**## 📡 API Design**

**\*\*Base URL:\\*\*** `\/api\/v1` — All APIs are versioned.

**### Authentication APIs**

```http
GET  /auth/me
POST /auth/logout
```

**### Customer APIs**

```http
GET   /customers/me
PATCH /customers/me
GET   /businesses
GET   /businesses/:businessId/rewards
GET   /businesses/:businessId/reward-balance
GET   /businesses/:businessId/reward-history
GET   /businesses/:businessId/visits
POST  /businesses/:businessId/check-ins
GET   /businesses/:businessId/claims
POST  /businesses/:businessId/claims
POST  /reward-tasks/:taskId/submit
GET   /notifications
PATCH /notifications/:id/read
```

**### Shop Owner APIs**

```http
GET   /owner/business
PATCH /owner/business

GET   /owner/customers
GET   /owner/customers/:customerId

GET   /owner/branches
POST  /owner/branches
PATCH /owner/branches/:id

GET   /owner/check-in-qr
POST  /owner/check-in-qr/rotate
GET   /owner/visits

GET   /owner/reward-rules
POST  /owner/reward-rules
PATCH /owner/reward-rules/:id

GET   /owner/rewards
POST  /owner/rewards
PATCH /owner/rewards/:id

GET   /owner/rewards/:rewardId/tasks
POST  /owner/rewards/:rewardId/tasks
PATCH /owner/rewards/:rewardId/tasks/:taskId

GET   /owner/task-submissions
POST  /owner/task-submissions/:id/approve
POST  /owner/task-submissions/:id/reject

GET   /owner/claims
POST  /owner/claims/:id/approve
POST  /owner/claims/:id/reject

GET   /owner/analytics
```

**### Tracker APIs**

```http
POST /tracker/requests
GET  /tracker/requests
GET  /tracker/requests/:id
POST /tracker/requests/:id/accept
```

**### Transaction APIs**

```http
POST /businesses/:businessId/transactions
```

Transaction APIs may support future payment/POS integrations. They do **not** award loyalty points in the current visit-based MVP.

**### API Overview Table**

| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/v1/auth/google` | Public | Authenticate user via Google OAuth token |
| `GET` | `/api/v1/rewards/balance` | Customer | Fetch current loyalty point balance and reward progress |
| `POST` | `/api/v1/businesses/:businessId/check-ins` | Customer | Verify store presence and record a loyalty visit |
| `POST` | `/api/v1/reward-tasks/:taskId/submit` | Customer | Submit completion/proof for a reward task |
| `POST` | `/api/v1/rewards/:id/claim` | Customer | Request an eligible loyalty reward |
| `POST` | `/api/v1/owner/task-submissions/:id/approve` | Business Manager | Approve a submitted required/optional task proof |
| `POST` | `/api/v1/tracker/request` | Business Manager | Issue item confirmation request |
| `PATCH` | `/api/v1/tracker/request/:id/accept` | Customer | Accept pending item confirmation request |
| `GET` | `/api/v1/tracker/history` | Business / Customer | Fetch historical item confirmation audit logs |
| `GET` | `/api/v1/admin/analytics` | Admin | Retrieve system-wide performance & usage metrics |

\---

**## 🖥️ Frontend Architecture**

Use **\*\*feature-based organization\*\***. Each feature contains its own components, hooks, API clients, schemas, types, and utils.

\`\`\`
features/
├── auth/
├── customer/
├── owner/
├── rewards/
├── claims/
├── transactions/
├── tracker/
├── notifications/
└── analytics/
\`\`\`

**### Dashboard Routing**

\`\`\`
/login

/customer
/customer/rewards
/customer/claims
/customer/history
/customer/visits
/customer/check-in
/customer/offers
/customer/profile

/owner
/owner/customers
/owner/transactions
/owner/branches
/owner/check-in
/owner/visits
/owner/rewards
/owner/rules
/owner/claims
/owner/analytics
/owner/settings

/admin
/admin/businesses
/admin/users
/admin/subscriptions
/admin/audit
/admin/settings
\`\`\`

**### Middleware Authorization Flow**

\`\`\`
Request → Authentication Middleware → User Identity → Role Guard
→ Tenant Guard → Permission Guard → Controller
\`\`\`

\> The frontend may redirect users to the appropriate dashboard, but the **\*\*backend must independently enforce permissions\*\***.

\---

**## 🔔 Notification Architecture**

Notifications are **\*\*asynchronous\*\*** and must never block the core transaction.

\`\`\`
Business Event → Database Commit → Queue → Notification Worker → Push / Email
\`\`\`

If push notification fails: reward transaction = ✅ SUCCESS, notification = 🔄 RETRY.

**### Notification Events**

\| Event | Trigger |
\| :---- | :------ |
\| \`REWARD\_AVAILABLE\` | Points credited to customer |
\| \`REWARD\_CLAIM\_REQUESTED\` | Customer submits a claim |
\| \`REWARD\_CLAIM\_APPROVED\` | Shop Owner approves claim |
\| \`REWARD\_CLAIM\_REJECTED\` | Shop Owner rejects claim |
\| \`TRACKER\_REQUEST\_CREATED\` | Business dispatches a confirmation request |
\| \`TRACKER\_REQUEST\_ACCEPTED\` | Customer accepts item delivery |

\---

**## 🔒 Security & Compliance**

**### Authentication**

\- Use OAuth/OIDC correctly with server-side token verification
\- Never trust user-provided role values
\- Stateless JWT with short-lived access tokens and secure HTTP-only refresh tokens

**### Authorization**

RBAC + tenant authorization:

\`\`\`
Customer    → own resources only
Shop Owner  → own business resources only
Administrator → platform resources according to permission
\`\`\`

**### Input Validation**

Validate every API request (body, query, path params, headers) using \`class-validator\` and \`class-transformer\`.

**### Rate Limiting**

Protect: authentication, check-in QR validation, geolocation/check-in, reward claim, task submission, transaction, and notification endpoints using \`@nestjs/throttler\`.

**### Data Protection**

\- HTTPS everywhere
\- Encrypt sensitive secrets & restrict database access
\- Least privilege for infrastructure
\- Rotate credentials regularly

**### QR & Geolocation Security**

- Do **\*\*not\*\*** expose customer email, phone, or reward balance inside the business QR payload.
- Prefer opaque tokens or signed business/branch identifiers.
- Validate the QR against the business/branch on the backend.
- Verify the customer's authenticated identity before awarding points.
- Validate the submitted location against the configured geofence on the backend.
- Do not trust frontend-only distance calculations.
- Rate-limit and audit rejected as well as successful check-ins.

**### Audit Logging**

Audit all critical events:

\`\`\`
USER\_LOGIN, BUSINESS\_CREATED, REWARD\_RULE\_CREATED, REWARD\_RULE\_UPDATED,
CHECK\_IN\_ATTEMPTED, CHECK\_IN\_VERIFIED, CHECK\_IN\_REJECTED,
POINTS\_GRANTED, REWARD\_CREATED, REWARD\_TASK\_CREATED,
REWARD\_TASK\_UPDATED, REWARD\_TASK\_SUBMITTED, REWARD\_TASK\_VERIFIED,
CLAIM\_REQUESTED, CLAIM\_APPROVED, CLAIM\_REJECTED,
TRACKER\_REQUEST\_CREATED, TRACKER\_REQUEST\_ACCEPTED,
BUSINESS\_SETTINGS\_UPDATED
\`\`\`

Audit record fields: \`actor, business, action, resource, resource\_id, timestamp, request\_id, metadata\`

**\*\*Never log secrets or authentication tokens.\*\***

\---

**## ⚠️ Error Handling**

Use consistent API error responses:

\`\`\`json
{
  "success": false,
  "error": {
    "code": "REWARD\_CLAIM\_ALREADY\_PROCESSED",
    "message": "This reward claim has already been processed."
  },
  "requestId": "req\_12345"
}
\`\`\`

**\*\*Standard error codes:\*\***

\`\`\`
AUTHENTICATION\_REQUIRED, FORBIDDEN, RESOURCE\_NOT\_FOUND, VALIDATION\_ERROR,
INVALID\_GEOLOCATION, OUTSIDE\_GEOFENCE, DUPLICATE\_CHECK\_IN,
CHECK\_IN\_NOT\_ELIGIBLE, REQUIRED\_TASK\_INCOMPLETE, INVALID\_TASK\_PROOF,
REWARD\_NOT\_ELIGIBLE, CLAIM\_ALREADY\_PROCESSED, RATE\_LIMITED, INTERNAL\_ERROR
\`\`\`

Do not expose stack traces in production.

\---

**## 🧪 Testing Strategy**

**### 1. Unit Tests**

Test: visit qualification, geofence calculations, duplicate check-in protection, reward calculations, task eligibility, state transitions, validation, permission logic.

**### 2. Integration Tests**

Test: database transactions, reward creation, claim approval, authentication integration, notification queue.

**### 3. End-to-End Tests**

**\*\*Customer Flow:\*\***
\`\`\`
Google Login → Join Business → Scan Business QR → Geolocation Verified
→ Visit Recorded → +1 Point → Reward Threshold Reached
→ Complete Required Task (if configured) → Request Claim
→ Owner Approves → Customer Sees Claimed
\`\`\`

**\*\*Tracker Flow:\*\***
\`\`\`
Owner Creates Request → User Receives Request → User Accepts
→ Database Updated → Owner Notified
\`\`\`

**### 4. Security Tests**

Test: unauthorized dashboard access, cross-tenant data access, IDOR, duplicate transactions/claims, token manipulation, rate limiting, input injection.

**### Critical Test Cases**

\| Area | Must Pass |
\| :--- | :-------- |
\| **\*\*Rewards\*\*** | Verified in-store presence grants points · Outside geofence does not · Duplicate check-in doesn't grant twice · Group members can each earn · Customer can't modify points · Balance correct after redemption |
\| **\*\*Claims\*\*** | Customer can request eligible reward · Required tasks block claim · Optional tasks do not block · Can't self-approve · Owner approves own-business only · No duplicate approval · Rejected recorded · Notification queued on state change |
\| **\*\*Tenant\*\*** | Business A ≠ Business B · Customer A ≠ Customer B · Owner can't access Admin · Customer can't access Owner |
\| **\*\*Check-In\*\*** | Valid QR accepted · Authenticated customer required · Inside geofence accepted · Outside geofence rejected · Duplicate visit blocked · Group members can each check in |
| **\*\*Tasks\*\*** | Owner can create task · Optional task does not block · Required task blocks until satisfied · Proof stored · Invalid/duplicate submission handled |
| **\*\*Tracker\*\*** | Owner creates request · Correct receiver gets request · Receiver can accept · Can't accept another's request · Single acceptance only |

\---

**## ⚡ Performance & Scalability**

**\*\*Priority areas:\*\*** Customer lookup, reward balance retrieval, geolocation/check-in verification, duplicate check-in protection, reward claim approval, business QR validation.

**### Strategies**

\- **\*\*Caching:\*\*** Redis for business public info, active reward rules, active offers, dashboard summaries
\- **\*\*Database:\*\*** Proper indexes, pagination (\`?page=1&limit=25\`), cursor pagination for large datasets
\- **\*\*Background Jobs:\*\*** Queue-based notification and analytics processing
\- **\*\*Connection Pooling:\*\*** Database and Redis connection management
\- **\*\*Query Optimization:\*\*** Avoid N+1 queries, use proper JOINs

\> ⚠️ Do not blindly cache rapidly changing balances. Reward balance correctness has priority over aggressive caching.

**### Idempotency & Concurrency**

**\*\*Check-in idempotency\*\*** protects against repeated QR scans, browser refreshes, network retries, and duplicate requests during the same visit period.

**\*\*Transaction idempotency\*\*** remains relevant to future payment/POS integrations, but payment is not the current loyalty trigger.

**\*\*Claim concurrency\*\*** protection via database transactions, row locking, atomic state transitions, and unique constraints ensures only one approval succeeds for simultaneous requests.

\---

**## 🔀 Development Workflow**

**### Git Workflow**

\`\`\`
main
  |
  +-- develop
        |
        +-- feature/google-auth
        +-- feature/reward-engine
        +-- feature/reward-claims
        +-- feature/tracker
\`\`\`

**\*\*Branch naming:\*\*** \`feature/\<name>\`, \`fix/\<name>\`, \`refactor/\<name>\`, \`docs/\<name>\`, \`test/\<name>\`, \`chore/\<name>\`

**### Commit Convention**

Use [Conventional Commits]\(https\://www\.conventionalcommits.org/):

\`\`\`
feat: add reward ledger
fix: prevent duplicate reward claim
test: add reward calculation tests
refactor: move reward engine to domain module
docs: update API documentation
chore: update dependencies
\`\`\`

**### Pull Request Checklist**

Every PR must include: **\*\*Summary\*\***, **\*\*Reason\*\***, **\*\*Implementation\*\***, **\*\*Testing\*\***, **\*\*Security Impact\*\***, **\*\*Database Changes\*\***, and **\*\*Screenshots\*\*** (for UI changes).

**### Code Review Checklist**

Verify: business logic correctness, authorization exists, tenant isolation preserved, inputs validated, errors handled, tests exist, proper indexes, no secrets committed, no unnecessary data returned, no duplicate processing, no sensitive data in logs.

**### Coding Standards**

\- **\*\*Strict TypeScript\*\*** — avoid \`any\`, prefer \`unknown\` with validation
\- **\*\*Naming:\*\*** \`camelCase\` for variables/functions, \`PascalCase\` for classes/components
\- **\*\*Clear names:\*\*** \`calculateRewardPoints()\`, \`approveRewardClaim()\`, \`verifyPayment()\`
\- **\*\*Business logic\*\*** lives in the backend/domain layer, not in React

\---

**## 🚢 Deployment**

**### Production Architecture**

\`\`\`
               Internet
                  |
                  v
          CDN / Load Balancer
                  |
         +--------+--------+
         |                 |
         v                 v
    Next.js App       API Server(s)
                          |
         +----------------+----------------+
         |                |                |
         v                v                v
    PostgreSQL          Redis          Object Storage
         |
         v
    Backup Storage
\`\`\`

**### Docker Services**

Development: \`web\`, \`api\`, \`postgres\`, \`redis\`

\`\`\`bash
docker compose up -d
\`\`\`

\> Production should use managed services where appropriate instead of running everything on one server.

\---

**## ⚙️ CI/CD**

**### Pull Request Pipeline**

\`\`\`
Install → Lint → Type Check → Unit Tests → Integration Tests → Build → Security Checks
\`\`\`

**### Production Deployment**

\`\`\`
Merge to main → CI → Build Images → Deploy → Health Check → Monitor
\`\`\`

**### Monitoring**

\| Area | Metrics |
\| :--- | :------ |
\| **\*\*Application\*\*** | Request rate, error rate, response time, 5xx errors, auth failures |
\| **\*\*Database\*\*** | CPU, memory, connections, query latency, slow queries, storage |
\| **\*\*Reward Engine\*\*** | Verified visits, points issued, duplicate/rejected check-ins, reward claims, task failures |
\| **\*\*Notifications\*\*** | Queue size, delivery rate, failure rate, retry count |

**### Backup & Recovery**

\- Automated backups with point-in-time recovery
\- Backup retention policy
\- Restore testing (a backup is not reliable until restoration is tested)

\---

**## 🗺️ Development Roadmap**

**### Phase 0 — Project Foundation**
Repository setup, monorepo, TypeScript, linting, formatting, CI, Docker, database connection, logging.
> **\*\*Deliverable:\\*\*** Application boots locally. Database connects. CI passes.

**### Phase 1 — Authentication**
Google auth, user creation, sessions, role model, protected routes, logout, account status.

**### Phase 2 — Multi-Tenant Business System**
Business model, owner-business relationship, onboarding, branches, tenant middleware, settings, isolation tests.

**### Phase 3 — Customer System**
Profile, business membership, customer dashboard, visit history, loyalty balance, notifications.

**### Phase 4 — Business Check-In System**
Business/branch locations, check-in QR generation, geofence configuration, browser location permission, location verification, visit records, duplicate check-in protection.

**### Phase 5 — Visit-Based Reward Engine**
Visit rules, one-point-per-period behavior, reward ledger, balance calculation, eligibility, group visit handling.

**### Phase 6 — Reward Management & Tasks**
Reward creation, thresholds, special items, task creation, OPTIONAL/REQUIRED configuration, proof submission and verification.

**### Phase 7 — Reward Claims**
Claim request, required-task eligibility, pending claims, approve/reject, history, atomic redemption.

**### Phase 8 — Notifications**
Visit, reward, task, claim, and tracker notifications; queue, retry mechanism, read/unread.

**### Phase 9 — Tracker System**
Request creation, receiver selection, item/quantity, notification, acceptance, history.

**### Phase 10 — Analytics**
Owner dashboard metrics, customer growth, verified visits, visit streaks, loyalty progress, rewards claimed, customer retention.

**### Phase 11 — Security Hardening**
Rate limiting, security headers, geolocation validation review, authorization review, tenant isolation tests, audit logging, secret management, dependency scanning.

**### Phase 12 — Performance & Production**
Load testing, database optimization, Redis, queue workers, monitoring, backups, disaster recovery, production deployment.

**### Recommended Implementation Order**

```
 1. Repository + CI             12. Reward Ledger
 2. Database + Prisma           13. Reward Eligibility
 3. Google Authentication       14. Reward Tasks
 4. User + Role System          15. Reward Claim Request
 5. Business/Tenant System      16. Shop Owner Approval
 6. Customer-Business            17. Notification System
 7. Customer Dashboard           18. Tracker System
 8. Business Branches            19. Analytics
 9. Business Check-In QR         20. Security Hardening
10. Geolocation / Geofence       21. Load Testing
11. Visit Reward Engine          22. Production Deployment
```

> ⚠️ Do not begin with advanced UI or analytics before authentication, check-in verification, reward ledger, authorization, and tenant-isolation foundations are correct.

\---

**## 🎯 MVP Scope**

**### In Scope**

| Actor | Features |
| :---- | :------- |
| **\*\*Customer\*\*** | Google Login, profile, business loyalty enrollment, business QR check-in, geolocation verification, visit history, loyalty balance & progress, reward tasks, reward request, notifications |
| **\*\*Shop Owner\*\*** | Google Login, business onboarding, branch/check-in configuration, geofence settings, visit reward rule config, customer/visit list, reward view, task configuration with OPTIONAL/REQUIRED setting, task verification, claim approval/rejection, notifications, basic loyalty analytics |
| **\*\*Administrator\*\*** | Login, business management, user management, basic platform analytics, audit logs |
| **\*\*Tracker\*\*** | Create request, select user, item name/quantity/remarks, accept request, history, notifications |

**### Explicitly Out of MVP**

Complex inventory management, full POS, advanced accounting, delivery tracking, employee management, complex logistics states, AI recommendations, referral engine, multi-currency accounting, advanced marketing automation, purchase/order-based loyalty points.

\---

**## 🔮 Future Roadmap**

- [ ] **\*\*Phase 2:\\*\*** Multiple branches, more reward rule types, advanced offers, SMS, WhatsApp, customer segmentation
- [ ] **\*\*Phase 3:\\*\*** Mobile application, POS integrations, payment integrations, inventory integrations, referral system, advanced analytics
- [ ] **\*\*Phase 4:\\*\*** Enterprise API, webhooks, third-party integrations, advanced tenant management, enterprise billing, regional infrastructure
- [ ] **\*\*Products & Offers Module:\\*\*** Digital menus, physical products, and promotional flash sales
- [ ] **\*\*Multi-Tier Loyalty:\\*\*** Customizable VIP tiers (Silver, Gold, Platinum) with dynamic point multipliers
- [ ] **\*\*Purchase/Order Loyalty:\\*\*** Revisit whether verified purchases/orders should become a separate loyalty event in a future product discussion
- [ ] **\*\*Automated Analytics Exports:\\*\*** Scheduled PDF/CSV reports delivered via email

\---

**## 🔧 Troubleshooting**

\<details>
\<summary>\<strong>Database connection fails\</strong>\</summary>

Check: \`DATABASE\_URL\`, PostgreSQL running, network connectivity, migration status.
\`\`\`bash
pnpm db\:migrate
\`\`\`
\</details>

\<details>
\<summary>\<strong>Authentication fails\</strong>\</summary>

Check: Google client ID, Google client secret, authorized redirect URI, application URL, OAuth configuration.
\</details>

\<details>
\<summary>\<strong>Points are not generated\</strong>\</summary>

Check: payment status, transaction reference, reward rule active, customer-business relationship, reward engine logs, database transaction.
\</details>

\<details>
\<summary>\<strong>Duplicate points appear\</strong>\</summary>

Check: visit-period unique constraint, idempotency key, reward ledger reference, concurrent check-in handling, QR replay protection, backend authorization, and transaction boundaries.
\</details>

\<details>
\<summary>\<strong>Customer sees another business's data\</strong>\</summary>

⚠️ **\*\*CRITICAL SECURITY ISSUE\*\*** — Immediately investigate: tenant middleware, \`business\_id\` filtering, authorization guard, database query.
\</details>

**### Security Incident Priority**

The following must be treated as **\*\*critical\*\*** and must not ship unresolved:

\- Cross-business data access
\- Customer account takeover
\- Unauthorized reward approval
\- Duplicate reward credit / duplicate check-in points
- Geolocation verification bypass
\- Database credential exposure
\- Authentication bypass

\---

**## ✅ Definition of Done**

A feature is complete only when:

1\. Requirements are understood
2\. Database changes are implemented
3\. Backend logic is implemented
4\. API validation exists
5\. Authentication/authorization exists
6\. Tenant isolation is verified
7\. Frontend is implemented
8\. Geolocation/check-in verification is tested
9\. Optional/required task behavior is tested
10\. Error states are handled
11\. Unit tests pass
12\. Integration tests pass
13\. Relevant E2E tests pass
14\. Documentation is updated
15\. Audit requirements are satisfied
16\. Security implications are reviewed
17\. CI passes
18\. Production build succeeds

\---

**## 📊 Product Success Metrics**

| Area | Metrics |
| :--- | :------ |
| **\*\*Customer\*\*** | Registered customers, active customers, verified visits, visit frequency, visit streaks, rewards earned, rewards claimed |
| **\*\*Business\*\*** | Active businesses, customers per business, verified visits, returning-customer rate, reward redemption rate, customer retention |
| **\*\*Platform\*\*** | Monthly active businesses/customers, verified check-in volume, API uptime, error rate, average response time |

\---

**## 📄 License**

This project is licensed under the **\*\*MIT License\*\***. See the [LICENSE]\(LICENSE) file for full details.

\---

**## 👥 Maintainers**

\`\`\`
Project: HexLoyal (Rewards.io)
Repository: https\://github.com/Gyrobird/Reqards.io
\`\`\`

\---

**## 📌 Status**

**\*\*In Development\*\***

The architecture and requirements in this README represent the current planned implementation. The current loyalty model is visit-based: customers earn points through verified in-store presence using business QR + geolocation verification. Purchase/order-based loyalty is intentionally deferred. Reward tasks are owner-configurable as OPTIONAL or REQUIRED. Any changes to visit verification, reward calculation, reward tasks, user roles, tenant isolation, or claim authorization should be documented and reviewed before implementation.