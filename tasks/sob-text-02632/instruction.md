{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTalia Zucker: She played the role of Claire Jardine in the ABC series Dirt Game with Joel Edgerton and Gerald Lepkowski in 2009.  Talia appeared as a guest character in the Australian drama series City Homicide and played a lead role in the children's series and Legacy of the Silver Shadow.  She played the recurring role of Erin Perry in the Australian soap opera Neighbours in 2005 and appeared in the popular Australian series Blue Heelers.  Talia played the role of Louisa Von Trapp in the Australia tour of The Sound of Music starring Lisa McCune and John Waters.  She appears as Sarah Wicks in the film \"Ned Kelly\" starring Heath Ledger.  Most recently Talia appears as the central character of Alice Palmer in the film \"Lake Mungo\" directed by Joel Anderson.\n\nThe Dark Knight (film): The Dark Knight is a 2008 superhero film directed, co-produced, and co-written by Christopher Nolan.  Featuring the DC Comics character Batman, the film is the second part of Nolan's \"The Dark Knight Trilogy\" and a sequel to 2005's \"Batman Begins\", starring an ensemble cast including Christian Bale, Michael Caine, Heath Ledger, Gary Oldman, Aaron Eckhart, Maggie Gyllenhaal and Morgan Freeman.  In the film, Bruce Wayne/Batman (Bale), Police Lieutenant James Gordon (Oldman) and District Attorney Harvey Dent (Eckhart) form an alliance to dismantle organized crime in Gotham City, but are menaced by a criminal mastermind known as the Joker (Ledger) who seeks to undermine Batman's influence and create chaos.\n\nThe Order (2003 film): The Order, also known as The Sin Eater, is a 2003 mystery horror film written and directed by Brian Helgeland, starring Heath Ledger, Benno Fürmann, Mark Addy, and Shannyn Sossamon.  Helgeland directed Ledger, Addy and Sossamon in the 2001 film \"A Knight's Tale\".\n\nState Theatre Centre of Western Australia: The State Theatre Centre of Western Australia is a theatre complex located within the Perth Cultural Centre in Perth, Western Australia.  The larger of three dedicated performance areas is known as the Heath Ledger Theatre in honour of Perth-born film actor Heath Ledger.\n\n14th Empire Awards: The 14th Empire Awards ceremony (officially known as the Jameson Empire Awards), presented by the British film magazine \"Empire\", honored the best films of 2008 and took place on 29 March 2009 at the Grosvenor House Hotel in London, England.  During the ceremony, \"Empire\" presented Empire Awards in 12 categories as well as four honorary awards.  To celebrate the 20th year anniversary of \"Empire\" magazine a special honorary award was presented, the Actor of our Lifetime and to mark the loss of Heath Ledger, he was awarded the special honorary Heath Ledger Tribute Award.  The Sony Ericsson Soundtrack Award was renamed to \"Best Soundtrack\" and the Best Sci-Fi/Fantasy award was renamed this year only to \"Best Sci-Fi/Superhero\".  The Best Newcomer and Best Soundtrack awards were presented for the last time.  Irish comedian Dara Ó Briain hosted the show for the first time.  The awards were sponsored by Jameson Irish Whiskey for the first time.\n\nTwo Hands (1999 film): Two Hands is a 1999 Australian comedy crime film, written and directed by Gregor Jordan.  The film stars Heath Ledger as Jimmy, a young man in debt to Pando, a local gangster played by Bryan Brown, and also stars Rose Byrne, David Field, and Susie Porter.  It won the Australian Film Institute Award for Best Film in 1999.  It was filmed in 1998 but was not released in Australia until 29 July 1999.  Before its release, it was screened at the Sundance Film Festival in the United States but was not released to DVD in the US until December 2005.\n\nHeath Ledger: Heathcliff Andrew Ledger (4 April 197922 January 2008) was an Australian actor and director.  After performing roles in several Australian television and film productions during the 1990s, Ledger left for the United States in 1998 to develop his film career.  His work comprised nineteen films, including \"10 Things I Hate About You\" (1999), \"The Patriot\" (2000), \"A Knight's Tale\" (2001), \"Monster's Ball\" (2001), \"Lords of Dogtown\" (2005), \"Brokeback Mountain\" (2005), \"The Dark Knight\" (2008), and \"The Imaginarium of Doctor Parnassus\" (2009), the latter two being posthumous releases.  He also produced and directed music videos and aspired to be a film director.\n\nMelissa Thomas: Mélissa Thomas is an Australian actress.  She is the daughter of the musician and record producer G. Wayne Thomas, (Morning of the Earth) and co-starred with Heath Ledger in the television series \"Sweat\" (1996) and has most recently been seen in the Heath Ledger episode of \"E! True Hollywood Story\" as herself, speaking frankly about life as his friend and co-star.  She has featured in a number of films and television series / mini-series over the years.\n\nThe Joker (The Dark Knight): The Joker is a fictional supervillain from American comic book publisher DC Comics and the main antagonist in Christopher Nolan's 2008 superhero film \"The Dark Knight\".  He was portrayed by late Australian actor Heath Ledger.  Ledger's interpretation of the character is specifically influenced by the graphic novels \"\" and \"\".  In the film, he wears the character's traditional color palette, while his facial appearance includes clown makeup that covers facial scars of a Glasgow smile.\n\n10 Things I Hate About You: 10 Things I Hate About You is a 1999 American romantic comedy film directed by Gil Junger and starring Julia Stiles, Heath Ledger, Joseph Gordon-Levitt, and Larisa Oleynik.  The screenplay, written by Karen McCullah Lutz and Kirsten Smith, is a modernization of William Shakespeare's late-16th century comedy \"The Taming of the Shrew\", retold in a late-1990s American high school setting.  In the story, new student Cameron (Gordon-Levitt) is smitten with Bianca (Oleynik) and, in order to get around her father's strict rules on dating, attempts to get bad boy Patrick (Ledger) to date Bianca's ill-tempered sister, Kat (Stiles).  The film is titled after a poem written by Kat about her bittersweet romance with Patrick.  Much of the filming took place in the Seattle metropolitan area, with many scenes shot at Stadium High School in Tacoma.\n\nQuestion: Heath Ledger had a role in the 1999 romantic comedy directed by whom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"actor_in_film\": {\n      \"type\": \"string\",\n      \"description\": \"The actor who had a role in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"director\",\n    \"actor_in_film\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "The release year of the film."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "actor_in_film": {
        "type": "string",
        "description": "The actor who had a role in the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "director",
      "actor_in_film"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
