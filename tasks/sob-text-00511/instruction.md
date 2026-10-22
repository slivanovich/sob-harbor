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
Magadan: Magadan (Russian: Магадан ; ] ) is a port town and the administrative center of Magadan Oblast, Russia, located on the Sea of Okhotsk in Nagayevo Bay in Taui Bay and serving as a gateway to the Kolyma region.  Population:  (2010 Census) ;  (2002 Census) ;  (1989 Census)

Ust-Omchug: Ust-Omchug (Russian: Усть-Омчуг ) is an urban locality (an urban-type settlement) and the administrative center of Tenkinsky District of Magadan Oblast, Russia, located at the 271 km mark of the highway to the northwest of Magadan.  Population:  (2010 Census) ;  (2002 Census) ;  (1989 Census)

Ceduna, South Australia: Ceduna is a town in South Australia located on the shores of Murat Bay on the west coast of Eyre Peninsula.  It lies west of the junction of the Flinders and Eyre Highways around 786 km northwest of the capital Adelaide.  The port town/suburb of Thevenard lies 3 km to the west on Cape Thevenard.  It is in the District Council of Ceduna, the federal Division of Grey, and the state electoral district of Flinders.  The name Ceduna is a corruption of the local Aboriginal Wirangu word "Chedoona" and is said to mean a place to sit down and rest.  The town has played an important but minor role in Australia's overall development due to it being a fishing port and a railway hub.

Larymna: Larymna (Greek: Λάρυμνα ) is a port town in Phthiotis, Greece.  It is situated on the North Euboean Gulf.  Since the 2011 local government reform, it is a part of the municipality Lokroi, of which it is a community.  Larymna took its name from the ancient Boeotian port town Larymna, which was situated at the same place.

El Taref Province: El Taref (Arabic: ولاية الطارف‎ ‎ , Berber: ) is a province ("wilaya") of Algeria.  El Kala is a port town in this province.  El Taref is the capital city.  El Kala, a port town in this province, is home to "El Kala National Park".

D7 motorway (Czech Republic): D7 motorway (Czech: "Dálnice D7" ), formerly Expressway R7 (Czech: "rychlostní silnice R7" ) is a highway northwest from Prague to Chomutov and German border.

Florida State Road 297: Known locally as Pine Forest Road, State Road 297 (SR 297) is a north–south divided highway northwest of Pensacola.  The road serves as a connector between Mobile Highway (US 90/SR 10) and Interstate 10 (SR 8) in the Pensacola metropolitan area.  The road also extends into the northern Pensacola suburbs, where it ends at an intersection with Nine Mile Road (Alt US 90/SR 10).  The road is also the main truck route to Pensacola Naval Air Station.

Port Town-nishi Station: Port Town-nishi Station (ポートタウン西駅 , Pōtotaun-nishi-eki , station number: P12) is a train station on the Nankō Port Town Line (New Tram) in Suminoe-ku, Osaka, Japan.  It literally means "Port Town West".

Kudiramalai: Kudiramalai (Sinhala: කුදිරමලෙයි, Tamil: குதிரைமலை, Greek: Hippuros, English: Horse Mountain) is a cape and ancient port town on the west coast of Sri Lanka.  On the Gulf of Mannar near Silavaturai, the town shares a history with nearby Karaitivu Island, the ancient port town of Mannar and the Ketheeswaram temple.  Kudiramalai is the northernmost point of Puttalam District and was a southern port of Mannar during the classical period, serving the northern kingdoms of the Jaffna Peninsula and Vanni country as one of their southernmost border towns.  It is west of Vanni from Trincomalee (Thiru-Konamalai), home of Koneswaram temple.

Port Town-higashi Station: Port Town-higashi Station (ポートタウン東駅 , Poutotaun-higashi-eki , station number: P13) is a train station on the Nankō Port Town Line (New Tram) in Suminoe-ku, Osaka, Japan.  It literally means "Port Town East".

Question: Ust-Omchug is on the highway northwest of which port town?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "port_town_name": {
      "type": "string",
      "description": "The name of the port town."
    },
    "ust_omchug_location_description": {
      "type": "string",
      "description": "Describes Ust-Omchug's location relative to the port town."
    },
    "highway_details": {
      "type": "object",
      "properties": {
        "distance_from_ust_omchug_km": {
          "type": "integer",
          "description": "The distance in kilometers from Ust-Omchug along the highway."
        },
        "direction_from_port_town": {
          "type": "string",
          "description": "The direction of the highway from the port town towards Ust-Omchug."
        }
      },
      "required": [
        "distance_from_ust_omchug_km",
        "direction_from_port_town"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "port_town_name",
    "ust_omchug_location_description",
    "highway_details"
  ],
  "additionalProperties": false
}
