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
Wrestling at the 2016 Summer Olympics: Wrestling at the 2016 Summer Olympics in Rio de Janeiro took place from 14 to 21 August at the Carioca Arena 2 in Barra da Tijuca.  Wrestling had been split into two disciplines, freestyle and Greco-Roman, which were further divided into different weight categories.  Men competed in both disciplines whereas women only participated in the freestyle events, with 18 gold medals awarded.  Wrestling had been contested at every modern Summer Olympic Games, except Paris 1900.

Clara Immerwahr: Clara Immerwahr (21 June 1870 – 2 May 1915) was a German chemist of Jewish descent.  She was the first woman to be awarded a doctorate in chemistry in Germany, and is credited with being a pacifist as well as a women's rights activist.  From 1901 until her suicide in 1915, she was married to the Nobel Prize-winning chemist Fritz Haber.

List of 2006 Winter Olympics medal winners: The 2006 Winter Olympics were held in Turin, Italy, from 10 February to 26 February 2006.  Approximately 2,508 athletes from 80 National Olympic Committees (NOCs) participated in these Games.  Overall, 84 events in 15 disciplines were contested; 45 events were opened to men, 37 to women and 2 were mixed pairs events.  Two disciplines were open only to men: Nordic combined and ski jumping, while figure skating was the only one in which men and women competed together in teams.

Equestrian at the 1994 Asian Games: Equestrian was contested at the 1994 Asian Games in Hiroshima, Japan.  Equestrian was contested from October 3 to October 9, 1994.  There were two equestrian disciplines: dressage and jumping.  All two disciplines are further divided into individual and team contests for a total of four events.

List of 2010 Winter Olympics medal winners: The 2010 Winter Olympics were held in Vancouver, Canada, from February 12 to February 28, 2010.  A total of 2,632 athletes representing 82 National Olympic Committees participated in these Games.  Overall, 86 events in 15 disciplines were contested; 46 events were open to men, 38 to women and 2 were mixed pairs.  Two disciplines were open only to men: Nordic combined and ski jumping, while figure skating was the only sport in which men and women competed together in teams.  Two new events were introduced: men's and women's ski cross.

List of 2011 Pan American Games medal winners: The 2011 Pan American Games were held in Guadalajara, Mexico from October 14 to October 30, 2011.  A total of about 6,000 athletes representing 42 National Olympic Committees participated in these Games.  Overall, 361 events in 36 disciplines were contested; 188 events were open to men, 160 to women and 13 were in mixed competition.  Two disciplines were open only to men: baseball and rugby sevens, while softball and Synchronized swimming were the sports in which only women were allowed to compete.  Racquetball and basque pelota returned to the Pan American Games after missing the last edition of the Games and rugby sevens made its debut.  New events in fencing, karate, squash, track cycling and water skiing made their debut at the Games.

Einstein's Gift: Einstein's Gift is a play written by Canadian playwright Vern Thiessen in 2003.  Through the recollections of Albert Einstein, the play focuses on the life and career of German chemist Dr. Fritz Haber, who helped improve living conditions with his work on nitrogen fixation.  His work was later used by the German army to produce chlorine gas used in Second Battle of Ypres in the First World War.  As Dr. Haber becomes increasingly involved with the German army, the play depicts how his actions and newly forged military connections affect his relationship with his wife, Clara, and his assistant, Otto.  As his passion in science intertwines with nationalistic pride, Haber manifested himself a scientist devoted to a country that never accepted his Jewish origin.

Adam Ondra: Adam Ondra (born February 5, 1993) is a Czech professional rock climber.  He specializes in lead climbing and bouldering and is the only athlete to have won the World Championships in two disciplines, lead and bouldering.  In addition, he won both medals in the same year, during the 2014 edition.  He also has a similar record in the World Cup, being the only athlete to have won the World Cup in two disciplines, lead in 2009 and bouldering in 2010.

Otto Hahn: Otto Hahn, {'1': ", '2': ", '3': ", '4': "} , {'1': ", '2': ", '3': 'ForMemRS', '4': "} (8 March 1879 – 28 July 1968) was a German chemist and pioneer in the fields of radioactivity and radiochemistry.  He was exclusively awarded the Nobel Prize in Chemistry in 1944 for the discovery and the radiochemical proof of nuclear fission.  He is referred to as the father of nuclear chemistry.

Clara Lieber: Clara Lieber (July 10, 1902 – December 14, 1982) was an American chemist known for her work with Otto Hahn on discovering fission, and her discovery of several isotopes of strontium and barium.

Question: Clara Lieber worked with the German chemist in the fields of what two disciplines?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "collaborator": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        },
        "role": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "nationality",
        "role"
      ],
      "additionalProperties": false
    },
    "fields_of_work": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 2,
      "description": "The disciplines in which the person and collaborator worked together."
    }
  },
  "required": [
    "person_of_interest",
    "collaborator",
    "fields_of_work"
  ],
  "additionalProperties": false
}
