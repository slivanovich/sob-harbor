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
Venezuela at the 2018 Summer Youth Olympics: Venezuela will compete at the 2018 Summer Youth Olympics, in Buenos Aires, Argentina from 6 October to 18 October 2018.

Youth Olympic Village (Buenos Aires): The Youth Olympic Village will be an Olympic Village built for the 2018 Summer Youth Olympics in the district of Villa Soldati, a southern neighborhood of Buenos Aires.

2010 Summer Youth Olympics torch relay: The 2010 Summer Youth Olympics torch relay was run from 23 July until 14 August 2010, prior to the 2010 Summer Youth Olympics held in Singapore.  The torch relay was termed The Journey of the Youth Olympic Flame, or JYOF, by the Singapore Youth Olympic Games Organising Committee (SYOGOC).  It began with the traditional flame lighting ceremony in Olympia, Greece on 23 July 2010, and was followed by a 13-day round the world tour across five cities, namely Berlin, Germany; Dakar, Senegal; Mexico City, Mexico; Auckland, New Zealand; and Seoul, South Korea.  Following the international leg, the torch arrived in host city Singapore on 6 August 2010 for the domestic leg.

Basketball at the 2018 Summer Youth Olympics: Basketball at the 2018 Summer Youth Olympics was held from October 6 to October 18.  The events took place at the Parque Mujeres Argentinas in Buenos Aires, Argentina.  As in previous Youth Olympic games the 3x3 format was used along with the returned of the skill challenge.

2018 Summer Youth Olympics: The Buenos Aires 2018 Summer Youth Olympic Games (Spanish: 'Juegos Olímpicos de la Juventud de 2018' ) is the third edition of the Summer Youth Olympics, a major international sports in which culture and education are also of great importance, are due to be celebrated in the tradition of the Summer Olympic Games on 6–18 October 2018 in Buenos Aires, Argentina.  It will be the first Summer Youth Olympic Games to be held outside Asia and the first Youth Games for either summer or winter to be held outside Eurasia.

Cecilia Grierson (Buenos Aires Premetro): Cecilia Grierson is a station on the Buenos Aires Premetro.  It was opened on 29 April 1987 together with the other Premetro stations.  The station is located in the Barrio of Villa Soldati, near Parque de la Ciudad.  It will provide access to the Predio Ferial Olímpico and the Youth Olympic Village (YOV) for the 2018 Summer Youth Olympics.

Spain at the 2018 Summer Youth Olympics: Spain will compete at the 2018 Summer Youth Olympics, in Buenos Aires, Argentina from 6 October to 18 October 2018.

2014 Summer Youth Olympics: The 2014 Summer Youth Olympic Games (officially known as II Summer Youth Olympic Games) (Chinese: 第二届夏季青年奧林匹克运动会) were the second Summer Youth Olympic Games, an international sports, education and cultural festival for teenagers, held from 16 to 28 August 2014 in Nanjing, China.

Predio Ferial Olímpico: The Predio Ferial Olímpico ("Olympic Fairground") will be an exhibition and convention centre in the district of Villa Soldati, to the south of Buenos Aires, that will be the site of the Main Media Center (MMC) and will host several events during the 2018 Summer Youth Olympics: boxing, fencing, gymnastics (Artistics - Rhythmic - Trampoline), judo, table tennis, taekwondo, weightlifting, wrestling, handball and badminton.

2023 Summer Youth Olympics: The 2023 Summer Youth Olympics will be the fourth edition of the Summer Youth Olympic Games, an international sports, education and cultural festival for teenagers, in a city designated by the International Olympic Committee (IOC).

Question: Cecilia Grierson is a station on the Buenos Aires Premetro, it will provide access to the Predio Ferial Olímpico and the Youth Olympic Village (YOV) for which third edition of the Summer Youth Olympics, a major international sports in which culture and education are also of great importance, are due to be celebrated in the tradition of the Summer Olympic Games on 6–18 October 2018 in Buenos Aires, Argentina?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "olympics_name": {
      "type": "string",
      "description": "The official name of the Summer Youth Olympics edition."
    },
    "edition_number": {
      "type": "integer",
      "description": "The sequential edition number of the Summer Youth Olympics."
    },
    "host_city": {
      "type": "string",
      "description": "The city hosting the Summer Youth Olympics."
    },
    "host_country": {
      "type": "string",
      "description": "The country hosting the Summer Youth Olympics."
    },
    "start_date": {
      "type": "string",
      "format": "date",
      "description": "The start date of the Summer Youth Olympics in YYYY-MM-DD format."
    },
    "end_date": {
      "type": "string",
      "format": "date",
      "description": "The end date of the Summer Youth Olympics in YYYY-MM-DD format."
    },
    "venues_with_access_from_cecilia_grierson": {
      "type": "array",
      "description": "A list of venues for the Olympics that are accessible via the Cecilia Grierson station.",
      "items": {
        "type": "object",
        "properties": {
          "venue_name": {
            "type": "string",
            "description": "The name of the venue."
          },
          "venue_type": {
            "type": "string",
            "description": "The type or function of the venue (e.g., Olympic Village, Exhibition Centre)."
          }
        },
        "required": [
          "venue_name",
          "venue_type"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "olympics_name",
    "edition_number",
    "host_city",
    "host_country",
    "start_date",
    "end_date",
    "venues_with_access_from_cecilia_grierson"
  ],
  "additionalProperties": false
}
