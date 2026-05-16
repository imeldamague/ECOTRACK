import paho.mqtt.client as mqtt
import time, random, json

MQTT_HOST = '10.10.4.10'
MQTT_PORT = 1883
POUBELLES = [f'poubelle_{i:02d}' for i in range(1, 11)]

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, 'ecotrack-simulator')
client.connect(MQTT_HOST, MQTT_PORT, 60)

print(f'=== ECOTRACK Simulateur démarré → {MQTT_HOST}:{MQTT_PORT} ===')

while True:
    for poubelle in POUBELLES:
        niveau = random.randint(10, 95)
        batterie = random.randint(60, 100)
        data = json.dumps({
            'id': poubelle,
            'niveau': niveau,
            'batterie': batterie,
            'statut': 'pleine' if niveau > 80 else 'normal'
        })
        client.publish(f'capteurs/{poubelle}', data)
        print(f'[{poubelle}] niveau:{niveau}% batterie:{batterie}%')
    print(f'--- Cycle terminé, prochain envoi dans 30 secondes ---')
    time.sleep(30)
