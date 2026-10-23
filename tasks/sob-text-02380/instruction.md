{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Ultimate Dance Battle: The Ultimate Dance Battle (\"TUDB\") is a Dutch and Flemish dance competition and reality show for professional level choreographers and dancers.  In The Netherlands the show airs on the Dutch television network RTL 5, and in Belgium on the Flemish channel 2BE.  American choreographer Dan Karaty (who has participated in various production and judging roles on other talent competitions, including \"So You Think You Can Dance\", \"The X-Factor\", and \"Holland's Got Talent\") is credited as creator and executive producer of \"The Ultimate Dance Battle\" series and he also serves as its main officiator.  The show is presented by Sean D'Hondt and Lieke van Lexmond.  Choreographer Isabelle Beernaert and her team \"Heart2Beat\" won the first season of the series in spring of 2011.\n\nMovmnt: movmnt magazine is an urban-leaning lifestyle magazine which was co-founded in 2006 by David Benaym and Danny Tidwell.  The magazine has featured columns by Mario Spinetti, Mia Michaels, Robert Battle, Debbie Allen, Alisan Porter, Rasta Thomas, and Frank Conway.  Both Travis Wall and Ivan Koumaev have made guest contributions to the publication, which has published photographs by Gary Land, Dave Hill, James Archibald Houston, and Alison Jackson.\n\nSo You Think You Can Dance (U.S. season 10): So You Think You Can Dance, a televised American dance competition, began broadcast of its tenth season on May 14, 2013.  It airs on the FOX Television Network and was hosted by Cat Deeley and featured returning permanent judges Nigel Lythgoe, who also serves as one of the show's executive producers, and Mary Murphy.  The show featured many of the format changes instituted in the previous season, including notably a single episode per week/voting round (seasons two through eight featured two episodes per week).  It was also the first season in the show's history that a tap dancer not only made it past the third week of competition, but made the finale.  It is also the first season to last longer than nine weeks.  Lythgoe announced in the finale that the show has been renewed for the eleventh season.\n\nNarrative Television Network: Narrative Television Network (NTN) makes movies, television shows and educational programming accessible to millions of blind and visually impaired people and their families.  Founded in 1988 by Jim Stovall, the Narrative Television Network unobtrusively adds the voice of a narrator to the existing program between the dialogue so that blind or low vision people can hear what they can’t see.  The Narrative Television Network has received an Emmy Award, a Media Access Award and an International Film and Video Award for its pioneering work in making movies, television and educational programming accessible for the visually impaired.  The Narrative Television Network website offers readers a “Text Only” version of its pages to increase accessibility for blind and visually impaired readers who use screen readers.\n\nThe CW: The CW Television Network (commonly referred to as just The CW) is an American English-language broadcast television network that is operated by The CW Network, LLC, a limited liability joint venture between CBS Corporation, the former owners of United Paramount Network (UPN), and Warner Bros.  Entertainment, a division of Time Warner, former majority owner of The WB Television Network.  The \"CW\" name is an abbreviation derived from the first letters of the names of its two parent corporations (CBS and Warner Bros.).\n\nYou Can Dance (French TV series): You Can Dance is a French televised dance competition with a format based on the American show \"So You Think You Can Dance\" It airs on the NT1 television network and is hosted by Benjamin Castaldi.  Premiering in early 2012, the show has aired one season.  As with other shows in the international So You Think You Can Dance franchise, its competitors—young semi-professional dancers from a variety of stylistic backgrounds—compete for judge favor and at-home-viewer votes by attempting to master routines from different styles to avoid being cut as the rounds progress.\n\nParir te Karogh Es: Parir te Karogh Es (Պարիր թե կարող ես in original Armenian orthography, and translated as \"So You Think You Can Dance\") is an Armenian televised dance competition based on the format of the international \"So You Think You Can Dance\" television franchise.  Broadcast by Armenian television network Shant TV and hosted by Grikor Aghakhanyan, it began airing in 2011 and has been broadcast for three seasons.  The first two seasons of the show had a single winner, while the third season had both a male and a female winner.  The show's second-season winner, Paul Karmiriyan, subsequently entered the U.S. version of \"So You Think You Can Dance\", and placed in the Top 6 on its tenth season.\n\nSo You Think You Can Dance (U.S. season 1): So You Think You Can Dance is an American television dance competition that airs on the Fox network.  The first season premiered on July 20, 2005 with Lauren Sánchez as host, Nigel Lythgoe as the main judge, and Mary Murphy, Dan Karaty, Mia Michaels and Brian Friedman as most frequent guest judges.  Nick Lazzarini was crowned America's Favorite Dancer on October 5, 2005 with 37.7% of the votes.\n\nMia Michaels: Mia Michaels (born February 23, 1966) is an American choreographer best known as a judge and for her contemporary choreography on the TV show \"So You Think You Can Dance\" (SYTYCD).  She has worked with musical artists such as Celine Dion, Madonna, Tom Cruise, Catherine Zeta-Jones, Ricky Martin, Gloria Estefan, and Prince.  In 2005 she choreographed Cirque du Soleil's world tour, \"Delirium\" as well as Celine Dion's Las Vegas show \"A New Day...\" for which she was later nominated for Emmy.  In 2007 she won an Emmy Award for Outstanding Choreography for her \"Calling You\" routine on season 2 of \"So You Think You Can Dance\"; she won again in 2010 for her work on season 5.  She was a main judge of So You Think You Can Dance together with Adam Shankman and Nigel Lythgoe for season 7.  She choreographed the dance sequence of \"Get Happy\" in Season 7 Episode 15 of the \"House\" episode \"Bombshells\".\n\nParamount Television Network: The Paramount Television Network (PTN) was a venture by American film corporation Paramount Pictures to organize a television network in the late 1940s.  The company built television stations KTLA in Los Angeles and WBKB in Chicago; it also invested US$400,000 in the DuMont Television Network, which operated stations WABD in New York City, WTTG in Washington, D.C., and WDTV in Pittsburgh.  Escalating disputes between Paramount and DuMont concerning breaches of contract, company control, and network competition erupted regularly between 1940 and 1956, and culminated in the dismantling of the DuMont Network.  Television historian Timothy White called the clash between the two companies \"one of the most unfortunate and dramatic episodes in the early history of the television industry.\"\n\nQuestion: What television network are both Mia Michaels and So You Think You Can Dance on?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"television_network_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television network.\"\n    },\n    \"connecting_show\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"show_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the show that both the personality and the network are associated with.\"\n        },\n        \"show_network\": {\n          \"type\": \"string\",\n          \"description\": \"The network on which the connecting show airs.\"\n        }\n      },\n      \"required\": [\n        \"show_title\",\n        \"show_network\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"connecting_personality\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"personality_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the personality associated with the connecting show and network.\"\n        },\n        \"role_in_show\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the personality in the connecting show.\"\n        }\n      },\n      \"required\": [\n        \"personality_name\",\n        \"role_in_show\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"A brief explanation of why this network is the answer, linking the personality and the show to the network.\"\n    }\n  },\n  \"required\": [\n    \"television_network_name\",\n    \"connecting_show\",\n    \"connecting_personality\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "television_network_name": {
        "type": "string",
        "description": "The name of the television network."
      },
      "connecting_show": {
        "type": "object",
        "properties": {
          "show_title": {
            "type": "string",
            "description": "The title of the show that both the personality and the network are associated with."
          },
          "show_network": {
            "type": "string",
            "description": "The network on which the connecting show airs."
          }
        },
        "required": [
          "show_title",
          "show_network"
        ],
        "additionalProperties": false
      },
      "connecting_personality": {
        "type": "object",
        "properties": {
          "personality_name": {
            "type": "string",
            "description": "The name of the personality associated with the connecting show and network."
          },
          "role_in_show": {
            "type": "string",
            "description": "The role of the personality in the connecting show."
          }
        },
        "required": [
          "personality_name",
          "role_in_show"
        ],
        "additionalProperties": false
      },
      "reasoning": {
        "type": "string",
        "description": "A brief explanation of why this network is the answer, linking the personality and the show to the network."
      }
    },
    "required": [
      "television_network_name",
      "connecting_show",
      "connecting_personality",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
