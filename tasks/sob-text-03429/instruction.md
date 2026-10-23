{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPatrick Warburton: Patrick John Warburton (born November 14, 1964) is an American comedic actor and voice actor.  In television, he is known for playing David Puddy on \"Seinfeld\", the title role on \"The Tick\", Jeb Denton on \"Less Than Perfect\", Jeff Bingham on \"Rules of Engagement\", and Lemony Snicket on \"A Series of Unfortunate Events\".  His voice roles include Kronk in \"The Emperor's New Groove\" and its sequels, paraplegic police officer Joe Swanson on \"Family Guy\", Brock Samson on \"The Venture Bros\", Lok in the \"Tak and the Power of Juju\" video game series and in the television series and Flynn in \"Skylanders\" video games.  In advertising he has played a \"control enthusiast\" in a series of commercials for National Car Rental.\n\nWhen Did You See Her Last?: When Did You See Her Last?  is the second book in the \"All the Wrong Questions\" series by Lemony Snicket (also known as Daniel Handler), a series set before the events of \"A Series of Unfortunate Events\".\n\nWho Could That Be at This Hour?: Who Could That Be at This Hour?  is the first novel of the children's novel series \"All the Wrong Questions\" by Lemony Snicket, a series set before the events of \"A Series of Unfortunate Events\".  The novel tells the story of a young Lemony Snicket, who is apprenticing for the V.F.D. under the worst-ranked agent, S. Theodora Markson.  The book was published on October 23, 2012 by Little, Brown and Company and illustrated by Seth.\n\nMy Antonia (film): My Antonia is a 1995 television film based on the novel of the same name written by Willa Cather.  The movie was directed by Joseph Sargent and starred Jason Robards, Eva Marie Saint, and Neil Patrick Harris.  It was filmed in part at the Stuhr Museum in Grand Island, Nebraska.\n\nNeil Patrick Harris: Neil Patrick Harris (born June 15, 1973) is an American actor, comedian, magician, and singer, known primarily for his comedy roles on television and his dramatic and musical stage roles.  On television, he is known for playing the title character on \"Doogie Howser, M.D.\" (1989–1993), Barney Stinson on \"How I Met Your Mother\" (2005–2014, for which he was nominated for four Emmy Awards), and Count Olaf on \"A Series of Unfortunate Events\" (2017 onward).\n\nA Series of Unfortunate Events (TV series): Lemony Snicket's A Series of Unfortunate Events, or simply A Series of Unfortunate Events, is an American black comedy-drama television series from Netflix, and developed by Mark Hudis and Barry Sonnenfeld, based on the children's novel series of the same name by Lemony Snicket.  It stars Neil Patrick Harris, Patrick Warburton, Malina Weissman, Louis Hynes, K. Todd Freeman and Presley Smith.\n\nAll the Wrong Questions: All the Wrong Questions is a four-part young adult book series and prequel to \"A Series of Unfortunate Events\" by Lemony Snicket (the pen name of American author Daniel Handler).  The series explores Snicket's childhood apprenticeship to the secret society V.F.D and expands the fictional universe introduced in the novel \"The Bad Beginning\", the first of thirteen installments in the \"A Series of Unfortunate Events\" books.\n\nMeryl Streep in the 2000s: Meryl Streep throughout the 2000s appeared in many cinematic and theatrical productions.  In 2001, Streep’s voice appeared in the animated film A.I. Artificial Intelligence.  Streep that same year cohosted the annual Nobel Peace Prize concert as well as appeared in the popular play The Seagull.  In 2002, Streep appeared in the films Adaptation and The Hours.  In 2003, Streep appeared unaccredited in the comedy Stuck on You and starred in the HBO play adaptation Angels in America.  In 2004, Streep was awarded the AFI Life Achievement Award and in that same year starred in the films The Manchurian Candidate and Lemony Snicket's A Series of Unfortunate Events.  In 2005, Streep starred in the film Prime.  Streep began 2006 with the film A Prairie Home Companion and that same year starred in The Devil Wears Prada and the stage production Mother Courage and Her Children.  In 2007, Streep appeared in the films Dark Matter, Rendition, Evening, and Lions for Lambs.  In 2008, Streep starred in the films Mamma Mia!  and Doubt.  In 2009, Streep starred in Julie & Julia and It’s Complicated as well as loaning her voice to the animated film Fantastic Mr. Fox.\n\nLemony Snicket's A Series of Unfortunate Events: Lemony Snicket's A Series of Unfortunate Events is a 2004 American dark comedy film directed by Brad Silberling.  It is a film adaptation of \"A Series of Unfortunate Events\" by Lemony Snicket, covering the first three novels \"The Bad Beginning\", \"The Reptile Room\", and \"The Wide Window\".  The film stars Jim Carrey, Liam Aiken, Emily Browning, Timothy Spall, Catherine O'Hara, Billy Connolly, Cedric the Entertainer, Luis Guzmán, Jennifer Coolidge and Meryl Streep, as well as Jude Law as the voice of Lemony Snicket.\n\nLiam Aiken: Liam Pádraic Aiken (born January 7, 1990) is an American actor.  He has starred in films such as \"Stepmom\" (1998), \"Road to Perdition\" (2002), and \"Good Boy! \" (2003), and played Klaus Baudelaire in \"Lemony Snicket's A Series of Unfortunate Events\" (2004), based on the series of books.\n\nQuestion: My Antonia starred the actor who played which part in \"A Series of Unfortunate Events\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor who starred in both productions.\"\n        },\n        \"role_in_my_antonia\": {\n          \"type\": \"string\",\n          \"description\": \"The role played by the actor in 'My Antonia'.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"series_of_unfortunate_events_role\": {\n      \"type\": \"string\",\n      \"description\": \"The part played by the actor in 'A Series of Unfortunate Events'.\"\n    },\n    \"series_of_unfortunate_events_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of 'A Series of Unfortunate Events' production (e.g., TV series, film).\"\n    }\n  },\n  \"required\": [\n    \"actor\",\n    \"series_of_unfortunate_events_role\",\n    \"series_of_unfortunate_events_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor who starred in both productions."
          },
          "role_in_my_antonia": {
            "type": "string",
            "description": "The role played by the actor in 'My Antonia'."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "series_of_unfortunate_events_role": {
        "type": "string",
        "description": "The part played by the actor in 'A Series of Unfortunate Events'."
      },
      "series_of_unfortunate_events_type": {
        "type": "string",
        "description": "The type of 'A Series of Unfortunate Events' production (e.g., TV series, film)."
      }
    },
    "required": [
      "actor",
      "series_of_unfortunate_events_role",
      "series_of_unfortunate_events_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
