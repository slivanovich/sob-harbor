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
Święty Krzyż TV Tower: Święty Krzyż TV Tower ( Polish: RTCN Święty Krzyż ) is the tallest free-standing TV tower in Poland.  (Taller architectural structures in Poland are guyed masts or highrise buildings and chimneys equipped with antennas).  Święty Krzyż TV Tower, which was built in 1966, is a 157 metre tall concrete TV tower situated near the monastery on Łysa Góra.  Święty Krzyż TV Tower is not accessible by tourists.  The hyperbolic-shaped basement floors resemble those of the Ochsenkopf TV Tower in Germany.

Miskolc-Avas TV Tower: Miskolc-Avas TV Tower (in colloquial speech "Avasi kilátó," Avas Lookout Tower) is a 72 metre tall TV tower with an observation deck on the Avas hill in Miskolc, Hungary.  The Avas TV Tower was designed by Miklós Hófer and György Vörös, and was built in 1966 in place of a wooden lookout tower.  It is commonly regarded as the symbol of the city, even though in the 1990s the bell tower of the Avas church was declared the city's symbol in its place.

Pitampura TV Tower: Pitampura TV Tower is a 235 m -tall television tower, built in 1988, with an observation deck that is located in the northwest of New Delhi, India.  It is the 15th tallest structure in India, and the tallest structure in Delhi.  Dilli Haat Pitampura is also situated near the TV tower.  The Tower was dedicated to the Nation as Dr. B. R. Ambedkar TV Tower 10 April 1992 by the Hon’ble Sh.  Ajeet Kumar Panja Minister for The State of Information & Broadcasting.

Borisova Gradina TV Tower: The Borisova Gradina TV Tower or the Old TV Tower is a 106-metre tall (including the aerial) TV tower in the garden Borisova Gradina in Sofia, the capital of Bulgaria.  It is known as the tower used for the first Bulgarian National Television broadcasts in 1959.

Rousse TV Tower: The Rousse TV Tower is a 204-metre-high TV tower built of reinforced concrete at Rousse, Bulgaria.  Originally, the structure was constructed as a 206-metre-high TV tower with a cafe/restaurant on top and was the tallest one on the Balkan peninsula until 2001.  In the 1990s an additional antenna was added bringing the height to 210 metres.  And, in March 2007, the antenna was reconstructed bringing its height to 204 metres.

Kherson TV Tower: Kherson TV Tower (Ukrainian: Херсонська телевежа "Kherson TV Tower") is a 200 m tall space framed Ukrainian truss communications tower that is made of steel.  The building is uniquely built, having been built by using the cross bracing system.  The tower is a truss TV tower, specifically, a Vierendeel truss tower, wherein a structure's members are not triangulated but form rectangular openings instead (see Vierendeel Truss).  The tower has an antenna that measures 199.95 m and a roof that measures 189.89 m .  The tower, possessing a total height of 200 m , is also considered the tallest structure in the whole oblast (province) of Kherson'ka.

Tortoise Mountain TV Tower: Tortoise Mountain TV Tower () is a 311.4 m high TV Tower at Wuhan, People's Republic of China.  It is a concrete tower equipped with an observation deck in a height of 210 m .  It does not stand directly upon the hill, which is occupied by an ancient temple complex (Qing Chuan Ge (晴川閣) from the Three Kingdoms, Song, and Ming Dynasties).  Guishan TV Tower is China's first self-developed TV tower, opened in 1986.

Yıldız: Yıldız (literally "a star" in Turkish) is a neighbourhood located in the Beşiktaş district of Istanbul, Turkey.  The neighbourhood comprises some of Istanbul's well-known historical locations, such as Yıldız Park and Yıldız Palace, the second largest palace in Istanbul.  Yıldız has a population of approximately 6,000.

Yıldız Park: Yıldız Park (Turkish: "Yıldız Parkı" ) is a historical, urban park in Beşiktaş district of Istanbul, Turkey.  It is one of the largest public parks in Istanbul.  The park is located in Yıldız quarter between the palaces of Yıldız and Çırağan.

Endem TV Tower: Endem TV Tower is a TV tower in Beylikdüzü, Istanbul, Turkey.  It was built between 1998 and 2002, and has a now closed revolving restaurant 154 m above ground, as well as an observation deck at 160 m .  The total height of the tower si 257 m including the antenna.

Question: Yıldız Park and Endem TV Tower, are located in which district?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the entities for which the location is being queried."
    },
    "location_type": {
      "type": "string",
      "description": "The type of geographical location being asked for (e.g., district, city, country)."
    },
    "districts": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The districts where the specified entities are located."
    }
  },
  "required": [
    "entity_names",
    "location_type",
    "districts"
  ],
  "additionalProperties": false
}
