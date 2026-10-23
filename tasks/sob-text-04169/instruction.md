{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNatasha Bassett: Natasha Bassett is an Australian actress, screenwriter, and director.  She may be best known for playing Britney Spears in the Lifetime biopic \"Britney Ever After\", which premiered on February 18, 2017.  Her 2014 short film titled \"Kite\", which she wrote and directed, was accepted into the Rhode Island International Film Festival.  She also appeared in the supporting role of Gloria DeLamour in the film \"Hail, Caesar! \".\n\nThe Pilot (Friends): The Pilot, also known as \"The One Where Monica Gets a Roommate\" , was the first episode of the American situation comedy series \"Friends\", premiered on NBC (National Broadcasting Company) on September 22, 1994.  It was written by series creators David Crane and Marta Kauffman, and directed by James Burrows.  The pilot introduces six friends who live and work in New York City; Monica (Courteney Cox) sleeps with a wine seller after their first date but is horrified to discover he tricked her into bed; her brother Ross (David Schwimmer) is depressed after his lesbian ex-wife moves her things out of their apartment; Monica's old schoolfriend Rachel (Jennifer Aniston) moves in with Monica after running out of her wedding; and their friends, Joey, Chandler, and Phoebe (Matt LeBlanc, Matthew Perry, and Lisa Kudrow), respectively offer them each support and advice.\n\nThe Troop: The Troop is an American-Canadian live-action, single camera comedy-adventure television series about a trio of teenagers who fight and capture monsters and other supernatural phenomena that invade the fictional town of Lakewood.  Created and executive produced by Max Burnett, Greg Coolidge and Chris Morgan, the series premiered on Nickelodeon on September 18, 2009.\n\nSenta Moses: Senta Michelle Moses is an American actress.  She is perhaps best known for her co-starring role as Phoebe, the lab assistant in the children's series \"Beakman's World\".\n\nMatreya Fedor: Matreya Natasha Fedor (born March 11, 1997) is a Canadian teen actress, known for her role as Echo Zizzleswift in \"Mr. Young\" and as Phoebe Collins in \"The Troop\".\n\nMr. Young: Mr. Young is a Canadian Teen situation comedy that premiered on March 1, 2011 on YTV.  The series was filmed in Burnaby, British Columbia.  The series was created by Dan Signer (who also worked on shows such as \"The Suite Life on Deck\" and \"A.N.T. Farm\"), and stars Brendan Meyer, Matreya Fedor and Gig Morton as attendees of Finnegan High School.  Further main cast includes Kurt Ostlund, Emily Tennant, and Milo Shandel.  The show ended its run on November 28, 2013 with three seasons and 80 episodes.  The whole series is available for streaming on Netflix in the United States, United Kingdom, Australia and New Zealand.\n\nSimone Robertson: Simone Robertson (28 May 1976 in Melbourne, Australia) is an Australian actress best known for her 1991–1993 role as Phoebe Gottlieb in the TV series \"Neighbours\".  Her sister is Aimee Robertson.  She is also a trained jazz and tap dancer.\n\nMichael Stephenson (filmmaker): Michael Paul Stephenson (born February 28, 1978) is an American film director, producer, writer, and actor.  He is best known for his starring role in \"Troll 2\" (1990) and for directing the ensuing documentary, \"Best Worst Movie\" (2009).  His second documentary, \"The American Scream\" (2012), premiered on NBCUniversal's Chiller network and was named a \"Must Watch\" by \"Entertainment Weekly\".  His latest film and narrative directorial debut, \"Girlfriend's Day\" (2017), is a Netflix original film.  Premiering on Valentine's Day 2017, the comedy stars Bob Odenkirk, Amber Tamblyn, Natasha Lyonne and Stacy Keach.\n\nTasha Yar: Natasha \"Tasha\" Yar is a fictional character that mainly appeared in the of the American science fiction television series \"\".  Portrayed by Denise Crosby, she is chief of security aboard the Starfleet starship USS \"Enterprise\"-D and carries the rank of lieutenant.  The character's concept was originally based upon the character of Vasquez from the 1986 film \"Aliens\".  Following further development she became known first as Tanya, and then Tasha.  Crosby had originally auditioned for the role of Deanna Troi, while Rosalind Chao became a favorite for Tasha.  After Marina Sirtis auditioned for the role, the show's creator Gene Roddenberry decided to switch the roles for the actresses, with Sirtis becoming Troi and Crosby becoming Yar.  Chao would later appear on the series in a recurring role as Keiko O'Brien.\n\nNatasha Lyonne: Natasha Bianca Lyonne Braunstein (born April 4, 1979), better known as Natasha Lyonne, is an American actress.  She is best known for her role as Jessica in the \"American Pie\" film series.  Her other films include \"Everyone Says I Love You,\" \"Slums of Beverly Hills,\" and \"But I'm a Cheerleader\".  She portrays Nicky Nichols in the Netflix series \"Orange Is the New Black,\" for which she received a nomination for the 2014 Primetime Emmy Award for Outstanding Guest Actress in a Comedy Series.\n\nQuestion: Matreya Natasha Fedor is known foer her role as Phoebe Collins in a televsion series that premiered on what date?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actress.\"\n    },\n    \"role_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actress.\"\n    },\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television series.\"\n    },\n    \"premiere_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The date the television series premiered.\"\n    },\n    \"premiere_network\": {\n      \"type\": \"string\",\n      \"description\": \"The network on which the series premiered.\"\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"role_name\",\n    \"series_name\",\n    \"premiere_date\",\n    \"premiere_network\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The full name of the actress."
      },
      "role_name": {
        "type": "string",
        "description": "The name of the character played by the actress."
      },
      "series_name": {
        "type": "string",
        "description": "The name of the television series."
      },
      "premiere_date": {
        "type": "string",
        "format": "date",
        "description": "The date the television series premiered."
      },
      "premiere_network": {
        "type": "string",
        "description": "The network on which the series premiered."
      }
    },
    "required": [
      "actress_name",
      "role_name",
      "series_name",
      "premiere_date",
      "premiere_network"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
