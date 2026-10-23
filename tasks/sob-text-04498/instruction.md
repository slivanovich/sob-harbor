{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHercules: Zero to Hero: Hercules: Zero to Hero is a 1999 comedy-drama adventure and fantasy animated television film produced by Walt Disney Television Animation, Walt Disney Animation Australia, Walt Disney Animation Japan and Toon City Animation, Inc., Manila, Philippines.  The film is a direct-to-video followup to 1997 animated feature \"Hercules\".  It was released on August 17, 1999.  The film serves as a package film combing three episodes of \"Hercules: The Animated Series\" as flashback segments.\n\nThe Sons of Hercules: The Sons of Hercules was a syndicated Embassy Pictures television show that aired in the United States of America in the 1960s.  The series repackaged 14 Italian sword-and-sandal films by giving them a standardized theme song for the opening and closing titles, as well as a standard introductory narration attempting to relate the lead character in each film to the Greek demigod Hercules.  These films however were not all originally made as \"Hercules\" films in Italy.  Although two of them did originally feature Hercules (and not his sons), four of the films were originally Maciste movies in Italy, two of them were originally Ursus movies, and the other six were just isolated gladiator or mythological hero movies not released theatrically in the US.\n\nUrsus (film): Ursus (also known as \"Mighty Ursus\") is a 1961 Italian peplum film directed by Carlo Campogalliani.  The film was later adapted for the American television film package, \"The Sons of Hercules\", where it was retitled \"\"Ursus, Son of Hercules\"\" (although Ursus was not at all related to Hercules in the original Italian version).  It was released in France as \"La fureur d'Hercule\" (\"The Fury of Hercules\").  \"The Mighty Ursus\" was originally released in the US on a double bill with \"Jack, the Giant Killer\" (1962) before being sold to television in the U.S.\n\nSnegithiye: Snegithiye (English:Oh Friend! \" (female)\" ) is a 2000 Tamil mystery thriller film directed by Priyadarshan.  The story is loosely based on the 1999 Marathi film \"Bindhaast\" written by Chandrakant Kulkarni.  The film notably features only female characters in the lead roles, played by Jyothika, Sharbani Mukherjee, Tabu and Ishita Arun.  Music was composed by Vidyasagar.  The film, released in 2000, proved to be an average grosser at the box office but bagged positive reviews from critics.  Today, it is considered a cult classic that was underrated at the time of its release.  Originally planned to be made as a bilingual, in Tamil and in Malayalam, the film released first in Tamil only, while the Malayalam dubbed version, \"Raakilipattu\", as well as the dubbed Hindi version, \"Friendship\", released seven years later.\n\nHercules (1997 film): Hercules is a 1997 American animated musical fantasy comedy film produced by Walt Disney Feature Animation for Walt Disney Pictures.  The 35th Disney animated feature film, the film was directed by Ron Clements and John Musker.  The film is loosely based on the legendary hero Heracles (known in the film by his Roman name, Hercules), the son of Zeus, in Greek mythology.  The film also featured the first positive portrayal of African American women in a Disney animated film.\n\nThe Legend of Hercules: The Legend of Hercules is a 2014 American 3D action fantasy film directed by Renny Harlin, written by Daniel Giat and Sean Hood, and starring Kellan Lutz, Gaia Weiss, Scott Adkins, Roxanne McKee and Liam Garrigan.  It was one of two Hollywood-studio Hercules films released in 2014, with Paramount Pictures' and MGM's co-production \"Hercules\".  It was released on January 10, 2014.  It was a box-office bomb and gained extremely poor reviews, unlike the latter film which was a modest box-office and opened to far stronger reviews.\n\nToys in the Attic (2009 film): Toys in the Attic (Czech: Na půdě aneb Kdo má dneska narozeniny?  ; festival title: In the Attic: Who Has a Birthday Today?)  is a 2009 Czech-French-Japanese-Slovak primarily stop-motion animated fantasy comedy thriller family film directed by Jiří Barta and written by Edgar Dutka and Barta which depicts a community of toys and other objects in an attic who come to life when no human is around.  It is an international co-production of Czech, Japanese and Slovak companies.  The film was released first in the Czech Republic on 5 March 2009 and has been shown subtitled at film festivals internationally.  An American dub – adapted, produced and directed by Vivian Schilling and performed by actors including Forest Whitaker, Joan Cusack, Cary Elwes and Schilling herself – has been recorded, which the film was first shown with on 3 March 2012 at the New York International Children's Film Festival and was released nationally on 24 August 2012 by Hannover House.\n\nDisney's Animated Storybook: Hercules: Disney's Animated Storybook: Hercules is the seventh entry in the \"Disney's Animated Storybook\" point-and-click adventure interactive storybook PC game series, based on theatrical and home video releases.  The game is part of Disney's \"Hercules\" franchise, and is specifically based on the 1997 Walt Disney Animation Studios film \"Hercules\", based on the mythical Greek hero Heracles and his defeat of the god of the underworld Hades. \" Disney's Animated Storybook: Hercules\" was developed by Media Station and published by Disney Interactive, who released the game on July 27, 1997.  The game received mixed reviews from critics.\n\nHercules (2014 film): Hercules is a 2014 American 3D action fantasy adventure film directed by Brett Ratner, written by Ryan J. Condal and Evan Spiliotopoulos and starring Dwayne Johnson, Ian McShane, Rufus Sewell and John Hurt.  It is based on the graphic novel \"Hercules: The Thracian Wars\".  Distributed jointly by Paramount Pictures and Metro-Goldwyn-Mayer, it was released on July 25, 2014.  It is one of two Hollywood-studio Hercules films released in 2014, the other one being Lionsgate's \"The Legend of Hercules\".\n\nThe Pacifier: The Pacifier is a 2005 American family comedy film directed by Adam Shankman, written by Thomas Lennon and Robert Ben Garant and stars Vin Diesel.  The film was released in March 2005 by Walt Disney Pictures and grossed $198 million worldwide.  It has a 20% approval rating on Rotten Tomatoes, which called it \"only moderately amusing\".\n\nQuestion: Which film was released first, The Pacifier or Hercules?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"first_film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\"\n        },\n        \"release_month\": {\n          \"type\": \"string\"\n        },\n        \"release_day\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"second_film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\"\n        },\n        \"release_month\": {\n          \"type\": \"string\"\n        },\n        \"release_day\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"release_month\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"earlier_release_film_title\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"first_film_details\",\n    \"second_film_details\",\n    \"earlier_release_film_title\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "first_film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          },
          "release_month": {
            "type": "string"
          },
          "release_day": {
            "type": "integer"
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      },
      "second_film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          },
          "release_month": {
            "type": "string"
          },
          "release_day": {
            "type": "integer"
          }
        },
        "required": [
          "title",
          "release_year",
          "release_month"
        ],
        "additionalProperties": false
      },
      "earlier_release_film_title": {
        "type": "string"
      }
    },
    "required": [
      "first_film_details",
      "second_film_details",
      "earlier_release_film_title"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
