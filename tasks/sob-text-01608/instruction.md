{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJingle All the Way 2: Jingle All the Way 2 is a 2014 American Christmas comedy film directed by Alex Zamm.  The film stars Larry the Cable Guy and Santino Marella.  It is the sequel to the 1996 comedy film \"Jingle All the Way\" starring Arnold Schwarzenegger.  The film is produced by 20th Century Fox and WWE Studios, the motion picture division of WWE, and was distributed straight-to-video by Fox on December 2, 2014.  On-air promotion from WWE occurred on their weekly episodic events.\n\nMixed Nuts: Mixed Nuts is a 1994 American Christmas comedy film directed by Nora Ephron, based on the 1982 French comedy film, \"Le Père Noël est une ordure\".  Co-written by Ephron and her sister Delia, the film features an ensemble cast which includes Steve Martin, Madeline Kahn, Rita Wilson, Anthony LaPaglia, Garry Shandling, Juliette Lewis, Adam Sandler and, in his first film role, Liev Schreiber.\n\nReina King: Reina King (born April 11, 1975) is an American film and television actress.  She began her acting career with the role of Carolyn (1985–1986), the adopted child of Roger and Nadine on the TV sitcom \"What's Happening Now!! \"—a sequel to the popular 1970s TV sitcom \"What's Happening!! \".  In 1987, she played Tiffany James in the movie \"Maid to Order\" and in 1988, she played actress Alfre Woodard's oldest daughter, Lanell Cooley, in the movie \"Scrooged\".  Reina also appeared in one episode (The Sing-Off, as Girl #2) of the sitcom \"227\" in 1988; the same sitcom her sister Regina King starred in as Brenda Jenkins.  In 1990, she played Rhonda in the film \"To Sleep with Anger\" with Mary Alice.  And in 1998, Reina was in the short film \"A Hollow Place\" as the mother of Corliss Young.\n\nA Bad Moms Christmas: A Bad Moms Christmas is an upcoming American Christmas comedy film directed and written by Jon Lucas and Scott Moore and is a sequel of the film \"Bad Moms\" (2016).  The film stars Mila Kunis, Kristen Bell and Kathryn Hahn reprising their roles from the first film, with Christine Baranski, Cheryl Hines and Susan Sarandon joining the cast.  The plot follows Amy, Carla and Kiki, as they must deal with their own mothers visiting during the holidays.  The film is scheduled to be released on November 1, 2017.\n\nHome Alone: Home Alone is a 1990 American Christmas comedy film written and produced by John Hughes and directed by Chris Columbus.  The film stars Macaulay Culkin as Kevin McCallister, a boy who is mistakenly left behind when his family flies to Paris for their Christmas vacation.  Kevin initially relishes being home alone, but soon has to contend with two would-be burglars played by Joe Pesci and Daniel Stern.  The film also features Catherine O'Hara and John Heard as Kevin's parents.\n\nOffice Christmas Party: Office Christmas Party is a 2016 American Christmas comedy film directed by Josh Gordon and Will Speck and written by Justin Malen and Laura Solon, based on a story by Jon Lucas and Scott Moore.  The film stars an ensemble cast, including Jason Bateman, Olivia Munn, T. J. Miller, Jillian Bell, Vanessa Bayer, Courtney B. Vance, Rob Corddry, Kate McKinnon and Jennifer Aniston, and was released on December 9, 2016 by Paramount Pictures.  It grossed $114 million worldwide.\n\nScrooged: Scrooged is a 1988 American Christmas comedy film, a modernization of Charles Dickens's \"A Christmas Carol\".  The film was produced and directed by Richard Donner, and the cinematography was by Michael Chapman.  The screenplay was written by Mitch Glazer and Michael O'Donoghue.  The original music score was composed by Danny Elfman.\n\nChristmas Eve (2015 film): Christmas Eve is a 2015 American Christmas comedy film, directed by Mitch Davis, written by Davis and Tyler McKellar, and produced by Davis and Larry King.  The film features a large ensemble cast led by Patrick Stewart, James Roday, Julianna Guill, Jon Heder, Cheryl Hines, and Gary Cole.\n\nChristmas with the Kranks: Christmas with the Kranks (also known as Jaded Couple Arguing in A Low and Passive Aggressive Manner) is a 2004 American Christmas comedy film based on the 2001 novel \"Skipping Christmas\" by John Grisham.  It was directed by Joe Roth and written and produced by Chris Columbus.\n\nNational Lampoon's Christmas Vacation: National Lampoon's Christmas Vacation is a 1989 American Christmas comedy film directed by Jeremiah S. Chechik.  It is the third installment in National Lampoon's \"Vacation\" film series, and was written by John Hughes, based on his short story in \"National Lampoon\" magazine, \"Christmas '59\".  The film stars Chevy Chase, Beverly D'Angelo and Randy Quaid, with Juliette Lewis and Johnny Galecki as the Griswold children Audrey and Rusty, respectively.\n\nQuestion: What 1988 American Christmas comedy film did Reina King play in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"reina_king_role\": {\n      \"type\": \"string\",\n      \"description\": \"The character played by Reina King in the film.\"\n    },\n    \"related_cast_member\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of a cast member related to Reina King's role.\"\n        },\n        \"relationship\": {\n          \"type\": \"string\",\n          \"description\": \"The relationship of this cast member to Reina King's character in the film.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"relationship\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"director\",\n    \"reina_king_role\",\n    \"related_cast_member\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "reina_king_role": {
        "type": "string",
        "description": "The character played by Reina King in the film."
      },
      "related_cast_member": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of a cast member related to Reina King's role."
          },
          "relationship": {
            "type": "string",
            "description": "The relationship of this cast member to Reina King's character in the film."
          }
        },
        "required": [
          "name",
          "relationship"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "director",
      "reina_king_role",
      "related_cast_member"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
