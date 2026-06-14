# ECOTRACK - Bloc 1 EASRSI

**Master 1 EASRSI - INGETIS Paris 2026**
**Soutenance : 29 & 30 juin 2026**
**GitHub : https://github.com/imeldamague/ECOTRACK**

## Equipe

- **Imelda** - Chef de projet / RSSI - ECO-MON - ECO-SEC - ECO-MQTT
- **Marie Claude** - Architecte reseau - ECO-PROXY - ECO-DB
- **Ephra** - Firewall & Dev - pfSense - ECO-APP - ECO-WEB

## Rapport

- [Telecharger le rapport Bloc 1](https://github.com/imeldamague/ECOTRACK/blob/main/bloc1/docs/ECOTRACK_Bloc1_Final.pdf)
- [Schema reseau Draw.io](https://github.com/imeldamague/ECOTRACK/blob/main/bloc1/diagrams/ECOTRACK_Schema_Final.drawio)
- [Diagramme BPMN](https://github.com/imeldamague/ECOTRACK/blob/main/bloc1/diagrams/ECOTRACK_BPMN_Processus.drawio)
- [Gantt 8 sprints](https://github.com/imeldamague/ECOTRACK/blob/main/bloc1/diagrams/ECOTRACK_Gantt.drawio)

---

## 🏗️ Architecture
<img width="1499" height="1049" alt="reseau" src="https://github.com/user-attachments/assets/cf5a0f59-a9ff-4ac5-a112-ecf2de3db3d7" />

## 15 Tests valides

- T1 - SQL Injection WAF -> 403 Forbidden
- T2 - XSS WAF -> 403 Forbidden
- T3 - Directory Traversal -> 403 Forbidden
- T4 - HTTPS HAProxy -> 200 OK
- T5 - HTTP redirect -> 302
- T6 - HAProxy stats -> UP
- T7 - Snort SSH bruteforce -> Alerte P1
- T8 - Snort scan ports -> Alerte P2
- T9 - Fail2ban -> IP bannie
- T10 - PostgreSQL LAN -> TLSv1.3
- T11 - PostgreSQL IoT -> TLSv1.3
- T12 - DB hors zone -> Connection refused
- T13 - Redis -> PONG
- T14 - MQTT TLS :8883 -> OK
- T15 - Splunk 7/7 VMs -> OK

## 8 Sprints Scrum

- S1 - 7-20 Avril - Infrastructure base - TERMINE
- S2 - 21 Avril-4 Mai - Reseau + BDD - TERMINE
- S3 - 5-18 Mai - Application IoT - TERMINE
- S4 - 19 Mai-1 Juin - Securite IDS + SIEM - TERMINE
- S5 - 2-8 Juin - WAF + 15 tests - TERMINE
- S6 - 9-12 Juin - Fusion 8 VMs - TERMINE
- S7 - 13-19 Juin - Docs + Demo - EN COURS
- S8 - 29-30 Juin - Soutenance INGETIS - A VENIR

*ECOTRACK - Bloc 1 - INGETIS Paris - Master 1 EASRSI - 2026*

---

