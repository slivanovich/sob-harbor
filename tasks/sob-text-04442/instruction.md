{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThaskara Lahala: Thaskara Lahala (English: Rebellion of the thief ) is a 2010 Malayalam-language comedy film directed by Ramesh Das starring Suraj Venjaramood in the title role.  This is the director's second movie; his first film, \"Thattakam\", was a box-office flop.  This is also the second movie in which comedy artist Suraj Venjaramood plays the title role.  Lakshmi Sharma of \"Palunku\" fame is the heroine of the film.  She plays the role of a police officer.\n\nThe Nerd: The Nerd is a two-act comedy written by American actor/playwright Larry Shue.  Actors who have taken on the title role include British comedian Rowan Atkinson.  It was the top grossing American play in London's West End in 1986.\n\nRowan Atkinson: Rowan Sebastian Atkinson, CBE (born 6 January 1955) is an English actor, comedian, and screenwriter best known for his work on the sitcoms \"Blackadder\" and \"Mr. Bean\".  Atkinson first came to prominence in the BBC's sketch comedy show \"Not the Nine O'Clock News\" (1979–82), receiving the 1981 BAFTA for Best Entertainment Performance, and via his participation in The Secret Policeman's Ball from 1979.  His other work includes the 1983 James Bond film \"Never Say Never Again\", playing a bumbling vicar in \"Four Weddings and a Funeral\" (1994), voicing the red-billed hornbill Zazu in \"The Lion King\" (1994), and featuring in the BBC sitcom \"The Thin Blue Line\" (1995–1996).  His work in theatre includes the 2009 West End revival of the musical \"Oliver! \".\n\nKirby Grant: Kirby Grant (November 24, 1911 – October 30, 1985), born Kirby Grant Hoon Jr., was a long-time B movie and television actor, mostly remembered for having played the title role in the Western-themed adventure television series \"Sky King\".  Between 1949 and 1954, Grant played the title role in the series of ten Corporal Rod Webb films.\n\nAngry Video Game Nerd: The Movie: Angry Video Game Nerd: The Movie is a 2014 American independent science fiction adventure comedy film written and directed by James Rolfe and Kevin Finn.  It is based on the web series of the same name, also created by Rolfe, with himself as the title role.\n\nAmrit (film): Amrit is a 1986 Indian Hindi film starring Rajesh Khanna in the title role playing the character of Amritlal Sharma.  The film was directed by Mohan Kumar immediately after directing Avtaar with Khanna in the title role and lyrics written by Anand Bakshi.  This movie gave Rajesh Khanna his fourth BJFA Best Actor award in 1987.  The film was critically acclaimed and received five stars in Bollywood Guide Collections.  The film was remade in Telugu as \"Aatma Bandhuvulu\".\n\nRenée Fleming: Renée Fleming (born February 14, 1959) is an American opera singer and soprano whose repertoire encompasses Richard Strauss, Mozart, Handel, bel canto, lieder, French opera and chansons, jazz and indie rock.  Fleming has a full lyric soprano voice.  She has performed coloratura, lyric, and lighter spinto soprano operatic roles in Italian, German, French, Czech, and Russian, aside from her native English.  She also speaks fluent German and French, along with limited Italian.  Her signature roles include Countess Almaviva in Mozart's \"Le nozze di Figaro\", Desdemona in Verdi's \"Otello\", Violetta in Verdi's \"La traviata\", the title role in Dvořák's \"Rusalka\", the title role in Massenet's \"Manon\", the title role in Massenet's \"Thaïs\", the title role in Richard Strauss's \"Arabella\", the Marschallin in \"Der Rosenkavalier\", and the Countess in \"Capriccio\".\n\nRay (film): Ray is a 2004 American musical biographical film focusing on 30 years in the life of rhythm and blues musician Ray Charles.  The independently produced film was written, produced and directed by Taylor Hackford, and stars Jamie Foxx in the title role.  Foxx received an Academy Award for Best Actor for his performance as well as the Golden Globe, BAFTA, Screen Actors Guild and Critics' Choice awards, becoming the second actor to win all five major lead actor awards for the same performance, and the only one to win the Golden Globe in the Musical or Comedy (rather than the Drama) category.\n\nGlenn Winslade: Glenn Winslade (born 1958) is an Australian operatic tenor known for his interpretations of dramatic roles such as Florestan in \"Fidelio\", the title role in \"Idomeneo\", the title role in \"La clemenza di Tito\", Erik in \"The Flying Dutchman\", the title role in \"Rienzi\", the title role in \"Lohengrin\", the title role in \"Tannhäuser\", the Emperor in \"Die Frau ohne Schatten\", Apollo in \"Daphne\", Bacchus in \"Ariadne auf Naxos\" and Max in \"Der Freischütz\".\n\nIan Holm: Sir Ian Holm CBE (born 12 September 1931) is an English actor known for his stage work and many film roles.  He received the 1967 Tony Award for Best Featured Actor for his performance as Lenny in \"The Homecoming\" and the 1998 Laurence Olivier Award for Best Actor for his performance in the title role of \"King Lear\".  He won the 1981 BAFTA Award for Best Actor in a Supporting Role for his role as athletics trainer Sam Mussabini in \"Chariots of Fire\", for which he was also nominated for an Academy Award.\n\nQuestion: For which movie did the actor who took the title role in The Nerd win a BAFTA in 1981?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who played the title role in 'The Nerd'.\"\n    },\n    \"bafta_award_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the actor won the BAFTA award.\"\n    },\n    \"bafta_award_category\": {\n      \"type\": \"string\",\n      \"description\": \"The category of the BAFTA award won by the actor.\"\n    },\n    \"winning_production_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the production for which the actor won the BAFTA award.\"\n    },\n    \"winning_production_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of production (e.g., film, TV show) for which the actor won the BAFTA award.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"bafta_award_year\",\n    \"bafta_award_category\",\n    \"winning_production_name\",\n    \"winning_production_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who played the title role in 'The Nerd'."
      },
      "bafta_award_year": {
        "type": "integer",
        "description": "The year the actor won the BAFTA award."
      },
      "bafta_award_category": {
        "type": "string",
        "description": "The category of the BAFTA award won by the actor."
      },
      "winning_production_name": {
        "type": "string",
        "description": "The name of the production for which the actor won the BAFTA award."
      },
      "winning_production_type": {
        "type": "string",
        "description": "The type of production (e.g., film, TV show) for which the actor won the BAFTA award."
      }
    },
    "required": [
      "actor_name",
      "bafta_award_year",
      "bafta_award_category",
      "winning_production_name",
      "winning_production_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
