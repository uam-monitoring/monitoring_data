import json
from haversine import haversine, Unit

def make_UAM_ADSB_JSON(idx, uamIdentification, date, time, timeReference, altitude, longitude, latitude):
    
    UAM_ADSB = {
        "flightIdentifier" : {
            "uamIdentification" : uamIdentification
        },
        "currentTime" : {
            "date" : date,
            "time" : time,
            "timeReference" : timeReference
        },
        "currentPosition" : {
            "altitude" : altitude,
            "longitude" : longitude,
            "latitude" : latitude
        }
    }

    with open('ADSTestData/ADSTestData{num}.json'.format(num=idx), 'w') as f:
        json.dump(UAM_ADSB, f, indent=4)


def get_waypoints(departure, arrival):
    waypoints = []
    distance = haversine(departure, arrival, unit = "m")

    div = distance // 100

    lat_unit = (departure[0] - arrival[0]) / div
    lon_unit = (departure[1] - arrival[1]) / div

    waypoints.append(departure)
    for mul in range(1, int(div)):
        waypoints.append((departure[0] - lat_unit * mul, departure[1] - lon_unit * mul))
    waypoints.append(arrival)
    
    return waypoints


if __name__ == "__main__":
    
    departure = (35.887983, 128.606638)
    arrival = (35.879337, 128.627656)

    waypoints = get_waypoints(departure, arrival)

    for idx, point in enumerate(waypoints):
        make_UAM_ADSB_JSON(
            idx = str(idx),
            uamIdentification = "BKDG001",
            date = "2025-05-25",
            time = "14:{min:02d}:{sec:02d}".format(min = idx // 12, sec = idx * 5 % 60),
            timeReference = "UTC",
            altitude = 300,
            longitude = point[1],
            latitude = point[0]
        )   

