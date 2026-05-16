# ECOTRACK
Plateforme IoT Gestion des Déchets Urbains - Master 1 Cybersécurité INGETIS
# ECOTRACK — Plateforme IoT Gestion des Déchets Urbains

## L'équipe Cyber-Réseaux
| Membre | Rôle | VMs |
|---|---|---|
| **Imelda** | Chef de projet | VM6 Splunk + VM7 Snort + VM8 MQTT |
| **Marie Claude** | Réseau & BDD | VM1 HAProxy + VM5 PostgreSQL |
| **Ephra** | Infrastructure | VM0 pfSense + VM3 ECO-APP + VM4 ECO-WEB |

## Ordre de démarrage (OBLIGATOIRE)
1. pfSense → attendre 2 minutes
2. ECO-DB → attendre 1 minute
3. ECO-MQTT
4. ECO-PROXY
5. ECO-APP + ECO-WEB
6. ECO-MON Splunk → attendre 2 minutes
7. ECO-SEC Snort

## Adressage IP
| VM | IP | Zone | Responsable |
|---|---|---|---|
| pfSense DMZ | 10.10.1.1 | DMZ | Ephra |
| ECO-PROXY | 10.10.1.10 | DMZ | Marie Claude |
| ECO-APP | 10.10.2.10 | LAN | Ephra |
| ECO-WEB | 10.10.2.20 | LAN | Ephra |
| ECO-DB | 10.10.2.30 | LAN | Marie Claude |
| ECO-MON Splunk | 10.10.3.10 | MGT | Imelda |
| ECO-SEC Snort | 10.10.3.20 | MGT | Imelda |
| ECO-MQTT | 10.10.4.10 | IoT | Imelda |

## Accès interfaces
| Service | URL | Identifiants |
|---|---|---|
| Splunk SIEM | http://10.10.3.10:8000 | admin / Ecotrack2026! |
| Grafana | http://10.10.3.10:3000 | admin / Ecotrack2026! |
| ECO-APP API | http://10.10.2.10:3000 | — |
| HAProxy stats | http://10.10.1.10:8080/haproxy-stats | — |

## Soutenance — 20 juin 2026
Master 1 Réseaux & Cybersécurité — INGETIS Paris
