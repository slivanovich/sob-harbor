{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe New Adventures of Pinocchio (film): The New Adventures of Pinocchio is a 1999 theatrical film that is a sequel to the 1996 film, \"The Adventures of Pinocchio\".  The film was directed by Michael Anderson and featured Martin Landau reprising his role as Geppetto with Udo Kier reprising his role as Lorenzini, but also playing Lorenzini's widow Madame Flambeau.  The film also featured Sarah Alexander, Simon Schatzberger, Warwick Davis and Ben Ridgeway, and introduced Gabriel Thomson as Pinocchio.  As of 2017, this is the last film Michael Anderson directed.\n\nFix Your Face: Fix Your Face is the first DJ mix released by TRV$DJAM.  It features Travis Barker on drums and DJ AM spinning records.  It was released online on August 27, 2008.\n\nJLA Adventures: Trapped in Time: JLA Adventures: Trapped in Time is a direct-to-video animated film featuring the Justice League of America.  It was first released on January 21, 2014 on DVD, and features Diedrich Bader, Travis Willingham and Kevin Michael Richardson, reprising their roles as Batman, Gorilla Grodd and Black Manta respectively.\n\nJustice League: Doom: Justice League: Doom is a 2012 direct-to-video animated superhero film, loosely based on \"\", a 2000 comic book storyline by writer Mark Waid that ran in the DC Comics series \"JLA\".  The film's script was adapted by writer Dwayne McDuffie, and it is directed by Lauren Montgomery.  A sequel to \"\", the film uses the same character designs by the lead character designer, Phil Bourassa as well as footage from the film in the opening.  It was released on February 28, 2012.  The film also features various actors reprising their roles from the \"DC animated universe\" and \"\" respectively.  It is the 13th film in the DC Universe Animated Original Movies line.\n\nDope Boys: \"Dope Boys\" is the second single from The Game's third studio album, \"LAX\".  The song features Travis Barker playing the drums.  The song samples \"Eleanor Rigby\" By The Beatles.\n\nFix Your Face Vol. 2 - Coachella '09: FIX YOUR FACE VOL.  2 - Coachella '09 is the second DJ mix released by TRV$DJAM.  It features Travis Barker on drums and DJ AM spinning records.\n\nBart Allen: Bart Allen is a fictional superhero in the DC Comics Universe .  Allen first appeared as the superhero Impulse, a teenage sidekick of the superhero the Flash, before later on becoming the second hero known as Kid Flash.  The character first made a cameo appearance in \"The Flash\" #91 in 1994, while his first full appearance in issue #92, and appeared as the lead character in \"Impulse\" (1995–2002) and \"The Flash: The Fastest Man Alive\" (2006–2007).  In the latter series, the character became the fourth hero to assume the identity of The Flash.  Bart also prominently features in the superhero team titles \"Young Justice\" and \"Teen Titans\".  As the Flash, Bart was also a core character in 10 issues of \"Justice League of America\".\n\nWally West: Wally West is a fictional superhero that appears in American comic books published by DC Comics.  He is the first Kid Flash and the third Flash.  His power consists mainly of superhuman speed.  He made his first appearance as the Kid Flash in the \"Flash #110\" in 1959.  Wally took up the mantle of the Flash following the death of Barry Allen from 1986 to 2009 in DC's main lineup.  His physical appearance is generally a redhead with green eyes, and is generally portrayed with a lighthearted, comical, and caring personality.  Wally has an important role as the Flash in DC Rebirth (2016).\n\nCaptain Cold: Captain Cold (Leonard Snart) is a fictional supervillain appearing in American comic books published by DC Comics.  Captain Cold is the leader of the Rogues, a loose criminal association, as well as the older brother of Golden Glider.  He also has served as a bitter enemy to the Silver Age Flash Barry Allen, both enemy and grudging friend to the third Flash Wally West, and one of the killers of the fourth Flash Bart Allen.\n\nGorilla Grodd: Gorilla Grodd is a fictional supervillain appearing in American comic book published by DC Comics, primarily as an enemy of The Flash.  The character first appeared in \"The Flash\" #106 (May 1959) and he was created by John Broome and Carmine Infantino.  Gorilla Grodd is an evil and super-intelligent gorilla who gained mental powers after being exposed to the radiation of a meteorite.\n\nQuestion: JLA Adventures: Trapped in Time features Travis Willingham reprising his role as what fictional supervillian who is primarily the enemy of The Flash?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"character_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"character_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character portrayed by the actor.\"\n        },\n        \"character_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of character, e.g., 'supervillain' or 'superhero'.\"\n        },\n        \"primary_enemy_of\": {\n          \"type\": \"string\",\n          \"description\": \"The hero the character is primarily an enemy of.\"\n        }\n      },\n      \"required\": [\n        \"character_name\",\n        \"character_type\",\n        \"primary_enemy_of\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"actor_name\",\n    \"character_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "character_details": {
        "type": "object",
        "properties": {
          "character_name": {
            "type": "string",
            "description": "The name of the character portrayed by the actor."
          },
          "character_type": {
            "type": "string",
            "description": "The type of character, e.g., 'supervillain' or 'superhero'."
          },
          "primary_enemy_of": {
            "type": "string",
            "description": "The hero the character is primarily an enemy of."
          }
        },
        "required": [
          "character_name",
          "character_type",
          "primary_enemy_of"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "actor_name",
      "character_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
