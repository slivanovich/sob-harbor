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
Changchun–Jilin Intercity Railway: Changchun–Jilin Intercity Railway is a high-speed rail line in Jilin Province, China, which opened for service on January 11, 2011.  It is the first intercity high-speed rail to be operational in Northeast China.  Like the Shanghai–Nanjing Intercity High-Speed Railway, which services Shanghai Hongqiao International Airport, the Changchun–Jilin Intercity Railway serves as an airport rail link for the cities of Changchun and Jilin.

Yiwu: Yiwu () is a city of about 1.2 million people in central Zhejiang province, China.  Its built-up ("or metro") area made of Yiwu and Dongyang cities was home to 2,038,413 inhabitants at the 2010 census.  The city is famous for its small commodity trade and vibrant market and is a regional tourist destination.  Although administratively Yiwu is a county-level city under the jurisdiction of Jinhua, it is better known than Jinhua nationally and internationally.

Yiwu Railway Station: Yiwu Railway Station () (IATA: YIU) is a railway station of the Hukun Railway and the Hangchangkun Passenger Railway located in Yiwu in Zhejiang province, People's Republic of China.  It is an important site on the Zhejiang-Jiangxi express railway line and under the administration of Shanghai Railway Bureau.  Now it is a first-class station.

Yiwu-London railway line: The Yiwu – London Railway Line is a freight railway route from Yiwu, China, to London, United Kingdom, covering a distance of roughly 12,000 km (7,456 miles).  This makes it the longest railway freight route in the world.  It is one of several long distance freight railway routes from China to Europe on the “New Eurasian Land Bridge” and part of establishing a modern-day Silk Road.  The route was opened on the 1st of January 2017, making London the 15th European city to have a railway route connection with China, and takes 18 days to complete (other European cities with China-Europe railway routes include Hamburg, Madrid, Rotterdam, Warsaw, etc.).

Turpan Jiaohe Airport: Turpan Jiaohe Airport () (IATA: TLQ, ICAO: ZWTP) is an airport serving the city of Turpan in Xinjiang Uyghur Autonomous Region, China.  It is located 10 kilometers northwest of the city, and named after the Jiaohe Ruins.  First built in the 1950s but out of use by the 1970s, the airport was relocated and rebuilt at the current site starting May 2009, with an investment of 430 million yuan.  Turpan Airport was reopened on 9 July 2010.

Yiwu–Madrid railway line: The Yiwu - Madrid Railway line is a railway route taken by container trains from the Chinese city of Yiwu to the Spanish city of Madrid, a distance of roughly 10,000 kilometres (about 6,111 miles ), 741 kilometres more than the Trans-Siberian Railway, the longest until now.  It is one of several routes used by long distance freight trains on the "New Eurasian Land Bridge".  (Other city pairs connected by regular freight trains running between China and Europe include e.g. Lianyungang and Rotterdam, or Yiwu and Warsaw; as of 2016, at least 12 Chinese cities and 9 European ones were connected by similar trains.)

Jiaohe, Jilin: Jiaohe () is a middle-sized city in east-central Jilin province, People's Republic of China.  It is under the administration of Jilin City, 65 km to the west, and it is well known for its production of tobacco.  The mayor of the city is Wang Gang (王钢 ).

Yiwu Gymnasium: Yiwu Gymnasium is an indoor sporting arena located in Yiwu, China.  The capacity of the arena is 6,000 spectators and opened in 2005.  It hosts indoor sporting events such as basketball and volleyball.  It hosts the Zhejiang Golden Bulls of the Chinese Basketball Association.

Yiwu Airport: Yiwu Airport () (IATA: YIW, ICAO: ZSYW) is a dual-use military and civil airport serving Yiwu, Jinhua in Zhejiang Province, China.  It is located 5.5 km northwest of the center of Yiwu and 51 km from the urban area of Jinhua.

Streptomyces tyrosinilyticus: Streptomyces tyrosinilyticus is a bacterium species from the genus of "Streptomyces" which has been isolated from river sediments from the South River in Jiaohe in the Jilin Province in China.

Question: Are the cities of Yiwu and Jiaohe, Jilin both located in China?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_focus": {
      "type": "string",
      "description": "The main subject or type of verification the question is asking for."
    },
    "cities_information": {
      "type": "array",
      "description": "Details about each city mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "city_name": {
            "type": "string",
            "description": "The name of the city."
          },
          "province": {
            "type": "string",
            "description": "The province where the city is located, if specified."
          },
          "country": {
            "type": "string",
            "description": "The country where the city is located."
          }
        },
        "required": [
          "city_name",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "all_cities_are_in_china": {
      "type": "boolean",
      "description": "The final answer to whether all specified cities are located in China."
    }
  },
  "required": [
    "question_focus",
    "cities_information",
    "all_cities_are_in_china"
  ],
  "additionalProperties": false
}
