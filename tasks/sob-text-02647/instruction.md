{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLee Purdy: Lee Purdy (born 29 May 1987) is a retired English boxer from Colchester, Essex, United Kingdom who fights in the welterweight division.  Despite having no amateur career he is a former British champion having won the British welterweight title on 16 April 2011 with a 5th round KO victory over Craig Watson.  He also previously held the Southern Area welterweight title and competed for the Commonwealth belt at the weight against former ABA champion Denton Vassell but was beaten over 12 rounds as Vassell won on a points decision.\n\n12 Rounds (film): 12 Rounds is a 2009 American action film directed by Renny Harlin and produced by WWE Studios.  The cast is led by John Cena, alongside Aidan Gillen, Steve Harris, Gonzalo Menendez, Brian J. White, Ashley Scott, and Taylor Cole.  The film was released to theaters in the United States on March 27, 2009.\n\nGeorge Gardiner (boxer): George Gardner (born March 17, 1877 – July 8, 1954), was a famous Irish-born American boxer who was the first undisputed World Light Heavyweight Champion.  He held claims to both the World Middleweight Title as well as the World Heavyweight Title.  He was the second man in history to hold the World's Light Heavyweight title, defeating the first Light Heavyweight Champion, Jack Root by KO after 12 rounds.\n\nJohnny Wilson (boxer): Johnny Wilson was born Giovanni Panica on March 23, 1893 in Harlem, New York City.  He was a professional boxer who fought from 1911 until 1926.  The highlight of Wilson's career came when he captured the world middleweight championship by defeating Mike O'Dowd by decision over 12 rounds on May 6, 1920.  Wilson held the crown until he was outpointed over 15 rounds by the all-time great Harry Greb.\n\nPaul Edwards (boxer): Paul Edwards (born 1 October 1986) is an English boxer who fights in the flyweight division.  He won the British welterweight title on 15 December 2010 with a victory over Shinny Bayaar after the bout was stopped with Bayaar having received a cut.  Edwards defended the title on 11 June 2011 and lost in his first defence to namesake Chris Edwards via split decision over 12 rounds.\n\n12 Rounds: 12 Rounds is a British rock band formed by Atticus Ross and singer Claudia Sarne, who are married.  After the release of their first album, \"Jitter Juice\", they toured with the Sneaker Pimps.  12 Rounds played the Reading Festival in 1996.  Their song \"Something's Burning\" was featured on the soundtrack to the 1997 film \"All Over Me\", and \"Just Another Day,\" their collaboration with Pale 3, was featured on the soundtrack to the 2000 film \"The Princess and the Warrior\".  The group released a few projects under various record labels before releasing \"My Big Hero\" under Trent Reznor's Nothing Records.  They were the opening act on Marilyn Manson's \"Mechanical Animals\" promo tour that ranged from September to December 1998.  A follow-up album was recorded with Reznor as producer; it remains unreleased.  Ross has nonetheless worked with Reznor on every Nine Inch Nails album since \"With Teeth\" as well as other projects.\n\n12 Rounds 3: Lockdown: 12 Rounds 3: Lockdown (also known as 12 Rounds 3 or 12 Rounds: Lockdown) is a 2015 American action film starring Dean Ambrose in his first American film debut and directed by Stephen Reynolds.  It is the sequel to the 2013 film \"\" starring Randy Orton and directed by Roel Reiné.  It is the third installment in the 12 Rounds trilogy and the second of six films, titled the 'Action Six-Pack' series, to be co-produced by WWE Studios and Lionsgate, who distribute the film.  This is the first film in the series not to be released by 20th Century Fox, and was released in select theaters across the United States, and on demand on September 11, 2015.\n\nJerome Dillon: Jerome Dillon is a professional musician, best known for his tenure as drummer with industrial rock group Nine Inch Nails from 1999–2005.  After his departure, his own project, Nearly, released its debut album \"reminder\" in December 2005, along with a cd maxi-single for the song \"Straight to Nowhere\".  \"All is Lost\", a song from \"reminder\" that Dillon co-wrote with 12 Rounds singer, Claudia Sarne, was featured in the 2008 film, Diary of a Nymphomaniac.  In addition, an authorized limited release live bootleg EP/DVD entitled \"reminder Live 2006\", was released in August 2006.  Dillon has worked as a composer for feature films since 2001.\n\n12 Rounds 2: Reloaded: 12 Rounds 2: Reloaded (also known as 12 Rounds 2 and 12 Rounds: Reloaded) is a 2013 American action film directed by Roel Reiné and produced by WWE Studios.  The film stars Randy Orton, Tom Stevens, Brian Markinson and Cindy Busby.  It is a sequel to the 2009's \"12 Rounds\" starring John Cena.  Unlike the original which saw a theatrical release, the film was released on direct-to-DVD and Blu-ray in the United States on June 4, 2013.\n\nTaylor Cole: Taylor Cole (born April 29, 1984 ) is an American actress and former fashion model.\n\nQuestion: What actress born in 1984 starred in the film \"12 Rounds\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"actress_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the actress.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"role_description\": {\n      \"type\": \"string\",\n      \"description\": \"Description of the actress's role in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"actress_details\",\n    \"role_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "actress_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the actress."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "role_description": {
        "type": "string",
        "description": "Description of the actress's role in the film."
      }
    },
    "required": [
      "film_title",
      "actress_details",
      "role_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
