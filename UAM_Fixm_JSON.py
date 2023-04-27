import json
from haversine import haversine, Unit

def make_UAM_FIXM_JSON(idx,
                       uamIdentification,
                       departure, departure_planned_date, departure_planned_time,
                       arrival, arrival_planned_date, arrival_planned_time,
                       waypoints):
    
    UAM_FIXM = {
        "flightIdentifier" : {
            "uamIdentification" : uamIdentification
        },
        "departure" : {
            "vertiport" : {
                "location" : {
                    "longitude" : departure[1],
                    "latitude" : departure[0]
                }
            },
            "plannedDepatureTime" : {
                "date" : departure_planned_date,
                "time" : departure_planned_time,
                "timeReference" : "UTC"
            }
        },
        "arrival" : {
            "vertiport" : {
                "location" : {
                    "longitude" : arrival[1],
                    "latitude" : arrival[0]
                }
            },
            "plannedDepatureTime" : {
                "date" : arrival_planned_date,
                "time" : arrival_planned_time,
                "timeReference" : "UTC"
            }
        },
        "route" : [
            {
                "longitude" : waypoint[1],
                "latitude" : waypoint[0]
            } for waypoint in waypoints
        ]
    }

    with open('FixmTestData/FixmTestData{num}.json'.format(num=idx), 'w') as f:
        json.dump(UAM_FIXM, f, indent=4)


def get_waypoints(departure, arrival):
    waypoints = []
    distance = haversine(departure, arrival, unit = "m")

    div = distance // 500

    lat_unit = (departure[0] - arrival[0]) / div
    lon_unit = (departure[1] - arrival[1]) / div

    for mul in range(1, int(div)):
        waypoints.append((departure[0] - lat_unit * mul, departure[1] - lon_unit * mul))
    
    return waypoints


if __name__ == "__main__":
    
    departure = (35.887983, 128.606638)
    arrival = (35.828633, 128.613750)

    waypoints = get_waypoints(departure, arrival)

    make_UAM_FIXM_JSON(idx = 1,
                       uamIdentification = "UAL123",
                       departure = departure, departure_planned_date = "dd", departure_planned_time = "tt",
                       arrival = arrival, arrival_planned_date = "dd", arrival_planned_time = "tt",
                       waypoints = waypoints)