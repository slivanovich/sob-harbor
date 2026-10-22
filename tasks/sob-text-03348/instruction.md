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
Ed Castillo: Edward D. Castillo, of the Luiseño-Cahuilla tribes, is a Native American activist who participated in the American Indian occupation of Alcatraz in 1969.  Current professor and director of Native American Studies at the Sonoma State University in California, he wrote several chapters in the Smithsonian Institution's "Handbook of North American Indians" and in "Mission Indian Federation: Protecting Tribal Sovereignty 1919-1967", published in the "Encyclopedia of Native Americans" in the 20th Century.  He is editor of Native American Perspectives on the Hispanic Colonization of Alta California and The Pomo, A Tribal History.  Castillo is a regular contributor of book reviews to historical journals such as Indian Historian, Journal of California Anthropology, Western Historical Quarterly, American Indian Quarterly and California History.

Sonoma State Historic Park: Sonoma State Historic Park is a California State Park located in the center of Sonoma, California.  The park consists of six sites: the Mission San Francisco Solano, the Sonoma Barracks (sometimes called the Presidio of Sonoma), the Blue Wing Inn, La Casa Grande, Lachryma Montis, and the Toscano Hotel.

Sonoma State University: Sonoma State University (SSU, Sonoma State, and Sonoma) is a public comprehensive university, part of the 23-campus California State University (CSU) system.  The main campus is located east of Rohnert Park, and north of Cotati, California, United States, approximately 10 mi south of Santa Rosa and 50 mi north of San Francisco.  The university is one of the smallest of the 23 CSU campuses in California.  Sonoma State offers 92 Bachelor's degrees, 19 Master's degrees, one Doctoral degree (Doctor of Education), and 11 teaching credentials.

Año Nuevo State Park: Año Nuevo State Park is a state park of California, USA, encompassing Año Nuevo Island and Año Nuevo Point, which are known for their pinniped rookeries.  Located in San Mateo County, the low, rocky, windswept point juts out into the Pacific Ocean about 55 mi south of San Francisco and the Golden Gate.  Año Nuevo State Natural Reserve, formerly a separate unit of the California state park system, was merged into Año Nuevo State Park in October 2008.  The coastal geographic center, or coastal-midpoint of California is located at the Northern end of this park at N 37°09′58″, W 122°21'40", as the absolute geographic center of California falls at N 37°09′58″, W 119°26′58″W.

Conquest of California: The California Campaign (1846–1847), colloquially the Conquest of California or Conquest of Alta California by the United States, was an early military campaign of the Mexican–American War that took place in the western part of Mexico's Alta California Department, in the present-day state of California.  The California Campaign was marked by a series of small battles throughout 1846 and early 1847.

California State Parks Peace Officer: California State Park Peace Officers (S.P.P.O) are fully sworn California State Police Officers, with two sub-classifications, the Ranger and the Lifeguard.  S.P.P.O.s often use the title of State Police Officer during enforcement contact, as many Park Rangers and Lifeguards within municipalities, counties and special districts are not armed Peace Officers, with authority throughout the state, on and off duty, like the California State Park Peace Officers law enforcement officer.  State Park Peace Officers perform a wide variety of general law-enforcement activities, including complex criminal investigations, traffic enforcement, and participate in statewide task forces, for gang suspension, narcotics enforcement, auto theft, and fish and wildlife crimes, under the jurisdiction of the California Department of Parks and Recreation in the state parks of California, United States.  Duties include general law enforcement, aquatic rescue (by lifeguards and other certified officers), search and rescue, emergency medical response, interpretation of natural, historic and cultural resources, resource protection, park management and proactive enforcement patrol.  The current sidearm of the California State Park Peace Officer is the Smith & Wesson M&P, the current patrol rifle is the Colt AR-15 Model LE6920, and the current patrol shotgun is the venerable, Remington Model 870 Police Magnum.

Sonoma Creek: Sonoma Creek is a 33.4 mi stream in northern California.  It is one of two principal drainages of southern Sonoma County, California, with headwaters rising in the rugged hills of Sugarloaf Ridge State Park and discharging to San Pablo Bay, the northern arm of San Francisco Bay.  The watershed drained by Sonoma Creek is roughly equivalent to the wine region of Sonoma Valley, an area of about 170 sqmi .  The State of California has designated the Sonoma Creek watershed as a “Critical Coastal Water Resource”.  To the east of this generally rectangular watershed is the Napa River watershed, and to the west are the Petaluma River and Tolay Creek watersheds.

El Camino Real (California): El Camino Real (Spanish for The Royal Road, also known as The King's Highway), sometimes associated with Calle Real (within the US state of California), usually refers to the 600-mile (965-kilometer) road connecting the 21 Spanish missions in California (formerly Alta California), along with a number of sub-missions, four presidios, and three pueblos, stretching at its southern end from the San Diego area Mission San Diego de Alcalá, all of the way up to the trail's northern terminus at Mission San Francisco Solano in Sonoma, just above San Francisco Bay.

Camilo Ynitia: Camilo Ynitia (alternative spelling "Camillo"; original native name transliterated as "Hueñux") was born in 1803, probably in the Miwok village of Olompali (located just north of present-day Novato, California) where his father had built an adobe brick home.  Camilo was a notable leader of the Coast Miwok, a Native American people.  Camilo was known as the last "Hoipu" (headman) of the Miwok community living at Olompali.  Camilo was also the only Native American on the northern frontier of Alta California to secure and keep a large Mexican-era land grant: In 1843 Governor Manuel Micheltorena of Alta California deeded him the Rancho Olompali, a large tract of land that is between present-day Novato and Petaluma, California.  A part of this land now comprises the Olompali State Historic Park.

Mission San Francisco Solano (California): Mission San Francisco Solano was the 21st, last and northernmost mission in Alta California.  It was the only mission built in Alta California after Mexico gained independence from Spain.  The difficulty of its beginning demonstrates the confusion resulting from that change in governance.  The California Governor wanted a robust Mexican presence on the Pacific coast from moving further inland.  A young Franciscan friar from Mission San Francisco de Asis wanted to move to a location with a better climate and access to a larger number of potential converts.

Question: What was the 21st, last and northernmost mission in Alta California, and is located on a part of a California State Park located in the center of Sonoma, California ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mission_name": {
      "type": "string",
      "description": "The full name of the mission."
    },
    "mission_number": {
      "type": "integer",
      "description": "The numerical order of the mission in Alta California."
    },
    "mission_status": {
      "type": "object",
      "properties": {
        "is_last_mission": {
          "type": "boolean",
          "description": "Indicates if it was the last mission built in Alta California."
        },
        "is_northernmost_mission": {
          "type": "boolean",
          "description": "Indicates if it was the northernmost mission in Alta California."
        }
      },
      "required": [
        "is_last_mission",
        "is_northernmost_mission"
      ],
      "additionalProperties": false
    },
    "located_within_park": {
      "type": "object",
      "properties": {
        "park_name": {
          "type": "string",
          "description": "The name of the state park where the mission is located."
        },
        "park_type": {
          "type": "string",
          "description": "The type of the park, e.g., 'California State Park'."
        },
        "park_city_location": {
          "type": "string",
          "description": "The city where the state park is located."
        }
      },
      "required": [
        "park_name",
        "park_type",
        "park_city_location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "mission_name",
    "mission_number",
    "mission_status",
    "located_within_park"
  ],
  "additionalProperties": false
}
