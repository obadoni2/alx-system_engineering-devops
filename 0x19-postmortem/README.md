Postmortem
            
               Man-in-the-Middle (MitM) Attack
                                                       




T
                                             



          Man-in-the-Middle (MitM) Attack Incident


On August 20th, 2024, from 11:00 AM to 2:30 PM (UTC), our services experienced a security breach caused by a sophisticated Man-in-the-Middle (MitM) attack. This attack compromised user traffic between our web application and several clients, intercepting sensitive information such as login credentials and session tokens. Roughly 40% of our users were affected, resulting in unauthorized access to some accounts. The root cause was the improper implementation of SSL certificate validation, which allowed the attacker to intercept encrypted traffic undetected.

### Timeline

- **11:00 AM (UTC)** - The first sign of the issue was a customer complaint regarding suspicious activity on their account. 
- **11:10 AM** - The security team was notified and began investigating the source of the breach, suspecting a credential leak from a third-party app.
- **11:30 AM** - After checking internal systems and logs, an abnormal spike in failed login attempts was detected, suggesting that unauthorized parties were trying to access user accounts.
- **12:00 PM** - Network logs were analyzed, revealing inconsistencies in encrypted traffic patterns between users and our servers, leading to the suspicion of an ongoing MitM attack.
- **12:15 PM** - The issue was escalated to the network security team, and they began inspecting the SSL/TLS certificates being used for user sessions.
- **12:30 PM** - The team discovered that, due to a misconfiguration, some users were connecting without proper certificate validation, allowing attackers to intercept traffic.
- **1:00 PM** - As a temporary measure, the affected systems were taken offline to prevent further data leakage.
- **1:30 PM** - The root cause was pinpointed, and engineers began reconfiguring SSL certificates and enforcing strict validation protocols.
- **2:15 PM** - After testing the new configuration and confirming the issue was resolved, services were brought back online.
- **2:30 PM** - The attack was fully mitigated, and users were informed of the breach, with a password reset recommended for all affected accounts.

### Root Cause and Resolution
The root cause of the MitM attack was a misconfiguration in our SSL/TLS setup. During a recent update, certificate validation checks were inadvertently relaxed, allowing malicious actors to intercept traffic between our web servers and users. This gap in encryption integrity enabled attackers to position themselves between users and our servers, decrypting sensitive information and exploiting it to access user accounts.

The resolution involved reconfiguring SSL/TLS settings across all affected systems, ensuring that certificate validation was strictly enforced. This included updating expired certificates, applying stronger encryption standards, and conducting rigorous testing to ensure the issue would not reoccur. Additionally, all potentially compromised users were required to reset their passwords.

### Corrective and Preventative Measures
In response to this incident, several measures have been put in place to prevent similar attacks in the future:

1. **Strengthening SSL/TLS Configuration:** A thorough review of all SSL/TLS configurations has been completed to ensure proper certificate validation, with enhanced security measures such as OCSP stapling and HSTS (HTTP Strict Transport Security) enabled.
2. **Regular Certificate Audits:** Implement routine certificate audits to ensure all SSL/TLS certificates are up-to-date, valid, and properly configured.
3. **Monitoring for Anomalous Traffic Patterns:** Upgrade network monitoring tools to detect abnormal traffic patterns and flag potential MitM attacks before they cause damage.
4. **Developer Training:** Conduct internal training sessions on secure communication protocols, emphasizing the importance of SSL/TLS best practices.

**TODO List:**
- Update SSL/TLS configurations to enforce strict validation on all systems.
- Automate alerts for expired or improperly configured certificates.
- Implement traffic anomaly detection tools that highlight potential MitM attack vectors.
- Develop guidelines for regular security audits of network and SSL/TLS settings.
- Roll out a user communication plan for swift password changes and enhanced security after an incident.

Through these preventative measures, we aim to bolster the security of our communication channels and prevent future breaches that could arise from MitM attacks. By tightening our encryption protocols, we will significantly reduce the risk of user data being intercepted and ensure a safer experience for all users.
