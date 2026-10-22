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
Santa Sofía, Boyacá: Santa Sofía is a town and municipality in the Department of Boyacá, part of the subregion of the Ricaurte Province, Colombia.  The urban centre of Santa Sofía is located at an altitude of 2387 m on the Altiplano Cundiboyacense, with the highest elevated parts of the municipality, that have a páramo ecosystem, reaching 3000 m .  Santa Sofía borders Moniquirá in the north, Gachantivá in the west, Villa de Leyva in the southeast, Sutamarchán in the south, Saboyá in the southwest, and Puente Nacional, Santander in the west.

Alūksne: Alūksne (German:    ) is a town on the shores of Lake Alūksne in northeastern Latvia near the borders with Estonia and Russia.  It is the seat of Alūksne municipality.  Alūksne is the highest elevated Latvian city, located in East Vidzeme Upland at 217 m above sea level.  The high elevation of the city affects the social and physical arrangement of the place.

Koprišnica: Koprišnica is a small village south of Dren along the Došnica river in the Republic of Macedonia.  It has the only waterfalls in the municipality of Demir Kapija.  There are no residents in the village, but former residents and families return to open the church on the Patron Saint's Day, coined Panagjur, on May 8.  It is the highest elevated village in the municipality.

Kangchenjunga: Kangchenjunga (Nepali: कञ्चनजङ्घा , "Kañcanajaṅghā"), also spelled Kanchenjunga, is the third highest mountain in the world, and lies partly in Nepal and partly in Sikkim, India.  It rises with an elevation of 8586 m in a section of the Himalayas called "Kangchenjunga Himal" that is limited in the west by the Tamur River, in the north by the Lhonak Chu and Jongsang La, and in the east by the Teesta River.

Valle d'Aosta DOC: The Valle d'Aosta DOC (or Vallée d'Aoste DOC, in French) is an Italian "denominazione di origine controllata" located in the Aosta Valley of northwest Italy.  Surrounded by the Alps, the Valle d'Aosta is home to the highest elevated vineyards in all of Europe.  The principal winemaking region of the Valle d'Aosta is found along the eastern banks of the Dora Baltea (fr. , "Doire baltée") river with the city of Aosta serving as the central winemaking location.  The region is divided into three main vineyard areas; the upper valley, Valdigne, the central valley (locally "Valle centrale" in Italian, "Vallée centrale" in French) and the lower valley, (locally "Bassa valle" in Italian, "Basse vallée" in French).  To the south is the winemaking region of Piedmont.  The Valle d'Aosta is Italy's smallest winemaking region both in terms of size and production with only about 330,000 cases produced annually in the region and only 36,000 cases produced under the DOC label.  Seventy five percent of the area's production is red wine made mostly from the Pinot noir, Gamay and Petit Rouge varieties.  A white wine is made from the indigenous Prié blanc grape by the cooperative of Blanc de Morgex et de La Salle.

Koniaków:    is a village in Beskid Śląski mountain range in Cieszyn County, Silesian Voivodeship, southern Poland.  It is the highest elevated village in Silesian Beskids and lies in the historical region of Cieszyn Silesia.  The village is primarily known for its tradition of intricate lace-making.

Suchá Hora transmitter: Suchá Hora transmitter is a facility for FM- and TV-transmission on 1,231.6 metres high mountain Skalka (Kremnica Mountains) near Banská Bystrica in Slovakia.  Suchá Hora transmitter uses as antenna mast a 312 metres tall guyed tubular mast, which is one of the tallest structure of Slovakia and one of the highest elevated supertall structures in Europe.

Momhil Sar: Momhil Sar, or Mumhail Sar as pronounced in Wakhi is at 7343 m above sea level, is the 64th highest mountain peak in the world.  Mumhail Sar in Wakhi means the mountain that overlooks or is above Grandmother's cattle pen or paddock.  It is situated in the Hispar Muztagh subrange of the Karakoram range, a few kilometres to the north-west of its parent peak Trivor.

Pasonanca: Pasonanca is a barangay of Zamboanga City, Philippines belonging to the First (West) Congressional district.  Known as the "Little Baguio in the South", it is one of the highest elevated barangays from the sea level in the city.  The village is home to the Pasonanca Park and the conservation area known as Pasonanca Natural Park.

San Lucchese Madonna: Madonna with Child by the Master of San Lucchese (14th century, around 1345) is an Italian painting, with tempera and gold lead on panel as its medium.  It is currently in San Francisco in the Legion of Honor.  There are bibles and auras around the saints, Madonna, and baby.  Figures are holding holy sceptres or sepulchers .  Some of the men have crowns it looks like.  The women at the end of each column are the highest elevated person.  Why are they in the back?

Question: Kangchenjunga and Momhil Sar, are some of which type, of the highest elevated landmarks?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "landmark_category": {
      "type": "string",
      "description": "The general category of the highest elevated landmarks."
    },
    "landmarks": {
      "type": "array",
      "description": "Details about each specific landmark mentioned.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the landmark."
          },
          "elevation_m": {
            "type": "integer",
            "description": "The elevation of the landmark in meters."
          },
          "world_ranking": {
            "type": "string",
            "description": "The world ranking of the landmark if specified."
          }
        },
        "required": [
          "name",
          "elevation_m",
          "world_ranking"
        ],
        "additionalProperties": false
      }
    },
    "context_source": {
      "type": "string",
      "description": "Indicates that the information is derived from the provided context."
    }
  },
  "required": [
    "landmark_category",
    "landmarks",
    "context_source"
  ],
  "additionalProperties": false
}
