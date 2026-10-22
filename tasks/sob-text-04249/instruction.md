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
Strasbourg: Strasbourg ( , ] ; Alsatian: "Strossburi"; German: "Straßburg" ] ) is the capital and largest city of the Grand Est region of France and is the official seat of the European Parliament.  Located close to the border with Germany in the historic region of Alsace, it is the capital of the Bas-Rhin département.  In 2014, the city proper had 276,170 inhabitants and both the Eurométropole de Strasbourg (Greater Strasbourg) and the Arrondissement of Strasbourg had 484,157 inhabitants.  Strasbourg's metropolitan area had a population of 773,347 in 2013 (not counting the section across the border in Germany), making it the ninth largest metro area in France and home to 13% of the Grand Est region's inhabitants.  The transnational Eurodistrict Strasbourg-Ortenau had a population of 915,000 inhabitants in 2014.

Fort des Ayvelles: The Fort des Ayvelles, also known as the Fort Dubois-Crancé, is a fortification near the French communes of Villers-Semeuse and Les Ayvelles in the Ardennes, just to the south of Charleville-Mézières.  As part of the Séré de Rivières system of fortifications, the fort was planned as part of a new ring of forts replacing the older citadel of Mézières with dispersed fortifications.  With advances in the range and destructive power of artillery, the city's defensive perimeter had to be pushed away from the city center to the limits of artillery range.  The Fort des Ayvelles was the only such fortification to be completed of the ensemble, as resources were diverted elsewhere.  At the time of its construction the fort controlled the Meuse and the railway line linking Reims, Montmédy, Givet and Hirson.  The Fort des Ayvelles was reduced in status in 1899, its masonry construction rendered obsolete by the advent of high-explosive artillery shells.  However, it was re-manned for the First World War before it was captured by the Germans on 29 August 1914.  The fort was partly destroyed in 1918.  During the Battle of France in 1940 the fort was bombarded.  French resisters were executed at Ayvelles during both world wars.  At present the fort is maintained by a preservation society, and may be visited.

Aincreville: Aincreville is a commune in the Meuse department in the Grand Est region in northeastern France.

Reims: Reims ( ; also spelled Rheims; ] ), a city in the Grand Est region of France, lies 129 km east-northeast of Paris.  The 2013 census recorded 182,592 inhabitants ("Rémoises" (feminine) and "Rémois" (masculine)) in the city of Reims proper (the "commune"), and 317,611 inhabitants in the metropolitan area ("aire urbaine").  Its river, the Vesle, is a tributary of the Aisne.

Amanty: Amanty is a commune in the Meuse department in the Grand Est region in northeastern France.

La Chaussée-sur-Marne: La Chaussée-sur-Marne is a commune in the Marne department in the Grand Est region in north-eastern France.  The town of La Chaussée-sur-Marne is located in the department of Marne of the French region Grand Est.  The town of La Chaussée-sur-Marne is located in the township of Vitry-le-François-Est part of the district of Vitry-le-François.

Charleville-Mézières: Charleville-Mézières (] ) is a commune in northern France, capital of the Ardennes department in the Grand Est region.  Charleville-Mézières is located on the banks of the Meuse River.

Ambly-sur-Meuse: Ambly-sur-Meuse is a commune in the Meuse department in the Grand Est region in northeastern France.

Abaucourt-Hautecourt: Abaucourt-Hautecourt is a French commune in the Meuse department in the Grand Est region of north-eastern France.

Les Ayvelles: Les Ayvelles is a commune in the Ardennes department in the Grand Est region of northern France.

Question: At the time of its construction, Fort des Ayvelles, controlled Meuse and the railway line linking what city in the Grand Est region of France, that lies 129 km east-northeast of Paris?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fortification_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the fortification."
        },
        "controlled_elements": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Elements controlled by the fortification at the time of its construction."
        }
      },
      "required": [
        "name",
        "controlled_elements"
      ],
      "additionalProperties": false
    },
    "linked_city_details": {
      "type": "object",
      "properties": {
        "city_name": {
          "type": "string",
          "description": "The name of the city linked by the railway line."
        },
        "region": {
          "type": "string",
          "description": "The region of France where the city is located."
        },
        "distance_from_paris_km": {
          "type": "integer",
          "description": "The distance of the city from Paris in kilometers."
        },
        "direction_from_paris": {
          "type": "string",
          "description": "The direction of the city from Paris."
        }
      },
      "required": [
        "city_name",
        "region",
        "distance_from_paris_km",
        "direction_from_paris"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the city that is the answer to the question."
    }
  },
  "required": [
    "fortification_details",
    "linked_city_details",
    "final_answer"
  ],
  "additionalProperties": false
}
