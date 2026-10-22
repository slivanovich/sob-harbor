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
Institute of Electrical and Electronics Engineers: The Institute of Electrical and Electronics Engineers (IEEE, pronounced "I triple E") is a professional association with its corporate office in New York City and its operations center in Piscataway, New Jersey.  It was formed in 1963 from the amalgamation of the American Institute of Electrical Engineers and the Institute of Radio Engineers.  Today, it is the world's largest association of technical professionals with more than 420,000 members in over 160 countries around the world.  Its objectives are the educational and technical advancement of electrical and electronic engineering, telecommunications, computer engineering and allied disciplines.

Samaná Peninsula: The Samaná Península is a peninsula in Dominican Republic situated in the province of Samaná.  The Samaná Peninsula is connected to the rest of the state by the Isthmus of Samaná.  The Peninsula contains many beaches, especially in the city of Santa Bárbara de Samaná.  It contains 3 rivers.  The main roads are the DR-5 and the Samaná Highway that leads from the peninsula to Santo Domingo.  The peninsula also contains the Samaná El Catey International Airport.  The peninsula also has a lot of agriculture and social economy.

Zege Peninsula: Zege Peninsula is located on the southern shore of Lake Tana in Ethiopia, and is situated at (11° 40’ to 11° 43’ N and 37 °19’ to 37 °21’ E).  It is 600 km northwest of Addis Ababa, the capital city of Ethiopia.  Lake Tana is the largest lake in Ethiopia, and is the source of the Blue Nile river.  Zege peninsula is attached to dry land on its western part.  As a place name, the word "zege" signifies a peninsula that encloses two rural qebele, the former monastery and Zägé town at the gate of the main land of the peninsula.  At present, Zegé is part of Bahir Dar city administration, and is 32 km from the main town, the capital of Amhara National Regional State.  The origin of the term "zegié" is somewhat obscure.  Informants from Ura Kidane miheret monastic church, one of the earliest church in the peninsula associated the term to Debra Zegag and Abba Nahom; where as some monks who were servants of Mähal Zegié Giyorgis attributed the term to Zengie (my shaft) and to Abun Betre Maryam, founder of Zegie monastery.  Still another church scholar, Aleqa Aynakulu Mersha, related the term to a name of a tribe called Zegie (Aleqa Aynekulu) 1955 E.C:466; Tadese Tamrat, 1994:954-959).  On the peninsula of Zege there are six Monastic churches, all established between the 14th and 17th centuries.

New Jersey: New Jersey is a state in the Northeastern and mid-Atlantic regions of the United States.  It is a peninsula, bordered on the north and east by the state of New York; on the east, southeast, and south by the Atlantic Ocean; on the west by the Delaware River and Pennsylvania; and on the southwest by the Delaware Bay and Delaware.  New Jersey is the fourth-smallest state by area but the 11th-most populous and the most densely populated of the 50 U.S. states.  New Jersey lies entirely within the combined statistical areas of New York City and Philadelphia and is the third-wealthiest state by median household income as of 2016.

Piscataway Creek (Virginia): Piscataway Creek is a tributary of the Rappahannock River in eastern Virginia, in the United States, approximately 17 mi in length.  It is fed by the Sturgeon Swamp and Mussel Swamp, lowlands near US Route 360 on the Middle Peninsula, and empties into the Rappahannock River three miles (5 km) downstream from the town of Tappahannock.  It is tidal for much of its course.

Bergen Peninsula: The Bergen Peninsula (Norwegian: "Bergenshalvøyen" , ] ) is a peninsula in Hordaland county, Norway.  The city of Bergen, Norway's second largest city, is located on the peninsula.  The peninsula extends out from the mainland and it is surrounded by the following fjords: Samnangerfjorden, Bjørnafjorden, Fusafjorden, Raunefjorden, Byfjorden, Salhusfjorden, Sørfjorden.  The peninsula is connected to the rest of mainland Norway by a narrow, 6.5 km wide strip of land between the villages of Trengereid and Årland.  The 465 km2 municipality of Bergen, the 140 km2 municipality of Os, and about 50 km2 of the municipality of Samnanger are all located on the peninsula.  The highest point is the 987 m tall mountain Gullfjellet.

Ferrer Colony and Ferrer Modern School: The Ferrer Colony and the associated Ferrer Modern School was an anarchist intentional community.  It was founded in 1911 in Manhattan in New York City and in 1915 it moved to Piscataway, New Jersey.  It lasted for more than 40 years before disbanding in 1953.

2016 Rutgers Scarlet Knights football team: The 2016 Rutgers Scarlet Knights football team represented Rutgers University in the 2016 NCAA Division I FBS football season.  It was the Scarlet Knights' third season as a member of the Big Ten Conference, and a member of the East Division.  The team was led by Chris Ash, who is in his first season.  Rutgers played its home games at High Point Solutions Stadium in Piscataway, New Jersey.  They finished the season 2–10, 0–9 in Big Ten play to finish in last place in the East Division.

17th Legislative District (New Jersey): New Jersey's 17th Legislative District is one of 40 in the New Jersey Legislature.  As of the 2011 apportionment, the district includes the Middlesex County municipalities of Milltown Borough, New Brunswick City, North Brunswick Township, Piscataway Township, along with the Somerset County municipality of Franklin Township.

Kitsap Peninsula: The Kitsap Peninsula lies west of Seattle across Puget Sound, in Washington state in the northwestern US.  Hood Canal separates the peninsula from the Olympic Peninsula on its west side.  The peninsula, a.k.a. "the Kitsap", encompasses all of Kitsap County except Bainbridge and Blake Islands, as well as the northeastern part of Mason County and the northwestern part of Pierce County.  The highest point on the Kitsap Peninsula is Gold Mountain.  The U.S. Navy's Puget Sound Naval Shipyard, and Naval Base Kitsap (comprising the former NSB Bangor and NS Bremerton) are on the Peninsula.  Its main city is Bremerton.

Question: Piscataway is a city in which peninsula?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city in question."
    },
    "peninsula_name": {
      "type": "string",
      "description": "The name of the peninsula where the city is located."
    },
    "state_name": {
      "type": "string",
      "description": "The name of the state where the city and peninsula are located."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "country": {
          "type": "string",
          "description": "The country where the peninsula is located."
        },
        "regions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Geographical regions the peninsula is part of."
        }
      },
      "required": [
        "country",
        "regions"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "city_name",
    "peninsula_name",
    "state_name",
    "location_details"
  ],
  "additionalProperties": false
}
