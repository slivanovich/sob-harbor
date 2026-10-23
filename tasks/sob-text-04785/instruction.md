{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSkal vi danse?: Skal vi danse?  is the Norwegian edition of the British television series, \"Strictly Come Dancing\".  It is produced by Monster Entertainment and broadcast on TV 2 Jon Peder Olrud and Geir Bie were producers in the first season.  The second and third seasons were produced by Ingvild Daae.  The series premiered on TV 2 on January 15, 2006.  \"Skal vi danse?\"  in Norwegian means \"shall we dance?\" .  Dancing celebrities with professional dancers and companies are reviewed by a panel of judges and the TV viewers.  Each pair consists of a celebrity and a professional dancer and the one with the fewest votes does not participate in the next round.\n\nBrendan Cole: Brendan Cole (born 23 April 1976) is a New Zealand ballroom dancer, specialising in Latin American dancing.  He is most famous for appearing as a professional dancer on the BBC One show, \"Strictly Come Dancing\".  From 2005 to 2009, he was a judge on the New Zealand version of the show, \"Dancing with the Stars\".\n\nCome Dancing: Come Dancing was a British ballroom dancing competition show that ran on and off on the BBC from 1950 to 1998, becoming one of television's longest-running shows.  Unlike its follow up show \"Strictly Come Dancing\" contestants were not celebrities.\n\nStrictly Come Dancing: Strictly Come Dancing (informally known as Strictly) is a British television dance contest, featuring contestants, celebrities, and other people, from all walks of life, with professional dance partners competing in a ballroom and Latin dance competition.  Each couple is scored out of 10 by a panel of judges.  The title of the show suggests a continuation of the long-running series \"Come Dancing\", with an allusion to the film \"Strictly Ballroom\".  The format has been exported to over 40 other countries, and has also inspired a modern dance-themed spin-off \"Strictly Dance Fever\".  The show is currently presented by Tess Daly and Claudia Winkleman.\n\nDianne Buswell: Dianne Buswell (born 1989) is an Australian ballroom dancer.  She has appeared on \"So You Think You Can Dance Australia\" and was a professional dancer on the Australian version of \"Dancing with the Stars\" in 2015.  Buswell became a professional dancer on \"Strictly Come Dancing\" beginning in 2017.\n\nStrictly Come Dancing (series 6): Strictly Come Dancing returned for its sixth series on 20 September 2008 on BBC One.  Bruce Forsyth and Tess Daly returned as co-presenters of the main show on BBC One, whilst Claudia Winkleman returned to present spin-off show \"\" on BBC Two.  Craig Revel Horwood, Arlene Phillips, Len Goodman and Bruno Tonioli returned as judges.\n\nMira Quien Baila: ¡Mira Quien Baila!  (] ; English: \"Look Who's Dancing\" ), also known as MQB, is a Spanish-language reality show broadcast on Univision in the United States.  The TV series is the Spanish version of British version \"Strictly Come Dancing\" and American version \"Dancing with the Stars\".  The show involved celebrities (including singers, actors and others) being paired up with professional dancers.  Each couple performed ballroom or Latin dances and competed for judges' critiques and audience votes.  Whichever couple received the lowest total amount of judges' critique and audience votes was eliminated until a champion was named at the end.  Each celebrity competed for a grand total of $50,000 for a charity of their choice.\n\nCraig Revel Horwood: Craig Revel Horwood (born 4 January 1965) is an Australian-British dancer, choreographer and theatre director in the United Kingdom.  He is a patron of the National Osteoporosis Society.  He is best known as a judge on the BBC dancing show \"Strictly Come Dancing.\"  He published his autobiography in 2008.\n\nThe Strictly: The Strictly is a signature dance routine from the BBC show \"Strictly Come Dancing\", which launched in the 13th series of the popular entertainment show.  The dance was devised by \"Strictly Come Dancing\"'s Director of Choreography, Jason Gilkison and draws inspiration from some of the show's most iconic moves, as well as celebrating some of the show's stars.\n\nStrictly Come Dancing: It Takes Two: Strictly Come Dancing: It Takes Two, also known as Strictly: It Takes Two or simply It Takes Two, is a British television programme, the companion show to the popular BBC One programme \"Strictly Come Dancing\".  It is broadcast on weeknights during the run of the main show on BBC Two at 6:30 pm.  Claudia Winkleman originally presented the show, however she left in 2011 and now presents the main show.  Since 2011, Zoë Ball has presented the show.\n\nQuestion: When was the Australian-British dancer who was one of the judges of \"Strictly Come Dancing\" born\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Australian-British dancer and judge.\"\n    },\n    \"role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the person on the show.\"\n    },\n    \"show_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television show.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the person.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"role\",\n    \"show_name\",\n    \"birth_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the Australian-British dancer and judge."
      },
      "role": {
        "type": "string",
        "description": "The role of the person on the show."
      },
      "show_name": {
        "type": "string",
        "description": "The name of the television show."
      },
      "birth_date": {
        "type": "string",
        "description": "The birth date of the person."
      }
    },
    "required": [
      "person_name",
      "role",
      "show_name",
      "birth_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
