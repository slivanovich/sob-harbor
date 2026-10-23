{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRazumovsky: Razumovsky or Rozumovsky (Russian: \"Разумовский\" , Ukrainian: \"Розумовський\", German: \"Razumofsky\") is an Imperial Russian name of Ukrainian Cossack origin from Siveria.  The main family line became extinct in the 19th century, while its Austrian branch exists to this day.  The Austrian branch was started by Grigory Razumovsky, who was forced to relocate to the Austrian Empire in 1816.\n\nCharles of Limburg Stirum: Count Charles Gaëtan Corneille Marie François-Xavier Ghislain of Limburg Stirum, GCVO, GCSG (September 15, 1906 – June 14, 1989), a Count of the Holy Roman Empire and Knight of the Golden Fleece (Austrian branch), was a member of the House of Limburg-Stirum.  During his life he was a Belgian Senator and Grand Master of the Royal Households of King Leopold III.\n\nChristoph Schönborn: Christoph Maria Michael Hugo Damian Peter Adalbert, Count of Schönborn, (] ) O.P. (German: \"Christoph Maria Michael Hugo Damian Peter Adalbert, Graf von Schönborn\"; born 22 January 1945), is a Bohemian-born Austrian Dominican friar and theologian, who is a cardinal of the Catholic Church.  He serves as the Archbishop of Vienna and President of the Austrian Bishops' Conference.  He was elevated to the cardinalate in 1998.  He is also the chaplain of the Order of the Golden Fleece (Austrian branch), of which he has been a member since 1961.  He is a member of the formerly sovereign princely House of Schönborn, several members of which held high offices of the Holy Roman Empire and the Catholic Church as prince-bishops, prince-electors and cardinals.\n\nSalomon Mayer von Rothschild: Salomon Mayer von Rothschild (9 September 1774 – 28 July 1855) was a German-born banker in the Austrian Empire and the founder of the Austrian branch of the prominent Mayer Amschel Rothschild family.\n\nArthur Trebitsch: Arthur Trebitsch (1880-1927) was an Austrian writer and racial theorist, known most notably for being an antisemite of Jewish origin.  He offered his services to help the fledgling Nazis to write their antisemitic literature, and was an influence on the early development of the Austrian branch of the Nazi party.\n\n2008–09 Austrian Football Bundesliga: The Austrian Football Bundesliga 2008–09 was the 97th season of top-tier football in Austria.  The competition is officially called \"tipp3-Bundesliga powered by T-Mobile\", named after the Austrian betting company tipp3 and the Austrian branch of German mobile phone company T-Mobile.  The season started on 8 July 2008 with Sturm Graz beating defending champions Rapid Vienna by 3–1.  The 36th and last round of matches took place on 31 May 2009.\n\nOrder of the Golden Fleece: The Order of the Golden Fleece (Spanish: \"Orden del Toisón de Oro\" , German: \"Orden vom Goldenen Vlies\" ) is a Roman Catholic order of chivalry founded in Bruges by the Burgundian duke Philip the Good in 1430, to celebrate his marriage to the Portuguese princess Isabella.  It became one of the most prestigious orders in Europe.  Today, two branches of the Order exist, namely the Spanish and the Austrian Fleece; the current grand masters are Felipe VI, King of Spain, and Karl von Habsburg, grandson of Emperor Charles I of Austria, respectively.  The chaplain of the Austrian branch is Cardinal \"Graf\" von Schönborn, Archbishop of Vienna.\n\nRoyal Canadian Army Chaplain Corps: The Royal Canadian Army Chaplain Corps (RCAChC) was an administrative corps of the Canadian Army.  The Canadian Army Chaplain Corps was authorized on 22 Mar 1948.  The Canadian Army Chaplain Corps was redesignated The Royal Canadian Army Chaplain Corps on 3 Jun 1948.  The Royal Canadian Army Chaplain Corps was succeeded by the Chaplain Branch (Canadian Forces) on May 2, 1969.  The official march of the Royal Canadian Army Chaplain Corps was \"Onward Christian Soldiers\".  The march has been changed to \"Ode to Joy\"\n\n2010–11 Austrian Football Bundesliga: The 2010–11 Austrian Football Bundesliga is the 99th season of top-tier football in Austria.  The competition was officially called \"tipp3-Bundesliga powered by T-Mobile\", named after the Austrian betting company tipp3 and the Austrian branch of German mobile phone company T-Mobile.  The season began in July 2010 and ended in May 2011.  Red Bull Salzburg are the defending champions, having won their sixth title last season.\n\n2009–10 Austrian Football Bundesliga: The 2009–10 Austrian Football Bundesliga is the 98th season of top-tier football in Austria.  The competition is officially called \"tipp3-Bundesliga powered by T-Mobile\", named after the Austrian betting company tipp3 and the Austrian branch of German mobile phone company T-Mobile.  The season began on the weekend of 18 July 2009 and ended on 13 May 2010.  RB Salzburg claimed the championship on the last matchday, their second consecutive title.\n\nQuestion: The Chaplain of the Austrian branch of the Order of the Golden Fleeze, serves as what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"chaplain_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the chaplain.\"\n    },\n    \"order_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the order.\"\n        },\n        \"branch\": {\n          \"type\": \"string\",\n          \"description\": \"The specific branch of the order.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"branch\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"served_roles\": {\n      \"type\": \"array\",\n      \"description\": \"A list of roles the chaplain serves.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  },\n  \"required\": [\n    \"chaplain_name\",\n    \"order_details\",\n    \"served_roles\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "chaplain_name": {
        "type": "string",
        "description": "The name of the chaplain."
      },
      "order_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the order."
          },
          "branch": {
            "type": "string",
            "description": "The specific branch of the order."
          }
        },
        "required": [
          "name",
          "branch"
        ],
        "additionalProperties": false
      },
      "served_roles": {
        "type": "array",
        "description": "A list of roles the chaplain serves.",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "chaplain_name",
      "order_details",
      "served_roles"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
