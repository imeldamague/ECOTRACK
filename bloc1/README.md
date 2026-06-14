ECOTRACK — Bloc 1 : Planifier et Organiser un Projet EASRSI

Master 1 EASRSI — INGETIS Paris 2026

Plateforme IoT de Gestion des Dechets Urbains — Paris

Soutenance : 29 & 30 juin 2026



Equipe
MembreRoleVMsImeldaChef de projet / RSSIECO-MON · ECO-SEC · ECO-MQTTMarie ClaudeArchitecte reseauECO-PROXY · ECO-DBEphraFirewall & DeveloppementVM0-pfSense · ECO-APP · ECO-WEB

Rapport Bloc 1
DocumentLienBloc 1 — Rapport completTelecharger le rapportSchema reseauECOTRACK_Schema_Final.drawioDiagramme BPMNECOTRACK_BPMN_Processus.drawioGantt 8 sprintsECOTRACK_Gantt.drawio

Architecture
INTERNET
    |
    | HTTPS :443
    v
[VM0 - pfSense 2.8.1] — FIREWALL — 31 regles — DENY ALL
    |           |              |                |
    v           v              v                v
 DMZ          LAN          Management         IoT
10.10.1.0   10.10.2.0     10.10.3.0       10.10.4.0
    |           |              |                |
ECO-PROXY  ECO-APP       ECO-MON          ECO-MQTT
HAProxy    Node.js       Splunk SIEM      Mosquitto
WAF ModSec ECO-WEB       Grafana          TLS :8883
:8091      Nginx         ECO-SEC          10 capteurs
           ECO-DB        Snort IDS
           PostgreSQL    Fail2ban
           Redis

Planning 8 Sprints Scrum
SprintPeriodeObjectifStatutS17-20 AvrilInfrastructure baseTERMINES221 Avril-4 MaiReseau + BDDTERMINES35-18 MaiApplication IoTTERMINES419 Mai-1 JuinSecurite IDS + SIEMTERMINES52-8 JuinWAF + 15 testsTERMINES69-12 JuinFusion 8 VMsTERMINES713-19 JuinDocs + DemoEN COURSS829-30 JuinSoutenance INGETISA VENIR

15 Tests Securite Valides
T1  SQL Injection WAF       -> 403 Forbidden
T2  XSS WAF                 -> 403 Forbidden
T3  Directory Traversal     -> 403 Forbidden
T4  HTTPS actif HAProxy     -> 200 OK
T5  HTTP -> HTTPS redirect  -> 302
T6  HAProxy stats           -> eco_app + eco_web UP
T7  Snort bruteforce SSH    -> Alerte Splunk P1
T8  Snort scan ports nmap   -> Alerte Splunk P2
T9  Fail2ban ban IP         -> IP bannie auto
T10 PostgreSQL LAN TLS      -> TLSv1.3
T11 PostgreSQL IoT TLS      -> TLSv1.3
T12 DB refusee hors zone    -> Connection refused
T13 Redis PING              -> PONG
T14 MQTT TLS :8883          -> TLS_ECOTRACK_OK
T15 Splunk 7 VMs            -> 7/7 connectees
