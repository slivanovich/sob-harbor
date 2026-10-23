{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2012 Sony Ericsson Open – Women's Singles: Victoria Azarenka was the defending champion but lost to Marion Bartoli in the quarterfinals, which ended Azarenka's 26 match winning streak to start the 2012 season.\n\n2012 US Open – Day-by-day summaries: The Women's single's final featured the then top ranked Victoria Azarenka against then three-time champion Serena Williams.  Williams had beaten Azarenka in the 2012 Wimbledon semifinals and had won her first six matches in the US Open easily without dropping a set.\n\nVictoria Azarenka career statistics: This is a list of the main career statistics of Belarusian professional tennis player, Victoria Azarenka.  To date, Azarenka has won twenty WTA singles titles including two grand slam singles titles, six WTA Premier Mandatory singles titles and three WTA Premier 5 singles titles.  She was also the runner-up at the 2011 WTA Tour Championships, 2012 US Open and 2013 US Open.  Among other achievements, Azarenka was the bronze medalist in women's singles and Gold medalist in mixed doubles with her compatriot, Max Mirnyi at the 2012 London Olympics.\n\n2012 Mutua Madrid Open – Women's Doubles: Victoria Azarenka and Maria Kirilenko were the defending champions but Azarenka chose not to participate in doubles this year. <br>\n\n2009 Sony Ericsson Open – Women's Singles: The 2009 Sony Ericsson Open – Women's Singles was the women's singles event of the 2009 Sony Ericsson Open, a WTA Premier Mandatory tennis tournament held in Key Biscayne, Florida in late March and early April.  World No. 1 Serena Williams was the defending champion and attempting to win a record sixth title at the tournament, but she lost in the final to Victoria Azarenka, 6–3, 6–1.  Azarenka won her third WTA singles title and first at the Premier or above level.\n\n2012 Australian Open – Women's Singles: Kim Clijsters was the defending champion but lost to Victoria Azarenka in the semifinals.  Azarenka went on to win her maiden Grand Slam title in the final, beating 2008 champion Maria Sharapova 6–3, 6–0.\n\n2009 French Open – Mixed Doubles: In the 2009 French Open – Mixed Doubles event Victoria Azarenka and Bob Bryan were the defending champions, but Azarenka chose not to participate, and only Bryan competed in the tournament. <BR>Bryan partnered with Liezel Huber and won in the final 5–7, 7–6(5), 10–7, against Vania King and Marcelo Melo.\n\n2008 US Open – Mixed Doubles: Victoria Azarenka and Max Mirnyi were the defending champions, but Azarenka chose not to participate, and only Mirnyi competed that year.\n\nVictoria Azarenka: Victória Fyódorovna Azárenka (Belarusian: Вікторыя Фёдараўна Азаранка ; Russian: Виктория Фёдоровна Азаренко; born 31 July 1989) is a Belarusian professional tennis player.  She is a former world No. 1.\n\nTony Roche: Anthony Dalton Roche, AO MBE (born 17 May 1945) is a former professional Australian tennis player, native of Tarcutta.  He played junior tennis in the New South Wales regional city of Wagga Wagga.  He won one Grand Slam singles title and thirteen Grand Slam doubles titles, and was ranked as high as World No. 2 by Lance Tingay of \"The Daily Telegraph\" in 1969.  He also coached multi-Grand Slam winning World No. 1s, Ivan Lendl, Patrick Rafter, Roger Federer, Lleyton Hewitt and former World No. 4, Jelena Dokic.\n\nQuestion: Who was born first Victoria Azarenka or Tony Roche?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_born_first\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who was born first.\"\n    },\n    \"person_born_first_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the person born first.\"\n    },\n    \"person_born_second\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who was born second.\"\n    },\n    \"person_born_second_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the person born second.\"\n    },\n    \"age_difference_years\": {\n      \"type\": \"integer\",\n      \"description\": \"The difference in birth years between the two individuals.\"\n    }\n  },\n  \"required\": [\n    \"person_born_first\",\n    \"person_born_first_birth_year\",\n    \"person_born_second\",\n    \"person_born_second_birth_year\",\n    \"age_difference_years\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_born_first": {
        "type": "string",
        "description": "The name of the person who was born first."
      },
      "person_born_first_birth_year": {
        "type": "integer",
        "description": "The birth year of the person born first."
      },
      "person_born_second": {
        "type": "string",
        "description": "The name of the person who was born second."
      },
      "person_born_second_birth_year": {
        "type": "integer",
        "description": "The birth year of the person born second."
      },
      "age_difference_years": {
        "type": "integer",
        "description": "The difference in birth years between the two individuals."
      }
    },
    "required": [
      "person_born_first",
      "person_born_first_birth_year",
      "person_born_second",
      "person_born_second_birth_year",
      "age_difference_years"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
