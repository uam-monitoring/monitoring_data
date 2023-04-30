import json

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


if __name__ == "__main__":

    make_UAM_ADSB_JSON(
        idx = "1",
        uamIdentification = "UAL123",
        date = "2025-05-25",
        time = "14:12:00",
        timeReference = "UTC",
        altitude = "400",
        longitude = "126.9525465",
        latitude = "37.5453577"
    )

