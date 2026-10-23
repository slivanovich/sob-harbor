{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDanger Island (serial): Danger Island (1931) is a Universal pre-Code film serial.  It is considered to be lost.  Kenneth Harlan played Captain Drake (the hero), and Lucile Brown played heroine Bonnie Adams.\n\nScott Parker (actor): W. Scott Parker III is an American actor, director, and screenwriter.  He has appeared in over one-hundred plays and films working with directors such as Derrick Borte, Giancarlo Esposito, and George Clooney.  Most recently he played Jefferson Calvert in the theatrical production of \"Four Queens - No Trump\" under the direction of Ted Lange.  In recent years, Mr. Parker has gravitated toward historical films including Capt. Philip Carteret of the HMS Harwich in the film Newton's Grace, Dr. Smith (Henry Box Brown), and Gen. George Washington (produced by North Carolina Museum of History).\n\nPlease Kill Mr. Know It All: Please Kill Mr. Know It All is a 2013 romantic comedy film directed by Colin Carter and Sandra Feldman.  The film stars Lara Jean Chorostecki, Jefferson Brown, Kristina Pesic, and Cliff Sanders.\n\nJust Off Broadway: Just Off Broadway is a 1942 Drama directed by Herbert I. Leeds, starring Lloyd Nolan and Marjorie Weaver.  This is the sixth of a series of seven that Lloyd Nolan played Michael Shayne for Twentieth Century Fox films.  Hugh Beaumont portrayed Shayne in five more films from Producers Releasing Corporation.\n\nThe Deal (2003 film): The Deal is a 2003 British television film directed by Stephen Frears from a script by Peter Morgan, based in part upon \"The Rivals\" by James Naughtie.  The film stars David Morrissey as Gordon Brown and Michael Sheen as Tony Blair, and depicts the Blair-Brown deal—a well-documented pact that Blair and Brown made whereby Brown would not stand in the 1994 Labour leadership election, so that Blair could have a clear run at becoming leader of the party and Prime Minister.  The film begins on 9 June 1983, as Blair and Brown are first elected to Parliament, and concludes in May 1994 at the Granita restaurant—the location of the supposed agreement—with a brief epilogue following the leadership contest.\n\nShark City: Shark City is a 2009 comedy film directed by Dan Eisen and starring Jefferson Brown, David J. Phillips, Carlo Rota, Corey Haim, Vivica A. Fox, Jordan Madley, Samantha Gutstadt, and Tony Nappo; with Skye Collyer, Adam Rodness, Sean Tweedley, Michael Gelbart, and Dylan Ramsey.  It was written by Evan Shear.\n\nChris Brown videography: Chris Brown is an American singer, songwriter and actor who has appeared in many music videos. His videography consists of sixty-four music videos, five guest appearances, four video albums, four film appearances and four television appearances.  Brown's first music video was for his debut single \"Run It! \", taken from his self-titled debut album.  Directed by Erik White, the video \"introduced the world\" to Brown's dance moves.  White and Brown directed the accompanying music video for the second single \"Yo (Excuse Me Miss)\", which made reference to Michael Jackson.  Some of Brown's other videos have been noted for its similarities to Jackson's work, including his music videos for \"Wall to Wall\" (2007), \"Yeah 3x\" (2010), \"She Ain't You\" (2011) and \"Turn Up the Music\" (2012).  In 2007, Brown made his acting debut in the film, \"Stomp the Yard\", as Duron.  That same year, he also appeared in \"This Christmas\" as Michael \"Baby\" Whitfield.  Brown's music video for the single \"Forever\" (2008) was directed by Joseph Kahn and was \"highly regarded as one of the best videos of 2008\".  It earned Brown three nominations at the 2008 MTV Video Music Awards in the categories of Best Dancing in a Video, Best Choreography and Video of the Year.\n\nDavid Krumholtz: David Krumholtz (born May 15, 1978) is an American actor.  He played Charlie Eppes in the CBS drama series \"Numbers\".  He played Seth Goldstein in \"Harold & Kumar Go to White Castle\" and its two sequels, \"Harold & Kumar Escape from Guantanamo Bay\" and \"A Very Harold & Kumar 3D Christmas\".  He is also known for his role as Bernard the Elf in \"The Santa Clause\" and its sequel, \"The Santa Clause 2\".  Additionally, he is known for his role as Mr. Universe in the 2005 film \"Serenity\" and played Michael the AV geek in \"10 Things I Hate About You\".  In 2016, he provided the voice for Kareem Abdul Lavash in the adult animated film \"Sausage Party\".\n\nJefferson Brown: Jefferson Brown (b. 1976) is a Canadian actor.  He is best known for playing the role of Michael in \"Make Your Move\".  Starting in March 2015, he appeared in a series of television commercials for Intact Insurance, promoting the company's policy on opening claims for clients within thirty minutes of being notified (he portraying the claimant).\n\nMake Your Move (film): Make Your Move (formerly called Cobu 3D, also known as Make Your Move 3D), is a \"Romeo and Juliet\"-inspired 2013 South Korean-American independent dance film starring K-pop singer BoA and ballroom dancer Derek Hough.  The film was directed by Duane Adler who wrote the script for the movies \"Save the Last Dance\" (2001) and \"Step Up\" (2006).  Hough took season twelve off of the show \"Dancing With the Stars\" to star in the film, which was shot in New York City and Toronto during the spring of 2011.  Aside from the lead stars, singer Yunho from TVXQ has a cameo appearance.  The film was choreographed by Tabitha and Napoleon D'umo, Yako Miyamoto, and Nick Gonzalez.\n\nQuestion: Who directed the film where Jefferson Brown played Michael?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"character_played\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"character_played\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\"\n        },\n        \"genre\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"director\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor\",\n    \"film\",\n    \"director\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "character_played": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "character_played"
        ],
        "additionalProperties": false
      },
      "film": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          },
          "genre": {
            "type": "string"
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      },
      "director": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor",
      "film",
      "director"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
