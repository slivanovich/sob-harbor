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
Canton of Calais-3: The canton of Calais-3 is an administrative division of the Pas-de-Calais department, in northern France.  It was created at the French canton reorganisation which came into effect in March 2015.  Its seat is in Calais.

Canton of Hénin-Beaumont-1: The canton of Hénin-Beaumont-1 is an administrative division of the Pas-de-Calais department, in northern France.  It was created at the French canton reorganisation which came into effect in March 2015.  Its seat is in Hénin-Beaumont.

Dover: Dover ( ; French: "Douvres" ) is a town and major ferry port in the home county of Kent, in South East England.  It faces France across the strait of Dover, the narrowest part of the English Channel, and lies south-east of Canterbury; east of Kent's county town Maidstone; and north-east along the coastline from Dungeness and Hastings.  The town is the administrative centre of the Dover District and home of the Dover Calais ferry through the Port of Dover.  The surrounding chalk cliffs are known as the White Cliffs of Dover.

Canton of Calais-1: The canton of Calais-1 is an administrative division of the Pas-de-Calais department, in northern France.  It was created at the French canton reorganisation which came into effect in March 2015.  Its seat is in Calais.

Subprefecture: Subprefecture is an administrative division of a country that is below prefecture or province.

Canton of Calais-2: The canton of Calais-2 is an administrative division of the Pas-de-Calais department, in northern France.  It was created at the French canton reorganisation which came into effect in March 2015.  Its seat is in Calais.

Port of Calais: The Port of Calais is a port in Calais, northern France.  The port is the fourth largest port in France and the largest for passenger traffic.  It accounts for more than a third of economic activity in the town of Calais.

Calais: Calais ( , traditionally ; ] ; Picard: "Calés" ; Dutch: "Kales" ) is a town and major ferry port in northern France in the department of Pas-de-Calais, of which it is a sub-prefecture.  Although Calais is by far the largest city in Pas-de-Calais, the department's prefecture is its third-largest city of Arras.  The population of the metropolitan area at the 2010 census was 126,395.  Calais overlooks the Strait of Dover, the narrowest point in the English Channel, which is only 34 km wide here, and is the closest French town to England.  The White Cliffs of Dover can easily be seen on a clear day from Calais.  Calais is a major port for ferries between France and England, and since 1994, the Channel Tunnel has linked nearby Coquelles to Folkestone by rail.

Canton of Hénin-Beaumont-2: The canton of Hénin-Beaumont-2 is an administrative division of the Pas-de-Calais department, in northern France.  It was created at the French canton reorganisation which came into effect in March 2015.  Its seat is in Hénin-Beaumont.

Boulogne-sur-Mer: Boulogne-sur-Mer (] , Latin: "Gesoriacum" or "Bononia", Dutch: "Bonen" ), often called Boulogne ( ), is a city in Northern France.  It is a sub-prefecture of the department of Pas-de-Calais.  Boulogne lies on the Côte d'Opale, a tourist coast on the English Channel, and is the most-visited location in its region after the Lille conurbation.  Boulogne is its department's second-largest city after Calais, and the 60th largest in France.  It is also the country's largest fishing port, specialising in herring.

Question: Calais ( , traditionally ; ] ; Picard: "Calés" ; Dutch: "Kales" ) is a town and major ferry port in northern France in the department of Pas-de-Calais, of which administrative division of a country that is below prefecture or province?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "town_name": {
      "type": "string",
      "description": "The name of the town in question."
    },
    "administrative_division_details": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "description": "The specific type of administrative division."
        },
        "is_below_prefecture_or_province": {
          "type": "boolean",
          "description": "Indicates if this administrative division is below a prefecture or province."
        }
      },
      "required": [
        "type",
        "is_below_prefecture_or_province"
      ],
      "additionalProperties": false
    },
    "division_type_definition": {
      "type": "string",
      "description": "The definition of the administrative division type."
    }
  },
  "required": [
    "town_name",
    "administrative_division_details",
    "division_type_definition"
  ],
  "additionalProperties": false
}
