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
Bolshaya Lyampa: Bolshaya Lyampa (Russian: Большая Лямпа ) is a river in Perm Krai, Russia, a right tributary of Uls River which in turn is a tributary of Vishera River.  The river is 34 km long.  Its source is near the border with Sverdlovsk Oblast.  It flows into the Uls River 55 km from the larger river's mouth.  The Bolshaya Lyampa's main tributary is the Malaya Lyampa River.

Apataki: Apataki is a coral atoll in the South Pacific Ocean, territorially part of French Polynesia.  It is one of the Palliser Islands, a subgroup of the Tuamotu Archipelago.  Apataki is located approximately 370 km northeast of the island of Tahiti, 17 km east of Arutua and 24 km northeast of Kaukura.  The island is approximately rectangular; it is 34 km long and 24 km wide.  It has a total area of approximately 706 km with a land area of approximately 21 km² .  Its wide lagoon has two navigable passes to enter it.

Chloris cubensis: Chloris cubensis is a species of grass native to the islands of the Caribbean.  It has been collected in Cuba, Puerto Rico, the Virgin Islands, Jamaica, Antigua, Barbados, and Guadeloupe.  Common name in English is Cuban windmill grass.

Yamzhach River: Yamzhach (Russian: Ямжач ) is a river in Perm Krai, Russia, a left tributary of the Kolva River, which in turn is a tributary of the Vishera River.  The river is 34 km long.  It flows into the Kolva River 380 km from the Kolva's mouth.  The main tributaries are the Passavozh (left) and Zapadnaya (left) rivers.

Barbados: Barbados ( or ) is an island country in the Lesser Antilles, in the Caribbean region of North America.  It is 34 km in length and up to 23 km in width, covering an area of 432 km2 .  It is situated in the western area of the North Atlantic and 100 km east of the Windward Islands and the Caribbean Sea; therein, it is about 168 km east of the islands of Saint Vincent and the Grenadines and 400 km north-east of Trinidad and Tobago.  Barbados is outside of the principal Atlantic hurricane belt.  Its capital and largest city is Bridgetown.

Bransfield Basin: The Bransfield Basin is a back-arc rift basin located off the Northern tip of the Antarctic Peninsula.  The basin lies within a Northeast and Southwest trending strait that separates the peninsula from the nearby South Shetland Islands to the Northwest.  The basin extends for more than 500 km from Smith Island (South Shetland Islands) to a portion of the Hero Fracture Zone.  The basin can be subdivided into three basins: Western, Central, and Eastern.  The Western basin is 130 km long by 70 km wide with a depth of 1.3 km , the Central basin is 230 km long by 60 km wide with a depth of 1.9 km , and the Eastern basin is 150 km long by 40 km wide with a depth of over 2.7 km .  The three basins are separated by the Deception Island and Bridgeman Island.  The moho depth in the region has been seismically interpreted to be roughly 34 km deep.

Bribie Island: Bribie Island is the smallest and most northerly of three major sand islands forming the coastline sheltering the northern part of Moreton Bay, Queensland, Australia.  The others are Moreton Island and North Stradbroke Island.  Bribie Island is 34 km long, and 8 km at its widest.

Massey Island: Massey Island is an uninhabited island in the Bathurst Island group, Qikiqtaaluk Region, Nunavut, Canada.  It is located in the Arctic Ocean, south of Île Vanier (across Pearse Strait) and north of Alexander Island and Île Marc (across Boyer Strait).  It has an area of 432 km2 , 47 km long and 34 km wide.

Lake Bogoria: Lake Bogoria is a saline, alkaline lake that lies in a volcanic region in a half-graben basin south of Lake Baringo, Kenya, a little south of the equator.  Lake Bogoria, like Lake Nakuru, Lake Elmenteita, and Lake Magadi further south in the Rift Valley, and Lake Logipi to the north, is home at times to one of the world's largest populations of lesser flamingos.  The lake is a Ramsar site and Lake Bogoria National Reserve has been a protected National Reserve since November 29, 1973.  Lake Bogoria is shallow (about 10 m depth), and is about 34 km long by 3.5 km wide, with a drainage basin of 700 km.

Zagarolo: Zagarolo is a town and "comune" in the Metropolitan City of Rome, in the region of Lazio of central Italy.  It has 17,803 inhabitants and a total area of 28 km2 .  It lies 34 km south-east of Rome, and it borders the municipalities of Colonna, Gallicano nel Lazio, Monte Compatri, Palestrina, Rome, San Cesareo (former frazione of Zagarolo).  Zagarolo's town center lies on a very narrow tuff hill, 2 km long and about 100 m wide, at an elevation of 310 m , surrounded by green valleys.  The south continuation of the important pilgrim route Via Francigena passes through the countryside of Zagarolo.

Question: What is the capital of the country that is 34km long and Chloris cubensis grows native?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "country_name": {
      "type": "string",
      "description": "The name of the country identified."
    },
    "country_length_km": {
      "type": "integer",
      "description": "The length of the country in kilometers."
    },
    "is_chloris_cubensis_native": {
      "type": "boolean",
      "description": "Indicates whether Chloris cubensis is native to this country."
    },
    "capital_city": {
      "type": "string",
      "description": "The capital city of the identified country."
    }
  },
  "required": [
    "country_name",
    "country_length_km",
    "is_chloris_cubensis_native",
    "capital_city"
  ],
  "additionalProperties": false
}
