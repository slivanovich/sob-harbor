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
Leonding: Leonding ] is a city southwest of Linz in the Austrian state of Upper Austria.  It borders Puchenau and the river Danube in the north, Wilhering and Pasching in the west, Traun in the south and Linz in the east.  With a population of more than 27 thousand people, Leonding is the most populous city of the Linz-Land district and the fourth most populous city in Upper Austria.

Bad Leonfelden: Bad Leonfelden is a municipality in the district of Urfahr-Umgebung in the Austrian state of Upper Austria.  Steven Beller, author of "A Concise History of Austria", who has family links to Bad Leonfelden, cites episodes from the town's history from its foundation in 1292 to the 21st century, to demonstrate the impact of historical and political events on the local life in Austria's rural provinces.  The Jugendstil mosaicist Leopold Forstner was born there.

Hallstatt: Hallstatt (] ) is a market town in the district of Gmunden, in the Austrian state of Upper Austria.  Situated on Hallstätter See, it is part of the Dachstein / Salzkammergut Cultural Landscape, one of the World Heritage Sites in Austria.

Freistadt:    (literally "Freetown") is a small Austrian town in the state of Upper Austria in the region Mühlviertel.  With a population of approximately 7,500 residents, it is a trade centre for local villages.  Freistadt is the economic centre of a district of the same name District Freistadt.  The nearest sizeable cities are Linz, the capital of Upper Austria, about 40 km in the south, and České Budějovice, the capital of Southern Bohemia, about 60 km in the north.

Wilhering: Wilhering is a municipality in the district Linz-Land in the Austrian state of Upper Austria.  Their slogan is "culture and life".  Culturally they have Cistercian Abbey and the Rococo church, for life they have the nature and woods that are around Wilhering.  The Cisterican Abbey was established in the 1146 and was then rebuilt after it had been burnt down.  It contains sketches and paintings by Austrian Baroque painters.  The church has Rococo interior which is one of the best examples of this style in Austria.

Sankt Konrad: St. Konrad (or Sankt Konrad) is a town in the Gmunden district in the Austrian state of Upper Austria in Austria.

Upper Austria: Upper Austria (German: "Oberösterreich" , ] ; Austro-Bavarian: "Obaöstarreich"; Czech: "Horní Rakousy" ) is one of the nine states or "Bundesländer" of Austria.  Its capital is Linz.  Upper Austria borders on Germany and the Czech Republic, as well as on the other Austrian states of Lower Austria, Styria, and Salzburg.  With an area of 11,982 km² and 1.437 million inhabitants, Upper Austria is the fourth-largest Austrian state by land area and the third-largest by population.

Peuerbach: Peuerbach is a town in Austria, in Grieskirchen (district) in the Austrian state of Upper Austria.

Matthias Bernegger: Matthias Bernegger (Latin: "Bernegerus" , also "Matthew"; born 8 February 1582 in Hallstatt, Salzkammergut, died 5 February 1640 in Strassburg) was a German philologist, astronomer, university professor and writer of Latin works.

Steyr: Steyr (] ) is a statutory city, located in the Austrian federal state of Upper Austria.  It is the administrative capital, though not part of Steyr-Land District.  Steyr is Austria's 12th most populated town and the 3rd largest town in Upper Austria.

Question: Matthias Bernegger was born in a town in what district of the Austrian state of Upper Austria?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person."
        },
        "birth_town": {
          "type": "string",
          "description": "The town where the person was born."
        }
      },
      "required": [
        "name",
        "birth_town"
      ],
      "additionalProperties": false
    },
    "birth_town_location": {
      "type": "object",
      "properties": {
        "town_name": {
          "type": "string",
          "description": "The name of the town."
        },
        "district_name": {
          "type": "string",
          "description": "The district the town is located in."
        },
        "state_name": {
          "type": "string",
          "description": "The state the town is located in."
        }
      },
      "required": [
        "town_name",
        "district_name",
        "state_name"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "object",
      "properties": {
        "district_of_birth": {
          "type": "string",
          "description": "The district where the person was born."
        }
      },
      "required": [
        "district_of_birth"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person",
    "birth_town_location",
    "answer"
  ],
  "additionalProperties": false
}
