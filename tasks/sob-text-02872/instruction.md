Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Morrison Hotel (Chicago): The Morrison Hotel was a high rise hotel at the corner of Madison and Clark Streets in the downtown Loop community area of Chicago, Illinois, United States.  It was designed by the architectural firm of Holabird & Roche and completed in 1925.  The hotel was demolished in 1965 to make room for the First National Bank Building (now Chase Tower).

Westin Virginia Beach Town Center: The Westin Virginia Beach Town Center is a 38 story high rise hotel and living residence in Virginia Beach Town Center.  The 4 star hotel is the bottom half of the 38 story building and the upper stories are the residents' homes.  There are 119 condominiums in the top floors ranging from 900 to 4000 sqft .  The building was built throughout 2006 and 2007.  Upon completion, it became the tallest building in Virginia, surpassing the James Monroe Building in Richmond.

East Lake Shore Drive District: The East Lake Shore Drive District is a historic district in the Near North Side community area of Chicago, Illinois.  It includes eight buildings at 140 E. Walton, 179-229 E. Lake Shore Drive, and 999 N. Lake Shore Drive designed by Marshall and Fox and Fugard & Knapp and the opposing park.  It was designated a Chicago Landmark district on April 18, 1985.  These buildings include seven luxury high rise apartment buildings and the Drake Hotel.  Note that neither of the buildings on either end of the district actually has an East Lake Shore Drive address.  This district is located within the Streeterville neighborhood and overlaps with the Gold Coast.

Riverfront Towers: Riverfront Towers is an apartment and condominium complex of three luxury high rise residential skyscrapers along the International Riverfront in Detroit, Michigan, United States.  Each Riverfront Tower creates an ascending tier of three towers.

Ilikai Hotel &amp; Luxury Suites: The Ilikai Hotel & Luxury Suites is a landmark oceanfront high rise hotel and condominium at the western end of Waikiki in Honolulu, Hawai'i.  When it opened in 1964, the Ilikai was the first luxury high rise hotel in Hawai'i.

Tampa Marriott Waterside: Tampa Marriott Waterside is a 326 ft high rise hotel in Tampa, Florida near the Tampa Convention Center It was completed in 2000 and has 27 floors.  The building also includes 750 units and 50000 sqft of meeting space.  It is the city's largest hotel and the 12th tallest in Tampa.

One St. Petersburg: One St. Petersburg is a high rise condominium currently under construction in the city of St. Petersburg, Florida.  When constructed, the high rise will contain 253 condominium rooms that will range from 1,400 to 2,500 square feet.  At its maximum height, it will be 41 stories high, and will be the tallest building in St. Petersburg and Pinellas County.  The buildings second high rise will include a hotel across the lot containing 174 rooms and will be 13 stories high.  On the ground level of the building will contain retail space.  The construction of the high rise began on November 16, 2015 and is estimated to be completed in 2018.

Hotel Capri: The Hotel NH Capri La Habana is a historic high rise hotel located in central Havana.

Waikiki: Waikīkī ( ; Hawaiian: ] ) (also known as Waikiki Beach) is a beachfront neighborhood of Honolulu, on the south shore of the island of Oʻ ahu, in Hawaii, United States.  Waikiki is most famous for Waikīkī Beach, but it is just one of six beaches in the district, the others being Queen's Beach, Kuhio Beach, Gray's Beach, Fort DeRussy Beach and Kahanamoku Beach.

Canyon Ranch Miami Beach: The Carillion Hotel & Spa, and the Carillion Residences, formerly known as Canyon Ranch Miami Beach, is a complex of three high rise luxury condominiums in North Beach, Miami Beach, Florida, United States.  It is located on the beachfront on the east side of Collins Avenue between 68th and 69th Streets.  The Carillon Hotel & Spa complex includes The Carillon Hotel & Spa North Tower, the 20 floor The Carillon Hotel & Spa South Tower, The Carillon Hotel building located between The Carillon Hotel & Spa Towers on Collins Avenue, as well as the proposed Golden Sands Canyon Ranch proposed to be built north of The Carillon Hotel & Spa North Tower.  The old Golden Sands Hotel and Lounge is being demolished to make way for the new Golden Sands building.  The 15-story Carillion Hotel building was built in 1955 but was vacant for 15 years until it was renovated in 2007 and became part of the Canyon Ranch complex.  The 22 floor The Carillon Hotel & Spa South Tower is 257 feet (78 meters) tall and was completed in 2008.  The tallest building, the north tower of The Carillon Hotel & Spa is 37 floors and 121 meters (~400 feet) tall, was completed in 2008 and is one of the tallest buildings in Miami Beach.  The Carillon Hotel & Spa North Tower looks like two separate, connected towers, but both are the North Tower building.

Question: The first luxury high rise hotel in Hawai'i is located on one of how many beaches in the district?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "hotel_name": {
      "type": "string",
      "description": "The name of the first luxury high-rise hotel in Hawai'i."
    },
    "location_district": {
      "type": "string",
      "description": "The district where the hotel is located."
    },
    "number_of_beaches_in_district": {
      "type": "integer",
      "description": "The total count of beaches in the specified district."
    },
    "beach_names": {
      "type": "array",
      "description": "A list of the names of the beaches in the district.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "hotel_name",
    "location_district",
    "number_of_beaches_in_district",
    "beach_names"
  ],
  "additionalProperties": false
}
