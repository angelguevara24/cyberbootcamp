## Day 1 Lesson Plan: Introduction to Incident Response

### Overview

Today's class provides an overview of Incident Response and its role in the security sector. We'll cover incident response planning, plan review, and Security Operation Centers planning.

### Class Objectives

By the end of class today, you will be able to:

- Define Incident Response and its purpose as it relates to Cyber Security.

- Articulate typical Incident Response goals.

- Define the purpose of a security operations center (SOC).

- Determine whether or not to outsource an SOC depending on the specific needs of a given company.

### Student Notes

* This unit covers security operations centers and incident response. By the end of this week, you will be able to explain the goals of security monitoring and security incident response in a company, understand and perform the roles of an SOC analyst, and investigate and document a network-based, application-based and email-based attack.

* Today's lesson is divided into sections of lecture and research. During activities, you will look up security topics and tools related to IR.

* Today's class provides an in-depth look into the career possibilities of the subject material. Encourage you who are interested in Incident Response to pay particular attention.


### Slideshow

- Slides for this lesson are available on Google Drive here: [Incident Response Day 1 Slides](https://docs.google.com/presentation/d/161PmW8-MGERmd0lyXo-AeqmJdEaBZkB0nW3ZL3Uw0HI/edit#slide=id.g5249e5d897_0_0).

- To add slides to the student-facing repository, download the slides as a PDF by navigating to File > "Download as" and choose "PDF document." Then, add the PDF file to your class repository along with other necessary files.

- **Note:** Editing access is not available for this document. If you or your you wish to modify the slides, please create a copy by navigating to File > "Make a copy...".


---

### Introduction to Incident Response

Today's class will begin with an introduction to incident response, and an overview of incident response plans and security operations centers (SOCs).

- Remember that there are various threats that can negatively affect a company, such as Malware, DDoS / Botnet attacks, phishing and data breaches. 

    - Therefore, companies put in place certain security systems to prevent these incidents, like System Firewalls, Intrusion Prevention Systems, Network Security Firewalls, and Application Security.

-  **Incident Response** deals with situations where those security systems **fail** and a company is negatively affected by incidents like malware, DDoS attacks, phishing, data breaches. Specifically:

    - Incident Response is a procedure that an organization uses to react to and mitigate a security problem.

    - There are always threats that can compromise an organization's system, therefore incident response is an essential element of an organization's security system. 

    - For example: If a company is a bank, the security systems are analogous to the bank’s alarm and security  guards. We can consider the threats to be bank robbers, and the incident response is analogous to the police responding _after_ the alarm went off and the robbers broke in.

    - Incident response isn't about blocking negative actors; it's about finding them and getting them out.

- Incident Response is a broad term. When we refer to it, we are talking about to the comprehensive actions that an organization takes when a security incident occurs. 

- In order to get a stronger idea of the topic, we will look at two key factors of this response: **planning for a response** and **maintaining an incident response team.** First, we'll look at the incident response teams.

#### Security Operations Center (SOC)

- Let's take a closer look atsecurity operations center by covering the following:

    - Incident response team members are responsible for setting up and implementing the IR Plan. You can think of this team as the first responders to security incidents.

    - They work out of a **Security Operation Center**, often referred to as simply an *SOC*. 

    - Ideally, these teams are working 24/7 to provide the best possible coverage for their organizations, but ultimately it is a decision made on a company to company basis. 

    - The extent of an SOCs operating hours is just one of many high-level business decisions that is covered in an incident response plan.  

#### SOC Team Tier Structure  

SOC analysts are often organized in a chain of command that is divided into three tiers. Also included in the SOC framework may be: SOC Management and Incident Handlers.

- **Tier 1** Analysts (aka 'Junior Analysts') are the first responders and the first line of defense. 
    - A Tier 1 analyst will often be in charge of monitoring alerts and verifying that they are not false positives. 
    - They follow pre-planed procedures, perform an initial investigation, solve simple incidents and escalate as needed.

- **Tier 2** analysts are the first escalation point for the Tier 1 Analysts. 
    - In other words, they help get past any blockers that the Tier 1 analyst may have. 
    - Tier 2 analysts can perform the duties of Tier 1 as needed but can also divert from written procedures. 
    - They will also support Tier 3 as needed, create documentation and procedures for Tier 1 and monitor Tier 1 performance.

- **Tier 3** analysts are the second 'escalation' point and may serve more of a forensics or deep investigative role. 
    - Tier 3 Analysts often own the tools used by the IR team, oversee complex incidents and mentor and monitor the performance of all other tiers.

- **SOC Manager** can perform all of the duties of a Tier 3 Analyst, but they also manage the team and have Human Resource responsibility for growing and maintaining the team.

- **Incident Handlers** function as a project manager for complex incidents ensuring that technical investigators have all the resources they need to complete an investigation. They also ensure that process steps are being followed and present info to less technical audiences as needed.

- Inform you that Tier 1 is an entry-level role and a starting point for most you that would choose this career path.

#### Security Monitoring Vs. Incident Response

Next, let's talk about the "philosophical" debate prevalent in the industry regarding Security Monitoring vs. Incident Response:

- There seems to be a 50/50 split between companies regarding the specific delineations of duties for security monitoring and incident response.

- Some companies have an entirely separate team that provides monitoring. 
    - When they see a problem, they escalate to another team who will then respond to that problem.

- Other companies have just one team that provides both the monitoring and responding since the skill sets for both responding and monitoring are very similar. 
    - The Monitoring Team (SOC) watches activity occur over the wire while the Response Team investigates and mitigates suspicious activity.

-  But regardless of whether it is one or multiple teams, SOCs only monitor the systems that provide alerts, such as SIEMs. Setting up and maintaining those systems is usually done by a different team, often the Security Engineering team.

#### Incident Response and SOC Professional Context

Next, we will cover the professional context of where IR and SOC fits into a security career path.

- First, let's talk about why incident response is a very prevalent and important career path:

    - Incident Response and the SOC eat up a big percentage of an organization's security budget.

    - IR is a great stepping stone or entry-level role into the cybersecurity field.

    - When you start in IR, it's typically easy to pivot into a more specialized security roles down the line.

- Below, are some of the entry-level Cyber Security Titles:

   - Security Analyst, SOC Analyst, Cyber Threat Analyst, Cyber Defense Analyst, Incident Response Analyst, Intelligence Analyst, etc.

#### Incident Response Plans

You will learn most about Incident Response planning through the exercises in today's class, but let's cover some basic definitions to get started:

  - **Incident Response Plan**: A formal, high level document detailing how the organization will respond to incidents.

  - **Response Process**: A more general document, not as formal as an IR plan.

  - **Response Procedure**: a step-by-step workflow for a given part a response. Steps often are organized in a flowchart. 
    - This is the document that a junior analyst would follow explicitly when responding to a given incident. A senior analyst would be familiar with the expected procedure and be able to go beyond it.

  - **Response Playbook**: A playbook is a collection of procedures for a given type of incident. It may be split up into various procedures under different aspects of a response; Detect & analyze, Eradicate and Recover, Post-Incidnet Procedure, etc.

  - **Post-Incident Report**: A document designed to provide an overview of what the analyst found and what they did in response to a particular incident. For every incident that warrants a response, a report is expected to be produced by the analyst.

  - **Tabletop exercise**: A common exercise where a security team is given a incident scenario and they discuss, in-detail, the steps they would take to respond to the incident.

#### Simple and Complex Incidents

- Emphasize that an incident responder may not be an expert on every possible incident. It is very common to call in specific expertise to assist in the response effort. 

  - For example, they may rely on an application developer to help analyze application logs before they tie in the results to the bigger picture of the incident.

- Explain that incidents vary in complexity: 
 
  - Simple incidents are usually opportunistic attacks that can be solved by junior analysts following specific steps. Examples include phishing attacks or malware downloads.

  - Complex incidents are either more widespread or more sophisticated. They require a more coordinated effort and have a higher severity. These may involve multiple IR team members and/or multiple IT teams. Examples include attacks that affects multiple employees and/or servers.

- Remember the very first step of Incident Response, regardless of complexity, is putting a plan of action in place. Before any response occurs, and in order for a team to effectively resolve an issue, there needs to be a plan. Every company should have a plan that documents exactly when to respond, what to do, how to do it, and who is in charge of doing what.

#### Incident Response Examples

- Let's look at the following example questions regarding production web server incidents that should be asked with a competent IR plan:

    - Do you immediately take it offline and just send a notification?

    - Who makes the decision to shut it down?

    - Do you need management approval to shut systems down?

    - Who needs to be notified?

    - Will it affect company revenue or customer experience?

    - At what point do you involve the Public Relations department?

    - At what point do you involve the legal team?

    - Who communicates the issue with the executive team?

- Security teams should have regular, scheduled exercises to test response plan efficiency on non-production systems. Organizations should also have regular tabletop exercises throughout the year. With each incident and exercise, the response should be evaluated and documented.

- The ability to effectively execute a plan and make these decisions can be critical to a company's bottom line:

    - Take a look at the following examples of UnderArmour Vs. Uber breaches. 

    - [UnderArmour](https://www.wired.com/story/under-armour-myfitnesspal-hack-password-hashing/) reported a breach in under a week, letting all of their affected users know and mitigating any further damage to their reputation.
    - [Uber](https://www.reuters.com/article/us-uber-databreach-idUSKCN1M62AJ) on the other hand had to pay 148 million dollars because they tried to cover up a breach.

- Another great example is the [Equifax Breach](https://www.cnbc.com/2019/03/07/equifax-marriott-ceos-testify-in-senate-over-data-breaches.html) which may very well have affected you in the class and resulted in senior Equifax executives to be brought in front of Congress.


### The NIST Guide for Incident Response

Let's take a closer look at Incident Response plans.

- If you had to write an incident response plan for their company, it would be fairly convenient if there were some kind of standard framework that organization could follow.

#### [NIST Guide for Computer Security Incident Handling](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r2.pdf)

- The NIST Guide is **the** industry standard for Incident Response and has very detailed plan and process descriptions for everything involved with an incident.

- Companies can also use the NIST standard as a framework for building out their own plans, only incorporating the items that make sense for them.

- An Incident Response plan must be continually executed, assessed, and updated to keep up with current threats. An IR plan that worked well 6 months ago may not be equipped for today's rapidly changing threats. 

### SOC Team Metrics

Next we'll cover how an SOC Team can be monitored in order to track performances.

- Performance monitoring is essential for judge how a team is performing and knowing when to make any policy adjustments. Let's look at the following:

    - Organizations call this measurements metrics and **Key Performance Indicators (KPIs)**

    - Metrics can assess the efficiency the whole IR team, each particular tier, or even each specific team member

    - The more metrics that an IR team keeps track of, the more they can drive improvement. 

- Provide some common SOC team metrics:

   - Mean time to respond to an incident (MTTR)

   - Time from detection to resolution by analyst

   - Time from detection to resolution by shift

   - Percentage of incidents escalated to Tier 2 analysts

   - Percentage of incidents escalated to Tier 3 or forensics analysts

   - Percentage of false positives by system

   - Percentage of reoccurring incidents by system

   - Number of incidents handled by week/month/year

#### Security Operations Center Outsourcing

Considering what we know about creating and maintaining a SOC, ask the you: _Do you think outsourcing an SOC to a third party company is a valid security plan?_

Let's look at three outsourcing security options:

- No Outsourcing: Everything done in-house

    - In-house SOC teams are common for companies that have very complex monitoring and IR needs.

- Some Outsourcing: What is outsourced varies

    - The most common scenario is that monitoring is outsourced by a Managed Security Service Provider (MSSP).

    - Another common scenario is that you outsource only complex incidents.

- All Outsourcing: Everything is outsourced to third parties
    - This is common for companies that prioritize security spending at the expense of robust monitoring, IR and SOC facilities.

-------

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
