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
Ports (comarca): Ports (] ) is a comarca in the province of Castellón, Valencian Community, Spain.  It mostly overlaps the historical comarca known as Ports de Morella (Spanish: "Los Puertos de Morella" ), except for the municipal areas surrounding Catí and Vilafranca that were excluded from the present-day Ports comarca.

A Pobra do Brollón: A Pobra do Brollón is a municipality in the Spanish province of Lugo in Galicia.  It belongs to the comarca named Terra de Lemos.  It has a population of 2,066 (Spanish 2010 Census) and an area of 175 km.

Maestrazgo, Aragon: Maestrazgo (Aragonese: "Mayestrato" ) is a comarca in southeastern Aragon, Spain.  Its names derives from the Maestrat/Maestrazgo mountain massif that extends to the east to the Comarques of the Valencian Community Alt Maestrat and Baix Maestrat.  The most important town is Cantavieja.  It is bordered by the Aragonese comarcas of Andorra-Sierra de Arcos, Cuencas Mineras, Comunidad de Teruel and Bajo Aragón, in the north and in the west and Gúdar-Javalambre in the south, as well as with the Castellón Province (Ports (comarca), Alt Maestrat Alcalatén) in the east.  Some municipal terms of this comarca are part of the historical region of Lower Aragon.

Bread: Bread is a staple food prepared from a dough of flour and water, usually by baking.  Throughout recorded history it has been popular around the world and is one of the oldest artificial foods, having been of importance since the dawn of agriculture.

Tierra del Pan: Tierra del Pan (Land of Bread) is a "comarca" located in the center of the province of Zamora, western Spain.  It belongs to the Autonomous Community of Castile and León.  The city of Zamora, capital of the province, is included in this comarca.

La Siberia: La Siberia is a comarca in the northeastern portion of the  province of Badajoz in the autonomous community of Extremadura, Spain.  Its capital is the municipality of Herrera del Duque.  The comarca is bordered on the north by the provinces of Cáceres and Toledo, on the west by Las Vegas Altas comarca, on the south by La Serena comarca, and on the east by the province of Ciudad Real.  The district contains 18 municipalities with a combined area of 2943 km2 and a population of 29,214 people.

Odra-Pisuerga: Odra-Pisuerga is a "comarca" (county, but without administrative roles) located in the west of the province of Burgos, in the autonomous community of Castile and León, Spain.  It is bounded by the west and south-west by the province of Palencia, south-east by the Arlanza comarca, west by the Alfoz de Burgos and north by the Páramos comarca.

Comarca del Ebro: The Comarca del Ebro is a comarca of the Province of Burgos in the autonomous community of Castile and León, Spain.  It is located in the northeast of the province, and is divided from northwest to southeast by the River Ebro.  The Obarenes Mountains separate the comarca from the Meseta Central to the west.  Its capital is Miranda de Ebro, and its population is roughly 58,000 in the 2000s.

Sierra de la Demanda (comarca): Sierra de la Demanda is a "comarca" located south-east of the province of Burgos in the autonomous community of Castile and León, Spain.  It is bounded on the north-east by the Montes de Oca comarca, north-west by the Alfoz de Burgos, south-east by the province of Soria, south-west by the Ribera del Duero comarca, on the east by the province of La Rioja and west by the Arlanza "comarca".  It is named after the mountain sub-range of Sierra de la Demanda, the northwesternmost end of the Sistema Ibérico.

List of bread dishes: This is a list of bread dishes and foods, which use bread as a primary ingredient.  Bread is a staple food prepared from a dough of flour and water, usually by baking.  Throughout recorded history it has been popular around the world and is one of the oldest artificial foods, having been of importance since the dawn of agriculture.

Question: What community in Spain owns a comarca named for one of the oldest artificial foods?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "autonomous_community": {
      "type": "string",
      "description": "The autonomous community in Spain that owns the comarca."
    },
    "comarca_name": {
      "type": "string",
      "description": "The name of the comarca."
    },
    "food_name": {
      "type": "string",
      "description": "The name of the food after which the comarca is named."
    },
    "food_description_keywords": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Keywords describing the historical significance of the food."
    }
  },
  "required": [
    "autonomous_community",
    "comarca_name",
    "food_name",
    "food_description_keywords"
  ],
  "additionalProperties": false
}
