{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTwo-Face: Two-Face (Harvey Dent) is a fictional supervillain appearing in American comic books published by DC Comics, commonly as an adversary of the superhero Batman.  The character was created by Bill Finger and Bob Kane and first appeared in \"Detective Comics\" #66 (Aug. 1942).  As one of Batman's most enduring enemies, Two-Face belongs to the collective of adversaries that make up Batman's rogues gallery.\n\nRa's al Ghul: Ra's al Ghul (Arabic: رأس الغول‎ ‎ \"Raʾs al-Ġūl\"; \"Ghoul's Head\" or \"Demon's Head\") is a fictional supervillain appearing in American comic books published by DC Comics, commonly as an adversary of the superhero Batman.  Created by editor Julius Schwartz, writer Dennis O'Neil and artist Neal Adams, the character first appeared in \"Batman\" #232's \"Daughter of the Demon\" (June 1971).  The character is one of Batman's most enduring enemies and belongs to the collective of adversaries that make up Batman's rogues gallery, though given his high status as a supervillain, he has also come into conflict with Superman and other superheroes in the DC Universe.\n\nBlack Mask (comics): Black Mask (Roman Sionis) is a fictional supervillain appearing in comic books published by DC Comics.  Created by Doug Moench and Tom Mandrake, he first appeared in \"Batman\" #386 (Aug. 1985).  The character is a brutally sadistic kingpin in Gotham City's criminal underworld who has a fixation with masks.  Black Mask is an adversary of the superhero Batman and belongs to the collective of enemies that make up his rogues gallery.\n\nDr. Doom (disambiguation): Doctor Doom (real name Doctor Victor von Doom, or Dr. Doom for short) is a Marvel comic book supervillain.  The name may also refer to:\n\nRogues gallery: A rogues gallery (or rogues' gallery) is a police collection of pictures or photographs of criminals and suspects kept for identification purposes.  The term is also used figuratively for any group of shady characters or the line-up of \"mugshot\" photographs that might be displayed in the halls of a dormitory or workplace or on an online mugshot publishing website.\n\nDoctor Doom: Doctor Victor Von Doom (or simply Doctor Doom) is a fictional supervillain appearing in American comic books published by Marvel Comics.  The son of Romani witch Cynthia Von Doom, Doctor Doom traditionally has been the archenemy of the Fantastic Four, and the leader of the fictional nation of Latveria.  He is both a genius inventor and a sorcerer.  While his chief opponents have been the Fantastic Four, he has also come into conflict with Iron Man, Spider-Man, Black Panther, the Avengers and multiple others.  Doom has been depicted as a superhero, taking up the mantle of Iron Man from Tony Stark, and going on to join the Avengers.\n\nDoom 2099: Doom 2099 (Victor Von Doom) is a fictional anti-hero appearing in American comic books published by Marvel Comics.  The character was primarily featured in the Marvel 2099 series \"Doom 2099\".  The character is based on Doctor Doom, created by Stan Lee and Jack Kirby.  The series was written by John Francis Moore for its first two years, and by Warren Ellis for its third.\n\nBlizzard (comics): Blizzard is a fictional character, a supervillain appearing in American comic books published by Marvel Comics.  The character is usually depicted as a member of Iron Man's rogues gallery.\n\nDoctor Doom's Fearfall: Doctor Doom's Fearfall is a space shot ride located in the Islands of Adventure theme park at Universal Orlando Resort.  As the name suggests, the ride is themed after the superhero team Fantastic Four archenemy, Doctor Doom.  The ride opened on May 28, 1999.\n\nDoomquest: \"Doomquest\" is a two-issue Iron Man story arc written by David Michelinie and Bob Layton with art by John Romita Jr. and published by Marvel Comics.  The arc first appears in \"Iron Man\" #149-#150.  One of the most popular stories of the title character, it establishes Doctor Doom as a member of his rogues gallery, a villainous counterpart who mirrors the superhero with his wealth, power armor and engineering skill.\n\nQuestion: Who wrote Doomquest which establishes Doctor Doom as a member of his rogues gallery?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"story_arc_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the comic book story arc.\"\n    },\n    \"writers\": {\n      \"type\": \"array\",\n      \"description\": \"The writers of the comic book story arc.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"established_villain\": {\n      \"type\": \"string\",\n      \"description\": \"The villain whose rogues gallery membership is established by this story arc.\"\n    },\n    \"established_hero_rogues_gallery\": {\n      \"type\": \"string\",\n      \"description\": \"The superhero whose rogues gallery the villain is established to be a part of.\"\n    }\n  },\n  \"required\": [\n    \"story_arc_name\",\n    \"writers\",\n    \"established_villain\",\n    \"established_hero_rogues_gallery\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "story_arc_name": {
        "type": "string",
        "description": "The name of the comic book story arc."
      },
      "writers": {
        "type": "array",
        "description": "The writers of the comic book story arc.",
        "items": {
          "type": "string"
        }
      },
      "established_villain": {
        "type": "string",
        "description": "The villain whose rogues gallery membership is established by this story arc."
      },
      "established_hero_rogues_gallery": {
        "type": "string",
        "description": "The superhero whose rogues gallery the villain is established to be a part of."
      }
    },
    "required": [
      "story_arc_name",
      "writers",
      "established_villain",
      "established_hero_rogues_gallery"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
