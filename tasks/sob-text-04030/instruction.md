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
Shunde, China Furniture Wholesale Market: Shunde, China Furniture Wholesale Market is located at Shunde district which connects Lecong town and Longjiang town along the 10 km highway, Foshan City, Guangdong Province, China.

Line 7, Guangzhou Metro: Line 7 of the Guangzhou Metro () or Panyu Line () runs across Panyu District.  Line 7's color is light green.  Line 7 is envisioned as tangential line that runs across southeast Guangzhou and Foshan, allowing for orbital traffic between the suburbs of Shunde, Panyu and Huangpu to avoid the crowded city center stations.  The first section starts at Guangzhou South Railway Station and ends at Higher Education Mega Center South, interchanging with Line 2 at Guangzhou South Railway Station, Line 3 at Hanxi Changlong, and Line 4 at Higher Education Mega Center South.  The total length is 17.1 km with 10 stations.  The plan for west extension of the first phase from Guangzhou South Railway Station to Meidi Dadao in Shunde District, Foshan was approved in October, 2015.  The construction of the west extension began in June, 2016.  The west extension is expected to be operational in 2020.  The first phase of the line (Guangzhou South — HEMC South) was opened on December 28, 2016.

Shunde District: Shunde District is a district in the city of Foshan in the Pearl River Delta, Guangdong Province, China.  Once a traditional agricultural county, it has become one of the most affluent counties in Guangdong and mainland China.  Since 2009, it is administrated independently of Foshan city, answerable directly to the Guangdong provincial government.

Shunfengshan Park: Shunfengshan Park (), located at the foot of Taiping Mountain in Shunde District, Foshan City, is one of the "Ten Attractions of Shunde".  It was built between 1999 and 2002, and was opened to public on October 24, 2004.

Leliu Subdistrict: Leliu Subdistrict () is a subdistrict of Shunde District, Foshan, Guangdong, China.  It lies in central of Shunde, with a resident population of 120,000 with its total area of 92 square kilometres.

Guangdong Country Garden School: Guangdong Country Garden School (CGS, ), is a private co-ed boarding school in Shunde District, Foshan City, just south of Guangzhou, in the People's Republic of China.  CGS has a campus area of 33 hectares with more than 4,300 students on campus, from age 3 to 18.  There are over 600 teachers including over 500 Chinese teachers and over 100 foreign teachers.

Shunde Port: Shunde Port () is a passenger port in Shunde, Foshan, Guangdong, China.  It is located at the right side of Wusha Bridge () in Daliang, Shunde.  It provides daily passenger vessel service between Shunde and Hong Kong.

Longjiang, Foshan: Longjiang () is a town in west-central Guangdong province, Southern China.  It is under the administration of Shunde District, Foshan City, which lies 15 km to the north-northeast.  Bordering towns are Leliu (勒流镇) to the east, Xingtan (杏坛镇) to the south, Lecong (乐从镇) to the north, and Jiujiang of Nanhai District to the west.

Shunde Railway Station: Shunde Station () is an elevated station of Guangzhou-Zhuhai Intercity Mass Rapid Transit.  The station is located at the east of Bigui Lu () and the west of Longzhou Lu () across Sanchongzhou Channel () in Daliang, Shunde District, Foshan, Guangdong, China, which is the city centre of Shunde District.  It started operations on 7 January 2011.

Xingning, Guangdong: Xingning (postal: Hingning; ) is a county-level city, under the jurisdiction of Meizhou City, Guangdong Province, China.  The second largest city in east Guangdong, Xingning has an area of 2105 km2 and a population of 1.13 million.

Question: Xingning, Guangdong and Shunde District, is in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "country_name": {
      "type": "string",
      "description": "The name of the country where the administrative divisions are located."
    },
    "administrative_divisions": {
      "type": "array",
      "description": "A list of administrative divisions mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "division_name": {
            "type": "string",
            "description": "The name of the administrative division."
          },
          "division_type": {
            "type": "string",
            "description": "The type of the administrative division (e.g., district, county-level city)."
          },
          "province": {
            "type": "string",
            "description": "The province to which the division belongs."
          }
        },
        "required": [
          "division_name",
          "division_type",
          "province"
        ],
        "additionalProperties": false
      }
    },
    "location_context": {
      "type": "string",
      "description": "A general description of the geographical context."
    }
  },
  "required": [
    "country_name",
    "administrative_divisions",
    "location_context"
  ],
  "additionalProperties": false
}
