{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLobbyist (TV series): Lobbyist (), originally titled Angel, was a 2007 South Korean television series produced by Korea Pictures International, Inc. that aired on SBS.  Budgeted at ₩12 million , overseas filming locations included the United States and Kyrgyzstan.  It starred Song Il-gook, Han Jae-suk and Jang Jin-young (in her last performance).\n\nJang Jin-young (singer): Jang Jin-young (born July 1, 1983) is a South Korean singer and the former lead singer of the boy group Black Beat.  He's currently more active as a vocal trainer for S.M. Entertainment's artists, particularly SHINee, EXO and Red Velvet.\n\nS.M. Entertainment: S.M. Entertainment () is a South Korean entertainment company established in 1995 by Lee Soo-man.  It is currently one of the largest entertainment companies in South Korea.  The company operates as a record label, talent agency, music production company, event management and concert production company, and music publishing house.\n\nScent of Love: Scent of Love (국화꽃 향기 lit.  Scent of Chrysanthemums) is a 2003 South Korean film, and the directorial debut of Lee Jeong-wook.  The film is based on a novel of the same name by Kim Ha-in, and stars Jang Jin-young and Park Hae-il in the lead roles.  Like her character, Jang Jin-young battled stomach cancer and died in 2009.  The film received an around of 900,000 admissions nationwide and on May 16, 2003 the film was screened at the Cannes Film Festival.\n\nBetween Love and Hate: Between Love and Hate (also known as The Unbearable Lightness of Dating) is a 2006 South Korean film starring Kim Seung-woo and Jang Jin-young, and is the directorial debut of screenwriter Kim Hae-gon.  Jang's performance won her Best Actress at the 2006 Korean Film Awards.  This would be Jang Jin-young's final film before her death almost 3 years later.\n\nSingles (2003 film): Singles is a 2003 South Korean romantic comedy film starring Jang Jin-young, Uhm Jung-hwa, Lee Beom-soo, and Kim Joo-hyuk.  It is based on the novel \"Christmas at Twenty-nine\" by Japanese writer Kamato Toshio.  The film was one of the highest grossing Korean films of all time earning 2,203,164 admissions nationwide.\n\nBlack Beat: Black Beat (블랙 비트) was a South Korean boy band formed by SM Entertainment.  The seven-member group released an album \"Volume 1 - Black Beat #2002\" in 2002.  They have not promoted as a group since SM Town 2006.  Several members are active as choreographers and vocal trainers for other SM Entertainment artists.  In 2007, lead vocalist Jang Jin-young teamed up with Kim Sung-pil to form the R&B duo, ByJinSung.\n\nSorum: Sorum is a 2001 South Korean horror film and the feature film debut of director Yoon Jong-chan.  Starring Kim Myung-min and Jang Jin-young, it tells the story of a young taxi driver who moves into a dilapidated old apartment building, the site of a brutal tragedy thirty years earlier.  The film has been nominated for and won several awards.\n\nPark Kyung-won: Park Kyung-won (24 June 1901 – 7 August 1933) was, along with Kwon Ki-ok of the Republic of China Air Force, one of the earliest Korean female aviators. Though it is generally agreed that Kwon was the first female pilot, Park is still recognised as the first Korean female civilian pilot, as Kwon was trained by the Republic of China Air Force.  She was the subject of the controversial 2005 South Korean film \"Blue Swallow\", in which she was portrayed by actress Jang Jin-young.\n\nJang Jin-young: Jang Jin-young (; June 14, 1974 – September 1, 2009) was a South Korean actress.  Her death came after a year-long battle with stomach cancer.\n\nQuestion: Jang Jin-young is currently more active as a vocal trainer for a company established in which year ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"vocal_trainer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who is a vocal trainer.\"\n    },\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the entertainment company.\"\n    },\n    \"company_establishment_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the company was established.\"\n    }\n  },\n  \"required\": [\n    \"vocal_trainer_name\",\n    \"company_name\",\n    \"company_establishment_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "vocal_trainer_name": {
        "type": "string",
        "description": "The name of the person who is a vocal trainer."
      },
      "company_name": {
        "type": "string",
        "description": "The name of the entertainment company."
      },
      "company_establishment_year": {
        "type": "integer",
        "description": "The year the company was established."
      }
    },
    "required": [
      "vocal_trainer_name",
      "company_name",
      "company_establishment_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
