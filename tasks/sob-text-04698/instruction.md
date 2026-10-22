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
Wetterspitzen: The Wetterspitzen are three of the rocky peaks on a mountain ridge in the Wetterstein mountains in the central part of the Eastern Alps in Germany.  They lie two kilometres, as the crow flies, southwest of Germany's highest peak, the Zugspitze, on the border between the Austrian province of Tyrol and the German state of Bavaria.  The "Wetterspitzen" form the southwest perimeter of the Zugspitze ledge ("Zugspitzplatt"); below and to the east is the ski region on the Schneeferner with its research station, the Schneefernerhaus.

Hochwanner: At 2744 m , the Hochwanner (formerly: "Kothbachspitze") is the second highest mountain in Germany after the Zugspitze (if the somewhat higher Schneefernerkopf is only considered as a sub-peak of the Zugspitze).  In addition the Hochwanner is the highest peak on the main ridge of the Wetterstein ("Wettersteinhauptkamm") running from "Gatterl" to the Upper Wettersteinspitze ("Oberen Wettersteinspitze") above Mittenwald in an east-west direction.  From the Hochwanner massif there is an all-round view of the Rein valley ("Reintal"), the Leutasch valley in Austria, the Gais valley, the Zugspitze, the Mieming Chain, the Jubiläumsgrat, the Karwendel mountains and far into the central Alps.

Isla Magueyes: Isla Magueyes (Isle of Maguey) is a 7.2 ha island 50 m from the southwest coast of the island of Puerto Rico.  It is encircled with mangrove and has an interior of dry scrub habitat, where it gets its name.  It is named for the presence of many century plants or maguey ("Agave americana").  The surrounding shelf of the island is mostly coral reef.  There are buildings on the western end of the island associated with the Department of Marine Sciences, University of Puerto Rico at Mayagüez.  UPR- Mayagüez is the most important center in the Atlantic region for the study of tropical marine science due to its location, facilities, and first-rate researchers.  The research facilities includes the Puerto Rico Water Resources and Environmental Research Institute, the Caribbean Coral Reef Institute (CCRI), the Research and Development Center, the Agricultural Research Station and the Caribbean Atmospheric Research Center (ATMOSCarib).

Zackenberg Station: Zackenberg (or ZERO - Zackenberg Ecological Research Operations) is an ecosystem research station and monitoring facility situated in the Northeast Greenland National Park in northeastern Greenland.  The station is owned by the Greenland Self-Government and was run by the Danish Polar Center (Dansk Polarcenter) until 2008.  In 2009 the running of the Station was transferred to the Dept of Arctic Environment @ the Danish National Environmental Research Institute

Schneefernerhaus: The Schneefernerhaus is a former hotel in the Alps, that is now used as an environmental research station.  It lies immediately below the summit of the Zugspitze at a height of 2,650 m and was opened on 20 June 1931.  It used to house the top station of the Bavarian Zugspitze Railway as well as a tourist hotel.  There was then a cable car from the Schneefernerhaus to the Zugspitze summit.  In 1938 a gallery for pedestrians was opened from the ridge station of the Tyrolean Zugspitze Cable Car to the Schneefernerhaus.  From 1945 to 1952 the hotel was commandeered for use as a "recreation facility" by the US Forces.

Zugspitze: The Zugspitze, (] ) at 2,962 m (9,718 ft) above sea level, is the highest peak of the Wetterstein Mountains as well as the highest mountain in Germany.  It lies south of the town of Garmisch-Partenkirchen, and the Austria–Germany border runs over its western summit.  South of the mountain is the "Zugspitzplatt", a high karst plateau with numerous caves.  On the flanks of the Zugspitze are three glaciers, including the two largest in Germany: the Northern Schneeferner with an area of 30.7 hectares and the Höllentalferner with an area of 24.7 hectares.  The third is the Southern Schneeferner which covers 8.4 hectares.

Eibsee Cable Car: The Eibsee Cable Car, which opened in 1963, is a cable car which connects the lower station (973 m above sea level) near lake Eibsee with the top station at 2950 m above sea level next to the summit of Zugspitze, Germany's highest mountain on the border to Austria.  The cable car was built to provide a faster access to the Zugspitze from its German side, as the cog railway from Garmisch-Partenkirchen does not go directly to the summit and takes much longer.  The "Eibsee Cable Car" belongs to "Bayerische Zugspitzbahn Bergbahn AG", the company operating the cog railway and most cable cars, gondola lifts and chairlifts in the Garmisch-Partenkirchen area.  It is thus possible to make round trips using both the cog railway and the cable car.  On the Austrian side, there is the Tyrolean Zugspitze Cable Car which starts at Ehrwald and meets the Eibsee Cable Car on the top.

Hydraulics Research Station: The Hydraulics Research Station (HRS) was created by the UK Department of Scientific and Industrial Research in 1947.  The Research Station was based in Wallingford, near Oxford.  It was established to deal with “looser boundary” problems such as coastal erosion, flood protection and the silting and scouring of rivers, estuaries and harbours.  The Hydraulics Research Station was housed at Howbery Park as a government establishment until 1982, when it was privatised from the Department of the Environment (DoE) to become Hydraulics Research Station Limited.  It is now known as HR Wallingford.  During its existence, HRS contributed to advance hydraulics research.  It also worked on water-related projects in the UK and around the world.

Zugspitze Glacier Cable Car: The Zugspitze Glacier Cable Car (German: "Zugspitz-Gletscherbahn" ) is a 1,000 metre long cable car on the Zugspitze, Germany's highest mountain.  It was opened in 1992 and links the plateau of the "Zugspitzplatt" directly with the summit, 360 metres higher.  Since the mountain station of the Bavarian Zugspitze Railway was moved from the Schneefernerhaus to the "Platt", the Schneefernerhaus and the old cableways, which ran down into the valley from the "Platt" (the "Hangbahn" and "alte Gletscherbahn") and up to the summit ("Gipfelseilbahn"), have lost their importance.

Desert Research Institute: Desert Research Institute (DRI) is the nonprofit research campus of the Nevada System of Higher Education (NSHE), the organization that oversees all publicly supported higher education in the U.S. state of Nevada.  At DRI, approximately 500 research faculty and support staff engage in more than $50 million in environmental research each year.  DRI's environmental research programs are divided into three core divisions (Atmospheric Sciences, Earth and Ecosystem Sciences, and Hydrologic Sciences) and two interdisciplinary centers (Center for Arid Lands Environmental Management and the Center for Watersheds and Environmental Sustainability).  Established in 1988 and sponsored by AT&T, the institute's Nevada Medal awards "outstanding achievement in science and engineering".

Question: What is the name of the former hotel in the Alps now used as an environmental research station which lies at the summit of the Zugspitze in Germany?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "station_name": {
      "type": "string",
      "description": "The name of the environmental research station."
    },
    "former_function": {
      "type": "string",
      "description": "The previous primary function of the facility."
    },
    "current_function": {
      "type": "string",
      "description": "The current primary function of the facility."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "mountain_name": {
          "type": "string",
          "description": "The name of the mountain where the station is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the station is located."
        },
        "height_meters": {
          "type": "integer",
          "description": "The height of the station above sea level in meters."
        },
        "proximity_to_summit": {
          "type": "string",
          "description": "Description of the station's location relative to the mountain summit."
        }
      },
      "required": [
        "mountain_name",
        "country",
        "height_meters",
        "proximity_to_summit"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "station_name",
    "former_function",
    "current_function",
    "location_details"
  ],
  "additionalProperties": false
}
