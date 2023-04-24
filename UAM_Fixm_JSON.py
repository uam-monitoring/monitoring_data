import json

def make_UAM_FIXM_JSON(idx,
                       uamIdentification,
                       departure_longitude,
                       departure_latitude,
                       departure_planned_date,
                       departure_planned_time,
                       arrival_longitude,
                       arrival_latitude,
                       arrival_planned_date,
                       arrival_planned_time,
                       first_waypoint_altitude,
                       first_waypoint_longitude,
                       first_waypoint_latitude,
                       second_waypoint_altitude,
                       second_waypoint_longitude,
                       second_waypoint_latitude,
                       third_waypoint_altitude,
                       third_waypoint_longitude,
                       third_waypoint_latitude,
                       fourth_waypoint_altitude,
                       fourth_waypoint_longitude,
                       fourth_waypoint_latitude,):
    
    UAM_FIXM = {
        "flightIdentifier" : {
            "uamIdentification" : uamIdentification
        },
        "departure" : {
            "vertiport" : {
                "location" : {
                    "longitude" : departure_longitude,
                    "latitude" : departure_latitude
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
                    "longitude" : arrival_longitude,
                    "latitude" : arrival_latitude
                }
            },
            "plannedDepatureTime" : {
                "date" : arrival_planned_date,
                "time" : arrival_planned_time,
                "timeReference" : "UTC"
            }
        },
        "route" : {
            "firstWaypointLocation" : {
                "location" : {
                    "altitude" : first_waypoint_altitude,
                    "longitude" : first_waypoint_longitude,
                    "latitude" : first_waypoint_latitude
                }
            },
            "secondWaypointLocation" : {
                "location" : {
                    "altitude" : second_waypoint_altitude,
                    "longitude" : second_waypoint_longitude,
                    "latitude" : second_waypoint_latitude
                }
            },
            "thirdWaypointLocation" : {
                "location" : {
                    "altitude" : third_waypoint_altitude,
                    "longitude" : third_waypoint_longitude,
                    "latitude" : third_waypoint_latitude
                }
            },
            "fourthWaypointLocation" : {
                "location" : {
                    "altitude" : fourth_waypoint_altitude,
                    "longitude" : fourth_waypoint_longitude,
                    "latitude" : fourth_waypoint_latitude
                }
            }
        }
    }

    with open('FixmTestData/FixmTestData{num}.json'.format(num=idx), 'w') as f:
        json.dump(UAM_FIXM, f, indent=4)


if __name__ == "__main__":
    make_UAM_FIXM_JSON(idx = 1,
                       uamIdentification = "UAL123",
                       departure_longitude = "126.9525465",
                       departure_latitude = "37.5453577",
                       departure_planned_date = "dd",
                       departure_planned_time = "tt",
                       arrival_longitude = "126.9525465",
                       arrival_latitude = "37.5453577",
                       arrival_planned_date = "dd",
                       arrival_planned_time = "tt",
                       first_waypoint_altitude = "100",
                       first_waypoint_longitude = "126.9525465",
                       first_waypoint_latitude = "37.5453577",
                       second_waypoint_altitude = "200",
                       second_waypoint_longitude = "126.9525465",
                       second_waypoint_latitude = "37.5453577",
                       third_waypoint_altitude = "300",
                       third_waypoint_longitude = "126.9525465",
                       third_waypoint_latitude = "37.5453577",
                       fourth_waypoint_altitude = "400",
                       fourth_waypoint_longitude = "126.9525465",
                       fourth_waypoint_latitude = "37.5453577",)
