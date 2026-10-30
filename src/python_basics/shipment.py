import csv


def calculate_total_weight(shipments):
    total = 0

    for shipment in shipments:
        total += shipment["weight_kg"]

    return total


def calculate_total_distance(shipments):
    total = 0

    for shipment in shipments:
        total += shipment["distance_km"]

    return total


def find_delayed_shipments(shipments):
    delayed_shipments = []

    for shipment in shipments:
        if shipment["delayed"]:
            delayed_shipments.append(shipment)

    return delayed_shipments


def calculate_delay_rate(shipments):
    if not shipments:
        return 0

    delayed_count = 0

    for shipment in shipments:
        if shipment["delayed"]:
            delayed_count += 1

    return delayed_count / len(shipments)


def load_shipments(filename):
    shipments = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            shipment = {
                "shipment_id": row["shipment_id"],
                "origin": row["origin"],
                "destination": row["destination"],
                "distance_km": int(row["distance_km"]),
                "weight_kg": int(row["weight_kg"]),
                "delayed": row["delayed"].lower() == "true"
            }

            shipments.append(shipment)

    return shipments


# Load data
shipments = load_shipments("data/raw/shipment.csv")


# Basic analysis
print("Total shipments:", len(shipments))

print("Total weight:",
      calculate_total_weight(shipments),
      "kg")

print("Total distance:",
      calculate_total_distance(shipments),
      "km")

print("Delay rate:",
      calculate_delay_rate(shipments) * 100,
      "%")


# Find delayed shipments
delayed_shipments = find_delayed_shipments(shipments)

print("\nDelayed shipments:")

for shipment in delayed_shipments:
    print(
        shipment["shipment_id"],
        shipment["origin"],
        "→",
        shipment["destination"]
    )