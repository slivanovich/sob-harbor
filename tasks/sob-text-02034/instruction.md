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
Happehatchee Center: The Happehatchee Center is a nature sanctuary and spiritual center operated by a non-profit organization in Estero, Florida.  It is located on 4.5 acres of subtropics forest, spanning 150 feet on both sides of the Estero River.  It is adjacent to the Koreshan State Historic Site and together these lands host a variety of flora and fauna along the river.

Cranbury (CDP), New Jersey: Cranbury is an unincorporated community and census-designated place (CDP) located within Cranbury Township, in Middlesex County, New Jersey, United States.  As of the 2010 United States Census, the CDP's population was 2,181.  Despite the similarity in the name of Cranbury Township and the CDP, the two are not one and the same, as had been the case for most paired Township / CDP combinations prior to the 2010 Census, in which the CDP was coextensive with a township of the same name.

Florence (CDP), New Jersey: Florence is an unincorporated community and census-designated place (CDP) located within Florence Township, in Burlington County, New Jersey, United States, that was established as part of the 2010 United States Census.  As of the 2000 United States Census, the CDP was combined as Florence-Roebling, which had a total population of 8,200.  As of the 2010 Census, the Florence-Roebling CDP was split into its components, Roebling (with a population of 3,715) and Florence.  As of the 2010 Census, the population of the Florence CDP was 4,426.

Center Point, Alabama: Center Point is a newly incorporated city and a former census-designated place (CDP) in northeastern Jefferson County, Alabama, United States.  It is part of the Birmingham metropolitan area.  At the 2000 census the population was 22,784.  However, after its incorporation in 2002, the city's boundaries are much smaller than those of the CDP.  As of the 2010 census, the population of the incorporated city was 16,921.  The public high school for Center Point is Center Point High School grades 9th-12th.  The public middle school for Center Point is Erwin Middle School grades 6th-8th.  Center Point has 2 public elementary schools, Erwin Intermediate School grades 3rd-5th and Center Point Elementary School grades K-2nd.

Barclay, New Jersey: Barclay is an unincorporated community and census-designated place (CDP) located within Cherry Hill, in Camden County, New Jersey, United States, that had been part of the Barclay-Kingston CDP until 2000, which was split to form the CDPs of Barclay and Kingston Estates as of the 2010 Census.  Until the 2000 Census, Barclay was included as part of the Barclay-Kingston CDP.  As of the 2010 United States Census, the CDP's population was 4,428.

Estero, Florida: Estero is a village in Lee County, Florida, United States.  As of the 2010 census, the CDP (Census Designated Population) was 18,176.  It is the home of Germain Arena, which hosts the home games for the Florida Everblades ECHL ice hockey team.  Florida Gulf Coast University is also located just outside the Estero Planning District.

Florence-Roebling, New Jersey: Florence-Roebling is an unincorporated community and former census-designated place (CDP) located within Florence Township, in Burlington County, New Jersey, United States, that existed up to and including the 2000 United States Census.  As of the 2000 Census, the CDP's population was 8,200.  With the 2010 United States Census, the CDP has been split into its components, with the creation of separate CDPs for Florence CDP (with a 2010 Census population of 4,426) and Roebling (3,715).

Roebling, New Jersey: Roebling is an unincorporated community and census-designated place (CDP) located within Florence Township, in Burlington County, New Jersey, United States, that was established as part of the 2010 United States Census.  As of the 2000 United States Census, the CDP was combined as Florence-Roebling, which had a total population of 8,200.  As of the 2010 Census, the Florence-Roebling CDP was split into its components, Florence (with a population of 4,426) and Roebling.  As of the 2010 Census, the population of the Florence CDP was 4,426.

North Laurel, Maryland: North Laurel is a census-designated place (CDP) in Howard County, Maryland, United States.  The published population was 4,474 at the 2010 census.  This population was substantially less than the CDP's population in 2000, and was the result of an error in defining the boundary prior to tabulation and publication of 2010 Census results.  The corrected 2010 Census population is 20,259.  North Laurel is located adjacent to the city of Laurel.

Branford Center, Connecticut: Branford Center is a neighborhood and census-designated place (CDP) in the town of Branford, Connecticut, United States.  The CDP encompasses the traditional town center area (roughly the area bounded by U.S. Route 1, the Amtrak railroad tracks, and the Branford River) and the area known as Branford Point (the portion of the CDP south of the railroad tracks).  The population of the CDP (including Branford Point) was 5,819 at the 2010 census.

Question: According to the 2010 census, what was the population of the CDP in which Happehatchee Center is located?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "location_name": {
      "type": "string",
      "description": "The name of the census-designated place (CDP)."
    },
    "census_year": {
      "type": "integer",
      "description": "The year of the census."
    },
    "population": {
      "type": "integer",
      "description": "The population of the CDP according to the specified census year."
    },
    "is_cdp": {
      "type": "boolean",
      "description": "Indicates if the location is a Census Designated Place."
    }
  },
  "required": [
    "location_name",
    "census_year",
    "population",
    "is_cdp"
  ],
  "additionalProperties": false
}
