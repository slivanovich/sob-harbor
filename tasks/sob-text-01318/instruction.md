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
Birla Science Museum: B. M. Birla Science Museum is an Indian science museum located in Hyderabad, India.  Constructed by civil engineer Mr. P. A. Singaravelu, it comprises a planetarium, museum, science center, art gallery as well as a dinosaurium.  The museum itself was the second phase of the science center when it opened in 1990.

Sands China: Sands China Limited () is an integrated resort developer and operator in Macau and a subsidiary of Las Vegas Sands Corp, the owner of The Venetian Las Vegas and The Palazzo.  It mainly operates in five segments in Macau: The Venetian Macao, Sands Macao, The Plaza Macao, Sands Cotai Central and ferry and other operations.  Its business involves gaming areas, meeting space, convention and exhibition halls, retail and dining areas and entertainment venues.

Museum of Light, Mexico City: The Museum of Light (Spanish Museo de la Luz) is a science museum dedicated to the phenomena of light, located in the former San Ildefonso College in the historic center of Mexico City.  It was opened in 1996 originally in the former church of the San Pedro y San Pablo College.  However, this building was closed in 2010 in order to convert it into the Museum of the Constitutions.  The Museum of Light was moved to its current and larger location, but it remains an extension of the Universum museum, the general science museum of the Universidad Nacional Autónoma de México.

CosmoCaixa Barcelona: CosmoCaixa Barcelona (] ) is a science museum located in Barcelona, Catalonia, Spain.  Formerly known as the Science Museum of Barcelona, it closed for renovations in 1998 and reopened in 2004 under its current name.  The museum features a variety of exhibitions, permanent and temporary, that showcase the environment, nature, science, and space.  CosmoCaixa also has a planetarium and exhibitions devoted to interaction such as touch and play for small children.  It also has a bookstore, gift shop, library, teaching center and cafe.  The museum is sponsored by la Caixa.  Entry to the Museum is free for students under 18.  Adults too can enjoy at the Museum with an entry ticket of 4 euros.

Las Vegas Sands: Las Vegas Sands Corporation is an American casino and resort operating company based in Paradise, Nevada, United States.  Its resorts feature accommodations, gaming and entertainment, convention and exhibition facilities, restaurants and clubs, as well as an art and science museum in Singapore.

Museum of Science and Industry (Manchester): The Museum of Science and Industry (MSI or formerly known as MOSI) in Manchester, England, is a large museum devoted to the development of science, technology and industry with emphasis on the city's achievements in these fields.  The museum is part of the Science Museum Group, a non-departmental public body of the Department for Culture, Media and Sport, having merged with the National Science Museum in 2012.

Gifu City Science Museum: The Gifu City Science Museum (岐阜市科学館 , Gifu-shi Kagakukan ) is a city-supported museum in Gifu, Gifu Prefecture, Japan.  It was built in 1955 and was moved to its present location and renamed the Gifu City Children’s Science Center in 1980.  When the planetarium was added in 1988, the name was again changed to the Gifu City Science Museum.  There are many hands-on exhibits in the museum.

Osaka Science Museum: The Osaka Science Museum (大阪市立科学館 , Ōsaka Shiritsu Kagakukan ) is a science museum in Naka-no-shima, Kita-ku, Osaka, Japan.  The museum is located between the Dōjima River and the Tosabori River, above Osaka's subterranean National Museum of Art.  Opened in 1989, the museum was constructed to mark the 100th anniversary of Osaka City.  The construction was funded through a 6.5 billion yen donation toward building costs from Kansai Electric.  Its theme is "The Universe and Energy".  Before the war a similar museum opened in 1937.  It was known as the Osaka City Electricity Science Museum and it was both the first science museum and the first planetarium in Japan.

Sands Macao: Sands Macao () is a hotel and casino resort located in Sé, Macau, China.  It is owned and operated by the Las Vegas Sands Corporation, and was designed by Steelman Partners, LLP.  It comprises a 229000 sqft casino, and a 289-suite hotel.

Sheldon Adelson: Sheldon Gary Adelson (pronounced ; born August 4, 1933) is an American business magnate, investor, and philanthropist.  He is the founder, chairman and chief executive officer of Las Vegas Sands Corporation, which owns the Marina Bay Sands in Singapore, and is the parent company of Venetian Macao Limited, which operates The Venetian Resort Hotel Casino and the Sands Expo and Convention Center.  He also owns the Israeli daily newspaper "Israel Hayom", and the "Las Vegas Review-Journal".  Adelson, a lifelong donor and philanthropist to a variety of causes, founded with his wife's initiative the Adelson Foundation.  He is a member of the Republican Party.

Question: The company that owns and operates Sands Macao also has an art and science museum in what city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company that owns and operates Sands Macao."
    },
    "owned_property": {
      "type": "string",
      "description": "The name of the property owned and operated by the company, as mentioned in the question."
    },
    "museum_location": {
      "type": "object",
      "properties": {
        "museum_type": {
          "type": "string",
          "description": "The type of museum owned by the company."
        },
        "city": {
          "type": "string",
          "description": "The city where the company's museum is located."
        }
      },
      "required": [
        "museum_type",
        "city"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "owned_property",
    "museum_location"
  ],
  "additionalProperties": false
}
