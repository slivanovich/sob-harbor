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
St. Francis (fireboat): St. Francis is a fireboat operated by the San Francisco Fire Department on San Francisco Bay since 2016.  Also known as "Fireboat 3", she was given the official name on October 17, 2016, the anniversary of the 1989 Loma Prieta earthquake.  Local schoolchildren helped pick the vessel's name.

Marina District, San Francisco: The Marina District is a neighborhood located in San Francisco, California.  The neighborhood sits on the site of the 1915 Panama–Pacific International Exposition, staged after the 1906 San Francisco earthquake to celebrate the reemergence of the city.  Aside from the Palace of Fine Arts (POFA), all other buildings were demolished to make the current neighborhood.  The Marina currently has the highest non-Hispanic white resident percentage of any recognized neighborhood in San Francisco.

2003 Alabama earthquake: The 2003 Alabama earthquake took place on April 29 at 3:59 A.M. Central Daylight Time (local time when the event occurred) eight miles (13 km) east-northeast of Fort Payne, Alabama.  The number of people who felt this quake was exceptionally high as the earthquake could be felt in 11 states across the East Coast and as far north as southern Indiana.  The earthquake was strongly felt throughout metropolitan Atlanta.  The Georgia Building Authority was called out to inspect the historic Georgia State Capitol in downtown Atlanta and other state-owned buildings, but found no problems.  However, this is not out of the ordinary as earthquakes east of the Rocky Mountains can be felt several times the area felt on West Coast earthquakes.  The earthquake was given a magnitude 4.6 on the moment magnitude scale by the USGS (other sources reported as high a magnitude as 4.9) and reports of the duration of the shaking range from 10 seconds to as long as 45 seconds.  It is tied with a 1973 earthquake near Knoxville, Tennessee as the strongest earthquake ever to occur in the Eastern Tennessee Seismic Zone, which is the second most active seismic zone east of the Rocky Mountains, with the New Madrid Seismic Zone the most active.

San Diego Marriott Marquis &amp; Marina: The San Diego Marriott Marquis & Marina is a hotel in San Diego, California.  Located in the Marina district of Downtown San Diego, the hotel is composed of two towers of equal height.  The two towers are the 20th tallest buildings in San Diego and are a prominent fixture in the city's skyline.  The 25-story towers have a height of 361 ft (110 m) and contain 1,362 rooms.  The hotel is affiliated with Marriott Hotels & Resorts.

Seismic hazard: A seismic hazard is the probability that an earthquake will occur in a given geographic area, within a given window of time, and with ground motion intensity exceeding a given threshold.  With a hazard thus estimated, risk can be assessed and included in such areas as building codes for standard buildings, designing larger buildings and infrastructure projects, land use planning and determining insurance rates.  The seismic hazard studies also may generate two standard measures of anticipated ground motion, both confusingly abbreviated MCE; the simpler probabilistic Maximum Considered Earthquake (or Event ), used in standard building codes, and the more detailed and deterministic Maximum Credible Earthquake incorporated in the design of larger buildings and civil infrastructure like dams or bridges.  It is important to clarify which MCE is being discussed.

Phoenix (fireboat): Phoenix is a fireboat owned by State of California and operated by the city of San Francisco in the San Francisco Bay since 1955.  "Phoenix" is known for helping to save Marina District buildings from further destruction by fire following the 1989 Loma Prieta earthquake.  Her worthy assistance resulted in a second vintage fireboat obtained for the city.  Both "Guardian" and "Phoenix" are based at Firehouse No. 35 at Pier 22½ of the Port of San Francisco.  "Phoenix" often leads parades of ships, and takes part in welcoming ceremonies.

Guardian (fireboat): Guardian is a fireboat owned by San Francisco Fire Department and operated in the San Francisco Bay since 1990 in reserve status.  "Guardian" was a gift to the people of San Francisco by anonymous donors following the notable role of the fireboat "Phoenix" in helping to save the Marina District buildings from further destruction by fire following the 1989 Loma Prieta earthquake.  Both "Guardian" and "Phoenix" fireboats are based at Firehouse No. 35 at Pier 22½ of the Port of San Francisco.  "Guardian" has 5 pumps which can deliver up to 26,000 gallons of water per minute, significantly more than "Phoenix"

Panama–Pacific International Exposition: The Panama–Pacific International Exposition (PPIE) was a world's fair held in San Francisco, in the United States, between February 20 and December 4 in 1915.  Its ostensible purpose was to celebrate the completion of the Panama Canal, but it was widely seen in the city as an opportunity to showcase its recovery from the 1906 earthquake.  The fair was constructed on a 635 acre (2.6 km) site in San Francisco, along the northern shore, between the Presidio and Fort Mason, now known as the Marina District.

Harbor Club Condominiums: Harbor Club Condominiums is a high-rise residential building in San Diego, California composed of two towers of equal height.  The 41-story towers have a height of 424 feet (129 m) and are a prominent fixture in San Diego's skyline.  Located in the Marina district of Downtown San Diego, Harbor Club was designed by architects BPA Architecture Planning Interiors.  The condos are located near the San Diego Convention Center and Petco Park.  The towers are currently the eighth tallest buildings in San Diego.

1989 Loma Prieta earthquake: The 1989 Loma Prieta earthquake occurred in Northern California on October 17 at local time.  The shock was centered in The Forest of Nisene Marks State Park approximately 10 mi northeast of Santa Cruz on a section of the San Andreas Fault System and was named for the nearby Loma Prieta Peak in the Santa Cruz Mountains.  With a moment magnitude of 6.9 and a maximum Mercalli intensity of IX ("Violent"), the shock was responsible for 63 deaths and 3,757 injuries.  The Loma Prieta segment of the San Andreas Fault System had been relatively inactive since the 1906 San Francisco earthquake (to the degree that it was designated a seismic gap) until two moderate foreshocks occurred in June 1988 and again in August 1989.

Question: On which day in 1989 did this earthquake occur in which the fireboat "Phoenix" was instrumental in saving the Marina District buildings from further destruction?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "earthquake_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The official name of the earthquake event."
        },
        "occurrence_date": {
          "type": "object",
          "properties": {
            "year": {
              "type": "integer",
              "description": "The year the earthquake occurred."
            },
            "month": {
              "type": "string",
              "description": "The month the earthquake occurred."
            },
            "day": {
              "type": "integer",
              "description": "The day of the month the earthquake occurred."
            }
          },
          "required": [
            "year",
            "month",
            "day"
          ],
          "additionalProperties": false
        },
        "magnitude": {
          "type": "number",
          "description": "The moment magnitude of the earthquake."
        }
      },
      "required": [
        "name",
        "occurrence_date"
      ],
      "additionalProperties": false
    },
    "fireboat_contribution": {
      "type": "object",
      "properties": {
        "fireboat_name": {
          "type": "string",
          "description": "The name of the fireboat involved."
        },
        "action_description": {
          "type": "string",
          "description": "Description of the fireboat's action during the event."
        },
        "target_area": {
          "type": "string",
          "description": "The specific district or area that benefited from the fireboat's actions."
        }
      },
      "required": [
        "fireboat_name",
        "action_description",
        "target_area"
      ],
      "additionalProperties": false
    },
    "final_answer_day": {
      "type": "integer",
      "description": "The specific day of the month the earthquake occurred, answering the question directly."
    }
  },
  "required": [
    "earthquake_details",
    "fireboat_contribution",
    "final_answer_day"
  ],
  "additionalProperties": false
}
