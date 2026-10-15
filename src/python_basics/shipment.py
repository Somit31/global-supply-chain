shipments = [
    {
        "shipment_id": "S1001",
        "origin": "Mumbai",
        "destination": "Delhi",
        "distance_km": 1400,
        "weight_kg": 850,
        "delayed": False
    },
    {
        "shipment_id": "S1002",
        "origin": "Chennai",
        "destination": "Kolkata",
        "distance_km": 1650,
        "weight_kg": 1200,
    },
    {
        "shipment_id": "S1003",
        "origin": "Delhi",
        "destination": "Bangalore",
        "distance_km": 2150,
        "weight_kg": 500,
        "delayed": False
    }
]

shipment = {
    "shipment_id": "S1001",
    "origin": "Mumbai",
    "destination": "Delhi",
    "distance_km": 1400,
    "weight_kg": 850,
    "delayed": True
}

print(shipment)
print(shipment["origin"])
print(shipment["distance_km"])

for shipment in shipments:
    print(shipment["shipment_id"], shipment["origin"], "→", shipment["destination"])
