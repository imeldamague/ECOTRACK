# ECOTRACK - Plateforme IoT Gestion des Dechets Urbains

**Master 1 Reseaux & Cybersecurite - INGETIS Paris**
**Soutenance : 29 & 30 juin 2026**
**GitHub : https://github.com/imeldamague/ECOTRACK**

## Equipe

| Membre | Role | VMs |
|--------|------|-----|
| Imelda | Chef de projet / RSSI | VM6 Splunk + VM7 Snort + VM8 MQTT |
| Marie Claude | Reseau & BDD | VM1 HAProxy + VM5 PostgreSQL |
| Ephra | Infrastructure | VM0 pfSense + VM3 ECO-APP + VM4 ECO-WEB |

## Ordre de demarrage (OBLIGATOIRE)

1. pfSense - attendre 2 minutes
2. ECO-DB - attendre 1 minute
3. ECO-MQTT
4. ECO-PROXY
5. ECO-APP + ECO-WEB
6. ECO-MON Splunk - attendre 2 minutes
7. ECO-SEC Snort

## Adressage IP

| VM | IP | Zone | Responsable |
|----|-----|------|-------------|
| pfSense DMZ | 10.10.1.1 | DMZ | Ephra |
| ECO-PROXY | 10.10.1.10 | DMZ | Marie Claude |
| ECO-APP | 10.10.2.10 | LAN | Ephra |
| ECO-WEB | 10.10.2.20 | LAN | Ephra |
| ECO-DB | 10.10.2.30 | LAN | Marie Claude |
| ECO-MON Splunk | 10.10.3.10 | MGT | Imelda |
| ECO-SEC Snort | 10.10.3.20 | MGT | Imelda |
| ECO-MQTT | 10.10.4.10 | IoT | Imelda |

## Acces interfaces

| Service | URL | Identifiants |
|---------|-----|--------------|
| Splunk SIEM | http://10.10.3.10:8000 | admin / ****** |
| Grafana | http://10.10.3.10:3000 | admin / ****** |
| ECO-APP API | http://10.10.2.10:3000 | - |
| HAProxy stats | http://10.10.1.10:8080/haproxy-stats | - |
| WAF ModSecurity | http://10.10.1.10:8091 | - |
| Adminer DB | http://10.10.2.30:80/adminer.php | ecotrack_user / ****** |

## Documentation

- [Bloc 1 - Planification projet](./bloc1/README.md)
- [Bloc 2 - Infrastructure](./bloc2/README.md)
- [Guide operationnel PDF]()

## Architecture
<img width="1499" height="1049" alt="reseau" src="https://github.com/user-attachments/assets/aa1644c8-ea41-4448-8131-87ac61c2c424" />

## Soutenance — 29 & 30 juin 2026
Master 1 Réseaux & Cybersécurité — INGETIS Paris
