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
Saint Joseph Preparatory High School: Saint Joseph Preparatory High School, formerly the Mount Saint Joseph Academy, is a Catholic, college-preparatory high school founded.  Its most recent organization followed upon the 2012 closings of Mount Saint Joseph Academy and Trinity Catholic High School.  The school occupies Mount Saint Joseph Academy's former campus, and both institutions were named in honor of Saint Joseph.

Catholic High School Athletic Association: The Catholic High School Athletic Association or CHSAA is a high school athletic association made up of Catholic high schools based in New York City, Long Island, and Westchester.  It is the largest Catholic high school athletic league in the United States.

Pontevedra, Negros Occidental: Also called Marayo, Pontevedra's center or poblacion area is marked by the newly renovated St. Michael the Archangel Parish, with the Saint Michael Academy, beside it.  To the east is the Public Market, ending up with Brgy.  Antipolo, notable place of some of prominent families "Hacienderos" as well as political clan of the town.  The western side offers scenic views of the Panay Gulf as well as Islands of Guimaras and Panay.

Mount Saint Michael Academy: Mount Saint Michael Academy, also known as "Mount", is an all-boys Roman Catholic high school in the Wakefield neighborhood of the New York City borough of the Bronx.  The school's campus also borders the city of Mount Vernon in neighboring Westchester County and is administered by the Archdiocese of New York.  The 22-acre (89,000 m²) campus is a college preparatory school for some 800 boys grades 6 through 12.  The school's motto is "ad astra per aspera", Latin for "to the stars through difficulties".  It is a member of the Catholic High School Athletic Association (CHSAA). MSM

St. Michael Academy: St. Michael Academy or St. Michael's Academy is the name of many schools and other educational institutions.  Most have a religious heritage and are named after Saint Michael:

Mount Saint Agnes College: Mount Saint Agnes College was a Catholic women's college located in the Mount Washington neighborhood of Baltimore, Maryland.  It opened in 1890 and was operated by the Sisters of Mercy.  In 1971, Mount Saint Agnes merged with nearby Loyola College in Maryland, which still oversees the Mount Saint Agnes Alumnae Association.  The college closed as its own degree-granting institution in 1972.

Watchung Conference: The Watchung Conference was a high school sports association under the jurisdiction of the New Jersey State Interscholastic Athletic Association (NJSIAA).  The conference consisted of eleven public high schools covering Essex County, Hudson County and Union County in northern New Jersey.  In 2009, the conference was disbanded.  The Essex County schools joined the Super Essex Conference, the Union County schools joined the Union County Interscholastic Athletic Association, and the Hudson County schools joined the temporary North Jersey Tri-County Conference, before joining their Hudson County schools in reviving the Hudson County Interscholastic Athletic Association in 2010.

Canyon Athletic Association: The Canyon Athletic Association, (previously known as the Arizona Charter Athletic Association), is an American non-profit regulatory organization for athletic competition among secondary schools located in Arizona.  The CAA administers primarily to small non-traditional education institutions including charter schools, public schools, home school organizations and parochial schools. .  As of 2014, the CAA membership consisted of approximately 125 High Schools and Junior High Schools.

Kresh Novakovic: Kresh Novakovic (born December 13, 1974) is an American actor born in the Bronx, New York.  He attended both Mount Saint Michael Academy (Bronx, NY) and Fordham University (Bronx, NY).

Hudson County Interscholastic League: The Hudson County Interscholastic League (formerly known as the Hudson County Interscholastic Athletic Association) is a New Jersey high school sports association operating under the jurisdiction of the New Jersey State Interscholastic Athletic Association (NJSIAA)and consisting of public and parochial high schools in Hudson County.>  The Hudson County Interscholastic Athletic Association was in hiatus for the 2009-10 school year, as all schools played in the temporary North Jersey Tri-County Conference, where they were joined with the non-Hudson County schools from the former Northern New Jersey Interscholastic League.

Question: Mount Saint Michael Academy is a member of the athletic association made up of high schools in what area?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "school_name": {
      "type": "string",
      "description": "The name of the high school."
    },
    "athletic_association_name": {
      "type": "string",
      "description": "The name of the athletic association the school is a member of."
    },
    "geographic_areas_covered": {
      "type": "array",
      "description": "A list of geographic areas where the athletic association's member schools are based.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "school_name",
    "athletic_association_name",
    "geographic_areas_covered"
  ],
  "additionalProperties": false
}
