import numpy as np

distances = np.array([1400, 1650, 2150, 620, 1960])

print("Distances:", distances)

print("Total:", np.sum(distances))

print("Average:", np.mean(distances))

print("Minimum:", np.min(distances))

print("Maximum:", np.max(distances))

print("Double distances:", distances * 2)

weights = np.array([850, 1200, 500, 700, 950])

print ("average weight", np.mean(weights))

print ("heavy shipments (more than 800)", weights[weights > 800])

print ("wights after 10% increase (in kg):",weights*1.1)

print ("distance/weights ratio (km/kg): ", distances / weights)

print ("largest weight shipment (kg): ", np.max(weights))

print ("lightest shipment (kg): ", np.min(weights))

print(distances.ndim)
print(distances.shape)
print(weights.ndim)
print(weights.shape)

shipments = np.array([
    [1400, 850],
    [1650, 1200],
    [2150, 500],
    [620, 700],
    [1960, 950]
])

print("Shipments:")
print(shipments)

print("Dimensions:", shipments.ndim)
print("Shape:", shipments.shape)
                                                    
print("shipment weights:", shipments[:, 1])
print("shipment distances:", shipments[:, 0])


print("row 2:", shipments[1, :])
print("column 1:", shipments[:, 1])