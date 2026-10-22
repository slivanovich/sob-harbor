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
Journal Square–33rd Street (via Hoboken): Journal Square–33rd Street via Hoboken (JSQ-33 via HOB) is a rapid transit service operated by the Port Authority Trans-Hudson (PATH) railroad.  It is colored yellow and blue on the PATH service map, and trains on this service display both yellow and blue marker lights.  This service operates from Journal Square in Jersey City, New Jersey by way of the Uptown Hudson Tubes to 33rd Street in Midtown Manhattan, New York, with trains reversing direction mid-route at Hoboken Terminal.  The 6.7 mi trip takes 26 minutes to complete.

Grove Street station (PATH): Grove Street (originally Grove-Henderson Streets) is a station on the PATH system.  Located at the intersection of Grove Street, Newark Avenue and Railroad Avenue in the Downtown neighborhood of Jersey City, New Jersey, it is served by the Newark–World Trade Center line at all times, the Journal Square–33rd Street line on weekdays, and the Journal Square–33rd Street (via Hoboken) line on weekends.

23rd Street station (PATH): 23rd Street is a station on the PATH system.  Located at the intersection of 23rd Street and Sixth Avenue in the Chelsea neighborhood of Manhattan, New York City, it is served by the Hoboken–33rd Street and Journal Square–33rd Street lines on weekdays, and by the Journal Square–33rd Street (via Hoboken) line on weekends.

Newark–World Trade Center: The Newark–World Trade Center is a rapid transit service operated by the Port Authority Trans-Hudson (PATH).  It is colored red on the PATH service map and trains on this service display red marker lights.  This service operates from Pennsylvania Station in Newark, New Jersey, by way of the Downtown Hudson Tubes to the World Trade Center in Lower Manhattan, New York.  Operating 24 hours a day, the 8.9 mi trip takes 22 minutes to complete.

Hoboken Terminal: Hoboken Terminal is one of the New York metropolitan area's major transportation hubs.  The commuter-oriented intermodal facility is in Hoboken, Hudson County, New Jersey, United States.  It is served by nine NJ Transit (NJT) commuter rail lines, one Metro-North Railroad line, various NJT buses and private bus lines, the Hudson–Bergen Light Rail, the Port Authority Trans Hudson (PATH) rapid transit system, and NY Waterway-operated ferries.  More than 50,000 people use the terminal daily, making it New Jersey's second-busiest railroad station and its third-busiest transportation facility, after Newark Liberty International Airport and Newark's Penn station.  Hoboken Terminal is wheelchair accessible, with high-level platforms for light rail and PATH services and portable lifts for commuter rail services.

Journal Square–33rd Street: Journal Square–33rd Street is a rapid transit service operated by the Port Authority Trans-Hudson (PATH).  It is colored yellow on the PATH service map and trains on this service display yellow marker lights.  This service operates from Journal Square in Jersey City, New Jersey by way of the Uptown Hudson Tubes to 33rd Street in Midtown Manhattan, New York.  The 5.7 mi trip takes 22 minutes to complete.

Hoboken–33rd Street: Hoboken–33rd Street is a rapid transit service operated by the Port Authority Trans-Hudson (PATH).  It is colored blue on the PATH service map and trains on this service display blue marker lights.  This service operates from the Hoboken Terminal in Hoboken, New Jersey by way of the Uptown Hudson Tubes to 33rd Street in Midtown Manhattan, New York.  The 3.5 mi trip takes 14 minutes to complete.

33rd Street station (PATH): 33rd Street is a terminal station on the PATH system.  Located at the intersection of 32nd Street and Sixth Avenue in the Herald Square neighborhood of Manhattan, New York City, it is served by the Hoboken–33rd Street and Journal Square–33rd Street lines on weekdays, and by the Journal Square–33rd Street (via Hoboken) line on weekends.  33rd Street serves as the northern terminus of all three lines.

Hoboken–World Trade Center: The Hoboken–World Trade Center is a rapid transit service operated by the Port Authority Trans-Hudson (PATH).  It is colored green on the PATH service map and trains on this service display green marker lights.  This service operates from the Hoboken Terminal in Hoboken, New Jersey, by way of the Downtown Hudson Tubes to the World Trade Center in Lower Manhattan, New York.  The 3 mi trip takes 11 minutes to complete, and is the shortest route in the PATH system.

PATH (rail system): Port Authority Trans-Hudson, abbreviated PATH, is a rapid transit system serving Newark, Harrison, Hoboken, and Jersey City in metropolitan northern New Jersey, as well as lower and midtown Manhattan in New York City.  The PATH is operated by, and named after, the Port Authority of New York and New Jersey.  PATH trains run 24 hours a day and 7 days a week.

Question: 33rd Street is a terminal station on the PATH system, Port Authority Trans-Hudson, abbreviated PATH, is a rapid transit system serving Newark, Harrison, Hoboken, and Jersey City in metropolitan northern New Jersey, as well as lower and midtown Manhattan in New York City, and named after what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "station_name": {
      "type": "string",
      "description": "The name of the station mentioned in the question."
    },
    "system_full_name": {
      "type": "string",
      "description": "The full name of the rapid transit system."
    },
    "system_abbreviation": {
      "type": "string",
      "description": "The abbreviation for the rapid transit system."
    },
    "system_type": {
      "type": "string",
      "description": "The type of transportation system."
    },
    "named_after_entity": {
      "type": "string",
      "description": "The entity after which the system is named."
    },
    "service_areas": {
      "type": "array",
      "description": "A list of cities or regions served by the system.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "station_name",
    "system_full_name",
    "system_abbreviation",
    "system_type",
    "named_after_entity",
    "service_areas"
  ],
  "additionalProperties": false
}
