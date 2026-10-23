{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOla Jordan: Aleksandra \"Ola\" Jordan (\"née\" Grabowska; born 30 September 1982) is a Polish professional ballroom dancer.  She appeared as a professional on the British TV show \"Strictly Come Dancing\" from 2006 to 2015.  After winning a championship event in her native Poland, Jordan moved to England and began a new partnership with James Jordan.  They married on 12 October 2003 and live near Maidstone in Kent.\n\nJoanne Clifton: Joanne Kirsty Clifton (born 24 October 1983), also known as Jo, is a British professional dancer, presenter, actress, singer.  born in Waltham, Lincolnshire.  She won the World Ballroom Showdance Championship in 2013 and also won the European Professional Ballroom Championship and World Dancesport Games.  She has been a professional dancer on the BBC TV series \"Strictly Come Dancing\" since 2014, winning the Christmas Special in 2015 with Harry Judd who was series 9 champion and the fourteenth series in 2016 with Ore Oduba.  Also appearing as an expert presenter on \"\" in 2015.\n\nJonathan Wilkins: Jonathan Wilkins is an English ballroom dancer and dance teacher, born in London.  He holds many titles in Professional Ballroom Dancing including being 10 times Professional Ballroom Champion, 1997 - 2007 ( in a partnership with Katusha Demidova which lasted eleven years, and brought considerable success).  In 2004 they won the World Classic Showdance Championship, which is one of the subsidiary World Dance Council Dance Sport events.  Their final result was to win the WDC Open Professional Ballroom title at the USA Open in Orlando, Florida 2007.\n\nLen Goodman: Leonard Gordon Goodman (born 25 April 1944) is an English professional ballroom dancer, dance judge, and coach.\n\nStrictly Come Dancing: Strictly Come Dancing (informally known as Strictly) is a British television dance contest, featuring contestants, celebrities, and other people, from all walks of life, with professional dance partners competing in a ballroom and Latin dance competition.  Each couple is scored out of 10 by a panel of judges.  The title of the show suggests a continuation of the long-running series \"Come Dancing\", with an allusion to the film \"Strictly Ballroom\".  The format has been exported to over 40 other countries, and has also inspired a modern dance-themed spin-off \"Strictly Dance Fever\".  The show is currently presented by Tess Daly and Claudia Winkleman.\n\nDianne Buswell: Dianne Buswell (born 1989) is an Australian ballroom dancer.  She has appeared on \"So You Think You Can Dance Australia\" and was a professional dancer on the Australian version of \"Dancing with the Stars\" in 2015.  Buswell became a professional dancer on \"Strictly Come Dancing\" beginning in 2017.\n\nPaul Killick: Paul Killick is a British professional ballroom dancer and an International Latin American Dance Champion.  He appeared in the first two series of the television show \"Strictly Come Dancing\".  Killick specialises in Latin dance and has won international titles including The World Cup, World Trophy, World Masters, World Series, Universal and British Professional Latin American DanceSport Championships.  Killick is also a choreographer, coach, television personality, dance judge, world-class adjudicator and the owner and director of the Arthur Murray International flagship studio in Beverly Hills.\n\nAnton du Beke: Anthony Paul Beke (born 20 July 1966), known professionally as Anton du Beke, is a British ballroom dancer and television presenter, best known as a professional dancer on the BBC One celebrity dancing show \"Strictly Come Dancing\" since the show began in 2004.  In 2009, he presented the UK version of \"Hole in the Wall\", for the BBC, replacing Dale Winton after being a team captain in 2008.\n\nBrendan Cole: Brendan Cole (born 23 April 1976) is a New Zealand ballroom dancer, specialising in Latin American dancing.  He is most famous for appearing as a professional dancer on the BBC One show, \"Strictly Come Dancing\".  From 2005 to 2009, he was a judge on the New Zealand version of the show, \"Dancing with the Stars\".\n\nStrictly Come Dancing (series 8): Strictly Come Dancing returned for its eighth series on BBC One with a red carpet launch show on 11 September 2010, and the competitive live shows began on 1 October.  The series concluded on 18 December when Kara Tointon and Artem Chigvintsev won the competition.  According to BARB data, this series was the consistently highest rated of the show to date, peaking at 14.28 million viewers.  Len Goodman, Bruno Tonioli, Craig Revel Horwood and Alesha Dixon returned as judges.\n\nQuestion: Which judge of Strictly Come Dancing is a professional ballroom dancer?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"judge_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the judge.\"\n    },\n    \"is_professional_ballroom_dancer\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the person is a professional ballroom dancer.\"\n    },\n    \"judged_show\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the TV show they judged.\"\n    },\n    \"judge_role_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of their role as a judge from the context.\"\n    }\n  },\n  \"required\": [\n    \"judge_name\",\n    \"is_professional_ballroom_dancer\",\n    \"judged_show\",\n    \"judge_role_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "judge_name": {
        "type": "string",
        "description": "The name of the judge."
      },
      "is_professional_ballroom_dancer": {
        "type": "boolean",
        "description": "True if the person is a professional ballroom dancer."
      },
      "judged_show": {
        "type": "string",
        "description": "The name of the TV show they judged."
      },
      "judge_role_description": {
        "type": "string",
        "description": "A description of their role as a judge from the context."
      }
    },
    "required": [
      "judge_name",
      "is_professional_ballroom_dancer",
      "judged_show",
      "judge_role_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
