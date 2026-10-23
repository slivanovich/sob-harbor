{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJerry Rector: Jerry Andrew Rector (born September 12, 1958) is an American actor, writer, director and producer, known for \"The Strain\" (2015), \"Ghost World\" (2001) and \"Mean Guns\" (1997).  He grew up in Detroit and has lived in Los Angeles, New York, Vancouver and Toronto.  With over 30 years in the entertainment business, Jerry has worked with renowned actors including Jack Lemmon, Walter Matthau and Patrick Stewart.\n\nMean Guns: Mean Guns is a 1997 action film starring Ice-T, Christopher Lambert, Michael Halsey, Deborah Van Valkenburgh, Kimberly Warren, and Hunter Doughty.  It was directed by Albert Pyun.\n\nWith The Guns: With The Guns is the debut album from the Welsh rock quartet The Guns.  Originally to be released in 2007 under German record label Motor Records, however, With The Guns was delayed for so long that The Guns decided to release it themselves.  The album was finally released independently on July 17, 2009 through iTunes, and on August 31, 2009, 1000 copies With The Guns CDs became available from their official website.  Produced by Richard Emanuel & Alex Wiltshire at The Lodge Productions studio, \"With The Guns\" produced two music videos, one of which is often played on UK music channel, Lava TV.\n\nJoan Sanderson: Joan Sanderson (24 November 1912 – 24 May 1992) was an English television and stage actress.  During a long career, the tall and commanding actress played dowagers, spinsters and matrons, as well as intense Shakespearean roles.  Her television work included the sitcoms, \"Please Sir! \" (1968–72) and \"Me and My Girl\" (1984–88).\n\nCold Case (season 1): Season one of Cold Case, an American television series, began airing on September 28, 2003.  Cold Case is a drama about Lilly Rush, an enigmatic and highly effective detective on the Philadelphia Homicide Squad.  Rush's instinctive understanding of the criminal mind and her singular passion for uncovering the truth makes her the perfect fit for investigating cold cases, yester-crimes that have remained unsolved – some only a few months old, others going back decades.  Rush and her team use their wits to take on aging evidence and witnesses with buried secrets, uncovering fresh clues, digging into old wounds and doggedly pursuing the truth.  Joining Rush on her mission are a team of talented detectives: Scotty Valens, Rush's confident and street-smart partner; Nick Vera, rough around the edges but a sharp investigator; Will Jeffries, an experienced veteran who's been around the block; Kat Miller, no-nonsense and resourceful; and Lieutenant John Stillman, Rush's mentor and sometime father figure.  With their assistance, Rush is able to take on the toughest cases, giving voice to victims unable to speak for themselves – making sure none is ever forgotten.  Season one regular cast members include Kathryn Morris, Danny Pino, John Finn, Thom Barry and Jeremy Ratchford.  In 3 episodes, Justin Chambers had played Chris Lassing, Lilly's partner on the Philadelphia Homicide Squad, but left the show to star as Alex Karev in ABC's hit drama show \"Grey's Anatomy\".\n\nMean Venus: Mean Venus is an American hard rock band from New Jersey.  The quintet consists of 'J' (lead singer and songwriter), Adrian Freyre & Marcelo Cardosa (guitar), Russ Ippoliti (drums), and Chigger (bass).  Formed in early 2006, Mean Venus has shared the stage with numerous national acts including 7Mary3, Skid Row, Extreme, Ratt, Dokken, L.A.Guns, Stryper, King's X, Rainbow, UFO, Sebastian Bach and others.  In April 2008, Mean Venus headlined the Hawaiian Chopper Magazine's Motorhead Classic in Honolulu, Hawaii.  They also performed at 2008's Clearwater Festival.  Mean Venus songs have received radio airplay all over the country (WDHA, WZZO, WYSP, etc.)\n\nDasavatharam (film): Dasavatharam (தமிழ்: தசாவதாரம், English: The Ten Avatars) is a 1976 Tamil Hindu - Devotional Mythology film was directed and script were written by K. S. Gopalakrishnan.  Music by S. Rajeswara Rao assets to the film.  It stars Ravikumar played titular role with Sirkazhi Govindarajan, Jayachitra, Gemini Ganesan, M. R. Radha, P. S. Veerappa, Sowcar Janaki and K. R. Vijaya other actor and actress played portraying supporting role.\n\nMalishka RJ: Malishka Mendonsa, popularly known as RJ Malishka , is a radio personality from Mumbai, India.  She works in Red FM 93.5.  Her show \"Morning No 1 with Malishka\" has won the \"Best Breakfast Programme/Show (Hindi) at the Indian Excellence in Radio Awards\" in the past.  Actress Vidya Balan was trained by RJ Malishka when the actress played the role of an RJ in 2006 Bollywood film Lage Raho Munnabhai.\n\nCry Blood, Apache: Cry Blood, Apache is a 1970 western film directed by Jack Starrett and assistant director Robert Tessier.  The film released by Liberty Entertainment was from an original story by Harold Roberts with a screenplay by Sean MacGregor and has been rereleased as part of a 20 movie DVD pack titled \"Mean Guns\" by Mill Creek Entertainment.\n\nDeborah Van Valkenburgh: Deborah Gaye Van Valkenburgh (born August 29, 1952) is an American actress.  She is known for playing Ted Knight's character's daughter in the role of Jackie Rush on the ABC television situation comedy \"Too Close for Comfort\", and for her role as Mercy in the cult 1979 film \"The Warriors\".  In 2012, she won the Supporting Actress in a Fantasy Film award at the PollyGrind Film Festival for the film \"Road to Hell\".\n\nQuestion: What actress played in both Jackie Rush and Mean Guns?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actress.\"\n    },\n    \"productions_acted_in\": {\n      \"type\": \"array\",\n      \"description\": \"A list of productions the actress played in, matching the query.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"production_title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the film or television series.\"\n          },\n          \"production_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of production (e.g., 'film', 'television situation comedy').\"\n          },\n          \"role_played\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the character or role played in this production, if specified.\"\n          }\n        },\n        \"required\": [\n          \"production_title\",\n          \"production_type\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"total_productions_matched\": {\n      \"type\": \"integer\",\n      \"description\": \"The total count of distinct productions found that match the query criteria.\"\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"productions_acted_in\",\n    \"total_productions_matched\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The full name of the actress."
      },
      "productions_acted_in": {
        "type": "array",
        "description": "A list of productions the actress played in, matching the query.",
        "items": {
          "type": "object",
          "properties": {
            "production_title": {
              "type": "string",
              "description": "The title of the film or television series."
            },
            "production_type": {
              "type": "string",
              "description": "The type of production (e.g., 'film', 'television situation comedy')."
            },
            "role_played": {
              "type": "string",
              "description": "The name of the character or role played in this production, if specified."
            }
          },
          "required": [
            "production_title",
            "production_type"
          ],
          "additionalProperties": false
        }
      },
      "total_productions_matched": {
        "type": "integer",
        "description": "The total count of distinct productions found that match the query criteria."
      }
    },
    "required": [
      "actress_name",
      "productions_acted_in",
      "total_productions_matched"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
