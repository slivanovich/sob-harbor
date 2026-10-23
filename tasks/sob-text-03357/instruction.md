{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNordic Society for Middle Eastern Studies: The Nordic Society for Middle Eastern Studies is a learned society formed in 1989 that is devoted to the promotion of the academic study of the Middle East in the Nordic region.  The Society arranges an academic conference on Middle Eastern studies, held every three years in a different Nordic country.  The 2016 conference was hosted by the University of Southern Denmark in Odense.  The current chairperson of the Nordic Society is Leif Stenberg, who is director of the Center for Middle Eastern Studies at Lund University.\n\nGolden Thread Productions: Golden Thread Productions, is a theatre company founded in 1996 in San Francisco, California that promotes theatre as a forum for cultural exchange, exploring Middle Eastern culture and identity as represented throughout the globe.  The mission is to make theatre a regular part of the Middle Eastern community’s cultural life, and to make the Middle East a regular part of the American theatre experience.  Golden Thread Productions defines the Middle East broadly and inclusively, believing that the common human experience transcends cultural and political differences.  Among the nations represented in past productions are Iran, Armenia, Egypt, Israel, Palestine, Algeria, and Afghanistan.\n\nCNERU: The \"Cordoba Near Eastern Research Unit\" (CNERU), is an interdepartmental and interdisciplinary unit of the Faculty of Humanities of the University of Córdoba (Spain), which offers undergraduate and graduate courses and seminars related to all areas of Near and Middle Eastern Studies and seeks to foster knowledge of Near and Middle Eastern societies from the ancient period to the modern times.  Through its academic activities CNERU also seeks to promote dialogue and understanding on the complexities of the modern Middle East.  CNERU assists with and enhances the dissemination of specialized knowledge of this field through publications and media diffusion in Spanish-speaking countries and abroad.  CNERU was founded in 2012 within the Faculty of Humanities of Cordoba University.\n\nClaudia Roden: Claudia Roden is a cookbook writer and cultural anthropologist based in the United Kingdom.  She is best known as the author of Middle Eastern cookbooks including \"A Book of Middle Eastern Food\", \"The New Book of Middle Eastern Food\" and \"Arabesque—Sumptuous Food from Morocco, Turkey and Lebanon\".\n\nAdriana Miller: Adriana Miller (\"The Legendary Adriana\") was born in Boston, Massachusetts during the Great Depression.  After extensive studying from an early age, she pursued a career in dance, specifically jazz and Middle Eastern.  During her time on stage as a jazz dancer, she worked with big names such as Frank Sinatra and Sammy Davis, Jr. When she transitioned to Middle Eastern dance, she became a trendsetter and is often attributed to being a major player in the renaissance of Middle Eastern dance in Washington, DC.  Her many achievements include teaching, choreography, performing as a professional dancer, producing, acting as an agent, working as a make-up artist, and designing costumes.\n\nJoe Hart: Charles Joseph John \"Joe\" Hart (born 19 April 1987) is an English professional footballer who plays as a goalkeeper for West Ham United, on loan from fellow Premier League club Manchester City, and the England national team.  With over 100 Premier League clean sheets, Hart holds the joint record for the most Premier League Golden Glove awards (four) and has amassed 73 international caps since his debut in 2008.\n\nBrothers of the Baladi: The Brothers of the Baladi is a World music band based in Portland, Oregon, USA, that plays both traditional Middle Eastern music, and also combines traditional Middle Eastern and western sounds and instruments for a unique Worldbeat sound.  Band leader/percussionist/vocalist Michael Beach provides lyrics in Arabic, Turkish, Persian, French, Spanish, Kurdish, Armenian and English, and the band features many traditional Middle Eastern instruments including oud, saz, mizmar, midjwiz, arghool, doumbek, riq, def, tar, bendir and davul.\n\nUmec: Umec is a fictional Middle Eastern country appearing in DC Universe.  Its name is an acronym, standing for \"unnamed middle eastern country\" per its co-creator Greg Rucka.  In \"The Adventures of Superman\", it was occupied by U.S. military forces.  Lois Lane was shot while embedded with the troops.  Like the other fictional DC Middle Eastern countries - Qurac, Syraq, Kahndaq and Bialya - it is supposed to be on the Persian Gulf.\n\nAbdullaziz Al-Dawsari: Abdullaziz Saeed Al-Dawsari (Arabic: عبد العزيز سعيد الدوسري‎ ‎ ; born 11 October 1988) is a Saudi football player.  He currently plays for his country, Saudi Arabia, as well as Al-Hilal in the Saudi Professional League.  In 2012, Al-Dosari was featured on the cover of the Middle Eastern edition of \"FIFA 13\", alongside Lionel Messi and Joe Hart.\n\nIGN Convention: IGN Convention (IGN Con) is a video games, movies, comics and pop culture convention held in various cities in the Middle East.  The event generally includes celebrities, video game tournaments, table top games, card games, movie previews, comic book stalls and a cosplay competition.  A number of Middle Eastern artists and game developers also showcase their work at IGN Convention.  This convention is owned and operated by IGN Middle East, the Middle Eastern edition of popular video games website IGN.\n\nQuestion: Abdullaziz Saeed Al-Dawsari was featured on the cover of the Middle Eastern edition of FIFA13 with a goalkeeper who plays for what country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"main_footballer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the primary footballer mentioned in the context.\"\n    },\n    \"game_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the video game.\"\n    },\n    \"game_edition_region\": {\n      \"type\": \"string\",\n      \"description\": \"The specific regional edition of the game.\"\n    },\n    \"featured_goalkeeper\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the goalkeeper featured alongside the main footballer.\"\n        },\n        \"national_team_country\": {\n          \"type\": \"string\",\n          \"description\": \"The country the goalkeeper plays for on the national team.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"national_team_country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"main_footballer_name\",\n    \"game_title\",\n    \"game_edition_region\",\n    \"featured_goalkeeper\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "main_footballer_name": {
        "type": "string",
        "description": "The name of the primary footballer mentioned in the context."
      },
      "game_title": {
        "type": "string",
        "description": "The title of the video game."
      },
      "game_edition_region": {
        "type": "string",
        "description": "The specific regional edition of the game."
      },
      "featured_goalkeeper": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the goalkeeper featured alongside the main footballer."
          },
          "national_team_country": {
            "type": "string",
            "description": "The country the goalkeeper plays for on the national team."
          }
        },
        "required": [
          "name",
          "national_team_country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "main_footballer_name",
      "game_title",
      "game_edition_region",
      "featured_goalkeeper"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
