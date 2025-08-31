import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Multiple hotels ka data store
HOTELS = {
    "Hotel Paradise": {
        "location": "Karachi, Pakistan",
        "rooms": "100 luxury rooms",
        "amenities": "Pool, Spa, Free WiFi, Breakfast",
        "price_range": "PKR 10,000 - PKR 25,000 per night"
    },
    "Ocean View Resort": {
        "location": "Gwadar, Pakistan",
        "rooms": "60 sea-view rooms",
        "amenities": "Private Beach, Restaurant, Water Sports",
        "price_range": "PKR 12,000 - PKR 30,000 per night"
    },
    "City Star Hotel": {
        "location": "Lahore, Pakistan",
        "rooms": "150 modern rooms",
        "amenities": "Conference Hall, Gym, Rooftop Cafe",
        "price_range": "PKR 8,000 - PKR 20,000 per night"
    }
}

class HotelAssistant:
    def __init__(self):
        self.model = genai.GenerativeModel("models/gemini-1.5-flash")

    def get_hotel_info(self, query: str) -> str:
        # User ke query se relevant hotel dhoondna
        matched_hotel = None
        for hotel_name in HOTELS.keys():
            if hotel_name.lower() in query.lower():
                matched_hotel = hotel_name
                break

        if not matched_hotel:
            return "Sorry, I couldn’t find that hotel. Please try again with a correct name."

        details = HOTELS[matched_hotel]

        # Dynamic instruction banani hai: user query + context
        prompt = f"""
        You are a helpful hotel booking assistant.
        The user asked: {query}

        Hotel Selected: {matched_hotel}
        Location: {details['location']}
        Rooms: {details['rooms']}
        Amenities: {details['amenities']}
        Price Range: {details['price_range']}

        Please respond to the user query clearly and professionally using this hotel information.
        """

        response = self.model.generate_content(prompt)
        return response.text
