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
St. George's Harbour, Bermuda: St. George's Harbour is a natural harbour in the north of Bermuda.  It serves as the port for the town of St. George's, located on St. George's Island, to its north.  To its south is St. David's Island.  The harbour and both islands lie within St. George's Parish.  It was for two centuries the primary harbour of the British Overseas Territory.

St. George Island State Park: St. George Island State Park (also known as the Dr. Julian G. Bruce St. George Island State Park) is a Florida State Park located on the east end of St. George Island, approximately 10 miles southeast of Eastpoint, in northwestern Florida.  Access to the park is off U.S. 98, by way of a 4-mile-long bridge.  The address is 1900 E. Gulf Beach Drive.

İstanbul Archaeology Museums: The Istanbul Archaeology Museums (Turkish: "" ) is a group of three archeological museums located in the Eminönü district of Istanbul, Turkey, near Gülhane Park and Topkapı Palace.

KMYU: KMYU, virtual channel 12 (VHF digital channel 9), is a primary MyNetworkTV-affiliated television station located in St. George, Utah, United States.  The station is owned by Sinclair Broadcast Group, as part of a triopoly with Salt Lake City-based CBS affiliate KUTV (channel 2) and independent station KJZZ-TV (channel 14).  KMYU and KUTV share studio facilities located on South Main Street in downtown Salt Lake City, and KMYU's transmitter is located atop Webb Hill 2.25 mile south of downtown St. George.  For official FCC purposes regarding a studio location in its city of license, KMYU has their studios in the J.C. Snow Building on East St. George Boulevard in downtown St. George, which also serves as KUTV's southern Utah news bureau.

St. George's University School of Medicine: St. George's University School of Medicine is the medical school of St. George's University located at St. George's.  The school is the oldest private medical school in the Caribbean and founded by Charles R. Modica on July 23, 1976.  In 1983, the United States invaded Grenada after a military coup ousted government leaders and led to the evacuation of St. George’s medical students, many of who were U.S. citizens.  As one of the largest medical schools in the Caribbean, the school placed more doctors into first-year US residency positions than any other medical school in the world between 2011 and 2012.  It was rated by The Princeton Review as one of the "Best 168 Medical Schools"

Tiled Kiosk: The Tiled Kiosk (Turkish: "Çinili Köşk" ) is a pavilion set within the outer walls of Topkapı Palace and dates from 1472 as shown on the tile inscript above the main entrance.  It was built by the Ottoman sultan Mehmed II as a pleasure palace or kiosk.  It is located in the most outer parts of the palace, next to Gülhane Park.  It was also called " Glazed Kiosk" ("Sırça Köşk").

İstanbul Sirkeci Terminal: Istanbul Sirkeci Terminal, also known as Istanbul Terminal (Turkish: "Sirkeci Garı" ), is a railway terminal in Istanbul.  The terminal is located on the tip of Istanbul's historic peninsula right next to the Golden Horn and just northwest of Gülhane Park and the famous Topkapı Palace.  Sirkeci Terminal, along with Haydarpaşa Terminal on the other side of the Bosphorus, are Istanbul's two intercity and commuter railway terminals.  Built in 1890 by the Oriental Railway as the eastern terminus of the world-famous Orient Express, Sirkeci Terminal has become a symbol of the city.  As of 19 March 2013 service to the station had been indefinitely suspended due to the rehabilitation of the existing line between Kazlıçeşme and Halkalı for the new Marmaray commuter rail line.  On 29 October 2013, a new underground station opened to the public and is currently serviced by Marmaray trains travelling across the Bosphorus.  Sirkeci Terminal has a total of 4 platforms (3 above, 1 underground) with 7 tracks (5 above, 2 underground).  Formerly, commuter trains to Halkalı would depart from tracks 2, 3 and 4 while regional trains to Kapıkule, Edirne and Uzunköprü along with international trains to Bucharest, Sofia and Belgrade would depart from tracks 1 and 5.

Utah State Route 34: State Route 34 (SR-34) is a short state highway in the city of St. George in southwestern Utah that connects Bluff Street (SR-18) to River Road while providing a connection to I-15.  The route runs two miles (more than three kilometers) through St. George on St. George Boulevard.  SR-34 was a portion of US-91 when it passed through the city, and serves as the northern part of the St. George Business Loop for I-15; Bluff St. (SR-18) from Interstate 15's Exit 6 to St. George Blvd. serves as the southern half.

Church of St. George of Samatya: Saint George of Samatya or Surp Kevork (Armenian: "Սամաթիոյ Սուրբ Գէորգ Եկեղեցի"; Turkish name: "Sulu Manastır", meaning: "Water Monastery") is an Armenian church in Istanbul.

Gülhane Park: Gülhane Park (Turkish: "Gülhane Parkı" , "Rosehouse Park"; from Persian: "Gulkhāna", "house of flowers") is a historical urban park in the Eminönü district of Istanbul, Turkey; it is located adjacent to and on the grounds of the Topkapı Palace.  The south entrance of the park sports one of the larger gates of the palace.  It is the oldest and one of the most expansive public parks in Istanbul.

Question: Church of St. George of Samatya and Gülhane Park, are located in which mutual city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The mutual city where both entities are located."
    },
    "entities_found": {
      "type": "array",
      "description": "Details about each entity and its location as found in the context.",
      "items": {
        "type": "object",
        "properties": {
          "entity_name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "location_description": {
            "type": "string",
            "description": "The specific location description for the entity from the context."
          }
        },
        "required": [
          "entity_name",
          "location_description"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of how the mutual city was identified."
    }
  },
  "required": [
    "city_name",
    "entities_found",
    "reasoning"
  ],
  "additionalProperties": false
}
