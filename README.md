# tsoha2024_pwnpatrol
A web-based application for sharing cybersecurity threat data (e.g., malware indicators, phishing attacks) securely between users and organizations.


# Cyber Threat Intelligence Sharing Platform


## Core Purpose

Provide a structured and collaborative environment for sharing threat intelligence such as malware indicators, phishing attempts, and vulnerabilities. Enable users to contribute, search, and retrieve critical threat data to enhance cyber defense strategies.

## Features

### 1. User Management
- **Roles & Organizations**: Users can be regular members or administrators.
- **Database Tables**:
  - `Users`: User details (id, username, password, role, organization_id).
  - `Organizations`: Organization info (id, name, contact info).
  - `UserRoles`: User role assignments.

### 2. Threat Data Management
- **Threat Indicators**: Store data such as IPs, domains, hashes, and phishing emails, and possible malware.
- **Events**: Categorize related threat indicators (e.g., "Phishing Campaign – March 2024").
- **Tags & TTPs**: Tag indicators/events and map to frameworks like MITRE ATT&CK.
- **Database Tables**:
  - `ThreatIndicators`: Threat data (id, type, value, description, event_id).
  - `Events`: Threat events (id, name, description, date, severity, organization_id).
  - `TTPs`: TTPs associated with threats (id, event_id, ttp_code, description).
  - `Tags` and `EventTags`: Tag management and relationships.

### 3. Vulnerability & Incident Tracking
- **Vulnerability Reports**: Track vulnerabilities with CVE numbers and remediation.
- **Incident Reports**: Document and link cybersecurity incidents.
- **Patch Status**: Track patching efforts related to vulnerabilities.
- **Database Tables**:
  - `Vulnerabilities`: Vulnerability info (id, CVE, description, severity, affected_systems, remediation).
  - `Incidents`: Incident records (id, date, description, status, event_id).
  - `PatchStatus`: Patching status (vulnerability_id, organization_id, status).

### 4. Search & Analytics
- **Advanced Search**: Filter data by tags, date range, type, severity, TTPs.
- **Real-time Alerts**: Set up notifications for new threat indicators.
- **Database Tables**:
  - `SearchLogs`: Log of search queries (id, user_id, query, date).
  - `Subscriptions`: User subscriptions to events or indicators (user_id, subscription_criteria, last_checked).

### 5. Administration & Security
- **Audit Logs**: Track user actions and data changes.
- **Data Expiration & Retention**: Manage data lifecycle and retention policies.
- **Encryption & RBAC**: Secure data and define user permissions.
- **Database Tables**:
  - `AuditLogs`: Action logs (id, user_id, action_type, timestamp).
  - `AccessControls`: User access permissions (id, user_id, entity_id, permission_level).
 
More info about the idea [here]([URL](https://en.wikipedia.org/wiki/MISP_Threat_Sharing)) and [here]([URL](https://www.misp-project.org/))
