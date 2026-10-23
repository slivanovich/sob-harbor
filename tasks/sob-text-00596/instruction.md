{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBleak Moments: Bleak Moments is a 1971 British film, the first film of Mike Leigh.  It began as a 75-minute stage play in March 1970 at the Open Space Theatre.  Leigh and Les Blair had formed their own company, Autumn Productions, and Leigh wanted to make a film of \"Bleak Moments.\"  He was able to realise that desire when Albert Finney and Michael Medwin's Memorial Films, which had recently made \"If...\" and was about to produce Gumshoe, \"delivered the main financial backing, as well as unused spare bits of film rolls.\"\n\nAll or Nothing (film): All or Nothing is a 2002 British drama film written and directed by Mike Leigh.  Typical of Leigh's work, the film is set in present-day London, and revolves around three working-class families and the depiction of their everyday lives.\n\nSimon Channing Williams: Simon Channing Williams (10 June 1945 – 11 April 2009) was a British film producer.  He was born in Maidenhead.  After having worked as a production assistant and producer of TV films and TV series in the 1970s and early 1980s, he and Mike Leigh formed the film production company Thin Man Films in 1988.  This company has produced all of Mike Leigh's films since then, among them the double Oscar-winning \"Topsy-Turvy\", the Oscar-nominated \"Vera Drake\" and the Palme d'Or-winning \"Secrets & Lies\".\n\nSecrets &amp; Lies (film): Secrets & Lies is a 1996 British drama film written and directed by Mike Leigh.  Led by an ensemble cast consisting of many Leigh regulars, it stars Marianne Jean-Baptiste as Hortense, a well-educated black middle-class London optometrist, who was adopted as a baby and has chosen to trace her family history – only to discover that her birth mother, Cynthia, played by Brenda Blethyn, is a working-class white woman with a dysfunctional family.  Claire Rushbrook co-stars as Cynthia's other daughter Roxanne, while Timothy Spall and Phyllis Logan portray Cynthia's brother and sister-in-law, who have secrets of their own affecting their everyday family life.\n\nThin Man Films: Thin Man Films is a British film production company, based in London.  It was founded in 1988 by director Mike Leigh and producer Simon Channing Williams to produce Mike Leigh's films.  They chose the company name because both founders were the opposite of it.\n\nVera Drake: Vera Drake is a 2004 British drama film written and directed by Mike Leigh and starring Imelda Staunton, Phil Davis, Daniel Mays and Eddie Marsan.  It tells the story of a working-class woman in London in 1950 who performs illegal abortions.  It won the Golden Lion at the Venice Film Festival and it was nominated for three Academy Awards and won three BAFTAs.\n\nDaniel Jewel: Daniel Jewel is a London-based film producer and director.  A graduate of Bristol University and Oxford University he has worked with British film directors such as Stephen Poliakoff, Charles Sturridge and Brian Gilbert.  In 2006 he produced the play Allegiance at the Edinburgh Festival, which starred Michael Fassbender as the Irish leader, Michael Collins.  The play was directed by Brian Gilbert.  In 2007 he produced and directed two films for Channel 4 about the shisha smoking cafes of London's Arabic quarter.  In 2008 he directed two documentaries for Al Gore's Current TV.  In late 2008 his production company, Third Man Films produced Sidney Turtlebaum starring Derek Jacobi and Rupert Evans which The Times called a \"Masterpiece\" and was nominated for a British Independent Film Award and short-listed for an Academy Award in 2010.\n\nPhoenix Pictures: Phoenix Pictures is an American film production company that has produced films since the late 1990s with features including \"Black Swan\" (2010), \"Shutter Island\" (2010), \"The People vs. Larry Flynt\" (1996), \"The Thin Red Line\" (1998), and \"Zodiac\" (2007).  Producers Mike Medavoy and Arnold Messer founded Phoenix in November 1995 as an independent production company.  They acquired financing from Onex Corporation, Pearson Television, and Sony Pictures Entertainment.  Its business model was based on packaging films to present to studios and to then navigate the films' development. \" Variety\" said Phoenix Pictures was one of the few companies to produce more than 25 films with the same executive team in place.\n\nNaked (1993 film): Naked is a 1993 British black comedy-drama film written and directed by Mike Leigh and starring David Thewlis as Johnny, a motor-mouthed intellectual and conspiracy theorist.  Stark and brutal in tone, \"Naked\" was a departure for Leigh, whose previous works were known for their subtle comedic dissections of middle-class and working-class manners.  Leigh's \"Naked\" screenplay relied heavily on lengthy improvisation during rehearsals, but little actual ad-libbing was filmed.  Critically acclaimed, the film won a number of awards, including best director and best actor at Cannes.  \"Naked\" marked a new career high for Leigh as a director and made the then-unknown Thewlis an internationally recognized star.\n\nAnother Year (film): Another Year is a 2010 British comedy-drama film written and directed by Mike Leigh, starring Lesley Manville, Jim Broadbent, and Ruth Sheen.  It premiered at the 2010 Cannes Film Festival in competition for the Palme d'Or.  The film was shown at the 54th London Film Festival before its general British release date on 5 November 2010.  At the 83rd Academy Awards, Mike Leigh was nominated for an Academy Award for Best Original Screenplay.\n\nQuestion: What is a 1996 British drama film written and directed by Mike Leigh, that was produced by a man who formed the film production company Thin Man Films in 1988?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"producer_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"producer_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the film's producer.\"\n        },\n        \"production_company_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the production company.\"\n        },\n        \"company_founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the production company was founded.\"\n        }\n      },\n      \"required\": [\n        \"producer_name\",\n        \"production_company_name\",\n        \"company_founding_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"director\",\n    \"producer_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the film was released."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "producer_details": {
        "type": "object",
        "properties": {
          "producer_name": {
            "type": "string",
            "description": "The name of the film's producer."
          },
          "production_company_name": {
            "type": "string",
            "description": "The name of the production company."
          },
          "company_founding_year": {
            "type": "integer",
            "description": "The year the production company was founded."
          }
        },
        "required": [
          "producer_name",
          "production_company_name",
          "company_founding_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "director",
      "producer_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
