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
Zawiszyn, Masovian Voivodeship: Zawiszyn is a village in the administrative district of Gmina Jadów, within Wołomin County, Masovian Voivodeship, in east-central Poland.  It lies approximately 6 km north-east of Jadów, 35 km north-east of Wołomin, and 57 km north-east of Warsaw.

Krusze, Masovian Voivodeship: Krusze is a village in the administrative district of Gmina Klembów, within Wołomin County, Masovian Voivodeship, in east-central Poland.  It lies approximately 6 km north-east of Klembów, 13 km north-east of Wołomin, and 35 km north-east of Warsaw.

Mokra Wieś, Masovian Voivodeship: Mokra Wieś is a village in the administrative district of Gmina Tłuszcz, within Wołomin County, Masovian Voivodeship, in east-central Poland.  It lies approximately 6 km north-east of Tłuszcz, 23 km north-east of Wołomin, and 44 km north-east of Warsaw.

South Channel Fort: South Channel Fort, also known as South Channel Island, is a 0.7 ha artificial island in southern Port Phillip, Victoria, Australia, 6 km north-east of the town of Sorrento.  It was part of a network of fortifications protecting the narrow entrance to Port Phillip.

Leśniaki, Będzin County: Leśniaki is a village in the administrative district of Gmina Siewierz, within Będzin County, Silesian Voivodeship, in southern Poland.  It lies approximately 6 km north-east of Siewierz, 24 km north-east of Będzin, and 36 km north-east of the regional capital Katowice.

Derkacze: Derkacze (German: "Dicking" ) is a village in the administrative district of Gmina Dobiegniew, within Strzelce-Drezdenko County, Lubusz Voivodeship, in western Poland.  It lies approximately 6 km north-east of Dobiegniew, 24 km north-east of Strzelce Krajeńskie, and 49 km north-east of Gorzów Wielkopolski.

Sorrento, Victoria: Sorrento is a township in Victoria, Australia, located on the shores of Port Phillip on the Mornington Peninsula, about one and a half hours by car south of Melbourne.  It is a largely upper-class, seaside resort area, but is also a quiet seaside township in the off-peak months of the year.  It was named by the Italian founders after the southern Italian town.

Hucisko, Zawiercie County: Hucisko is a village in the administrative district of Gmina Włodowice, within Zawiercie County, Silesian Voivodeship, in southern Poland.  It lies approximately 6 km north-east of Włodowice, 12 km north-east of Zawiercie, and 52 km north-east of the regional capital Katowice.

Białe Błota, Świecie County: Białe Błota is a village in the administrative district of Gmina Jeżewo, within Świecie County, Kuyavian-Pomeranian Voivodeship, in north-central Poland.  It lies approximately 6 km north-east of Jeżewo, 16 km north-east of Świecie, 56 km north of Toruń, and 60 km north-east of Bydgoszcz.

Starowola, Wołomin County: Starowola is a village in the administrative district of Gmina Jadów, within Wołomin County, Masovian Voivodeship, in east-central Poland.  It lies approximately 6 km north-east of Jadów, 36 km north-east of Wołomin, and 58 km north-east of Warsaw.

Question: South Channel Fort is located 6 km north-east of a town on the shores of what port?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fort_name": {
      "type": "string",
      "description": "The name of the fort."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "distance_from_town_km": {
          "type": "number",
          "description": "The distance from the specified town in kilometers."
        },
        "direction_from_town": {
          "type": "string",
          "description": "The cardinal direction from the specified town."
        },
        "town_name": {
          "type": "string",
          "description": "The name of the town the fort is located relative to."
        },
        "port_name": {
          "type": "string",
          "description": "The name of the port associated with the town."
        }
      },
      "required": [
        "distance_from_town_km",
        "direction_from_town",
        "town_name",
        "port_name"
      ],
      "additionalProperties": false
    },
    "port_location_description": {
      "type": "string",
      "description": "A description of the port's location or context."
    }
  },
  "required": [
    "fort_name",
    "location_details",
    "port_location_description"
  ],
  "additionalProperties": false
}
