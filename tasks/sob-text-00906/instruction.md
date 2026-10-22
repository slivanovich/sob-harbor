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
Mylau: Mylau is a town and a former municipality in the Vogtlandkreis district, in the Free State of Saxony, Germany with about 2600 citizens.  Since 1 January 2016 it is part of the town Reichenbach im Vogtland.  It is situated in the valleys of the river Göltzsch and the Raumbach, a stream flowing from Reichenbach im Vogtland that is locally known as the Soap Stream (German: "Seifenbach") because of the textile painting factories that had been built by its banks.  The town lies 6 km southeast of Greiz, and 20 km southwest of Zwickau.  Mylau has the smallest area of any town ("Stadt") in what was formerly East Germany, although there are 10 towns in what was formerly West Germany that are even smaller in area.

Köstritzer: The Köstritzer brewery, founded in 1543, is one of the oldest producers of Schwarzbier (black lager) in Germany.  It is located in Bad Köstritz, which is close to Gera in Thuringia.

Bad Köstritz: Bad Köstritz is a town in the district of Greiz, in Thuringia, Germany.  It is situated on the White Elster river, 7 km northwest of Gera.  Bad Köstritz is known for the Köstritzer brewery and its Schwarzbier (black beer).

Vogtlandkreis: The Vogtlandkreis (] ) is a "Landkreis" (rural district) in the southwest of the Free State of Saxony, Germany, at the borders to Thuringia, Bavaria, and the Czech Republic.  Neighboring districts are (from south clockwise) Hof, Saale-Orla, Greiz, Zwickau and Erzgebirgskreis.  Plauen is the administrative center of the district.

Vogtländisches Oberland: Vogtländisches Oberland is a former municipality in the district of Greiz, in Thuringia, Germany.  It was disbanded on 31 December 2012.  The villages Cossengrün, Hohndorf and Schönbach became part of the town Greiz, the villages Arnsgrün, Bernsgrün and Pöllwitz became part of the town Zeulenroda-Triebes.  Its population was 2,851 (2011), and its area was 71.62 km.

Saale-Holzland-Kreis: Saale-Holzland (official German name: Saale-Holzland-Kreis) is a "Kreis" (district) in the east of Thuringia, Germany.  Neighboring districts are (from the north clockwise) the district Burgenlandkreis in Saxony-Anhalt, the district-free city Gera, the districts Greiz, Saale-Orla, Saalfeld-Rudolstadt, Weimarer Land and the district-free city Jena.

Altenburger Land: Altenburger Land is a district in Thuringia, Germany.  It is bounded by (from the west and clockwise) the district of Greiz, the Burgenlandkreis (Saxony-Anhalt), and the districts Leipziger Land, Mittweida, Chemnitzer Land, Zwickauer Land in Saxony.

Zwickauer Land: Zwickauer Land is a former Kreis (district) in the south-west of the Free State of Saxony, Germany.  Neighboring districts were (from north-east clockwise) Chemnitzer Land, Stollberg, Aue-Schwarzenberg, Vogtlandkreis, and the districts Greiz and Altenburger Land in Thuringia.  The district-free city of Zwickau was located in the center of the district and nearly completely surrounded by it.

Weißendorf: Weißendorf is a municipality in the district of Greiz, in Thuringia, Germany.  Hitler once said a speech in this district.

Hohenleuben: Hohenleuben is a town in the district of Greiz, in Thuringia, Germany.  It is situated 12 km northwest of Greiz, and 19 km south of Gera.

Question: What brewery, founded in 1543, is located in the district of Greiz in Germany?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "brewery_name": {
      "type": "string",
      "description": "The name of the brewery."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the brewery was founded."
    },
    "location": {
      "type": "object",
      "properties": {
        "town": {
          "type": "string",
          "description": "The town where the brewery is located."
        },
        "district": {
          "type": "string",
          "description": "The district where the brewery is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the brewery is located."
        }
      },
      "required": [
        "town",
        "district",
        "state"
      ],
      "additionalProperties": false
    },
    "product_type": {
      "type": "string",
      "description": "The type of beer the brewery is known for."
    }
  },
  "required": [
    "brewery_name",
    "founding_year",
    "location",
    "product_type"
  ],
  "additionalProperties": false
}
