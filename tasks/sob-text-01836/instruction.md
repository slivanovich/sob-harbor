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
Spirit Mountain (Nevada): Spirit Mountain, also known as Newberry Peak, is a mountain in the Laughlin, Nevada area that is listed on the United States National Register of Historic Places.  It is part of the Newberry Mountains in Nevada and the summit is the highest point in the Spirit Mountain Wilderness.

Enterprise, Nevada: Enterprise is an unincorporated town and census-designated place and part of Las Vegas Township in Clark County, Nevada, United States, south of Las Vegas.  The population was 108,481 at the 2010 census, up from 14,676 at the 2000 census.  As an unincorporated town, it is governed by the Clark County Commission with input from the Enterprise Town Advisory Board.  Enterprise was formed in December 1996.

Spirit Mountain Wilderness: Spirit Mountain Wilderness Area is a 33518 acre wilderness area located in the Newberry Mountains in Clark County, Nevada, 10 mi northwest of Laughlin.  Spirit Mountain lies within the area.  It is managed by the Bureau of Land Management and the National Park Service.

Winchester, Nevada: Winchester is an unincorporated town and census-designated place (CDP) and part of Las Vegas Township in Clark County, Nevada, United States that contains part of the Las Vegas Strip.  It is one of a number of CDPs in the unincorporated urbanized area directly south of Las Vegas.  The population was 27,978 at the 2010 census.  It is governed by the Clark County Commission with advice from the Winchester Town Advisory Board.  "Winchester, NV" does not appear in postal addresses; the United States Postal Service has assigned "Las Vegas, NV" as the place name for the ZIP codes containing Winchester.

Laughlin, Nevada: Laughlin is an unincorporated town and census-designated place in Clark County, Nevada, United States, and a port located on the Colorado River.  Laughlin is 90 mi south of Las Vegas, located in the far southern tip of Nevada.  It is best known for its gaming, entertainment, and water recreation.  As of the 2010 census, the population was 7,323.  The nearby communities of Bullhead City, Arizona; Needles, California; Fort Mohave, Arizona; and Mohave Valley, Arizona, bring the Laughlin area's total population to about 100,000.

Moapa, Nevada: Moapa is an unincorporated town and census-designated place (CDP) in Clark County, Nevada, United States.  The population was 1,025 at the 2010 census.  It is the largest town in Clark County by land area.  Both the second and the third tallest structures in Nevada, the Moapa Entrevision Tower and the Moapa Kemp Tower respectively, are located in Moapa.

Searchlight, Nevada: Searchlight is an unincorporated town and census-designated place (CDP) in Clark County, Nevada, United States, at the topographic saddle between two mountain ranges.  As of the 2010 census it had a population of 539.

Clark County Water Reclamation District: The Clark County Water Reclamation District (District) is a government wastewater treatment agency in Clark County, Nevada.  As a member of the Southern Nevada Water Authority, its mission is to treat millions of gallons of wastewater that is produced every day.  The District is the largest water treatment agency in Southern Nevada and is responsible for treating wastewater from unincorporated parts of Clark County within the Las Vegas Valley, including most of the Las Vegas Strip, and the communities of Blue Diamond, Moapa Valley, Nevada, Indaian Springs, Nevada, Laughlin, Nevada, and Searchlight.

Moapa Valley, Nevada: Moapa Valley is an unincorporated town and census-designated place in Clark County, Nevada, United States.  As of the 2010 census, it had a population of 6,924.  The valley in which the community lies, also named Moapa Valley, is about 40 mi long and lies roughly northwest to southeast.

Paradise, Nevada: Paradise is an unincorporated town and census-designated place (CDP) in Clark County, Nevada, United States, adjacent to the city of Las Vegas.  The population was 223,167 at the 2010 census, making it the most populous unincorporated community in Nevada.  As an unincorporated town, it is governed by the Clark County Commission with input from the Paradise Town Advisory Board.  Paradise was formed on December 8, 1950.

Question: Spirit Mountain, also known as Newberry Peak, is a mountain in the Laughlin,an unincorporated town and census-designated place in Clark County, Nevada, in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_name": {
      "type": "string",
      "description": "The primary name of the entity being described."
    },
    "entity_type": {
      "type": "string",
      "description": "The type of geographical feature or place."
    },
    "located_in_country": {
      "type": "string",
      "description": "The country where the entity is located."
    },
    "alternative_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other names by which the entity is known."
    },
    "associated_town": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the nearby town."
        },
        "type": {
          "type": "string",
          "description": "The classification of the town (e.g., unincorporated town, CDP)."
        },
        "county": {
          "type": "string",
          "description": "The county where the town is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the town is located."
        }
      },
      "required": [
        "name",
        "type",
        "county",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "entity_name",
    "entity_type",
    "located_in_country",
    "alternative_names",
    "associated_town"
  ],
  "additionalProperties": false
}
