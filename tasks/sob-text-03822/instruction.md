{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGazelle (New-Gen): Gazelle (Elle) is a fictional character, a superhero appearing in American comic books published by Marvel Comics.  The character appears in the NEW-GEN comic books.  Created by Chris Matonti, J.D. Matonti, and Julia Coppola, she first appeared in NEW-GEN #1 (2010).  He was one of the children from the world of NEW-GEN granted extraordinary abilities by Deadalus' nanobot infestation.  She is a founding member of the A.P.N.G. superhero team.\n\nMister Fantastic: Mister Fantastic (Reed Richards) is a fictional superhero appearing in American comic books published by Marvel Comics.  The character is a founding member of the Fantastic Four.  Richards possesses a mastery of mechanical, aerospace and electrical engineering, chemistry, all levels of physics, and human and alien biology. \" BusinessWeek\" listed Mr. Fantastic as one of the top ten most intelligent fictional characters in American comics.  He is the inventor of the spacecraft that was bombarded by cosmic radiation on its maiden voyage, granting the Fantastic Four their powers.  Richards gained the ability to stretch his body into any shape he desires.\n\nDiamond (comics): Diamond (Kent Chang) is a fictional character, a superhero appearing in American comic books published by Marvel Comics.  The character appears in the NEW-GEN comic books.  Created by Chris Matonti, J.D. Matonti, and Julia Coppola, he first appeared in NEW-GEN #1 (2010).  He was one of the children from the world of NEW-GEN granted extraordinary abilities by Deadalus' nanobot plague.  He is a founding member of the A.P.N.G.\n\nDie-Cut (comics): Die-Cut (real name: Czorn Yson) is a fictional character appearing in American comic books published by Marvel Comics.  The character appears in comic books published by the Marvel UK imprint.  He first appeared in \"Death's Head II & the Origin of Die-Cut\" #1 (1993).  Die-Cut then co-starred in another miniseries, \"Die-Cut vs G-Force\", before receiving his own \"Die-Cut\" limited series in November 1993.\n\nDeadalus (comics): Sylvester Deadalus (Sly) is a fictional character, a supervillain appearing in American comic books published by Marvel Comics.  The character appears in the NEW-GEN comic books.  Created by Chris Matonti, J.D. Matonti, and Julia Coppola, he first appeared in NEW-GEN #1 (2010).\n\nCarlie Cooper: Carlie Cooper is a fictional character appearing in American comic books published by Marvel Comics.  The character appears in comic books centered on Spider-Man.  She is named after Joe Quesada's daughter.  Carlie is friends with Peter Parker (Spider-Man), Harry Osborn, Vin Gonzales, and Lily Hollister.  She is one of the first potential romantic interests for Parker following his long relationship with Mary Jane Watson in the \"\" story arc and eventually becomes his girlfriend for a time.\n\nIron Lad: Iron Lad (Nathaniel \"Nate\" Richards) is a fictional superhero appearing in American comic books published by Marvel Comics.  The character appears in particular in \"Young Avengers\", a team of which Iron Lad is a member.  He first appeared in \"Young Avengers\" #1 (April 2005), created by writer Allan Heinberg and illustrator Jim Cheung.  He is an adolescent version of Kang the Conqueror, armed with a bio-metal suit that responds to mental commands.  He is named after the father of Reed Richards.\n\nFlyer (New-Gen): Flyer (Jude Jackson) is a fictional character, a superhero appearing in American comic books published by Marvel Comics.  The character appears in the NEW-GEN comic books.  Created by Chris Matonti, J.D. Matonti, and Julia Coppola, he first appeared in NEW-GEN #1 (2010).  He is a founding member of the A.P.N.G., and gained his powers when Deadalus released a nanobot plague on the world of New-Gen.\n\nGabriel (New-Gen): John Gabriel is a fictional character, a superhero appearing in American comic books published by Marvel Comics.  The character appears in the NEW-GEN comic books.  Created by Chris Matonti, J.D. Matonti, and Julia Coppola, he first appeared in NEW-GEN #1 (2010).  He is the founder and leader of the A.P.N.G., and the leading scientific mind in the field of nanotechnology on the world of New-Gen.\n\nValeria Richards: Valeria Meghan Richards is a fictional character of Marvel Comics, the daughter of Mister Fantastic (Reed Richards) and the Invisible Woman (Susan Storm Richards), husband and wife and two original members of the superhero team the Fantastic Four.  She is the younger sister of Franklin Richards (though because of time travel she has sometimes been older than her brother).  Valeria made her first appearance under the name Valeria von Doom and the code name Marvel Girl.\n\nQuestion: Who is the publisher of American comic books in which Valeria Meghan Richards, a fictional character appears in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the fictional character.\"\n    },\n    \"publisher\": {\n      \"type\": \"string\",\n      \"description\": \"The publisher of the American comic books featuring the character.\"\n    },\n    \"is_fictional\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the character is fictional.\"\n    }\n  },\n  \"required\": [\n    \"character_name\",\n    \"publisher\",\n    \"is_fictional\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "character_name": {
        "type": "string",
        "description": "The full name of the fictional character."
      },
      "publisher": {
        "type": "string",
        "description": "The publisher of the American comic books featuring the character."
      },
      "is_fictional": {
        "type": "boolean",
        "description": "Indicates if the character is fictional."
      }
    },
    "required": [
      "character_name",
      "publisher",
      "is_fictional"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
