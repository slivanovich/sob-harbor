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
Charles Lindbergh: Charles Augustus Lindbergh (February 4, 1902 – August 26, 1974), nicknamed Slim, Lucky Lindy, and The Lone Eagle, was an American aviator, military officer, author, inventor, explorer, and environmental activist.  At age 25 in 1927, he went from obscurity as a U.S. Air Mail pilot to instantaneous world fame by making his Orteig Prizewinning nonstop flight from Long Island, New York, to Paris.  He covered the 33 ⁄ -hour, 3,600 smi alone in a single-engine purpose-built Ryan monoplane, "Spirit of St. Louis".  This was the first solo transatlantic flight and the first non-stop flight between North America and mainland Europe.  Lindbergh was an officer in the U.S. Army Air Corps Reserve, and he received the United States' highest military decoration, the Medal of Honor, for the feat.

Douglas Campbell (aviator): Douglas Campbell (June 7, 1896 – December 16, 1990) was an American aviator and World War I flying ace.  He was the first American aviator flying in an American-trained air unit to achieve the status of ace.

Elizabeth Strohfus: Elizabeth "Betty" Strohfus (November 19, 1919 – March 6, 2016) was an American aviator and pioneering member of the Women Airforce Service Pilots (WASP) during World War II.  Strohfus, one of just 1,074 female pilots to earn silver wings for the WASPs, flew noncombat missions from 1943 to 1944, often ferrying military planes throughout the United States.  She also trained male air and infantry gunners at Las Vegas Army Airfield during the early 1940s.  Elizabeth Strohfus was the recipient of two Congressional Gold Medals for her service in the WASPs and was inducted into the Minnesota Aviation Hall of Fame.  She was believed to be one of the last surviving WASP aviators.

Lindy's: Lindy's is a deli and restaurant with two locations in Manhattan, New York City, at 825 7th Avenue (at 53rd Street) and 401 7th Avenue (at 32nd Street).  Lindy's is best known for its original incarnation which opened in 1921 on Broadway.  It is currently owned by the Riese Organization.

Fred Zinn: Friedrich Wilhelm "Fred" Zinn was a volunteer American aviator of German descent who flew with French Armée de l'Air forces in World War I and an early pioneer of aerial photography for wartime reconnaissance and Military intelligence.

Fred Hartsook: Fred Hartsook (26 October 1876 – 30 September 1930) was an American photographer and owner of a California studio chain described as "the largest photographic business in the world" at the time, who counted Henry Ford, Charles Lindbergh, Mary Pickford, and sitting President Woodrow Wilson among his celebrity clients.  He later became the owner of the Hartsook Inn, a resort in Humboldt County, and two ranches in Southern California on which he reared prized Holstein cattle.  Hartsook was married to Bess Hesby, queen of the San Francisco Pan-Pacific Exposition of 1915.

Douglas Corrigan: Douglas Corrigan (January 22, 1907 – December 9, 1995) was an American aviator born in Galveston, Texas.  He was nicknamed "Wrong Way" in 1938.  After a transcontinental flight from Long Beach, California, to New York City, he flew from Floyd Bennett Field in Brooklyn, New York, to Ireland, though his flight plan was filed to return to Long Beach.  He claimed his unauthorized flight was due to a navigational error, caused by heavy cloud cover that obscured landmarks and low-light conditions, causing him to misread his compass.  However, he was a skilled aircraft mechanic (he was one of the builders of Charles Lindbergh's "Spirit of St. Louis") and had made several modifications to his own plane, preparing it for his transatlantic flight.  He had been denied permission to make a nonstop flight from New York to Ireland, and his "navigational error" was seen as deliberate.  Nevertheless, he never publicly admitted to having flown to Ireland intentionally.

Vasse and Wonnerup Floodgates: The Vasse and Wonnerup Floodgates is a heritage listed site in Western Australia that comprises two locations.  The two locations are the site of the Vasse floodgates on the Vasse River and the Wonnerup floodgates on the Wonnerup Estuary.  In addition, the 2004 site of the Vasse floodgate was also the site of the Ballarat Bridge which was built in 1871 as part of a logging rail line where the Ballarat Steam engine was the first steam engine to operate in Western Australia.

Hiram Mann: Hiram Mann (May 23, 1921 – May 17, 2014) was an American aviator, retired lieutenant colonel in the United States Air Force, and member of the Tuskegee Airmen's 332nd Fighter Group, an elite squadron of African-American airmen during World War II.  Mann flew forty-eight missions over Europe as a member of the 332nd Fighter Group during the war.  Mann was a member of the "Red Tails," as the Tuskegee Airmen were called at the time, so-called because the tails of the P-51D Mustangs flown by the African-American pilots in combat missions were painted crimson red.  (The term "Tuskegee Airmen" did not come into use until the creation of a veteran's organization in 1972).  Mann nicknamed his own fighter plane "The Iron Lady" after his wife.

Lucky Lindy!: "Lucky Lindy" is a song composed by Abel Baer, with lyrics by L. Wolfe Gilbert.  It was published by Harmony in 1927.

Question: Fred Hartsook had, as a client the American aviator, nicknamed Lucky Lindy, who flew nonstop between which two locations?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "aviator_name": {
      "type": "string",
      "description": "The full name of the American aviator."
    },
    "nickname": {
      "type": "string",
      "description": "The specific nickname of the aviator mentioned in the question."
    },
    "flight_details": {
      "type": "object",
      "properties": {
        "flight_type": {
          "type": "string",
          "description": "Description of the flight type (e.g., nonstop, solo transatlantic)."
        },
        "origin_location": {
          "type": "string",
          "description": "The starting location of the nonstop flight."
        },
        "destination_location": {
          "type": "string",
          "description": "The ending location of the nonstop flight."
        },
        "year_of_flight": {
          "type": "integer",
          "description": "The year the flight took place."
        },
        "duration_hours": {
          "type": "number",
          "description": "The duration of the flight in hours."
        },
        "distance_smi": {
          "type": "integer",
          "description": "The distance covered by the flight in statute miles."
        }
      },
      "required": [
        "flight_type",
        "origin_location",
        "destination_location",
        "year_of_flight",
        "duration_hours",
        "distance_smi"
      ],
      "additionalProperties": false
    },
    "was_hartsook_client": {
      "type": "boolean",
      "description": "Indicates if the aviator was a client of Fred Hartsook."
    }
  },
  "required": [
    "aviator_name",
    "nickname",
    "flight_details",
    "was_hartsook_client"
  ],
  "additionalProperties": false
}
