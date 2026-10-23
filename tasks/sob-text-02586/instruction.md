{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Body in the Library (film): The Body in the Library is a 1984 television film adaptation of Agatha Christie's 1942 detective novel \"The Body in the Library\", which was co-produced by the BBC and the A&E Network.  The film uses an adapted screenplay by T. R. Bowen and was directed by Silvio Narizzano.  Starring Joan Hickson in the title role, it was the first film presented in the British television series \"Miss Marple\" and premiered in three parts from 26 to 28 December 1984 on BBC One.  In the United States the film was first broadcast on 4 January 1986 as a part of PBS's \"Mystery! \".  In his review in \"The New York Times\", critic John J. O'Connor wrote: \"Miss Christie would no doubt approve of Joan Hickson, the veteran British character actress who plays Miss Marple... This BBC/Arts & Entertainment co-production offers an especially good example of Agatha Christie in adaptation.  The characters are nicely realized and the suspense holds.  Miss Hickson is lovely, neither as awesome as Miss Rutherford nor as overly cute as Helen Hayes.  And the supporting cast is admirable, particularly Gwen Watford as Dolly and David Horovitch as Inspector Slack.  As someone notes about the case, 'you'll have to admit it has all the bizarre elements of a cheap thriller.'  Once hooked, you won't be able to turn it off.\"\n\nMurder on the Nile/Hidden Horizon: Murder on the Nile (1944) is a murder mystery play by crime writer Agatha Christie, based on her 1937 novel \"Death on the Nile\".  The notable John Anderson chose to portray McNaught in this play before retiring from the stage.\n\nThirteen at Dinner (film): Thirteen at Dinner is a 1985 British-American made-for-television mystery film featuring the Belgian detective Hercule Poirot.  Adapted by Rod Browning from the Agatha Christie novel \"Lord Edgware Dies\", it was directed by Lou Antonio and starred Peter Ustinov, Faye Dunaway, Jonathan Cecil, Diane Keen and Bill Nighy.  David Suchet, later to play Poirot in the long-running television series entitled \"Agatha Christie's Poirot\", played the role of Inspector Japp.  Suchet considers his performance as Japp to be \"possibly the worst performance of [his] career.\"\n\nVerdict (play): Verdict is a 1958 play by British mystery writer Agatha Christie.  It is unusual for Agatha Christie plays in more than one way: for example, it is an original play, not based on a story or novel; and though there is a murder in the story, it is a melodrama more than a typical 'whodunnit' mystery as the murder takes place on stage.\n\nThe Mousetrap: The Mousetrap is a murder mystery play by Agatha Christie.  \"The Mousetrap\" opened in London's West End in 1952, and has been running continuously since then.  The longest running West End show, it has by far the longest initial run of any play in history, with its 25,000th performance taking place on 18 November 2012.  The play is known for its twist ending, which the audience are traditionally asked not to reveal after leaving the theatre.\n\nList of Agatha Christie's Marple episodes: Agatha Christie's Marple is a British ITV television series based on the Miss Marple and other murder mystery novels by Agatha Christie.  It is also known as Marple.  The title character was played by Geraldine McEwan from the first to third series, until her retirement from the role.  She was replaced by Julia McKenzie from the fourth series onwards.  The first six episodes were all adaptations of \"Miss Marple\" novels by Christie.  Subsequent episodes were derived both from works featuring Miss Marple but also Christie novels that did not feature the character.\n\nAgatha Christie Memorial: The Agatha Christie Memorial is a memorial to author and playwright Agatha Christie, located at the intersection of Cranbourn Street and Great Newport Street by St Martin's Cross near Covent Garden, in London, United Kingdom.  It is located in the heart of London's theatre district.  This was chosen to pay homage to Christie's contribution to theatre: her murder mystery play \"The Mousetrap\" is the world's longest-running show, and she was the first female playwright to have three plays performing simultaneously in the West End.\n\nMiss Marple (TV series): Miss Marple is a British television series based on the Miss Marple murder mystery novels by Agatha Christie, starring Joan Hickson in the title role.  It aired from 26 December 1984 to 27 December 1992.  All 12 original Miss Marple Christie novels were dramatised.  The adaptations were written by T. R. Bowen, Julia Jones, Alan Plater, Ken Taylor and Jill Hyem, and the series was produced by George Gallaccio.  In addition to its availability on VHS and DVD, the series began to be released on Blu-ray Disc in October 2014, marking its 30th anniversary.\n\nMartin Miller (actor): Martin Miller, born Rudolph Muller (2 September 1899 – 26 August 1969) was a Czech-Austrian character actor who played many small roles in British films and television series from the early 1940s until his death.  He was best known for playing eccentric doctors, scientists and professors, although he played a wide range of small, obscure rolesincluding photographers, waiters, a pet store dealer, rabbis, a Dutch sailor and a Swiss tailor.  On stage he was noted in particular for his parodies of Adolf Hitler and roles as Dr. Einstein in \"Arsenic and Old Lace\" and Mr. Paravinci in \"The Mousetrap\".\n\nAgatha Christie's Poirot: Agatha Christie's Poirot is a British mystery drama television series that aired on ITV from 8 January 1989 to 13 November 2013.  David Suchet stars as the eponymous detective, Agatha Christie's fictional Hercule Poirot.  Initially produced by LWT, the series was later produced by ITV Studios.  In the United States, PBS and A&E have aired it as Poirot.\n\nQuestion: Martin Miller, born Rudolph Muller, was a Czech-Austrian character actor who played many small roles in British films and television series from the early 1940s until his death, on stage he was noted in particular for his parodies of Mr. Paravinci in which murder mystery play by Agatha Christie, and opened in London's West End in 1952, and has been running continuously since then?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"birth_name\": {\n      \"type\": \"string\",\n      \"description\": \"The birth name of the actor.\"\n    },\n    \"role_played\": {\n      \"type\": \"string\",\n      \"description\": \"The specific role the actor was noted for.\"\n    },\n    \"play_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"play_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the murder mystery play.\"\n        },\n        \"author\": {\n          \"type\": \"string\",\n          \"description\": \"The author of the play.\"\n        },\n        \"opening_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the play opened.\"\n        },\n        \"location_opened\": {\n          \"type\": \"string\",\n          \"description\": \"The location where the play first opened.\"\n        },\n        \"running_continuously_since_opening\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the play has been running continuously since its opening.\"\n        }\n      },\n      \"required\": [\n        \"play_title\",\n        \"author\",\n        \"opening_year\",\n        \"location_opened\",\n        \"running_continuously_since_opening\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"birth_name\",\n    \"role_played\",\n    \"play_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "birth_name": {
        "type": "string",
        "description": "The birth name of the actor."
      },
      "role_played": {
        "type": "string",
        "description": "The specific role the actor was noted for."
      },
      "play_details": {
        "type": "object",
        "properties": {
          "play_title": {
            "type": "string",
            "description": "The title of the murder mystery play."
          },
          "author": {
            "type": "string",
            "description": "The author of the play."
          },
          "opening_year": {
            "type": "integer",
            "description": "The year the play opened."
          },
          "location_opened": {
            "type": "string",
            "description": "The location where the play first opened."
          },
          "running_continuously_since_opening": {
            "type": "boolean",
            "description": "Indicates if the play has been running continuously since its opening."
          }
        },
        "required": [
          "play_title",
          "author",
          "opening_year",
          "location_opened",
          "running_continuously_since_opening"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "birth_name",
      "role_played",
      "play_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
