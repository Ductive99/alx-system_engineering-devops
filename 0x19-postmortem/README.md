# Deployement Failure: Service Disruption (Fiction)

The following is the incident report for the D.U.C. application outage that occured on March 9, 2024. We would like to to apologize to absolutely nobody.

![Conor McGregor - "I want to take this chance to apologize..."](./resources/conor.gif)

## Issue Summary:

Following a recent deployeent of updates to our applicatio, a critical failure occured resulting in widespread service disruption. Users experienced a high rate of 500 errors, with the system reaching peak failure rate of 100%. The incident started at 12:27 AM (UTC) and lasted for approximately 2 hours untile 2:34 PM (UTC).

## Timeline (in UTC)

- 12:19 PM: Deployement push begins
- 12:27 PM: Outage begins
- 01:20 PM: Teams noticed the alerts
- 01:49 PM: Deployement change rollback
- 02:04 PM: Server restarts begin
- 02:34 PM: 100% of traffic back online

## Impact:

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Moroccan_cuscus%2C_from_Casablanca%2C_September_2018.jpg" alt="Moroccan Couscous" width="200" align="left">

During the outage, most user requests resulted in 500 errors, causing frustration and dissatisfaction among our user base. The inability to access key features of the application led to a decline in user engagement and potential loss of revenue, which is currently being evaluated by the financial team. In addition, many developers missed their lunch break which is a Couscous meal on Friday. This could also explain, why it took the team so long (~1hour) to notice the outage, as they were ready to feast.

## Root cause:

The root cause of the deployment failure was identified as a misconfiguration in the new code release. Specifically, a configuration file containing critical environment variables was mistakenly omitted from the deployment package. As a result, the application failed to establish essential connections to backend services, leading to widespread errors and downtime. Measures have been implemented to enhance the deployment process, including improved testing protocols and comprehensive checklist reviews to prevent similar incidents in the future.

## Resolution and Recovery:

After identifiying the misconfiguration, the development and operations teams immediately intiated a rollback procedure to revers the application to tis previous stable state. The rollback process was completed within 30 minutes of detecting the issue, restoring functionality to the application and resolving the service diruption.

## Corrective and Prevantative Measures:

1. Improved Deployement Checklist: Implement a checklist for all deployment procedures to ensure that critical configuration files are included in the deployment package.

2. Automated Testing: Improve testing processes to check for essential dependencies.

3. Documentation Review: Improve documentation to ensure that all necessary configuration files and environment variables are clearly documented.

Moving forward, we aim to strengthen our deployement processes by implementing all the measures mentioned above.

Sincerely,

The D.U.C. Infrastructure Team
