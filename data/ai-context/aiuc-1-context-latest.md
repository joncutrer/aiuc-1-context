AIUC-1 2026-Q1 | 2026-03-05 | https://www.aiuc-1.com
Security/safety/reliability standard for AI agents. 51 requirements across 6 domains. Quarterly releases Jan/Apr/Jul/Oct 15. Versions: 2026-Q1 2025-Q1
Domains: A=Data&Privacy B=Security C=Safety D=Reliability E=Accountability F=Society
Crosswalks: ISO 42001 | MITRE ATLAS | EU AI Act | NIST AI RMF | OWASP Top Ten | CSA AICM | OWASP AIVSS

# Requirements

| Domain | ID | Title | Full Requirement | Status | Frequency | Capabilities | Keywords |
|---|---|---|---|---|---|---|---|
| Data & Privacy | A001 | Establish input data policy | Establish and communicate AI input data policies covering how customer data is used for model training, inference processing, data retention periods, and customer data rights | Mandatory | Every 12 months | Universal | Data Retention, Model Training Data, Opt-Out |
| Data & Privacy | A002 | Establish output data policy | Establish AI output ownership, usage, opt-out and deletion policies to customers and communicate these policies | Mandatory | Every 12 months | Universal | Data Ownership, Usage, Deletion, Consent, Opt-Out |
| Data & Privacy | A003 | Limit AI agent data collection | Implement safeguards to limit AI agent data access to task-relevant information based on user roles and context | Mandatory | Every 12 months | Universal | Data Collection, Data Access, Agent Permissions, Access Permissions |
| Data & Privacy | A004 | Protect IP & trade secrets | Implement safeguards or technical controls to prevent AI systems from leaking company intellectual property or confidential information | Mandatory | Every 12 months | Universal | Intellectual Property, Confidential Information, Data Protections |
| Data & Privacy | A005 | Prevent cross-customer data exposure | Implement safeguards to prevent cross-customer data exposure when combining customer data from multiple sources | Mandatory | Every 12 months | Universal | Cross-Customer Data, Model Training, Data Rights |
| Data & Privacy | A006 | Prevent PII leakage | Establish safeguards to prevent personal data leakage through AI outputs | Mandatory | Every 12 months | Universal | Personal Data Leakage |
| Data & Privacy | A007 | Prevent IP violations | Implement safeguards and technical controls to prevent AI outputs from violating copyrights, trademarks, or other third-party intellectual property rights | Mandatory | Every 12 months | Text-generation, Voice-generation, Image-generation | Intellectual Property, Copyright Protection |
| Security | B001 | Third-party testing of adversarial robustness | Implement adversarial testing program to validate system resilience against adversarial inputs and prompt injection attempts in line with adversarial threat taxonomy | Mandatory | Every 3 months | Universal | Adversarial Testing, Red Teaming, Prompt Injection, Jailbreak |
| Security | B002 | Detect adversarial input | Implement monitoring capabilities to detect and respond to adversarial inputs and prompt injection attempts | Optional | Every 3 months | Universal | Monitor, Adversarial, Jailbreak, Prompt Injection |
| Security | B003 | Manage public release of technical details | Implement controls to prevent over-disclosure of technical information about AI systems and organizational details that could enable adversarial targeting | Optional | Every 12 months | Universal | Public Disclosure, Open-Source, External Threats |
| Security | B004 | Prevent AI endpoint scraping | Implement safeguards to prevent probing or scraping of external AI endpoints | Mandatory | Every 12 months | Universal | Scraping, Probing, Rate Limiting, Query Quotas, Zero Trust |
| Security | B005 | Implement real-time input filtering | Implement real-time input filtering using automated moderation tools | Optional | Every 12 months | Text-generation, Voice-generation, Image-generation | Prompt Injection, Jailbreak, Adversarial Input Protection |
| Security | B006 | Prevent unauthorized AI agent actions | Implement safeguards to limit AI agent system access based on context and declared objectives | Mandatory | Every 12 months | Automation | Access Permissions, Agent Permissions |
| Security | B007 | Enforce user access privileges to AI systems | Establish and maintain user access controls and admin privileges for AI systems in line with policy | Mandatory | Every 3 months | Universal | Access Controls, Organizational Policy |
| Security | B008 | Protect model deployment environment | Implement security measures for AI model deployment environments including encryption, access controls and authorization | Mandatory | Every 12 months | Universal | Model Environment, Encryption, Access Controls |
| Security | B009 | Limit output over-exposure | Implement output limitations and obfuscation techniques to safeguard against information leakage | Mandatory | Every 12 months | Text-generation, Voice-generation | Output Obfuscation, Fidelity Reduction, Information Leakage, Adversarial Use, Response Filtering |
| Safety | C001 | Define AI risk taxonomy | Establish a risk taxonomy that categorizes risks within harmful, out-of-scope, and hallucinated outputs, tool calls, and other risks based on application-specific usage | Mandatory | Every 3 months | Universal | Risk Taxonomy, Severity Rating |
| Safety | C002 | Conduct pre-deployment testing | Conduct internal testing of AI systems prior to deployment across risk categories for system changes requiring formal review or approval | Mandatory | Every 12 months | Universal | Internal Testing, Pre-Deployment Testing |
| Safety | C003 | Prevent harmful outputs | Implement safeguards or technical controls to prevent harmful outputs including distressed outputs, angry responses, high-risk advice, offensive content, bias, and deception | Mandatory | Every 12 months | Text-generation, Voice-generation, Image-generation | Harmful Outputs, Distressed, Angry, Advice, Offensive, Bias |
| Safety | C004 | Prevent out-of-scope outputs | Implement safeguards or technical controls to prevent out-of-scope outputs (e.g. political discussion, healthcare advice) | Mandatory | Every 12 months | Text-generation, Voice-generation | Out-of-Scope, Political Discussion, Technical Controls |
| Safety | C005 | Prevent customer-defined high risk outputs | Implement safeguards or technical controls to prevent additional high risk outputs as defined in risk taxonomy | Mandatory | Every 12 months | Universal | High-Risk Outputs, Risk Taxonomy, Technical Controls |
| Safety | C006 | Prevent output vulnerabilities | Implement safeguards to prevent security vulnerabilities in outputs from impacting users | Mandatory | Every 3 months | Universal | Harmful Outputs, Code Injection, Data Exfiltration |
| Safety | C007 | Flag high risk outputs | Implement an alerting system that flags high-risk outputs for human review | Optional | Every 12 months | Universal | Human Review, Escalation |
| Safety | C008 | Monitor AI risk categories | Implement monitoring of AI systems across risk categories | Optional | Every 12 months | Universal | Monitoring, High-Risk Outputs |
| Safety | C009 | Enable real-time feedback and intervention | Implement mechanisms to enable real-time user feedback collection and intervention mechanisms | Optional | Every 3 months | Universal | Feedback, Intervention, User Control, Transparency |
| Safety | C010 | Third-party testing for harmful outputs | Appoint expert third parties to evaluate system robustness to harmful outputs including distressed outputs, angry responses, high-risk advice, offensive content, bias, and deception at least every 3 months | Mandatory | Every 3 months | Text-generation, Voice-generation, Image-generation | Harmful Outputs, Distressed, Angry, Advice, Offensive, Bias, Risk Severity, Toxigen, Third-Party Testing |
| Safety | C011 | Third-party testing for out-of-scope outputs | Appoint expert third parties to evaluate system robustness to out-of-scope outputs at least every 3 months (e.g. political discussion, healthcare advice) | Mandatory | Every 3 months | Text-generation, Voice-generation | Out-of-Scope, Political Discussion, Third-Party Testing |
| Safety | C012 | Third-party testing for customer-defined risk | Appoint expert third-parties to evaluate system robustness to additional high-risk outputs as defined in risk taxonomy at least every 3 months | Mandatory | Every 3 months | Universal | High-Risk Outputs, Risk Taxonomy, Third-Party Testing |
| Reliability | D001 | Prevent hallucinated outputs | Implement safeguards or technical controls to prevent hallucinated outputs | Mandatory | Every 12 months | Text-generation, Voice-generation | Hallucinations, Technical Controls |
| Reliability | D002 | Third-party testing for hallucinations | Appoint expert third-parties to evaluate hallucinated outputs at least every 3 months | Mandatory | Every 3 months | Text-generation, Voice-generation | Hallucinations, Third-Party Testing |
| Reliability | D003 | Restrict unsafe tool calls | Implement safeguards or technical controls to prevent tool calls in AI systems from executing unauthorized actions, accessing restricted information, or making decisions beyond their intended scope | Mandatory | Every 12 months | Automation | Tool Calls, Tool Selection, Technical Controls |
| Reliability | D004 | Third-party testing of tool calls | Appoint expert third-parties to evaluate tool calls in AI systems, including executing unauthorized actions, accessing restricted information, or making decisions beyond their intended scope at least every 3 months | Mandatory | Every 3 months | Automation | Tool Calls, Tool Selection, Third-Party Testing |
| Accountability | E001 | AI failure plan for security breaches | Document AI failure plan for AI privacy and security breaches assigning accountable owners and establishing notification and remediation with third-party support as needed (e.g. legal, PR, insurers) | Mandatory | Every 12 months | Universal | Incident Response, Security, Privacy, Regulatory Deadlines |
| Accountability | E002 | AI failure plan for harmful outputs | Document AI failure plan for harmful AI outputs that cause significant customer harm assigning accountable owners and establishing remediation with third-party support as needed (e.g. legal, PR, insurers) | Mandatory | Every 12 months | Text-generation, Voice-generation, Image-generation | Incident Response, Emergency Response, Harmful Outputs, Hallucinations, Vendors |
| Accountability | E003 | AI failure plan for hallucinations | Document AI failure plan for hallucinated AI outputs that cause substantial customer financial loss assigning accountable owners and establishing remediation with third-party support as needed (e.g. legal, PR, insurers) | Mandatory | Every 12 months | Text-generation, Voice-generation | Hallucinations, Incident Response, Customer Loss |
| Accountability | E004 | Assign accountability | Document which AI system changes across the development & deployment lifecycle require formal review or approval, assign a lead accountable for each, and document their approval with supporting evidence | Mandatory | Every 12 months | Universal | Decision Owners, Deployment |
| Accountability | E005 | Assess cloud vs on-prem processing | Establish criteria for selecting cloud provider, and circumstances for on-premises processing considering data sensitivity, regulatory requirements, security controls, and operational needs | Mandatory | Every 12 months | Universal | Deployment, Cloud Security, On-Premise Security, Data Residency |
| Accountability | E006 | Conduct vendor due diligence | Establish AI vendor due diligence processes for foundation and upstream model providers covering data handling, PII controls, security and compliance | Mandatory | Every 12 months | Universal | Vendor Due Diligence, Open-Source, Foundation Models, Upstream Models |
| Accountability | E007 | [Retired] Document system change approvals | Merged with E004 - see changelog (Q1 2026 update) | Optional | Every 12 months | Universal | Approvals, Workflows |
| Accountability | E008 | Review internal processes | Establish regular internal reviews of key processes and document review records and approvals | Mandatory | Every 12 months | Universal | Internal Reviews, Documentation |
| Accountability | E009 | Monitor third-party access | Implement systems to monitor third party access | Optional | Every 12 months | Universal | Access, Logins |
| Accountability | E010 | Establish AI acceptable use policy | Establish and implement an AI acceptable use policy | Mandatory | Every 12 months | Universal | Acceptable Use, Breach |
| Accountability | E011 | Record processing locations | Document AI data processing locations | Mandatory | Every 12 months | Universal | Data Processing, Storage Location, Data Protections |
| Accountability | E012 | Document regulatory compliance | Document applicable AI laws and standards, required data protections, and strategies for compliance | Mandatory | Every 6 months | Universal | Regulatory, EU, NY, NIST, ISO, GDPR |
| Accountability | E013 | Implement quality management system | Establish a quality management system for AI systems proportionate to the size of the organization | Optional | Every 12 months | Universal | EU, Quality management, Regulatory |
| Accountability | E014 | Share transparency reports | Merged with E017 - see changelog (Q1 2026 update) | Optional | Every 12 months | Universal | Transparency |
| Accountability | E015 | Log model activity | Maintain logs of AI system processes, actions, and model outputs where permitted to support incident investigation, auditing, and explanation of AI system behavior | Mandatory | Every 12 months | Universal | Explainability, Logs |
| Accountability | E016 | Implement AI disclosure mechanisms | Implement clear disclosure mechanisms to inform users when they are interacting with AI systems rather than humans | Mandatory | Every 12 months | Universal | Labelling, Transparency |
| Accountability | E017 | Document system transparency policy | Establish a system transparency policy and maintain a repository of model cards, datasheets, and interpretability reports for major systems | Optional | Every 12 months | Universal | Transparency, System Cards |
| Society | F001 | Prevent AI cyber misuse | Implement or document guardrails to prevent AI-enabled misuse for cyber attacks and exploitation | Mandatory | Every 12 months | Text-generation, Automation, Voice-generation | Cyber Attacks |
| Society | F002 | Prevent catastrophic misuse | Implement or document guardrails to prevent AI-enabled catastrophic system misuse (chemical / bio / radio / nuclear) | Mandatory | Every 12 months | Text-generation, Voice-generation, Image-generation | CBRN, Chemical, Bioweapon, Radioactive, Nuclear |

# Controls & Evidence

## A001: Establish input data policy
*Mandatory | Capabilities: Universal*

### A001.1 Documentation: Policy for input data ownership, usage and retention
- **Application:** Core - This should include:
- **Control:** - Defining and communicating input data usage policies. Including specifying how customer data is used for inference and model training, establishing data retention periods, and documenting customer data rights.
- **Category:** Legal Policies
- **Typical location:** Terms of Service, Privacy Policy, DPA
- **Typical evidence:** Typically demonstrated by Terms of Service, Privacy Policy or Data Processing Agreement
- **Priority guidance:** Prioritize validating control status: Legal review may be required to pass AIUC-1

### A001.2 Config: Data retention implementation
- **Application:** Core - This should include:
- **Control:** - Implementing technical controls to enforce data retention and deletion policies. For example, automating data deletion based on retention schedules, using secure removal mechanisms, and managing data lifecycles.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code, Engineering Practice
- **Typical evidence:** Screenshot of automated deletion implementation or data lifecycle system - may include cron job or scheduled task deleting expired data, deletion script in Python/Bash with retention period logic, data lifecycle management tool configuration (e.g., AWS S3 lifecycle rules, database TTL settings), or deletion audit logs from database or storage system.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### A001.3 Documentation: Data subject right processes
- **Application:** Supplemental - This may include:
- **Control:** - Documenting processes for handling end-user data subject rights. For example, handling requests for opt-in/opt-out rights, access, portability, or deletion of input data.
- **Category:** Legal Policies
- **Typical location:** Data Processing Agreement, Privacy Policy
- **Typical evidence:** May be included in DPA, GDPR appendix, External Privacy Policy or similar internal or external policies documenting processes for data handling


## A002: Establish output data policy
*Mandatory | Capabilities: Universal*

### A002.1 Documentation: Output usage and ownership policy
- **Application:** Core - This should include:
- **Control:** - Establishing output ownership and usage rights policies. For example, specifying customer ownership of AI-generated outputs versus AI inputs, defining permitted uses of outputs (commercial use, redistribution, modification), documenting usage restrictions or limitations, and clarifying how ownership applies to different output types or use cases.
- Disclosing opt-out and deletion procedures for AI outputs. For example, documenting how customers can opt out of output storage or reuse, explaining deletion request processes, specifying retention periods and data handling practices, and clarifying how customers can control or revoke permissions for their outputs.
- **Category:** Legal Policies
- **Typical location:** Terms of Service
- **Typical evidence:** Typically demonstrated by Terms of Service, Data Processing Agreement, Master Service Agreement, Privacy Policy, or AI Addendum. May be a combination of these policies.
- **Priority guidance:** Prioritize validating control status: Legal review may be required to pass AIUC-1


## A003: Limit AI agent data collection
*Mandatory | Capabilities: Universal*

### A003.1 Config: Data collection scoping
- **Application:** Core - This should include:
- **Control:** - Configuring data collection limits to reduce data and privacy exposure. For example, limiting data collection to task-relevant information based on context, implementing scoping based on user roles or workflow requirements, and avoiding persistent or out-of-scope data access.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Code implementing data collection restrictions - may include RAG retrieval function with document filtering logic, session scoping configuration limiting data access per session ID, workflow conditional logic gating data collection by stage, permission decorators or middleware checking user roles before data access, or scoping functions rejecting out-of-scope queries with error messages.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### A003.2 Config: Alerting system for auth failures
- **Application:** Supplemental - This may include:
- **Control:** - Deploying monitoring mechanisms. Including ensuring AI systems only perform necessary inference and logging deviations from defined operational scope.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of code showing an alert or error handling system is triggered upon authz check failure, or screenshot of alerting configurations in logging software (e.g. Posthog, Sentry, Datadog, Axiom, or downstream alert in Slack)

### A003.3 Config: Authorization system integration
- **Application:** Supplemental - This may include:
- **Control:** - Integrating with existing authorization systems to align agent access permissions with organizational policies.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of code showing authorization checks when context is collected or before tool execution using existing authorization systems (e.g. oAuth, OSO, custom IAM) - should verify that authorization is checked at time of data collection/tool call, not just at initial agent invocation


## A004: Protect IP & trade secrets
*Mandatory | Capabilities: Universal*

### A004.1 Documentation: User guidance on confidential information
- **Application:** Core - This should include:
- **Control:** - Providing user guidance on protecting confidential information. For example, instructing employees not to input trade secrets, proprietary code, or confidential business information into AI systems, communicating data handling policies for AI tool usage, or establishing clear guidelines on what information can and cannot be shared with AI agents.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Policy document, training materials, or user guidelines instructing users on protecting confidential information when using AI systems.

### A004.2 Documentation: foundational model IP protections
- **Application:** Supplemental - This may include:
- **Control:** - Leveraging foundation model provider protections. For example, using providers with zero data retention policies, requiring contractual commitments that inputs are not used for training, selecting models with enhanced privacy guarantees for sensitive use cases.
- **Category:** Legal Policies
- **Typical location:** Vendor Contracts
- **Typical evidence:** Provider contracts, terms of service, or documentation showing IP protection commitments. Often found in third party's terms of use/service, DPA or AI Addendum/Schedule

### A004.3 Config: IP detection implementation
- **Application:** Supplemental - This may include:
- **Control:** - Implementing technical controls to detect proprietary information in outputs.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code, Product
- **Typical evidence:** Screenshot of code or configuration detecting proprietary information patterns in AI outputs - may include labelling proprietary files, filtering rules for internal identifiers/data labels/API keys, scanning logic for trade secret terminology, or rejection demonstrations showing appropriate responses to proprietary requests.

### A004.4 Config: IP disclosure monitoring
- **Application:** Supplemental - This may include:
- **Control:** - Establishing output monitoring for high-risk IP scenarios. For example, logging AI responses that accessed confidential data sources, implementing human review workflows for outputs flagged as potentially containing sensitive information.
- **Category:** Technical Implementation
- **Typical location:** Engineering Practice, Logs
- **Typical evidence:** Logs, audit trails, or review workflow documentation for AI outputs potentially containing sensitive information - may include logs of responses accessing confidential sources, flagged output review queues, or human approval workflows for high-risk disclosures.


## A005: Prevent cross-customer data exposure
*Mandatory | Capabilities: Universal*

### A005.1 Documentation: Consent for combined data usage
- **Application:** Core - This should include:
- **Control:** - Establishing explicit consent and disclosure for combined data usage. For example, informing customers when their data will be combined with competitor data, disclosing data anonymization and abstraction policies, providing opt-out mechanisms.
- **Category:** Legal Policies
- **Typical location:** Data Processing Agreement, Terms of Service
- **Typical evidence:** Typically demonstrated by Data Processing Agreement or Terms of Service
- **Priority guidance:** Prioritize validating control status: Legal review may be required to pass AIUC-1

### A005.2 Config: Customer data isolation controls
- **Application:** Core - This should include:
- **Control:** - Implementing customer data isolation controls. For example, enforcing strict logical and physical separation of customer data, applying tenant-specific encryption, validating data flow boundaries in shared infrastructure, establishing technical barriers between customer datasets during training.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot showing app_IDs in database schema, screenshot showing that namespace by appID is used in vector store for RAG or that logical isolation is implemented in an equivalent way, or screenshot of authz check in code verifying appIDs match before returning objects.

### A005.3 Config: Privacy-enhancing controls
- **Application:** Supplemental - This may include:
- **Control:** - Implementing specific privacy-enhancing technologies (PETs) to reduce competitive exposure.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** May include tokenization, hashing, or anonymization techniques (robust to prevent re-identification or reversal) making data algorithmic-usable but not human-readable, differential privacy implementation obfuscating individual contributions, federated learning configuration avoiding centralized raw data, or data masking/pseudonymization protecting customer identities.


## A006: Prevent PII leakage
*Mandatory | Capabilities: Universal*

### A006.1 Config: PII detection and filtering
- **Application:** Core - This should include:
- **Control:** - Implementing safeguards to prevent personal data leakage through AI system outputs and logs. For example, filtering prompts and outputs for personal identifiers before storage or display, implementing automated PII detection and redaction in system logs, preventing retention of outputs containing sensitive personal information, or blocking responses that would expose personal identifiers.
- **Category:** Technical Implementation
- **Typical location:** Eng: LLM output filtering logic, Eng: User LLM input filtering logic
- **Typical evidence:** Screenshot of code filtering LLM inputs and/or outputs for personal identifiers - may include keyword checks or regex patterns detecting PII (e.g. names, emails, SSNs, phone numbers), scrubbing functions removing personal data before storage or logging, output filtering blocking responses containing personal identifiers, log redaction configuration removing PII from application or system logs, or structured logging with PII isolation controls.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### A006.2 Config: PII access controls
- **Application:** Core - This should include:
- **Control:** - Requiring authentication and authorization for PII access. For example, role-based access controls for PII-containing systems, multi-factor authentication for sensitive data access, or approval-gated access to customer information.
- **Category:** Technical Implementation
- **Typical location:** Engineering Practice
- **Typical evidence:** Screenshot of IAM configuration or user roles list for systems containing PII - e.g. role-based access controls for log aggregation tools or internal dashboards with PII, authentication requirements for PII access, or approval workflow documentation (Jira tickets, approval systems) for internal workforce requests to view customer data.

### A006.3 Config: DLP system integration
- **Application:** Supplemental - This may include:
- **Control:** - Integrating with existing data loss prevention (DLP) systems to monitor and block outputs containing personal data in violation of policy.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of output pipeline integrating with DLP system to scan and block PII policy violations - may include DLP integration code scanning AI outputs before delivery to users, DLP configuration rules for PII detection, or logs showing blocked outputs containing personal data.


## A007: Prevent IP violations
*Mandatory | Capabilities: Text-generation, Voice-generation, Image-generation*

### A007.1 Documentation: Model provider IP infringement protections
- **Application:** Core - This should include:
- **Control:** - Documenting foundation model provider IP protections which may serve as primary infringement safeguards. For example, indemnification clauses or copyright/trademark guardrails.
- **Category:** Legal Policies
- **Typical location:** Vendor Contracts
- **Typical evidence:** Foundation model provider contract, terms of service, or data processing agreement showing IP protection commitments including copyright/trademark handling policies, indemnification clauses, liability coverage, and any documented limitations or exclusions. May include vendor questionnaire responses or certification documents addressing IP protections.

### A007.2 Config: IP infringement filtering
- **Application:** Supplemental - This may include:
- **Control:** - Establishing supplementary content filtering mechanisms where provider protections have gaps or limitations. For example, detecting copyrighted material in outputs, implementing trademark screening.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code, Eng: LLM output filtering logic
- **Typical evidence:** Screenshot of code, API configuration, or filtering system showing detection of copyrighted material, trademark screening, or content validation checks applied to AI outputs - this could be pattern matching logic, third-party API integration (e.g. copyright detection services), or custom filtering rules.

### A007.3 Logs: User-facing notices
- **Application:** Supplemental - This may include:
- **Control:** - Implementing user guidance and guardrails to reduce IP risk. For example, usage policies that explain prohibited content types, user warnings in product, restricting output generation in known infringement domains.
- Implementing restrictions in AI acceptable use policy.
- **Category:** Technical Implementation
- **Typical location:** Product, Acceptable Use Policy
- **Typical evidence:** Screenshot of user-facing IP risk guidance - may include warning messages when attempting high-risk operations, help center articles about IP infringement guidance, or UI elements explaining prohibited use cases.


## B001: Third-party testing of adversarial robustness
*Mandatory | Capabilities: Universal*

### B001.1 Report: adversarial testing results
- **Application:** Core - This should include:
- **Control:** - Establishing a taxonomy for adversarial risks. For example, drawing on NIST's AI 100-2e2023 attack classifications and aligning these to system architecture and use cases.
- Conducting comprehensive adversarial testing at least quarterly. For example, performing structured red-teaming, prompt injection assessments, jailbreaking attempts, adversarial perturbation testing, semantic manipulation, and simulated malicious tool invocations.
- Maintaining secure testing documentation. For example, recording test cases, methods, outcomes, and system behaviors with restricted access controls, implementing secure storage for sensitive testing materials.
- Establishing improvement processes based on findings. For example, assigning owners and remediation timelines based on test severity, tracking fixes through risk registers or issue management systems, documenting updates to safeguards and procedures.
- **Category:** Third-party Evals
- **Typical location:** Third-party evaluation report
- **Typical evidence:** Third-party evaluation report showing adversarial robustness testing - must include risk taxonomy tested, testing methodology and findings, secure documentation practices, and improvement tracking with remediation timelines and documentation.

### B001.2 Documentation: Security program integration
- **Application:** Supplemental - This may include:
- **Control:** - Aligning adversarial testing with broader security testing programs. For example, integrating AI-specific test cases into broader penetration testing, sharing threat models across red/blue teams, aligning test cycles with security audit and compliance calendars.
- **Category:** Operational Practices
- **Typical location:** Engineering Practice, Internal processes
- **Typical evidence:** Penetration test reports with AI-specific test cases, shared threat models, and testing calendars, or documentation of broader security program incorporating AI adversarial testing requirements.


## B002: Detect adversarial input
*Optional | Capabilities: Universal*

### B002.1 Config: Adversarial input detection and alerting
- **Application:** Core - This should include:
- **Control:** - Establishing detection and alerting. For example, implementing monitoring for prompt injection patterns, jailbreak techniques, adversarial input attempts, and exceeding rate limits, configuring alerts and threat notifications for suspicious activities.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of monitoring system, SIEM, or detection code showing rules and alerts for adversarial inputs - may include prompt injection detection patterns, jailbreak technique signatures, rate limit monitoring with threshold alerts, or notification configurations (Slack, PagerDuty, email)

### B002.2 Logs: Adversarial incident and response
- **Application:** Core - This should include:
- **Control:** - Implementing incident logging and response procedures. For example, logging suspected adversarial attacks with relevant context, escalating to designated personnel based on severity, and documenting response actions in a centralized system.
- **Category:** Technical Implementation
- **Typical location:** Logs, Engineering Tooling
- **Typical evidence:** Screenshot of incident management system or logs showing adversarial attack handling - may include log entries with timestamps and user/session context, escalation runbooks defining severity thresholds, or incident tickets in Jira/PagerDuty/ServiceNow documenting response actions and workflows.

### B002.3 Documentation: Updates to detection config
- **Application:** Core - This should include:
- **Control:** - Maintaining detection effectiveness through quarterly reviews. For example, updating detection rules based on emerging adversarial techniques, analyzing incident patterns and documenting system improvements.
- **Category:** Technical Implementation
- **Typical location:** Engineering Practice, Internal processes
- **Typical evidence:** Quarterly review documentation showing detection updates - for example, review meeting notes with incident pattern analysis, updated detection rules with version history, or tracking records showing rule improvements (e.g. GitHub/Jira tickets).

### B002.4 Config: Pre-processing adversarial detection
- **Application:** Supplemental - This may include:
- **Control:** - Implementing adversarial input detection prior to AI model processing where feasible. For example, using pre-processing filters to flag likely threats before model processing.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of pre-processing filtering logic or gateway - may include pattern-matching or heuristic code checking inputs before model processing, WAF or API gateway rules blocking adversarial patterns, or IP-based filtering.

### B002.5 Config: AI security alerts
- **Application:** Supplemental - This may include:
- **Control:** - Integrating adversarial input detection into existing security operations tooling. For example, forwarding flagged inputs to SIEM platforms, correlating detection with authentication and network logs, enabling SOC teams to triage AI-related security events.
- **Category:** Technical Implementation
- **Typical location:** Engineering Tooling
- **Typical evidence:** Screenshot of SIEM platform, SOC tooling, or log forwarding configuration showing adversarial detection integration - may include Splunk/Datadog/Elastic SIEM ingesting AI adversarial alerts, correlation rules linking AI events with authentication or network logs, SOC dashboard displaying AI security event triage, or code forwarding flagged inputs to security platforms.


## B003: Manage public release of technical details
*Optional | Capabilities: Universal*

### B003.1 Documentation: Technical information disclosure guidelines
- **Application:** Core - This should include:
- **Control:** - Documenting limitations on technical information release. For example, limiting public disclosure of model architectures, algorithms, training data details, system configurations, and performance metrics, requiring approval before sharing technical specifications or implementation details.
- Controlling organizational information to balance transparency with security. For example, limiting disclosure of AI team details, development timelines, and other information that could reveal technical capabilities, reviewing public communications for sensitive information.
- **Category:** Operational Practices
- **Typical location:** Internal policies
- **Typical evidence:** Policy document, SOP, or handbook section defining limitations and approval requirements for publicly sharing AI system technical details - may include communication policy limiting disclosure of model architectures or configurations, engineering handbook with approval workflows for technical specifications, or internal procedures controlling release of organizational AI information.

### B003.2 Documentation: Public disclosure approval records
- **Application:** Supplemental - This may include:
- **Control:** - Establishing approval processes. For example, requiring designated review for public content referencing AI capabilities in e.g. publications, presentations, and marketing materials, and documenting approved disclosures with business justification.
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Approval email, ticket, or review documentation for public AI communications - may include approval requests in email or Jira/Slack for blog posts or press releases, marketing review records for AI capability disclosures, or periodic security review logs for public-facing AI content.


## B004: Prevent AI endpoint scraping
*Mandatory | Capabilities: Universal*

### B004.1 Config: Anomalous usage detection
- **Application:** Core - This should include:
- **Control:** - Implementing systems distinguishing between high-volume legitimate usage and adversarial behavior. For example, using behavioral analytics and user profiling to calibrate detection thresholds and prevent false positives against trusted users.
- **Category:** Technical Implementation
- **Typical location:** Engineering Tooling, Engineering Code
- **Typical evidence:** Screenshot of anomaly detection system or configuration file - may include behavioral analytics dashboard (Datadog, Elastic, Splunk) with user scoring rules, rate limiting configuration with tier-based thresholds (config.yaml, API gateway settings), user allowlists or reputation tables, or code implementing session-based threshold logic.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### B004.2 Config: Rate limits
- **Application:** Core - This should include:
- **Control:** - Implementing rate limiting and query restrictions. For example, establishing per-user quotas to prevent model extraction, blocking excessive query patterns, implementing progressive restrictions for suspicious behavior, or using economic disincentives for high-volume usage.
- **Category:** Technical Implementation
- **Typical location:** Engineering Tooling
- **Typical evidence:** Screenshot of rate limiting configuration for API endpoints - may include per-user quota settings, query throttling rules, progressive restriction policies, WAF configuration (Cloudflare, AWS WAF, Azure Application Gateway) with blocking rules for excessive patterns, or pricing tier settings implementing usage-based cost increases.

### B004.3 Report: External pentest of AI endpoints
- **Application:** Core - This should include:
- **Control:** - Conducting simulated external attack testing of AI endpoints. For example, performing automated attack simulations, testing endpoint protection effectiveness against high-volume and distributed attacks, and documenting methodologies appropriate to organizational threat profile.
- **Category:** Technical Implementation
- **Typical location:** Engineering Practice
- **Typical evidence:** Third-party penetration test report for AI endpoints including attack simulations tested (e.g. scraping attempts, brute force, reconnaissance), rate limiting and endpoint protection validation, distributed attack testing, test methodology, and findings on protection effectiveness.

### B004.4 Documentation: Vulnerability remediation
- **Application:** Core - This should include:
- **Control:** - Maintaining endpoint security through remediation. For example, tracking identified vulnerabilities, implementing protective measures based on testing outcomes, and regularly updating endpoint defenses and detection thresholds.
- **Category:** Technical Implementation
- **Typical location:** Engineering Practice
- **Typical evidence:** Screenshot of issue tracking system (GitHub, Jira, Linear) showing endpoint vulnerability lifecycle - must include vulnerability identification, remediation proposal, implementation, and production deployment with timestamps and approval records.


## B005: Implement real-time input filtering
*Optional | Capabilities: Text-generation, Voice-generation, Image-generation*

### B005.1 Config: Input filtering
- **Application:** Core - This should include:
- **Control:** - Integrating automated moderation tools to filter inputs before they reach the foundation model. For example, integrating third-party moderation APIs, implementing custom filtering rules, configuring blocking or warning actions for flagged content, and establishing confidence thresholds based on risk category and severity
- **Category:** Technical Implementation
- **Typical location:** Eng: User LLM input filtering logic, Engineering Tooling
- **Typical evidence:** Screenshot of moderation tool integration showing API configuration, filtering rules, action settings (block/warn/modify), and confidence thresholds for different violation categories - this could be screenshots of configuration files, admin dashboard settings, or API integration code.

Example moderation tools: OpenAI Moderation API, Claude content filtering, VirtueAI/Hive/Spectrum Labs

### B005.2 Documentation: Input moderation approach
- **Application:** Supplemental - This may include:
- **Control:** - Documenting the moderation logic and rationale. For example, explaining chosen moderation tools, threshold justifications, and decision criteria for different risk categories.
- **Category:** Technical Implementation
- **Typical location:** Internal processes, Engineering Practice
- **Typical evidence:** Document explaining moderation approach including tool selection rationale, threshold settings with justifications, action logic for different violation types, and examples of how different input categories are handled.

### B005.3 Demonstration: Warning for blocked inputs
- **Application:** Supplemental - This may include:
- **Control:** Providing feedback to users when inputs are blocked.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot of user-facing messages or UI flows showing how blocked inputs are communicated to users - this could be error messages, warning dialogs, or alternative suggestions provided when content is filtered.

### B005.4 Logs: Input filtering
- **Application:** Supplemental - This may include:
- **Control:** - Logging flagged prompts for analysis and refinement of filters, while ensuring compliance with privacy obligations.
- **Category:** Technical Implementation
- **Typical location:** Logs
- **Typical evidence:** Screenshot of logging system showing how flagged inputs are captured, what metadata is included/excluded for privacy, retention policies, and audit trail - may include privacy documentation explaining logging disclosures to users.

### B005.5 Documentation: Input filter performance
- **Application:** Supplemental - This may include:
- **Control:** - Periodically evaluating filter performance and adjusting thresholds accordingly. For example, accuracy, latency, false positives/negatives.
- **Category:** Technical Implementation
- **Typical location:** Engineering Practice
- **Typical evidence:** Report or dashboard showing analysis of filter performance metrics (false positives, false negatives, accuracy, latency) and documented threshold adjustments made based on performance data - should include timestamps and rationale for changes.


## B006: Prevent unauthorized AI agent actions
*Mandatory | Capabilities: Automation*

### B006.1 Config: Agent service access restrictions
- **Application:** Core - This should include:
- **Control:** - Implementing technical restrictions that limit agent capabilities to authorized scope. For example, restricting agent access to approved backend services and APIs, enforcing network segmentation or API gateway rules, or implementing service-level authorization preventing access to sensitive systems.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of configuration showing technical limitations on agent backend access - may include API gateway rules restricting accessible services, network policies defining allowed endpoints, service-level authorization configuration, or architecture diagram showing agent isolation boundaries.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### B006.2 Config: Agent security monitoring and alerting
- **Application:** Core - This should include:
- **Control:** - Deploying monitoring and alerting for agent actions that exceed security boundaries. For example, logging all agent service interactions, alerting on access attempts to unauthorized systems or APIs, or anomaly detection flagging unusual connection patterns.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code, Logs
- **Typical evidence:** Screenshot of monitoring configuration tracking agent security-relevant actions - may include logging setup capturing agent service calls and authentication attempts, alert rules for unauthorized system access, security monitoring dashboard showing agent infrastructure interactions, or example logs demonstrating boundary violations are detected.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1


## B007: Enforce user access privileges to AI systems
*Mandatory | Capabilities: Universal*

### B007.1 Config: User access controls
- **Application:** Core - This should include:
- **Control:** - Implementing system-level access controls tailored to AI systems. For example, using role-based or attribute-based access to restrict access to model configuration, training datasets, tool-calling capabilities, or prompt logs, based on job function and system sensitivity.
- Restricting administrative and configuration privileges to authorized personnel. For example, limiting ability to alter system behavior, tools, or models.
- **Category:** Technical Implementation
- **Typical location:** Engineering Tooling
- **Typical evidence:** Screenshot of IAM platform, permission files, or admin panel showing role-based or attribute-based access restrictions for AI system resources (model configurations, training datasets, tool-calling capabilities, prompt logs) - may include IAM role assignments, permission policies, or authorization code validating user permissions before accessing sensitive AI components.

### B007.2 Documentation: Access reviews
- **Application:** Core - This should include:
- **Control:** - Conducting access reviews and updates at least quarterly. For example, validating access assignments, updating based on policy or role changes,  documenting access changes with AI-specific context (e.g. model access justification, changes to agent capability boundaries, or access to sensitive prompt/response history).
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Quarterly access review documentation - may include access review meeting notes, tracking records of access changes with justifications, or reports documenting role changes and access modifications based on policy updates.


## B008: Protect model deployment environment
*Mandatory | Capabilities: Universal*

### B008.1 Config: Model access controls
- **Application:** Core - This should include:
- **Control:** - Implementing model access protection. For example, restricting access to production AI models based on job function and operational need, implementing MFA for model system access, maintaining user access reviews appropriate to organizational size.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code, Internal processes
- **Typical evidence:** Screenshot of IAM configuration, permission settings, or admin panel showing role-based access restrictions for production AI models covering IAM role assignments restricting model access by job function, MFA configuration for model system access, and access review records validating model permissions.

### B008.2 Config: API deployment security
- **Application:** Core - This should include:
- **Control:** - Establishing deployment security controls. For example, applying scoped API tokens or signed requests, using TLS for all endpoint traffic, implementing schema validation to protect model APIs from malformed or adversarial input.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of API security configuration for model endpoints - may include scoped API token implementation, TLS/HTTPS certificate configuration for model API traffic, or schema validation code protecting model APIs from malformed or adversarial input.

### B008.3 Config: Model hosting security
- **Application:** Supplemental - This may include:
- **Control:** - Securing model hosting environments. For example, using up-to-date and minimal container images, scanning for known vulnerabilities in dependencies and base images, and applying infrastructure-level isolation techniques based on risk level (e.g. container namespaces, VM separation, or dedicated GPU access).
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of container configuration or infrastructure setup for model hosting - may include Dockerfile with minimal base images and up-to-date dependencies, vulnerability scanning results from Trivy or Snyk for container images, or infrastructure configuration showing isolation techniques (container namespaces, VM separation, network policies, dedicated GPU allocation).

### B008.4 Config: Model integrity verification
- **Application:** Supplemental - This may include:
- **Control:** - Verifying model integrity before and during deployment. For example, using cryptographic checksums or signed artifacts to detect tampering, scanning model files for malicious payloads.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of deployment pipeline or code implementing model integrity checks - may include cryptographic checksum verification, model artifact signature validation, hash comparison before deployment, model scanning configuration detecting malicious payloads (e.g. Pickle, ONNX) using tools like Cisco's pickle-fuzzer, Trail of Bit's Fickling, or deployment logs recording model version hashes.


## B009: Limit output over-exposure
*Mandatory | Capabilities: Text-generation, Voice-generation*

### B009.1 Config: Output volume limits
- **Application:** Core - This should include:
- **Control:** - Reducing or limiting the number of results shown in outputs to relevant only to balance security and utility. For example, character limits, limits on inference time.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code, Product
- **Typical evidence:** Screenshot of code or configuration implementing output restrictions - may include character or token limits, inference time limits, result count restrictions, or timeout configurations preventing excessive output. Can be demonstrated by product demo showing system timeout when requesting output exceeding limits.

### B009.2 Demonstration: User output notices
- **Application:** Supplemental - This may include:
- **Control:** - Providing user-facing notices or documentation about output limitations.
- **Category:** Operational Practices
- **Typical location:** Product
- **Typical evidence:** Screenshot of product interface showing user notices about output limitations - may include messages indicating truncated or suppressed outputs for security or privacy reasons, user documentation explaining limitation policies, or help articles describing output restrictions.

### B009.3 Config: Output precision controls
- **Application:** Supplemental - This may include:
- **Control:** - Limiting the fidelity of model outputs in certain use cases. For example, applying output rounding, threshold bands, or obfuscation techniques to reduce the risk of model inversion.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of code implementing output fidelity limitations - may include rounding logic for numerical outputs, threshold bands reducing precision, or obfuscation techniques preventing model inversion, precision-sensitive data disclosure, or adversarial model extraction attacks.


## C001: Define AI risk taxonomy
*Mandatory | Capabilities: Universal*

### C001.1 Documentation: AI risk taxonomy
- **Application:** Core - This should include:
- **Control:** - Defining risk categories with severity levels and examples based on industry and deployment context. For example, classifying harmful outputs such as distressed outputs, angry responses, high-risk advice, offensive content, bias, and deception, identifying other high-risk use cases such as safety-critical instructions, legal recommendations, financial advice.
- Aligning risk taxonomy with external frameworks and standards.
- Establishing severity grading appropriate to organizational context and risk tolerance. For example, implementing consistent scoring methodology across risk categories, defining thresholds for flagging and human review.
- **Category:** Operational Practices
- **Typical location:** Internal policies
- **Typical evidence:** Internal policy document, risk framework, or taxonomy defining AI risk categories with severity levels and examples specific to deployment context. Example taxonomies to draw upon include NIST AI RMF functions, EU AI Act article 9, ISO42001 controls.

### C001.2 Documentation: Risk taxonomy reviews
- **Application:** Core - This should include:
- **Control:** - Maintaining taxonomy currency with documented change management. For example, updating based on emerging threats or incidents.
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Meeting notes, change log, or review documentation showing quarterly reviews of the risk taxonomy. Could include review dates, participants, decisions made (categories added/removed/modified, threshold adjustments), rationale for changes, approvals records, and version history showing taxonomy updates over time with timestamps. Can be standalone or part of broader internal audit/review or change management procedures.


## C002: Conduct pre-deployment testing
*Mandatory | Capabilities: Universal*

### C002.1 Documentation: Pre-deployment test and approval records
- **Application:** Core - This should include:
- **Control:** - Conducting pre-deployment testing with documented results and identified issues. For example, structured hallucination testing, adversarial prompting, safety unit tests, and scenario-based walkthroughs.
- Completing risk assessments of identified issues before system deployment. For example, potential impact analysis, mitigation strategies, and residual risk evaluation.
- Obtaining approval sign-offs from designated accountable. For example, documented rationale for approval decisions and maintained records for review purposes.
- **Category:** Technical Implementation
- **Typical location:** Engineering Practice
- **Typical evidence:** Test results with identified issues and severity ratings, risk assessment with mitigation decisions, and approval sign-offs with rationale - may be combined in deployment gate documentation or provided as separate documents (e.g., test suite outputs from GitHub Actions/pytest, Jira/Linear tickets with risk assessment and approval, staging environment test reports, deployment checklist with sign-offs).

### C002.2 Config: SDLC integration
- **Application:** Supplemental - This may include:
- **Control:** - Integrating AI system testing into established software development lifecycle (SDLC) gates. For example, including threat modelling and risk evaluation during design phases, requiring risk evaluation and sign-off at staging or pre-production milestones, aligning with CI/CD or MLOps pipelines, and documenting test artefacts in shared repositories."
- **Category:** Technical Implementation
- **Typical location:** Engineering Practice
- **Typical evidence:** CI/CD pipeline configuration or workflow showing AI testing integrated as deployment gate - may include GitHub Actions/Jenkins/GitLab CI config files requiring test passage, pull request templates with testing checklists, or branch protection rules enforcing pre-deployment validation.

### C002.3 Documentation: Vulnerability scan results
- **Application:** Supplemental - This may include:
- **Control:** - Implementing pre-deployment vulnerability scanning of AI artifacts and dependencies. For example, scanning AI models and ML libraries for security vulnerabilities, validating runtime behavior for unsafe operations, and analyzing outputs for harmful content before deployment.
- **Category:** Technical Implementation
- **Typical location:** Engineering Tooling
- **Typical evidence:** Screenshot of security scanning tools or CI/CD pipeline showing vulnerability analysis of AI artifacts and dependencies - may include GitHub/GitLab security tab with dependency alerts, Snyk or Dependabot vulnerability findings, pip-audit or safety check terminal output showing CVE scans, model file scanning results, or CI/CD logs showing security scan execution.


## C003: Prevent harmful outputs
*Mandatory | Capabilities: Text-generation, Voice-generation, Image-generation*

### C003.1 Config: Harmful output filtering
- **Application:** Core - This should include:
- **Control:** - Implementing content filtering for harmful output types. For example, detecting and blocking distressed responses, angry language, offensive content, biased statements, and deceptive information.
- **Category:** Technical Implementation
- **Typical location:** Eng: LLM output filtering logic
- **Typical evidence:** Screenshot of content filtering rules, moderation API configuration, or classifier settings showing detection and blocking logic for harmful output types - may include filtering rules in code, third-party moderation tool configuration (e.g., OpenAI Moderation API, Perspective API), or custom classifier model settings with harm category definitions.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### C003.2 Config: Guardrails for high-risk advice
- **Application:** Core - This should include:
- **Control:** - Implementing guardrails for advice generation. For example, restricting high-risk recommendations in sensitive domains, requiring disclaimers for guidance.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of system prompts, guardrail rules, or domain restrictions showing safety controls on advice generation - may include defensive prompting, domain-specific output restrictions (e.g., medical/legal/financial advice blocklists), or conditional response templates that add warnings for sensitive topics.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### C003.3 Config: Guardrails for biased outputs
- **Application:** Supplemental - This may include:
- **Control:** - Implementing bias detection and mitigation controls. For example, monitoring for discriminatory patterns, implementing fairness checks in outputs.
- **Category:** Technical Implementation
- **Typical location:** Eng: LLM output filtering logic
- **Typical evidence:** Documentation of bias eval results testing for stereotypical responses across demographic attributes, manual review logs documenting bias assessments, or output filtering rules blocking discriminatory patterns - may include automated fairness evaluation tools or bias monitoring dashboards if implemented.

### C003.4 Documentation: Filtering performance benchmarks
- **Application:** Supplemental - This may include:
- **Control:** - Evaluating harm mitigation controls using performance metrics.
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Test results, metrics dashboard, or evaluation report showing performance of harm controls - may include false positive/negative rates, coverage analysis of test scenarios, benchmark results against harm datasets (e.g., ToxiGen, RealToxicityPrompts), or confusion matrices showing filtering accuracy across harm categories.


## C004: Prevent out-of-scope outputs
*Mandatory | Capabilities: Text-generation, Voice-generation*

### C004.1 Config: out-of-scope guardrails
- **Application:** Core - This should include:
- **Control:** - Detecting and blocking out-of-scope requests. For example, detecting conversations outside intended use cases, blocking prohibited topics, providing redirection messages when users hit boundaries, and escalating or restricting access for repeated violations.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of blocking rules, defensive prompting, or filtering configuration showing how out-of-scope requests are detected and handled - may include topic blocklists, redirection message templates, escalation rules for repeated attempts, or system prompts defining allowed topics.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### C004.2 Logs: Out-of-scope attempts
- **Application:** Core - This should include:
- **Control:** - Tracking out-of-scope violations and updating boundaries. For example, logging boundary violations, adjusting restrictions based on misuse patterns.
- **Category:** Technical Implementation
- **Typical location:** Logs
- **Typical evidence:** Logs showing out-of-scope attempts with frequency data. May include documentation of boundary updates made in response to violations, monitoring dashboard of flagged requests, change log showing restriction updates with rationale, or incident reports triggering scope adjustments.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### C004.3 Demonstration: User guidance on scope
- **Application:** Supplemental - This may include:
- **Control:** - Providing user guidance on system capabilities and limitations. For example, communicating what the AI system can and cannot do, intended use cases, and topics or requests outside the system's scope.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot of user-facing guidance explaining system capabilities and limitations - may include onboarding tooltips or welcome screens, help documentation or FAQs describing intended use, UI warnings when approaching scope boundaries, or published usage guidelines.


## C005: Prevent customer-defined high risk outputs
*Mandatory | Capabilities: Universal*

### C005.1 Config: Risk detection and response
- **Application:** Core - This should include:
- **Control:** - Implementing detection and blocking mechanisms aligned with organizational risk taxonomy. For example, deploying filtering based on defined risk categories and severity thresholds.
- Implementing response actions for detected risks. For example, blocking high-severity outputs, flagging medium-risk content for review, logging violations for monitoring and analysis.
- **Category:** Technical Implementation
- **Typical location:** Eng: LLM output filtering logic
- **Typical evidence:** Screenshot of filtering rules, system configuration, or code showing detection logic mapped to AI risk taxonomy categories and corresponding response actions per severity level - may include risk classifiers with block/flag/log rules, content moderation API configuration defining actions by risk type, or defensive prompting.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### C005.2 Documentation: Human review workflows
- **Application:** Supplemental - This may include:
- **Control:** - Establishing escalation procedures for flagged high-risk content. For example, defining when human review is required and establishing approval workflows for edge cases.
- **Category:** Technical Implementation
- **Typical location:** Engineering Practice
- **Typical evidence:** Documentation or workflow configuration showing human review and escalation procedures for flagged content - may include runbook defining escalation criteria and review SLAs, workflow diagram showing approval process, or ticketing system configuration (Jira, Linear) with content review queues and assignment rules.

### C005.3 Config: Automated response mechanisms
- **Application:** Supplemental - This may include:
- **Control:** - Implementing automated real-time interventions. For example, blocking or modifying outputs based on severity.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of code or system configuration showing automated response mechanisms - may include logic blocking or modifying outputs based on risk scores, or dynamic warning messages triggered by content flags.


## C006: Prevent output vulnerabilities
*Mandatory | Capabilities: Universal*

### C006.1 Config: Output sanitization
- **Application:** Core - This should include:
- **Control:** - Establishing output sanitization and validation procedures before presenting content to users. For example, encoding or stripping potentially malicious content, validating structured outputs against safe schemas, blocking unsafe URLs, and enforcing secure rendering modes.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of code or configuration implementing output sanitization - may include HTML/JavaScript/shell syntax encoding functions, URL validation or rewriting rules blocking unsafe links, schema validation checking structured outputs (JSON/YAML/XML) against whitelists, CSP header configuration, or template rendering with auto-escaping enabled.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### C006.2 Demonstration: Warning labels for untrusted content
- **Application:** Core - This should include:
- **Control:** - Implementing security labeling and content handling based on trust level. For example, marking untrusted or third-party content, distinguishing external data from system-generated content, and applying differentiated security controls based on content source.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot of UI or code showing trust-based content handling - may include visual indicators marking third-party content (badges, styling, warning icons), metadata tags tracking content source and trust level, or code applying conditional security controls based on content origin (e.g., stricter sanitization for external sources).
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### C006.3 Config: Adversarial output detection
- **Application:** Supplemental - This may include:
- **Control:** - Detecting advanced output-based attack patterns. For example, identifying prompt injection attempts, model subversion techniques, payloads targeting downstream systems, or obfuscated exploits designed to bypass filters.
- **Category:** Technical Implementation
- **Typical location:** Eng: LLM output filtering logic
- **Typical evidence:** Screenshot of detection rules or monitoring system identifying advanced attack patterns in outputs - may include pattern matching for prompt injection chains or jailbreak tokens, payload signature scanning detecting command injection or SQL queries, or anomaly detection flagging obfuscated exploits bypassing basic filters.


## C007: Flag high risk outputs
*Optional | Capabilities: Universal*

### C007.1 Documentation: Definition of high-risk recommendations criteria
- **Application:** Core - This should include:
- **Control:** - Defining high-risk output criteria drawing on risk taxonomy.
- **Category:** Operational Practices
- **Typical location:** Internal policies
- **Typical evidence:** Document or policy defining high-risk outputs requiring human review - should specify criteria for flagging (e.g. financial advice thresholds, medical/legal/safety domains, reputational harm triggers). Can be standalone or included in existing AI risk taxonomy/AI risk policy.

### C007.2 Config: High-risk detection mechanisms
- **Application:** Core - This should include:
- **Control:** - Implementing automated detection mechanisms for high-risk outputs. For example, using content filtering, risk scoring, or classification models to identify outputs requiring review or flagging.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of detection code, configuration file, or rules engine showing high-risk output filtering - may include keyword lists or regex patterns flagging sensitive topics, scoring logic assigning risk values to recommendations, if/then rules defining high-risk conditions, ML model configuration (e.g., classification thresholds in config.yaml), or API response showing confidence scores with risk thresholds.

### C007.3 Documentation: Human review workflows
- **Application:** Supplemental - This may include:
- **Control:** - Establishing human review workflows for flagged high-risk outputs. For example, assigning reviewers, defining escalation procedures for complex cases, managing review queues with response time tracking, and documenting review decisions.
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Workflow documentation or ticketing system configuration showing human review process for flagged outputs - may include runbook with reviewer assignments and escalation paths, queue management in Jira/Linear/support ticketing with pending review tracking, SLA targets for review response times, or procedure document defining review decision documentation requirements.


## C008: Monitor AI risk categories
*Optional | Capabilities: Universal*

### C008.1 Logs: AI risk monitoring
- **Application:** Core - This should include:
- **Control:** - Establishing ongoing monitoring of AI outputs across risk categories. For example, conducting regular evaluations prioritized by risk severity, sampling outputs for review, and tracking system behavior patterns.
- **Category:** Technical Implementation
- **Typical location:** Engineering Tooling
- **Typical evidence:** Screenshot of monitoring dashboard, logging system, or evaluation reports showing ongoing AI output tracking - may include output sampling logs with review results, behavior trace logs showing system patterns, prompt-response logging configuration, evaluation schedules prioritized by risk severity, or monitoring metrics dashboard tracking trends over time.

### C008.2 Documentation: Monitoring findings
- **Application:** Supplemental - This may include:
- **Control:** - Maintaining documentation. For example, recording identified scenarios with clear examples, updating risk taxonomy based on monitoring findings and incidents.
- **Category:** Technical Implementation
- **Typical location:** Engineering Practice
- **Typical evidence:** Document or change log showing identified risk scenarios with examples - may include incident reports triggering taxonomy changes, risk scenario database with concrete examples, or version history of risk taxonomy showing updates with rationale linked to monitoring findings.

### C008.4 Config: Security tooling
- **Application:** Supplemental - This may include:
- **Control:** - Integrating AI output monitoring with existing security tools. For example, forwarding alerts and flagged outputs to SIEM platforms, applying standard logging formats (e.g. JSON, syslog) to support automated threat detection workflows.
- **Category:** Technical Implementation
- **Typical location:** Engineering Tooling
- **Typical evidence:** Screenshot of SIEM integration, log forwarding configuration, or security tool settings showing AI monitoring data flowing into existing security infrastructure - may include Splunk/Datadog/Elastic forwarding rules for AI alerts, JSON/syslog format configuration for AI logs, or SIEM dashboard showing AI-related events alongside other security telemetry.


## C009: Enable real-time feedback and intervention
*Optional | Capabilities: Universal*

### C009.1 Demonstration: User intervention mechanisms
- **Application:** Core - This should include:
- **Control:** - Enabling user intervention capabilities. For example, providing mechanisms for users to pause, stop, or redirect system behavior, implementing feedback collection tools for users to report issues or concerns, ensuring technical controls persist across devices and interaction contexts.
- Ensuring accessibility of feedback and intervention mechanisms. For example, adhering to WCAG 2.1 standards for color contrast, screen reader compatibility, keyboard navigation, and clear messaging for users with disabilities.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot, screen recording or voice recording demonstrating intervention controls (stop/pause/redirect buttons, feedback forms, issue reporting mechanisms) with accessibility features integrated (e.g. keyboard navigation, high contrast modes, screen reader labels)

### C009.2 Documentation: User feedback & intervention reviews
- **Application:** Supplemental - This may include:
- **Control:** - Reviewing user feedback and intervention logs regularly. For example, evaluating patterns in interventions, adapting communication methods based on user needs and emerging risk considerations.
- Analyzing collected feedback using structured methodologies. For example, categorizing by risk domain, prioritizing based on frequency and severity,  routing high-impact or repeat issues into product backlog or compliance workflows.
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Logs, reports, or dashboard showing review and analysis of user feedback and intervention patterns - may include feedback summary reports, intervention frequency analysis, categorization by risk domain, documentation of system changes made in response to patterns, or integration with product backlog/compliance workflows.


## C010: Third-party testing for harmful outputs
*Mandatory | Capabilities: Text-generation, Voice-generation, Image-generation*

### C010.1 Report: Harmful output testing
- **Application:** Core - This should include:
- **Control:** - Appointing qualified third-party assessors. Including selecting assessors with relevant technical capabilities for identified risk areas, maintaining records of assessor qualifications and independence.
- Conducting regular testing. Including performing assessments of harmful outputs at least every quarter, defining testing scope and methodologies based on risk classifications and industry benchmarks like ToxiGen, coordinating with internal security and testing teams.
- Maintaining documentation. Including testing scope, results, and remediation actions taken, tracking follow-up activities and resolution timelines.
- **Category:** Third-party Evals
- **Typical location:** Third-party evaluation report
- **Typical evidence:** Third-party evaluation report showing harmful output testing - must include documentation of assessor qualifications, testing methodology and findings, and improvement tracking with remediation timelines and documentation.


## C011: Third-party testing for out-of-scope outputs
*Mandatory | Capabilities: Text-generation, Voice-generation*

### C011.1 Report: Out-of-scope output testing
- **Application:** Core - This should include:
- **Control:** - Appointing qualified third-party assessors. Including selecting assessors with relevant technical capabilities for identified risk areas, maintaining records of assessor qualifications and independence.
- Conducting regular testing. Including defining testing scope and methodologies based on risk taxonomy and performing assessments of out-of-scope outputs at least every quarter. 
- Maintaining documentation. Including testing scope, results, and remediation actions taken, tracking follow-up activities and resolution timelines.
- **Category:** Third-party Evals
- **Typical location:** Third-party evaluation report
- **Typical evidence:** Third-party evaluation report showing out-of-scope output testing - must include documentation of assessor qualifications, testing methodology and findings, and improvement tracking with remediation timelines and documentation.


## C012: Third-party testing for customer-defined risk
*Mandatory | Capabilities: Universal*

### C012.1 Third-party evaluation report assessing customer-defined risk
- **Application:** Core - This should include:
- **Control:** - Appointing qualified third-party assessors. Including selecting assessors with relevant technical capabilities for identified risk areas, maintaining records of assessor qualifications and independence.
- Conducting regular testing. Including defining testing scope and methodologies based on risk taxonomy and performing assessments of high-risk areas at least every quarter.
- Maintaining documentation. Including testing scope, results, and remediation actions taken, tracking follow-up activities and resolution timelines.
- **Category:** Third-party Evals
- **Typical location:** Third-party evaluation report
- **Typical evidence:** Third-party evaluation report showing testing of customer-defined risk - must include documentation of assessor qualifications, testing methodology and findings, and improvement tracking with remediation timelines and documentation.


## D001: Prevent hallucinated outputs
*Mandatory | Capabilities: Text-generation, Voice-generation*

### D001.1 Config: Groundedness filter
- **Application:** Core - This should include:
- **Control:** - Implementing factual accuracy controls. For example, deploying available fact-checking mechanisms, flagging uncertain or low-confidence responses.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of code or configuration showing groundedness validation - may include filters checking responses against source documents, fact-checking API integration, or logic comparing generated content to retrieved context for factual accuracy.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### D001.2 Demonstration: User-facing citations & source attributions
- **Application:** Core - This should include:
- **Control:** - Establishing information source validation. For example, requiring citations for factual claims, implementing source reliability checks.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot of UI or output format showing citations and source attributions provided to users - may include inline citations, source links, reference lists, or attribution labels identifying where information originated.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### D001.3 Demonstration: User-facing uncertainty labels
- **Application:** Supplemental - This may include:
- **Control:** - Maintaining uncertainty communication. For example, displaying confidence levels, providing appropriate disclaimers for generated information.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot of UI or output format showing confidence levels, uncertainty disclaimers, or warnings for generated information - may include confidence score displays, low-certainty warnings, or standard disclaimers about potential inaccuracies.


## D002: Third-party testing for hallucinations
*Mandatory | Capabilities: Text-generation, Voice-generation*

### D002.1 Report: Hallucination testing results
- **Application:** Core - This should include:
- **Control:** - Appointing qualified third-party assessors. Including selecting assessors with relevant technical capabilities for identified risk areas, maintaining records of assessor qualifications and independence.
- Conducting regular testing. Including defining testing scope and methodologies based on risk taxonomy and performing assessments at least every quarter.
- Maintaining documentation. Including testing scope, results, and remediation actions taken, tracking follow-up activities and resolution timelines.
- **Category:** Third-party Evals
- **Typical location:** Third-party evaluation report
- **Typical evidence:** Third-party evaluation report showing hallucination testing - must include risk taxonomy tested, testing methodology and findings, and improvement tracking with remediation timelines and documentation.


## D003: Restrict unsafe tool calls
*Mandatory | Capabilities: Automation*

### D003.1 Config: Tool authorization & validation
- **Application:** Core - This should include:
- **Control:** - Implementing function call validation and authorization. For example, restricting tool access to approved functions, validating parameters before execution.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of code or configuration showing function allowlists, parameter validation logic, or authz checks before tool execution - may include tool permission schemas, input validation functions, or access control lists restricting available tools per agent/user.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### D003.2 Config: Rate limits for tools
- **Application:** Core - This should include:
- **Control:** - Enforcing rate limits and transaction caps for autonomous tool use.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of code or configuration showing rate limits and transaction caps on tool usage - may include per-tool usage quotas, time-windowed limits, or circuit breakers preventing excessive autonomous tool calls.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### D003.3 Config: Tool call log
- **Application:** Core - This should include:
- **Control:** - Establishing execution monitoring and logging. For example, tracking all tool calls, monitoring for unauthorized access attempts or scope violations.
- **Category:** Technical Implementation
- **Typical location:** Logs
- **Typical evidence:** Screenshot of logging configuration, monitoring dashboard, or audit logs showing tracked tool calls - may include tool execution logs with timestamps and parameters, alerts for unauthorized access attempts, or monitoring system flagging scope violations.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### D003.4 Config: Human-approval workflows
- **Application:** Supplemental - This may include:
- **Control:** - Requiring human approval for sensitive tool operations. For example, requiring human confirmation before executing high-risk actions, implementing approval workflows for operations beyond autonomous boundaries.
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Screenshot of approval workflow, code requiring human confirmation, or ticketing system for sensitive tool operations

### D003.5 Documentation: tool call log reviews
- **Application:** Supplemental - This may include:
- **Control:** - Reviewing patterns of AI tool usage. For example, identifying anomalies, updating tool permissions, and retiring unused or high-risk functions during scheduled evaluations.
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Reports or documentation showing periodic review of tool usage patterns, permission updates, and function retirement decisions - may include usage analytics identifying anomalies, change logs showing permission adjustments, or records of deprecated/retired tools with rationale.


## D004: Third-party testing of tool calls
*Mandatory | Capabilities: Automation*

### D004.1 Report: Tool call testing
- **Application:** Core - This should include:
- **Control:** - Appointing qualified third-party assessors. Including selecting assessors with relevant technical capabilities for identified risk areas, maintaining records of assessor qualifications and independence.
- Conducting regular testing. Including defining testing scope and methodologies based on risk taxonomy and performing assessments of tool calls at least every quarter.
- Maintaining documentation. Including testing scope, results, and remediation actions taken, tracking follow-up activities and resolution timelines.
- **Category:** Third-party Evals
- **Typical location:** Third-party evaluation report
- **Typical evidence:** Third-party evaluation report showing tool call testing - must include risk taxonomy tested, testing methodology and findings, and improvement tracking with remediation timelines and documentation.


## E001: AI failure plan for security breaches
*Mandatory | Capabilities: Universal*

### E001.1 Documentation: AI failure plan for security breaches
- **Application:** Core - This should include:
- **Control:** - Assigning a breach response lead from existing staff. For example, IT manager, security officer, or designated executive with authority to engage external counsel and specialists as needed.
- Defining breach notification procedures. For example, customer communications, regulatory reporting requirements, and vendor notifications based on applicable privacy laws.
- Implementing security remediation measures. For example, system freeze capabilities, vulnerability fixes, access control updates, and coordination with external security consultants when internal expertise is insufficient.
- Establishing evidence collection requirements with guidance on preserving evidence for potential legal review. For example, system logs, user activity records, and basic documentation.
- **Category:** Operational Practices
- **Typical location:** AI failure plan
- **Typical evidence:** Can be standalone document or integrated in existing incident response procedures/policies


## E002: AI failure plan for harmful outputs
*Mandatory | Capabilities: Text-generation, Voice-generation, Image-generation*

### E002.1 Documentation: AI failure plan for harmful outputs
- **Application:** Core - This should include:
- **Control:** - Implementing customer communication protocols. For example, disclosure procedures, explanation of corrective actions, and follow-up commitments with executive approval for significant incidents.
- Establishing immediate mitigation steps with designated staff responsibilities. For example, system freeze capabilities, output suppression, customer notification, and system adjustments.
- **Category:** Operational Practices
- **Typical location:** AI failure plan
- **Typical evidence:** Can be standalone document or integrated in existing incident response procedures/policies

### E002.2 Documentation: Additional harmful output failure procedures
- **Application:** Supplemental - This may include:
- **Control:** - Defining harmful output categories with reference to risk taxonomy. For example, discriminatory content, offensive material, inappropriate recommendations, ideally with concrete examples.
- Coordinating external support engagement. For example,  legal counsel consultation, PR support, and insurance claim procedures.
- **Category:** Operational Practices
- **Typical location:** AI failure plan
- **Typical evidence:** May include harmful output category definitions referenced to risk taxonomy, external support contact list (legal counsel, PR firms, insurance providers), support engagement procedures or runbooks, or escalation criteria for involving external parties.


## E003: AI failure plan for hallucinations
*Mandatory | Capabilities: Text-generation, Voice-generation*

### E003.1 Documentation: AI failure plan for hallucinations
- **Application:** Core - This should include:
- **Control:** - Establishing compensation assessment procedures. For example, loss evaluation methods, settlement approaches, and payment authorization levels with appropriate approval requirements.
- Implementing remediation measures. For example, system freeze capabilities, model adjustments, output validation improvements, customer notification, and enhanced monitoring.
- **Category:** Operational Practices
- **Typical location:** AI failure plan
- **Typical evidence:** Can be standalone document or integrated in existing incident response procedures/policies

### E003.2 Documentation: Additional hallucination failure procedures
- **Application:** Supplemental - This may include:
- **Control:** - Defining hallucination incident types. 
- Coordinating potential external support. For example, legal consultation for significant claims, financial review when needed, and insurance coverage activation.
- **Category:** Operational Practices
- **Typical location:** AI failure plan
- **Typical evidence:** May include hallucination incident categories (e.g. factual errors, incorrect recommendations), external support contact list (legal counsel, financial reviewers, insurance providers), support engagement procedures, or escalation criteria for involving external parties.


## E004: Assign accountability
*Mandatory | Capabilities: Universal*

### E004.1 Documentation: Change approval policy and records
- **Application:** Core - This should include:
- **Control:** - Defining AI system changes requiring approval including model selection, material changes to the meta prompt, adding / removing guardrails, changes to end-user workflow, other changes that drive material. For example, +/-10% performance on evals.
- Assigning an accountable lead as approver for each of these changes. Can follow a RACI structure to formalize roles of those consulted and informed.
- **Category:** Operational Practices
- **Typical location:** Internal policies
- **Typical evidence:** Documentation or policy defining which AI system changes require approval with assigned accountable leads, and approval records showing sign-offs with supporting evidence. Can be a change management policy, overview table in e.g. Notion, approval logs from Jira/Linear/GitHub, or deployment gate documentation.

### E004.2 Config: Code signing implementation
- **Application:** Supplemental - This may include:
- **Control:** - Implementing code signing and verification processes for AI models, libraries, and deployment artefacts to ensure only digitally signed components are approved for production use.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code, Engineering Practice
- **Typical evidence:** Screenshot of code signing configuration, CI/CD pipeline requiring signed artifacts, or verification process for AI components - may include model signing process, signature verification in deployment pipeline, artifact registry showing signed models/libraries, or policy enforcement blocking unsigned components from production.


## E005: Assess cloud vs on-prem processing
*Mandatory | Capabilities: Universal*

### E005.1 Documentation: Deployment decisions
- **Application:** Core - This should include:
- **Control:** - Conducting deployment risk assessments. For example, evaluating data sensitivity, regulatory compliance requirements, IP protection needs, and security controls for cloud vs. on-premises AI processing.
- Documenting decision criteria and rationale. For example, establishing clear selection factors, maintaining records of deployment choices with business justification.
- Reviewing deployment decisions when requirements change. For example, reassessing choices when data sensitivity, regulations, or threat landscape evolves.
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Risk assessment and decision record evaluating cloud vs. on-premises factors (e.g. data sensitivity, regulatory requirements, security controls) with documented criteria and rationale - may include deployment decision memos, risk assessment reports, and records of periodic reviews when requirements changed.


## E006: Conduct vendor due diligence
*Mandatory | Capabilities: Universal*

### E006.1 Documentation: Vendor due diligence
- **Application:** Core - This should include:
- **Control:** - Defining assessment criteria for foundational or upstream AI models. For example, data handling and ownership practices, PII controls, security measures, compliance status, open-source.
- Conducting documented assessments. For example, scoring results, verification activities such as certifications reviewed and references contacted, and approval decisions. 
- Maintaining assessment records with sufficient detail for audit purposes and retaining due diligence evidence before vendor approval.
- **Category:** Operational Practices
- **Typical location:** Vendor Contracts, Internal processes
- **Typical evidence:** Vendor assessment records showing evaluation criteria, scoring results, verification activities, approval decisions with accountable leads, and retained evidence supporting the assessment. May include vendor questionnaires, security reviews, compliance documentation, or due diligence reports.


## E007: [Retired] Document system change approvals
*Optional | Capabilities: Universal*

### E007.1 Retired
- **Application:** Core - This should include:
- **Control:** - Documenting formal review and approval decisions for changes defined in E004: Assign accountability.
- **Category:** 
- **Typical evidence:** This requirement was merged into E004 at the Q1, 2026 standard update. See aiuc-1.com/changelog for more information


## E008: Review internal processes
*Mandatory | Capabilities: Universal*

### E008.1 Documentation: Internal review
- **Application:** Core - This should include:
- **Control:** - Reviewing decision processes every quarter including AI system changes, foundational model selection, security assessment.
- Maintaining a centralized repository of decision records and internal review of these record. For example, supporting evidence reviewed, remediation plans.
- Documenting and tracking remediation of any risks identified.int
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Centralized repository, policy, or tickets showing quarterly internal reviews - e.g. review meeting notes or calendars, decision logs in Jira/Notion/Confluence, risk registers with remediation status, threat modelling outcomes, or audit trails of review activities.

### E008.2 Documentation: External feedback integration
- **Application:** Supplemental - This may include:
- **Control:** - Collecting and implementing external feedback on AI systems. For example, system risks, new threat patterns, new mitigation strategies.
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Documentation showing external feedback collected and implemented - may include external security advisories reviewed, threat intelligence integrated, third-party recommendations adopted, or records of external input incorporated into system improvements.


## E009: Monitor third-party access
*Optional | Capabilities: Universal*

### E009.1 Config: Third-party access monitoring
- **Application:** Core - This should include:
- **Control:** - Configuring logging for third-party interactions. For example, capturing API connections, user access sessions, data exchanges, and service integrations.
- Capturing access metadata. For example, user identification, authentication timestamps, accessed resources, session duration, origin IP addresses, and resource usage patterns.
- **Category:** Technical Implementation
- **Typical location:** Engineering Tooling
- **Typical evidence:** Screenshot of logging system or SIEM configuration showing third-party interactions being monitored with captured metadata - may include cloud logging interface (Google Cloud Logging, AWS CloudWatch, Azure Monitor) showing logged API requests with timestamps/IPs/user agents, access logs capturing authentication events and resource access, or SIEM dashboard displaying third-party connection monitoring with relevant metadata fields.


## E010: Establish AI acceptable use policy
*Mandatory | Capabilities: Universal*

### E010.1 Documentation: AI acceptable use policy
- **Application:** Core - This should include:
- **Control:** - Defining prohibited AI usage for end-users. For example, jailbreak attempts, malicious prompt injection, unauthorized data extraction, generation of harmful content, and misuse of customer data.
- **Category:** Legal Policies
- **Typical location:** Acceptable Use Policy
- **Typical evidence:** Policy document defining acceptable and/or prohibited AI usage - can be standalone document or parts of, e.g., terms of service
- **Priority guidance:** Prioritize validating control status: Legal review may be required to pass AIUC-1

### E010.2 Config: AUP violation detection
- **Application:** Core - This should include:
- **Control:** - Implementing detection and monitoring tools. For example, prompt analysis, output filtering, usage pattern anomalies, and suspicious access attempts.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Screenshot of code, configuration, or monitoring system detecting acceptable use policy violations - may include prompt analysis logic, output filtering rules, anomaly detection for usage patterns, or alerting on suspicious access attempts.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### E010.3 Demonstration: User notification for AUP breaches
- **Application:** Core - This should include:
- **Control:** - Implementing user feedback when policy is breached. For example, showing alerts or error messages when inputs violate acceptable use.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot of user-facing alerts or error messages displayed when acceptable use policy is violated - may include in-product warning messages, blocked request notifications, or error screens explaining policy violations.
- **Priority guidance:** Prioritize validating control status: Technical resources may be needed to pass AIUC-1

### E010.4 Documentation: Guardrails enforcing acceptable use
- **Application:** Supplemental - This may include:
- **Control:** - Real-time monitoring, blocking, or alerting capabilities.
- Maintaining logging and tracking systems. For example, incident creation, violation tracking with case assignment and resolution documentation.
- Conducting regular effectiveness reviews. For example, quarterly analysis of violation trends, tool performance assessment, policy updates based on emerging threats, and user training adjustments.
- **Category:** Technical Implementation
- **Typical location:** Engineering Practice
- **Typical evidence:** Documentation or screenshots showing additional AUP enforcement mechanisms - may include real-time blocking/alerting systems, violation tracking logs with incident management, effectiveness review reports analyzing violation trends and policy updates, or training materials addressing emerging misuse patterns.


## E011: Record processing locations
*Mandatory | Capabilities: Universal*

### E011.1 Documentation: AI processing locations
- **Application:** Core - This should include:
- **Control:** - Maintaining AI infrastructure location documentation. For example, geographic locations of foundation model processing locations and inference endpoint regions, documenting third-party AI service provider data handling locations.
- Reviewing and updating documentation regularly.
- **Category:** Operational Practices
- **Typical location:** Trust Center
- **Typical evidence:** Subprocessor list showing third-party AI provider locations, infrastructure documentation listing cloud regions and inference endpoints, or data flow diagram with geographic processing locations and version history or review dates.

### E011.2 Documentation: Data transfer compliance
- **Application:** Supplemental - This may include:
- **Control:** - Implementing transfer compliance procedures. For example, assessing data transfer requirements for AI training data and inference processing, maintaining approved transfer mechanisms for foundation model providers and AI infrastructure, mitigating transfer risk for cross-border AI model training.
- **Category:** Legal Policies
- **Typical location:** Internal policies, Data Processing Agreement
- **Typical evidence:** Demonstrated by DPA, data transfer impact assessments, approved transfer mechanism documentation (Standard Contractual Clauses, adequacy decisions), cross-border data flow approvals for AI training/inference, or risk assessments for international AI processing.


## E012: Document regulatory compliance
*Mandatory | Capabilities: Universal*

### E012.1 Documentation: Regulatory compliance reviews
- **Application:** Core - This should include:
- **Control:** - Identifying relevant regulations. For example, data protection laws. For example, GDPR, CCPA, sector-specific requirements, emerging AI standards. For example, EU AI Act.
- Documenting compliance procedures and strategies appropriate for company size and operations.
- Reviewing the repository every 6 months and when additional requirements may be triggered. For example, regulations change or business operations expand into new jurisdictions.
- **Category:** Legal Policies
- **Typical location:** Internal processes
- **Typical evidence:** Compliance register, assessment memo or review tickets (e.g. in Notion), or policy listing applicable regulations with compliance strategies - should include review dates or version history showing periodic updates.
- **Priority guidance:** Prioritize validating control status: Legal review may be required to pass AIUC-1


## E013: Implement quality management system
*Optional | Capabilities: Universal*

### E013.1 Documentation: Quality objectives and risk management
- **Application:** Core - This should include:
- **Control:** - Defining quality objectives, metrics, and risk management approach for AI systems. For example, establishing performance targets, safety thresholds, risk assessment methodologies, and measurement processes appropriate to system risk level.
- **Category:** Operational Practices
- **Typical location:** Internal policies
- **Typical evidence:** Documentation showing quality objectives, metrics, and risk management approach - may include quality metrics dashboard or reports, risk assessment documentation for AI systems, performance targets and safety thresholds, or measurement methodologies defining how quality is evaluated.

### E013.2 Documentation: Change management procedures
- **Application:** Core - This should include:
- **Control:** - Establishing change management, approval processes, and documentation standards. For example, defining review and approval requirements for AI system changes, assigning accountability for quality decisions, documenting design and development procedures.
- **Category:** Operational Practices
- **Typical location:** Internal policies
- **Typical evidence:** Documentation showing change management and approval processes - may include change approval workflows or procedures, RACI matrix assigning accountability for quality decisions, design and development procedure documents, or documentation standards and templates for AI systems. May be fulfilled by evidence submitted to E004: Assign accountability.

### E013.3 Config: Issue tracking and monitoring
- **Application:** Core - This should include:
- **Control:** - Implementing defect tracking, continuous improvement, and post-market monitoring. For example, maintaining issue tracking systems, conducting root cause analysis, documenting corrective actions, establishing post-market monitoring processes.
- **Category:** Technical Implementation
- **Typical location:** Engineering Tooling
- **Typical evidence:** Screenshot of issue tracking system or monitoring records - may include issue tracker (Jira, Linear, GitHub) with defects and corrective actions, root cause analysis reports, post-market monitoring logs or dashboards, or continuous improvement documentation showing lessons learned.

### E013.4 Documentation: Data management procedures
- **Application:** Supplemental - This may include:
- **Control:** - Establishing data management and record-keeping systems. For example, documenting data governance procedures, maintaining technical documentation, implementing record retention policies for model training data and system outputs.
- **Category:** Operational Practices
- **Typical location:** Internal policies
- **Typical evidence:** Documentation showing data management and record-keeping practices - may include data governance policies, technical documentation standards, record retention procedures, or data lineage tracking systems for training data and system outputs.

### E013.5 Documentation: Stakeholder communication procedures
- **Application:** Supplemental - This may include:
- **Control:** - Documenting communication procedures with regulatory authorities and stakeholders. For example, establishing protocols for regulatory reporting, stakeholder notifications for incidents, and procedures for authority interactions.
- **Category:** Operational Practices
- **Typical location:** Internal processes
- **Typical evidence:** Procedures document or communication protocols - may include incident reporting templates or protocols to regulatory authorities, stakeholder notification procedures for serious incidents, guidelines for interacting with competent authorities or notified bodies, or escalation procedures for regulatory communications.


## E014: Share transparency reports
*Optional | Capabilities: Universal*

### E014.1 Not applicable
- **Application:** Supplemental - This may include:
- **Control:** This requirement was merged into E017 at the Q1, 2026 standard update. See aiuc-1.com/changelog for more information
- **Category:** 
- **Typical evidence:** Not applicable


## E015: Log model activity
*Mandatory | Capabilities: Universal*

### E015.1 Config: Logging implementation
- **Application:** Core - This should include:
- **Control:** - Capturing system activity details to support incident investigation and behavior explanation. For example, logging inputs, processing steps, outputs, and metadata for AI systems.
- **Category:** Technical Implementation
- **Typical location:** Logs
- **Typical evidence:** Screenshot of logging code or configuration showing what system activity is captured - may include code logging inputs and outputs, logging configuration file specifying what to log, or example log entries showing captured information (timestamps, inputs, outputs, user actions).

### E015.2 Config: Log storage
- **Application:** Core - This should include:
- **Control:** - Implementing log storage with appropriate retention periods, access controls, and data sanitation to support auditing and incident response.
- **Category:** Technical Implementation
- **Typical location:** Logs, Engineering Tooling
- **Typical evidence:** Screenshot of log storage system showing retention policies, access controls and sanitation practices - may include log management platform (Datadog, Splunk, CloudWatch) with retention period settings and PII-masking, access control configuration showing who can view logs, or storage settings with automatic deletion rules.

### E015.3 Config: Log integrity protection
- **Application:** Supplemental - This may include:
- **Control:** - Implementing technical controls to ensure logs are tamper-evident and independently verifiable. For example, ensuring that captured records cannot be modified or deleted after creation, ensuring sequence integrity so that gaps, omissions, and reordering are detectable during incident investigation or audit.
- **Category:** Technical Implementation
- **Typical location:** Logs, Engineering Code
- **Typical evidence:** Screenshot or documentation of log immutability controls - for example, write-once-read-many (WORM) storage configuration, cryptographic hashing of log entries, append-only database settings, or third-party log management platform features.


## E016: Implement AI disclosure mechanisms
*Mandatory | Capabilities: Universal*

### E016.1 Demonstration: Text AI disclosure
- **Application:** Core - This should include:
- **Control:** - Implementing AI disclosure for text-based interactions. For example, displaying clear notices when users interact with AI chatbots, virtual assistants, or automated messaging systems.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot of text-based AI disclosure - may include chatbot interface with "You're chatting with AI" notice, messaging system showing AI agent identifier, website chat widget with AI disclosure banner, or automated email/SMS with AI generation notice.

### E016.2 Demonstration: Voice AI disclosure
- **Application:** Core - This should include:
- **Control:** - Implementing AI disclosure for voice-based interactions. For example, providing audio notifications at the beginning of voice calls or interactions.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot of transcript or audio recording of voice AI disclosure.

### E016.3 Demonstration: Labelling AI-generated content
- **Application:** Core - This should include:
- **Control:** - Labelling AI-generated media and documents in a machine-readable and detectable format. For example, marking AI-generated images, videos, audio, or documents with metadata, watermarks, or labels indicating artificial generation.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot showing AI generation labeling implementation - may include Content Credentials or C2PA metadata embedded in files, visible watermarking system with AI generation marks, classifier output detecting and flagging AI-generated content, or metadata tagging system marking files as artificially generated.

### E016.4 Demonstration: Automation AI disclosure
- **Application:** Core - This should include:
- **Control:** - Disclosing when autonomous AI agents or automated workflows are performing actions. For example, notifying users when AI systems are making decisions, processing requests, or executing tasks without human oversight.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot showing AI automation disclosure in product - may include "Powered by AI" or "AI Agent" labels in interface, workflow dashboard displaying AI-automated tasks, status indicators showing "AI is handling this" or "Automated by AI," or notification messages stating "AI agent completed your request."

### E016.5 Demonstration: System response to AI inquiry
- **Application:** Core - This should include:
- **Control:** - Establishing reactive disclosure capabilities when users ask if they are interacting with AI.
- **Category:** Technical Implementation
- **Typical location:** Product
- **Typical evidence:** Screenshot of chatbot or voice agent transcript responding to "Are you AI?"


## E017: Document system transparency policy
*Optional | Capabilities: Universal*

### E017.1 Documentation: Transparency policy
- **Application:** Core - This should include:
- **Control:** - Establishing a transparency policy defining documentation requirements for major AI systems. For example, specifying required documentation elements, establishing documentation standards.
- **Category:** Legal Policies
- **Typical location:** Internal policies
- **Typical evidence:** Policy document defining transparency documentation requirements - may include criteria for systems requiring documentation, required documentation elements (capabilities, limitations, use cases, risks), or documentation standards and templates.

### E017.2 Documentation: Model cards and system documentation
- **Application:** Core - This should include:
- **Control:** - Creating transparency documentation for major AI systems. For example, documenting system characteristics, data provenance, and model behavior for systems meeting documentation criteria.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Transparency documentation artifacts - may include model card (PDF, Markdown, web page) with system capabilities/limitations/intended use, datasheet showing training data sources and characteristics, interpretability report with example inputs/outputs and decision explanations, technical documentation describing model architecture and performance metrics, or an AI Bill of Materials (may follow CycloneDX or SPDX 3.0)

### E017.3 Documentation: Transparency report sharing policy
- **Application:** Supplemental - This may include:
- **Control:** - Defining policies for sharing transparency documentation with external stakeholders. For example, establishing when reports are shared, specifying recipient categories, determining what information is disclosed to each stakeholder type.
- Documenting sharing procedures including approval workflows, version control, and distribution tracking. For example, establishing approval requirements before external sharing, maintaining version control of shared documents, tracking which stakeholders received which versions.
- **Category:** Operational Practices
- **Typical location:** Internal processes, Internal policies
- **Typical evidence:** Policy document defining transparency sharing practices - may include sharing triggers, recipient categories with disclosure levels (regulators, customers, affected parties, public), or matrix mapping stakeholder types to shared documentation (model cards, datasheets, performance reports, incident summaries).


## F001: Prevent AI cyber misuse
*Mandatory | Capabilities: Text-generation, Automation, Voice-generation*

### F001.1 Documentation: Foundation model cyber capabilities
- **Application:** Core - This should include:
- **Control:** - Results of testing from foundation model developer on offensive cyber capabilities and mitigations.
- **Category:** Legal Policies
- **Typical location:** Vendor Contracts
- **Typical evidence:** Provider model cards, cybersecurity assessment reports from model developers, or foundation model documentation describing offensive cyber capabilities and mitigations

### F001.2 Config: Cyber use detection
- **Application:** Supplemental - This may include:
- **Control:** - Implementing malicious use detection and blocking. For example, deploying available content filtering to detect requests for malicious code generation, attack planning, and vulnerability exploitation guidance, configuring automated blocking of cyber attack assistance requests, maintaining databases of prohibited use patterns.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Content filtering rules blocking cyber attack requests, keyword or pattern matching detecting malicious code generation attempts, automated blocking configuration for exploit development queries, or prohibited use pattern database.


## F002: Prevent catastrophic misuse
*Mandatory | Capabilities: Text-generation, Voice-generation, Image-generation*

### F002.1 Documentation: Foundation model CBRN capabilities
- **Application:** Core - This should include:
- **Control:** - Results of testing from foundation model developer on CBRN capabilities and mitigations.
- **Category:** Legal Policies
- **Typical location:** Vendor Contracts
- **Typical evidence:** List of foundation models used with CBRN capability information - may include provider model cards with CBRN assessments, weapons of mass destruction risk evaluations from model developers, or other documentation describing CBRN-related capabilities and mitigations.

### F002.2 Config: Catastrophic misuse monitoring
- **Application:** Supplemental - This may include:
- **Control:** - Establishing catastrophic misuse monitoring. For example, monitoring AI system interactions for patterns indicating weapons development or mass harm intent, implementing real-time alerting for detected catastrophic misuse attempts, documenting suspicious queries and system responses.
- **Category:** Technical Implementation
- **Typical location:** Engineering Code
- **Typical evidence:** Monitoring dashboard or alert configuration for catastrophic misuse patterns - may include usage monitoring flagging CBRN-related queries, alert rules for weapons development patterns, logs of detected and blocked catastrophic misuse attempts, or incident records documenting suspicious CBRN-related interactions.

# Domain Descriptions

## A. Data & Privacy
Protect against data leakage, IP leakage, and training on user data without consent

## B. Security
Protect against adversarial attacks like jailbreaks and prompt injections as well as unauthorized tool calls

## C. Safety
Prevent harmful AI outputs and brand risk through testing, monitoring and safeguards

## D. Reliability
Prevent hallucinations and unreliable tool calls to business systems

## E. Accountability
Assign accountability, enforce oversight, create emergency responses and vet suppliers

## F. Society
Prevent AI from enabling societal harm through cyberattacks or national security risks

# Framework Crosswalks

AIUC-1 is designed to be:

**Customer-focused.** We prioritize requirements that enterprise customers demand and vendors can pragmatically meet— increasing confidence without adding unnecessary compliance.

**Adaptable.** We update AIUC-1 as regulation, AI progress, and real-world deployment experience evolves.

**Transparent.** We keep a public changelog and share our lessons.

**Forward-looking.** We require AI vendors to conduct testing and review systems at least quarterly to ensure that an AIUC-1 certificate stays relevant.

**Insurance-enabling.** We emphasize the risks that lead to direct harms and financial losses.

**Predictable.** We review the standard in partnership with our technical contributors and push updates on January 15, April 15, July 15, and October 15 of each year.

In practice, this means that **AIUC-1 builds on other AI frameworks** including the [EU AI Act](/crosswalks/eu-ai-act), the [NIST AI RMF](/crosswalks/nist-ai-rmf), [ISO 42001](/crosswalks/iso-42001), [MITRE ATLAS](/crosswalks/mitre-atlas), and [OWASP AIVSS](/crosswalks/owasp-aivss). The regular update cadence will mean AIUC-1 updates also reflect changes to these frameworks.

**AIUC-1 does not duplicate the work of non-AI frameworks like SOC 2, ISO 27001, or GDPR.** Companies should ensure compliance with these frameworks as needed independently of AIUC-1.

AIUC-1 is already being adopted by multiple AI vendors to address enterprise concerns. It has been developed with technical contributors from MITRE, Cisco, MIT, Stanford, Google Cloud, Orrick, and more.

AICPA SOC 2

EU GDPR

Canada Artificial Intelligence and Data Act (AIDA)

ISO 27001

More detail on how each of these frameworks is addressed by AIUC-1 is available in the "crosswalk" section of each requirement.

### AIUC-1 operationalizes emerging AI legislation and best practices

Framework

Description

How AIUC-1 compares

Framework

EU AI Act

Description

EU regulation classifying AI systems by risk levels (minimal, limited, high, unacceptable) with corresponding compliance obligations

How AIUC-1 compares

Operationalizes the EU AI Act by aligning with its requirements. Certification against AIUC-1 is a strong step towards compliance with the EU AI Act as it:

Enables compliance for _minimal_ and _limited_ risk systems

Enables compliance for _high risk_ systems only if specific control activities are met (AIUC can help guide AI companies through this process)

Provides documentation for internal conformity assessments for _high risk_ systems as required in _Annex VI_

Framework

NIST AI RMF

Description

US government framework for managing AI risks throughout the AI lifecycle with four core functions: Govern, Map, Measure, Manage

How AIUC-1 compares

Operationalizes the NIST AI RMF. Certification against AIUC-1:

Translates NIST's high-level actions into specific, auditable controls

Provides concrete implementation guidance for key areas such as harmful output prevention, third-party testing and risk management practices

Framework

ISO 42001

Description

International standard for AI management systems (AIMS) covering responsible AI development and deployment

How AIUC-1 compares

Aligns with ISO 42001. Certification against AIUC-1:

Incorporates the majority of controls from ISO 42001

Translates ISO's management system approach into concrete, auditable requirements

Extends ISO 42001 with third-party testing requirements of, e.g., hallucinations and jailbreak attempts

Addresses additional key concerns such as AI failure plans and AI-specific system security

Framework

MITRE ATLAS

Description

Knowledge base of adversarial tactics, techniques and mitigation strategies for machine learning systems, similar to MITRE ATT&CK for cybersecurity

How AIUC-1 compares

Integrates MITRE ATLAS, which is a technical contributor to AIUC-1. Certification against AIUC-1:

Incorporates ATLAS mitigation strategies in requirements and controls

Strengthens robustness against the adversarial tactics and techniques identified in ATLAS

Goes beyond ATLAS's focus on security alone

Framework

OWASP Top 10 for LLM Applications

Description

Curated list of the most critical security threats to LLM and generative AI systems

How AIUC-1 compares

Integrates OWASP's Top 10 for LLM Applications. Certification against AIUC-1:

Addresses Top 10 threats in requirements and controls

Strengthens robustness against the threats identified with concrete requirements and controls

Goes beyond OWASP's focus on security alone

Framework

OWASP AIVSS

Description

Scoring system for quantifying how agentic capabilities amplify security risks, producing numerical scores (0-10) that combine technical vulnerability severity with agent-specific factors

How AIUC-1 compares

Integrates the OWASP AIVSS, which is a technical contributor to AIUC-1. Certification against AIUC-1:

Covers all agent risks identified in AIVSS

Enables organizations to mitigate risks quantified in OWASP AIVSS

Incorporates AIVSS agent risk amplification factors in standard requirements

Framework

CSA AI Controls Matrix

Description

Cloud Security Alliance's AI Controls Matrix providing security controls framework specifically designed for AI/ML systems

How AIUC-1 compares

Certification against AIUC-1:

Addresses key controls for AI vendors from the AICM such as adversarial robustness, system transparency, and documentation of criteria for cloud & on-prem processing

Enables a compliance burden significantly lower than CSA's AICM due to its targeted focus on top AI enterprise concerns

Avoids duplicating controls in areas where CSA is industry-leading, such as data center infrastructure, physical server security, and other domains outside of the AIUC-1 scope

Framework

Regional US regulation

Description

e.g. California SB 1001, New York City Local Law 144, Colorado AI Act

How AIUC-1 compares

Simplifies compliance with regional regulation. AIUC can help guide AI companies through the process of meeting California SB 1001, the Colorado AI Act, and New York City Local Law 144 through optional requirements.

AIUC-1 already addresses top concerns in emerging regional regulations such as discrimination and bias, human-in-the-loop, and data handling.

Framework

Description

e.g. HIPAA, Fair Credit Reporting Act, Fair Housing Act, FTC guidance on AI & algorithms

How AIUC-1 compares

Simplifies compliance with AI requirements in sector-specific regulation. Certification against AIUC-1:

Prepares organizations to comply with, e.g., FTC guidance on AI & algorithms

Addresses top concerns in sector-specific regulations such as discrimination and bias, human-in-the-loop, monitoring and logging, third-party interactions, and data handling in base requirements

Offers AI companies optional add-on requirements for relevant use cases (e.g., for financial transactions, PII handling)

Framework

Description

First inter-governmental AI standard (2019, updated 2024) with five principles for trustworthy AI adopted by 47+ countries

How AIUC-1 compares

Operationalizes OECD's AI Principles. Certification against AIUC-1:

Translates OECD's five principles into concrete, auditable requirements

Addresses additional key areas such as third-party testing, AI failure plans, and adversarial resilience

### Frameworks outside the scope of AIUC-1

Framework

Description

How AIUC-1 compares

Framework

AICPA SOC 2

Description

Leading cybersecurity standard

How AIUC-1 compares

Certification against AIUC-1:

Extends SOC 2 Security controls specifically for AI systems (e.g., jailbreak attempts)

Extends SOC 2 Privacy controls specifically for AI systems (e.g., data used for model training)

Extends SOC 2 Availability controls specifically for AI systems (e.g., system reliability/hallucinations)

Avoids duplication of existing requirements in SOC 2 on general cyber security best practices

Framework

Additional ISO standards including ISO 27001 and ISO 42006

Description

International standards for, e.g., information security management systems (ISMS)

How AIUC-1 compares

Certification against AIUC-1:

Focuses on ISO 42001, which is specific to AI systems

Extends several ISO 27001 controls into the AI domain including the Confidentiality-Integrity-Availability triad

 _AIUC is following the newly-introduced ISO 42006 standard closely._

Framework

EU GDPR

Description

European data protection regulation with AI-relevant provisions on automated decision-making, profiling, and data subject rights

How AIUC-1 compares

 GDPR.

Framework

Canada Artificial Intelligence and Data Act (AIDA)

Description

Canada's proposed Artificial Intelligence and Data Act regulating AI systems based on impact assessments and risk mitigation

How AIUC-1 compares

AIDA has not been passed into law yet.

AIUC can help with guidance on how to meet AIDA once passed having incorporated similar principles of risk mitigation, risk assessment, transparency, and incident notification.

AIUC-1 is continuously updated as new legislation, frameworks, threat patterns and best practices emerge — in collaboration with our network of technical contributors and experts from leading institutions within AI safety, security and reliability. This ensures that the standard stays current, comprehensive and enables easy compliance with applicable frameworks.

Last updated March 2, 2026.

# Diff: 2025-Q1 → 2026-Q1

Unchanged: index, data-and-privacy, security, safety, reliability, accountability, society, crosswalks

