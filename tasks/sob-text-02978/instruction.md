{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLost Girls: Lost Girls is a graphic novel written by Alan Moore and illustrated by Melinda Gebbie, depicting the sexually explicit adventures of three female fictional characters of the late 19th and early 20th century: Alice from Lewis Carroll's \"Alice's Adventures in Wonderland\" and \"Through the Looking-Glass\", Dorothy Gale from L. Frank Baum's \"The Wonderful Wizard of Oz\", and Wendy Darling from J. M. Barrie's \"Peter and Wendy\".  They meet as adults in 1913 and describe and share some of their erotic adventures with each other.\n\nBritten and Brülightly: Britten and Brülightly is a British graphic novel written and illustrated by Hannah Berry, and published by Random House under their Jonathan Cape imprint on April 3, 2008.\n\nV for Vendetta: V for Vendetta is a British graphic novel written by Alan Moore and illustrated by David Lloyd (with additional art by Tony Weare), published by DC Comics.  Later versions were published by Vertigo, an imprint of DC Comics.  The story depicts a dystopian and post-apocalyptic near-future history version of the United Kingdom in the 1990s, preceded by a nuclear war in the 1980s which had devastated most of the rest of the world.  The fascist Norsefire party has exterminated its opponents in concentration camps and rules the country as a police state.  The comics follow its title character and protagonist, V, an anarchist revolutionary dressed in a Guy Fawkes mask, as he begins an elaborate and theatrical revolutionist campaign to kill his former captors, bring down the fascist state and convince the people to abandon democracy in favour of anarchy, while inspiring a young woman, Evey Hammond, to be his protégé.\n\nAdam Susan: Adam James Susan is a fictional character and the main antagonist of the comic book series (later graphic novel) \"V for Vendetta\", created by writer Alan Moore and illustrator David Lloyd.  He is renamed Adam Sutler (the surname being a portmanteau of \"Susan\" and \"Hitler\") in the film adaptation, in which he is portrayed by John Hurt.\n\nJohn Coulthart: John Coulthart (born 15 March 1962) is a British graphic artist, illustrator, author and designer who has produced book covers and illustrations, CD covers and posters.  He is also the author of the critically acclaimed Lovecraft-inspired book The Haunter of the Dark: And Other Grotesque Visions which contains a collaboration with Alan Moore entitled \"The Great Old Ones\" that is unique to this book and also has an introduction by Alan Moore).\n\nAlan Moore's Magic Words: Alan Moore's Magic Words (ISBN  ) is a graphic novel containing some of comic creator Alan Moore's songs, poems and writings turned into comics or with added art.  All the adaptations are made by writer Art Brooks.  The art was created by various European artists: Fred Torres, Ailantd, Sergio Bleda, Juan Jose Ryp, etc.  It was printed by Avatar Press in both hardback and softback in 2002.  Reprints the original GN published in Europe as Magical Mystery Moore Vol.  1.\n\nThe Diary of Edward the Hamster 1990–1990: The Diary of Edward the Hamster 1990–1990 is a British graphic novel written by Miriam and Ezra Elia.  Published in 2012 in Romanian by Humanitas, and in September 2013 by Penguin Press-owned Blue Rider Press, the book takes the form of a diary of an unhappy pet hamster that Miriam and her brother Ezra once owned.  In the book, Edward is presented as a existentialist diarist, given to writing about his life, his disdain for doing tricks and for the free-roaming but mentally imprisoned family cat—with Edward striving to find meaning before his too-short life comes to an end.\n\nProduction of Watchmen: Watchmen is a 2009 film based on the twelve-issue graphic novel series of the same name created by writer Alan Moore, artist Dave Gibbons, and colorist John Higgins, published by DC Comics between 1986 and 1987.  The graphic novel's film rights were acquired by producer Lawrence Gordon in 1986.  Many problems halted the adaptation's development, with four different studios and various directors and screenwriters being attached to the project through twenty years.  In 2006, Zack Snyder, who at the time was filming 'another comic book adaptation', was hired by Warner Bros. to helm \"Watchmen\".  Filming started in 2007, and following deals with two of the previous companies involved in the development—Paramount Pictures was responsible for international distribution rights after budgetary issues in 2004, resulting in a lawsuit by 20th Century Fox.  Fox, which was already contacted by Gordon in 1987, received $1 million of the gross—the \"Watchmen\" adaptation was finally released in March 2009.\n\nCombat Zone: True Tales of G.I.s in Iraq: Combat Zone: True Tales of GI's in Iraq is a graphic novel written by Karl Zinsmeister.  Penciller Dan Jurgens illustrated the graphic novel with cover art contributed by Esad Ribic.  The title was released as a single volume trade paperback in 2005.  The graphic novel depicted Zinsmeister's journalistic reports on his time with the 82nd Airborne.  Zinsmeister's initial account of his time with the 82nd Airborne was recounted in his book \"Boots on the Ground: a month with the 82nd Airborne in the battle for Iraq\"\n\nTop 10: The Forty-Niners: Top 10: The Forty-Niners is a graphic novel published by America's Best Comics in 2005.  It is a prequel to the ABC series \"Top 10\", a police procedural set in the city of Neopolis, where superpowers, robots, monsters, and other comic fodder are the norm for all citizens.  It was written by Alan Moore, drawn by Gene Ha, and colored by Art Lyon, with lettering, logos, and design by Todd Klein.  Unlike the original series and its spin-off \"Smax\", it was released in one 112 page edition instead of being released in separate issues and collected later.  It won the 2006 Eisner Award in the \"Best Graphic Album: New\" category.\n\nQuestion: What British graphic novel written by Alan Moore included antagonist Adam James Susan?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"graphic_novel_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the graphic novel.\"\n    },\n    \"writer\": {\n      \"type\": \"string\",\n      \"description\": \"The writer of the graphic novel.\"\n    },\n    \"is_british\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the graphic novel is British.\"\n    },\n    \"antagonist\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the antagonist character.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the character in the graphic novel (e.g., main antagonist).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"graphic_novel_title\",\n    \"writer\",\n    \"is_british\",\n    \"antagonist\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "graphic_novel_title": {
        "type": "string",
        "description": "The title of the graphic novel."
      },
      "writer": {
        "type": "string",
        "description": "The writer of the graphic novel."
      },
      "is_british": {
        "type": "boolean",
        "description": "Indicates if the graphic novel is British."
      },
      "antagonist": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the antagonist character."
          },
          "role": {
            "type": "string",
            "description": "The role of the character in the graphic novel (e.g., main antagonist)."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "graphic_novel_title",
      "writer",
      "is_british",
      "antagonist"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
