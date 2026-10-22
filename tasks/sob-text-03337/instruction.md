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
Tamasheq language: Tamasheq is a variety of the Tuareg languages.  It is spoken by the Tuareg people, principally in the Timbuktu area.  There are two divergent dialects: "Timbuktu" (Tombouctou, Tanaslamt) and "Tadghaq" (Kidal) in Mali.

Thủ Dầu Một: Thủ Dầu Một (  ) is the capital city of Bình Dương Province, Vietnam, located at around .  The city has an area of 118.66 km², population is 244,277 (2012), and is located 20 km north of downtown Hồ Chí Minh City, on the left bank of the Saigon River, upstream from the city.  Although this is an administratively separate city, it is considered as a satellite city of the Ho Chi Minh City Metropolitan Area.

Kandhara: Kandhara is a village in the Dhenkanal district of the Indian state of Orissa, situated on the banks of the Ramial and Dolia rivers.  It is located 20 km northwest of Kamakshyanagar, 55 km north of Dhenkanal, 135 km north of the state capital Bhubaneswar, 100 km west of Jajpur Road, and 65 km east of Talcher.

Timbuktu: Timbuktu (pron.: ), also spelled as Tinbuktu, Timbuctoo and Timbuktoo (Berber: ;French: "Tombouctou" ; Koyra Chiini: "Tumbutu"), is an ancient city in Mali, situated 20 km north of the Niger River.  The town is the capital of the Timbuktu Region, one of the eight administrative regions of Mali.  It had a population of 54,453 in the 2009 census.

Tetserret language: Tetserret (Tin Sert) is a Berber language spoken by the Ait-Awari and Kel Eghlal Tuareg tribes of the Akoubounou ("Akabinu") commune in Niger.  This main speech area is located between Abalak, Akoubounou and Shadwanka.  The variant spoken by the Kel Eghlal is called "taməsəɣlalt".  The Tamasheq equivalent "shin-sart" / "shin-sar" / "tin-sar" is used in some older literature.  Popular understanding among some Ait-Awari derives the name "tet-serret", and its Tamasheq equivalent "shin-sart", from expressions meaning 'the (language) of Sirte'.

Mount Abel (British Columbia): Mount Abel is a mountain on Vancouver Island, British Columbia, Canada, located 20 km east of Woss and 20 km north of Sutton Peak.

Iwellemmedan people: The Iwellemmedan ("Iwəlləmədǎn"), also spelled Iullemmeden, Aulliminden, Ouilliminden, Lullemmeden, and Iwellemmeden, are one of the seven major Tuareg tribal or clan confederations (called ""Drum groups"").  Their communities are historically nomadic and intermixed with other ethnic groups.  The Iwellemmeden inhabit a wide area ranging from east and north central Mali, through the Azawagh valley, into northwestern Niger and south into northern Nigeria.  While once a single confederation of dozens of Tuareg clans, subject peoples, and allied groups, since the 18th century they have been divided into Kel Ataram (west) and Kel Dinnik (east) confederations.  Following colonial rule and independence, the Iwellemmedan homelands cross the Mali/Niger border, and their traditional seasonal migration routes have spread Iwellemmedan communities into Burkina Faso and Nigeria as well.  They speak the Tawellemmet variant of the Tamasheq language, although some current or historical sub-clans speak other Tamasheq variants as well as Songhai languages and Arabic dialects.

Ennore creek: Ennore creek is a backwater located in Ennore, Chennai along the Coromandel Coast of the Bay of Bengal.  It is located in the zone comprising lagoons with salt marshes and backwaters, submerged under water during high tide and forming an arm of the sea with the opening to the Bay of Bengal at the creek.  The zone is spread over an area of 4 km, and the creek covers an area of 2.25 km.  It is located 20 km north of the city centre and 2.6 km south of the Ennore Port, and the creek area stretches 3 km into the sea and 5 km along the coast.  The creek is nearly 400 m wide, elongated in northeast-southwest direction and merging with the backwater bodies.  Once a flourishing mangrove swamp, the creek has been degraded to patches in the fringes mainly due to human activities in the region.  The depth of the creek varies from 1 to 2 m and is shallow near the mouth.  The north–south trending channels of the creek connect it with the Pulicat Lake to the north and to the distributaries of the Kosasthalaiyar River in the south.  The northwestern part of the creek merges with the tidal flats.  The soil in the region is of loamy and alluvial types.  Most of the area consists of tracts of alluvial soil and the eastern region comprises beach dunes, tidal flats and creek.  The creek is oriented from west to east and opens into the Bay of Bengal to the east at Ennore.  The creek acts as an outlet for the excess water from the Poondi Reservoir.  The creek separates the town of Ennore from the Ennore Port located in the north and the Kattupalli Shipyard located further north.  The North Chennai Thermal Power Station is located at the north of the creek and the Ennore Thermal Power Station is located to the south.  The creek is part of the Pulicat water system, including the Pulicat lagoon and the Buckingham Canal.  As per the 1991 Coastal Regulation Zone notification, the entire Pulicat water system is designated CRZ I.  The creek is experiencing siltation due to emergence of the Ennore Port.

Rycroft, Alberta: Rycroft is a village in northern Alberta, Canada.  It is located 68 km north of the city of Grande Prairie and 7 km east of Spirit River.  Dunvegan Provincial Park is located 20 km north of the community.

New England National Park: The New England National Park is a protected national park located on the Northern Tablelands in the New England region of New South Wales, Australia.  The 67303 ha park was created in May 1935 and is situated approximately 560 km north of Sydney, and 10 km south of Waterfall Way, just 85 km east of Armidale and 65 km west of Coffs Harbour.  The closest village to New England National Park is Ebor, located 20 km away.

Question: The Tamasheq language is spoken principally in an area located 20 km north of what river?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "language_name": {
      "type": "string",
      "description": "The name of the language."
    },
    "principal_speaking_area": {
      "type": "string",
      "description": "The main area where the language is spoken."
    },
    "location_relative_to_river": {
      "type": "object",
      "properties": {
        "distance_km": {
          "type": "integer",
          "description": "The distance from the river in kilometers."
        },
        "direction": {
          "type": "string",
          "description": "The cardinal direction relative to the river."
        },
        "river_name": {
          "type": "string",
          "description": "The name of the river."
        }
      },
      "required": [
        "distance_km",
        "direction",
        "river_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "language_name",
    "principal_speaking_area",
    "location_relative_to_river"
  ],
  "additionalProperties": false
}
