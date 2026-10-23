{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAchamillai Achamillai: Achamillai Achamillai (lit.  \"Fearless\") is a 1984 Indian Tamil-language political satire film directed by K. Balachander.  It stars Rajesh and Saritha in the lead with Pavithra, Delhi Ganesh and Charle in other prominent roles.  The film deals with party switching and depicts its influence on the lives of small-time politicians.  The film met with critical acclaim, winning three awards at the 32nd Filmfare Awards South, as well as the National Film Award for Best Feature Film in Tamil.  The title refers to a popular poem composed by Bharathiyar.\n\nOmar Fadel: Omar Fadel is an award winning, Los Angeles based composer for film, television, and video games.  He is also a multi-instrumentalist, whose scores frequently feature him on a wide array of instruments, including guitar, piano, cello, drums and percussion.  Omar’s work can be heard in numerous films, television shows and video games, namely the global game franchise , The Dictator, and the Oscar nominated film, Day One.\n\nThe Dictator (2012 film): The Dictator is a 2012 British-American political satire black comedy film co-written by and starring Sacha Baron Cohen as his fourth feature film in a leading role.  The film is directed by Larry Charles, who previously directed Baron Cohen's mockumentaries \"Borat\" and \"Brüno\".  Baron Cohen, in the role of Admiral General Aladeen, the dictator of the fictional Republic of Wadiya visiting the United States, stars alongside Anna Faris, Ben Kingsley, Jason Mantzoukas, and an uncredited appearance by John C. Reilly.\n\nCircus Palestine: Circus Palestine (Hebrew: קרקס פלשתינה‎ ‎ , translit.  Kirkas Palestina) is a 1998 Israeli political satire film directed by Eyal Halfon, which was nominated for seven Israeli Film Academy Awards, winning five.  The film was selected as the Israeli entry for the Best Foreign Language Film at the 71st Academy Awards, but was not accepted as a nominee.\n\nThe United: The United (Arabic: المتحدين) is an unreleased film produced by Touchstone Pictures.  It was conceived as Disney's first ever Arabic-language film, intended primarily for Middle Eastern audiences.  Produced by Rachel Gandin, \"The United\" was directed by Amin Matalqa, written by Nizar Wattad, and features performances from Farouk Al-Fishawy, Waleed Zuaiter, Bosaina, and Amir Scandar.  It was shot in and around Amman, Jordan in January 2011 by veteran cinematographer Ray Peschke, and edited by Debbie Berman.  In addition to an original score by composer, Omar Fadel, the United also features a vocal collaboration between three of the Arab world's best known rappers, Omar Offendum, Deeb, and Salah Edin.\n\nJames Dorsa: James Dorsa is a composer and harpsichordist who is currently a member of the faculty at California State University Northridge's Music Department. .  He is most recognized for his award winning composition of Jupiter's Moons.\n\nSaare Jahaan Se Mehnga: Saare Jahaan Se Mehnga is a 2013 Bollywood satire film directed by Anshul Sharma starring Sanjay Mishra and Pragati Pandey.  Written by Rupesh Thapliyal and Vijay Manral, Lyrics by Naveen Tyagi the film also has Ranjan Chhabra, Disha, Vishwa Mohan Badola, Pramod Pathak, Zakir Hussain and Sitaram Panchal.  \"Saare Jahaan Se Mehnga...\", produced by Ashok Pandey under the banner of Revel Films, is a satire on the rising prices in the country.\n\n1. April 2000: 1.  April 2000 is a 1952 political satire film directed by Wolfgang Liebeneiner and starring Hilde Krahl, made during the Allied Occupation of Austria (1945–55).  The script was reportedly commissioned at the request of the Austrian government, and is a political satire depicting a harmless, potentially congenial future Austria still subject to needless and stifling oversight by the four Allied powers, as established following the defeat of Nazi Germany in World War II (as it was when the film was made).  The film was entered into the 1953 Cannes Film Festival.\n\nThe Warning (2015 film): The Warning is a 2015 American horror and thriller film directed by Dirk Hagen, written by Summer Moore, and starring Moore, Jeff Allen, and Tiffany Joy Williams.  The film is a Found footage satire film based on true accounts of the satanic panic in the 1980s-1990s, that is filmed in the \"Devil Worshipping Capital of the Western World\" Manitou Springs, Colorado.\n\nBad Kids Go to Hell: Bad Kids Go to Hell is a 2012 dark comedy thriller film directed by Matthew Spradlin, who co-wrote it with Barry Wernick.  Based on Spradlin and Wernick's best-selling graphic novel of the same name, the film stars Amanda Alch, Marc Donato, Augie Duke, Roger Edwards, Ali Faulkner, and Cameron Deane Stewart as six prep school students, who serve detention in a seemingly haunted school library.  It had a limited theatrical release on October 27, 2012.  On December 7, 2012, it was released nationwide.  The film was also screened at various public destinations across the U.S.\n\nQuestion: Omar Fadel's award winning composition can be found in the 2012 dark British satire film directed by what director?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\"\n        },\n        \"genres\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        },\n        \"nationalities\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"genres\",\n        \"nationalities\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"composer_name\": {\n      \"type\": \"string\"\n    },\n    \"director_name\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"film_details\",\n    \"composer_name\",\n    \"director_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          },
          "genres": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "nationalities": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "title",
          "release_year",
          "genres",
          "nationalities"
        ],
        "additionalProperties": false
      },
      "composer_name": {
        "type": "string"
      },
      "director_name": {
        "type": "string"
      }
    },
    "required": [
      "film_details",
      "composer_name",
      "director_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
