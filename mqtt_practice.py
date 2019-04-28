import paho.mqtt.client as mqtt
broker_address = "192.168.86.101"
broker_portno = 1883
client = mqtt.Client()
client.connect(broker_address, broker_portno)
client.subscribe("Test")
client.publish(topic = "Test", payload = "Hello",qos=0)