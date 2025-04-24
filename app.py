# dataset.py

from datetime import datetime, timedelta

# All Tamil Nadu districts with their coordinates
district_coords = {
    "Ariyalur": (11.1406, 79.0766),
    "Chengalpattu": (12.6928, 79.9831),
    "Chennai": (13.0827, 80.2707),
    "Coimbatore": (11.0168, 76.9558),
    "Cuddalore": (11.7447, 79.7682),
    "Dharmapuri": (12.1277, 78.1576),
    "Dindigul": (10.3673, 77.9803),
    "Erode": (11.3410, 77.7172),
    "Kallakurichi": (11.7380, 78.9640),
    "Kanchipuram": (12.8342, 79.7036),
    "Kanyakumari": (8.0883, 77.5385),
    "Karur": (10.9601, 78.0766),
    "Krishnagiri": (12.5307, 78.2170),
    "Madurai": (9.9252, 78.1198),
    "Mayiladuthurai": (11.1014, 79.6525),
    "Nagapattinam": (10.7630, 79.8434),
    "Namakkal": (11.2210, 78.1670),
    "Nilgiris": (11.4101, 76.6950),
    "Perambalur": (11.2340, 78.8806),
    "Pudukkottai": (10.3793, 78.8214),
    "Ramanathapuram": (9.3700, 78.8336),
    "Ranipet": (12.9416, 79.3211),
    "Salem": (11.6643, 78.1460),
    "Sivagangai": (9.8474, 78.4836),
    "Tenkasi": (8.9604, 77.3150),
    "Thanjavur": (10.7867, 79.1378),
    "Theni": (10.0063, 77.4760),
    "Thiruvallur": (13.1466, 80.0270),
    "Thiruvarur": (10.7710, 79.6365),
    "Thoothukudi": (8.7642, 78.1348),
    "Tiruchirappalli": (10.7905, 78.7047),
    "Tirunelveli": (8.7139, 77.7567),
    "Tirupathur": (12.4964, 78.5704),
    "Tiruppur": (11.1085, 77.3411),
    "Tiruvannamalai": (12.2253, 79.0747),
    "Vellore": (12.9165, 79.1325),
    "Viluppuram": (11.9391, 79.5000),
    "Virudhunagar": (9.5690, 77.9629)
}

def get_sample_data():
    now = datetime.now()
    return [
        {"text": "Robbery in Chennai", "lat": 13.0827, "lon": 80.2707, "time": (now - timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M")},
        {"text": "Assault in Coimbatore", "lat": 11.0168, "lon": 76.9558, "time": (now - timedelta(minutes=25)).strftime("%Y-%m-%d %H:%M")},
        {"text": "Kidnapping in Madurai", "lat": 9.9252, "lon": 78.1198, "time": (now - timedelta(minutes=40)).strftime("%Y-%m-%d %H:%M")},
        {"text": "Chain snatching in Salem", "lat": 11.6643, "lon": 78.1460, "time": (now - timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M")},
        {"text": "Vehicle theft in Thanjavur", "lat": 10.7867, "lon": 79.1378, "time": (now - timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M")}
    ]

# Location fetcher for districts
def get_coordinates(district_name: str):
    name = district_name.strip().title()
    return district_coords.get(name, None)
