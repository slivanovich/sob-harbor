{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJoão Rebelo: João Rebelo (born 20 March 1961 in Aljustrel) is a Portuguese former sport shooter who competed in the 1984 Summer Olympics, in the 1988 Summer Olympics, in the 1992 Summer Olympics, in the 1996 Summer Olympics, in the 2000 Summer Olympics.\n\nKatherine Schwarzenegger: Katherine Eunice Schwarzenegger (born December 13, 1989) is an American author and the elder daughter of actor/politician Arnold Schwarzenegger and broadcast journalist Maria Shriver.  A member of the Kennedy family, Schwarzenegger is a great-niece of John F. Kennedy, the 35th President of the United States.\n\nList of Olympic medalists in badminton: Badminton is a sport contested at the Summer Olympic Games.  Badminton was first held as a demonstration sport at the 1972 Summer Olympics, and was an exhibition sport at the 1988 Summer Olympics; the men's and women's singles and doubles have been held at every Summer Olympics since the 1992 Summer Olympics.  The mixed doubles badminton tournament started in the 1996 Summer Olympics.\n\nStan Huntsman: Stanley Houser \"Stan\" Huntsman (March 20, 1932 – November 23, 2016) was an American track and field (athletics) coach.  He was a men's assistant coach during the 1976 Summer Olympics and the men's head coach of the American team of the 1988 Summer Olympics.  He would have been assistant coach during the 1980 Summer Olympics, but the American team did not compete due to a boycott.  He was also the head coach of the 1993 World Championships in Helsinki.  The American team won six gold medals and a total of 18 medals together, both the most by any nation.  At the 1988 Summer Olympics the American team won seven gold medals, the most in track and field for any nation.  He was elected to the National Track and Field Hall of Fame in 2004.\n\nJorge González (sport shooter): Jorge González (born 2 May 1957) is a Spanish former sport shooter who competed in the 1984 Summer Olympics, in the 1988 Summer Olympics, in the 1992 Summer Olympics, in the 1996 Summer Olympics, and in the 2000 Summer Olympics.\n\nList of Olympic venues in equestrian: For the Summer Olympics, there are 53 venues that have or will be used for equestrian.  From 1912 to 1992, the events took place in more than one venue.  Since the 1992 Summer Olympics, the equestrian events have taken place on a single venue in an effort to reduce costs.  During the 1964 to the 1980 Summer Olympics, an equestrian event was the final event before the closing ceremonies of the respective Olympics.  The last equestrian event that took place at the main stadium was at the 1988 Summer Olympics though it was not the final event before the closing ceremonies.  That honor would fall for the end of the men's marathon event.  Stockholm Olympic Stadium is the only equestrian venue to serve host for more than one Summer Olympics, doing so in 1912 and 1956.\n\nAleksandr Lukyanov: Aleksandr Viktorovich Lukyanov (Russian: Александр Викторович Лукьянов , born August 19, 1949) is a Russian rower who competed for the Soviet Union in the 1976 Summer Olympics, in the 1980 Summer Olympics, and in the 1988 Summer Olympics and for Russia in the 1996 Summer Olympics and in the 2000 Summer Olympics.\n\nVenues of the 1988 Summer Olympics: For the 1988 Summer Olympics, a total of thirty-one sports venues were used.  South Korea hosted its first World Championships in 1978 in shooting sports.  Three years later, Seoul was awarded the 1988 Summer Olympics.  Many of the venues constructed for the 1988 Games were completed two years earlier in time for the Asian Games.  The 1986 Asian Games served as test events for the 1988 Summer Olympics.  The men's marathon course was lined by 36,000  policemen.  Steffi Graf won a gold medal in women's singles to complete the \"Golden Slam\".  None of the football venues used for these games were used for the 2002 FIFA World Cup that Korea co-hosted with Japan.\n\nMaria Shriver: is an American journalist and activist.  She is the former First Lady of California, and the estranged wife of former California Governor Arnold Schwarzenegger.  She has received a Peabody Award and was co-anchor for NBC's Emmy-winning coverage of the 1988 Summer Olympics.  As executive producer of \"The Alzheimer's Project\", Shriver earned two Emmy Awards and an Academy of Television Arts & Sciences award for developing a \"television show with a conscience\".  She is a member of the Kennedy family (her mother, Eunice Kennedy Shriver, was a sister of John F. Kennedy, Robert F. Kennedy, and Ted Kennedy).  Shriver is currently a special anchor and correspondent for NBC News.\n\nMikako Kotani: Mikako Kotani (小谷 実可子 , Kotani Mikako , born 30 August 1966) is a Japanese former synchronized swimmer who competed in the 1988 Summer Olympics, where she gained a bronze medal each for the solo and duet events, and the 1992 Summer Olympics.  She was the first woman to be Japan's flag-bearer for the 1988 Summer Olympics Opening Ceremony.\n\nQuestion: The mother of Katherine Eunice Schwarzenegger received what award for her coverage of the 1988 Summer Olympics?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who received the award.\"\n    },\n    \"relationship_to_katherine\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the person to Katherine Eunice Schwarzenegger.\"\n    },\n    \"award_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the award received.\"\n    },\n    \"event_covered\": {\n      \"type\": \"string\",\n      \"description\": \"The specific event for which the coverage received the award.\"\n    },\n    \"role_in_coverage\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the person during the event coverage.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"relationship_to_katherine\",\n    \"award_name\",\n    \"event_covered\",\n    \"role_in_coverage\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who received the award."
      },
      "relationship_to_katherine": {
        "type": "string",
        "description": "The relationship of the person to Katherine Eunice Schwarzenegger."
      },
      "award_name": {
        "type": "string",
        "description": "The name of the award received."
      },
      "event_covered": {
        "type": "string",
        "description": "The specific event for which the coverage received the award."
      },
      "role_in_coverage": {
        "type": "string",
        "description": "The role of the person during the event coverage."
      }
    },
    "required": [
      "person_name",
      "relationship_to_katherine",
      "award_name",
      "event_covered",
      "role_in_coverage"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
