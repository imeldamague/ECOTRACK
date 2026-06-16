# ECOTRACK - Bloc 2 EASRSI

**Concevoir et Developper des Solutions Securite**
**Master 1 EASRSI - INGETIS Paris 2026**
**Soutenance : 29 & 30 juin 2026**

## Equipe

- **Imelda** - Chef de projet / RSSI - ECO-MON - ECO-SEC - ECO-MQTT
- **Marie Claude** - Architecte reseau - ECO-PROXY - ECO-DB
- **Ephra** - Firewall & Dev - pfSense - ECO-APP - ECO-WEB

## Rapport Bloc 2

- [Telecharger le rapport Bloc 2](https://github.com/user-attachments/files/29013243/ECOTRACK_Bloc2_groupe.2-imelda-marieclaude.pdf)

  Diagramme STRIDE
  <img width="1677" height="1227" alt="ECOTRACK_STRIDE_Diagram drawio" src="https://github.com/user-attachments/assets/02e96fe8-1684-458d-aef1-516f3ea16a8a" />

## Architecture securite - 5 couches
<img width="1499" height="1049" alt="reseau" src="https://github.com/user-attachments/assets/cf4de50b-c3e5-48b3-a7f0-33be7054a6f4" />

## Stack securite

- Firewall : pfSense 2.8.1 - 31 regles - DENY ALL
- WAF : ModSecurity OWASP CRS 3.3.2 - SQL/XSS/Traversal -> 403
- IDS : Snort 3.12.2.0 - 5 regles custom ECOTRACK
- SIEM : Splunk Enterprise 10.0 - 3 dashboards SOC/IoT/Infra
- Anti-bruteforce : Fail2ban - ban apres 5 tentatives SSH
- Chiffrement : TLS 1.3 partout - MQTT :8883 + PostgreSQL + HTTPS

## 15 Tests de securite - 15/15 valides

- T1 - SQL Injection WAF -> 403 Forbidden
- T2 - XSS WAF -> 403 Forbidden
- T3 - Directory Traversal -> 403 Forbidden
- T4 - HTTPS HAProxy -> 200 OK
- T5 - HTTP redirect -> 302
- T6 - HAProxy stats -> eco_app + eco_web UP
- T7 - Snort SSH bruteforce -> Alerte Splunk P1
- T8 - Snort scan ports -> Alerte Splunk P2
- T9 - Fail2ban -> IP bannie auto
- T10 - PostgreSQL LAN -> TLSv1.3
- T11 - PostgreSQL IoT -> TLSv1.3
- T12 - DB hors zone -> Connection refused
- T13 - Redis -> PONG
- T14 - MQTT TLS :8883 -> OK
- T15 - Splunk 7/7 VMs -> OK

## CI/CD GitHub Actions

Pipeline operationnel - 3 jobs verts - Success en 24s

- Job 1 : Validation configurations
- Job 2 : Audit securite Bandit
- Job 3 : Rapport conformite ANSSI 6/8

## Conformite ANSSI - 6/8 (75%)

- R12 - Segmentation 4 zones - CONFORME
- R14 - DENY ALL pfSense - CONFORME
- R26 - Chiffrement TLS - CONFORME
- R44 - Logs Splunk centraux - CONFORME
- R64 - Snort 3 IDS - CONFORME
- R67 - WAF ModSecurity - CONFORME
- R78 - MAJ systemes - PARTIEL
- R80 - Chiffrement au repos - PARTIEL

*ECOTRACK - Bloc 2 - INGETIS Paris - Master 1 EASRSI - 2026*
