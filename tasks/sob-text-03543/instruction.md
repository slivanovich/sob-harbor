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
Parukkaikudi: Parukkaikudi is a Village in the Ramanathapuram district of the Indian state of Tamil Nadu.  Parukkaikudi is a small Village/hamlet in Mudukulathur Taluk in Ramanathapuram District of Tamil Nadu State, India.  It comes under Anaiseri Panchayath.  It is located 31 km towards west from District headquarters Ramanathapuram, 3 km from Mudukulathur, and 526 km from the state capital Chennai.

Ramanathapuram: Ramanathapuram (   ), also known as Ramnad, is a city and a municipality in Ramanathapuram district in the Indian state of Tamil Nadu.  It is the administrative headquarters of Ramanathapuram district and the second largest town (by population) in Ramanathapuram district.  s of 2011 census, the town had a population of 61,440. Density of population: 320 people per square kilometer; Literacy Rate: 81.48% - Male: 87.89%, Female: 74.93%; Male Female Ratio: 1000:977. Ramanathapuram is the top producer of chilli pepper in Tamil Nadu.  It is connected to other cities by NH-49.

Virudhunagar district: Virudhunagar District is an administrative district of Tamil Nadu state in southern India.  Virudhunagar is the district headquarters.  Virudhunagar district was formed by the separation of Old Ramanathapuram District on 1987 into Ramanathapuram District, Sivagangai District and the west part as Virudhunagar District.  Virudhunagar District was formerly called Karmavirer Kamarajar District.  As of 2011, Virudhunagar district had a population of 1,942,288 with a sex-ratio of 1,007 females for every 1,000 males.

Paramakudi: Paramakudi is a largest town, in Ramanathapuram district in the Indian state of Tamil Nadu.  The river Vaigai flows through Paramakudi on its way to the Bay of Bengal.  It is the political and revenue headquarters of Ramanathapuram district.

Kangeyam: Kangeyam or Kangayam is a second grade municipality in Kangeyam taluk of Tirupur district in the Indian state of Tamil Nadu.  It is situated on National Highway 67.

Rameswaram: Rameswaram, (also spelt as Ramesvaram, Rameshwaram) is a town and a second grade municipality in the Ramanathapuram district in the South Indian state of Tamil Nadu.  It is located on Pamban Island separated from mainland India by the Pamban channel and is about 40 kilometres from Mannar Island, Sri Lanka.  It is situated in the Gulf of Mannar, at the very tip of the Indian peninsula.  Pamban Island, also known as Rameswaram Island, is connected to mainland India by the Pamban Bridge.  Rameswaram is the terminus of the railway line from Chennai and Madurai.  Together with Varanasi, it is considered to be one of the holiest places in India to Hindus, and part of the Char Dham pilgrimage.

Gurudwara Guru Nanak Dham: Gurudwara Guru Nanak Dham is a gurudwara situated in the town of Rameswaram in Tamil Nadu, India.  The gurudwara was constructed to commemorate the visit of the first Sikh guru, Guru Nanak to Rameswaram in about 1511.  The gurudwarar was visited by the Governor of Tamil Nadu, Surjit Singh Barnala in 2005.  Barnala assured the priests of help in repairing and enlarging the gurudwara.

Ramanathapuram district: Ramanathapuram District is an administrative district of Tamil Nadu state in southern India.  The city of Ramanathapuram is the district headquarters.  Ramanthapuram District has an area of 4123 km.  It is bounded on the north by Sivaganga District, on the northeast by Pudukkottai District, on the east by the Palk Strait, on the south by the Gulf of Mannar, on the west by Thoothukudi District, and on the northwest by Virudhunagar District.  The district contains the Pamban Bridge, an east-west chain of low islands and shallow reefs that extend between India and the island nation of Sri Lanka, and separate the Palk Strait from the Gulf of Mannar.  The Palk Strait is navigable only by shallow-draft vessels.  As of 2011, Ramanathapuram district had a population of 1,353,445 with a sex-ratio of 983 females for every 1,000 males.

Kilakarai: Kilakarai, Kilakkarai or Keelakarai (Tamil: கீழக்கரை ) is a municipality in Ramanathapuram district in the Indian state of Tamil Nadu.  As of 2011, the town had a population of 38,355.  Kilakarai is one of the Taluka in Ramanathapuram District.

Thuraiyur: Thuraiyur is a town and a municipality in Tiruchirappalli district in the Indian state of Tamil Nadu.  It was upgraded to a III Grade Municipality from Town Panchayat on 17 January 1970, and to a II Grade Municipality in May 1998.  It was upgraded to Selection Grade Municipality in the year 2008.  It is also a taluka.

Question: When was the gurudwara situated in a second grade municipality in the Ramanathapuram district in the South Indian state of Tamil Nadu built?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "gurudwara_name": {
      "type": "string",
      "description": "The name of the gurudwara."
    },
    "location": {
      "type": "object",
      "properties": {
        "town_name": {
          "type": "string",
          "description": "The name of the town where the gurudwara is located."
        },
        "municipality_grade": {
          "type": "string",
          "description": "The grade of the municipality."
        },
        "district_name": {
          "type": "string",
          "description": "The name of the district."
        },
        "state_name": {
          "type": "string",
          "description": "The name of the state."
        },
        "country_name": {
          "type": "string",
          "description": "The name of the country."
        }
      },
      "required": [
        "town_name",
        "municipality_grade",
        "district_name",
        "state_name",
        "country_name"
      ],
      "additionalProperties": false
    },
    "construction_year": {
      "type": "integer",
      "description": "The year the gurudwara was constructed."
    },
    "reason_for_construction": {
      "type": "string",
      "description": "The reason or event commemorated by the construction of the gurudwara."
    }
  },
  "required": [
    "gurudwara_name",
    "location",
    "construction_year",
    "reason_for_construction"
  ],
  "additionalProperties": false
}
