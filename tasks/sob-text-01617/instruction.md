{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n24th AVN Awards: The 24th AVN Awards ceremony, presented by Adult Video News (AVN), honored the best pornographic films of 2006 and took place January 13, 2007 at the Mandalay Bay Events Center in Paradise, Nevada.  During the ceremony, Adult Video News presented AVN Awards (commonly referred to as the Oscars of porn)) in 119 categories released during the eligibility period, Oct. 1, 2005 to Sept. 30, 2006.  The ceremony, televised in the United States by Playboy TV, was produced and directed by Gary Miller.  Adult film star Jessica Drake hosted for the first time, with comedian Jim Norton, who also co-hosted in 2004.\n\n13th AVN Awards: The 13th AVN Awards ceremony, organized by Adult Video News (AVN) honored the best pornographic films of 1995 and took place on January 7, 1996 at the Aladdin Theatre for the Performing Arts in Paradise, Nevada, beginning at 8:15 p.m. PST / 11:15 p.m. EST.  During the ceremony, AVN presented AVN Awards in 97 categories.  The ceremony, taped for broadcast in the United States by Spice Networks, was produced and directed by Gary Miller and Mark Stone.  Comedian Bobby Slayton hosted the show for the first time, alongside actress co-hosts Jenna Jameson and Julia Ann.  Hall of Fame inductees were honored at a gala held a month earlier.\n\n20th AVN Awards: The 20th AVN Awards ceremony, presented by Adult Video News (AVN), took place January 11, 2003 at the Venetian Hotel Grand Ballroom, at Paradise, Nevada, U.S.A.  During the ceremony, AVN presented AVN Awards in nearly 90 categories honoring the best pornographic films released between Oct. 1, 2001 and Sept. 30, 2002.  The ceremony was produced by Gary Miller and directed by Mark Stone.  Comedian Doug Stanhope co-hosted the show for the first time with adult film star Chloe.\n\n30th AVN Awards: The 30th AVN Awards ceremony, or XXX AVN Awards, was an event during which \"Adult Video News\" (\"AVN\") presented its annual AVN Awards to honor the best pornographic movies and adult entertainment products of 2012.  Movies or products released between October 1, 2011 and September 30, 2012 were eligible.  The ceremony was held on January 19, 2013 at The Joint in the Hard Rock Hotel and Casino, Paradise, Nevada.  Comedian April Macie, AVN Hall of Fame inductee Jesse Jane and Asa Akira, who won Female Performer of the Year, hosted the AVN Awards.  The awards show was held immediately after the Adult Entertainment Expo at the same venue.\n\n14th AVN Awards: The 14th AVN Awards ceremony, organized by Adult Video News (AVN), took place January 11, 1997 at Riviera Hotel & Casino, Winchester, Nevada, beginning at 7:45 p.m. PST / 10:45 p.m. EST.  During the show, AVN presented AVN Awards (the industry's equivalent of the Academy Awards) in 41 categories honoring the best pornographic films released released between Oct. 1, 1995 and Sept. 30, 1996.  The ceremony was produced by Gary Miller and directed by Mark Stone.  Comedian Bobby Slayton returned as host, with actresses Nici Sterling and Kylie Ireland as co-hosts.  At a pre-awards event held the previous evening, 60 more AVN Awards, mostly for technical achievements, were given out by hostess Dyanna Lauren and comedy ventriloquist Otto of Otto & George, however, the pre-awards event was neither televised nor distributed on VHS tapes as was the main evening’s ceremony.\n\nJulia Ann: Julia Ann (born October 8, 1969) is the stage name of American pornographic actress, feature dancer.  She is a member of the AVN Hall of Fame and the XRCO Hall of Fame.\n\n18th AVN Awards: The 18th AVN Awards ceremony, presented by Adult Video News (AVN), took place January 8, 2001 at the Venetian Hotel Grand Ballroom, at Paradise, Nevada, U.S.A.  During the ceremony, AVN presented AVN Awards in 77 categories honoring the best pornographic films released between Oct. 1, 1999 and Sept. 30, 2000.  The ceremony was produced by Gary Miller and directed by Mark Stone.  Adult film star Jenna Jameson hosted the show for the second time.\n\n17th AVN Awards: The 17th AVN Awards ceremony, presented by Adult Video News (AVN), took place January 8, 2000 at the Venetian Hotel Grand Ballroom, at Paradise, Nevada, U.S.A.  During the ceremony, AVN presented AVN Awards (often dubbed the \"Academy Awards Of Porn\") in 77 categories honoring the best pornographic films released between Oct. 1, 1998 and Sept. 30, 1999.  The ceremony was produced by Gary Miller and directed by Mark Stone.  Adult film star Juli Ashton hosted the show.\n\n16th AVN Awards: The 16th AVN Awards ceremony, organized by \"Adult Video News\" (AVN) honored the best of 1998 in pornographic movies and took place on January 9, 1999, at Bally's Las Vegas, Las Vegas, Nevada.  During the ceremony, AVN presented AVN Awards in 68 categories.  The ceremony, televised by Playboy TV, was produced by Gary Miller and directed by Mark Stone.  Comedian Robert Schimmel returned as host and actresses Alisha Klass, Midori and Serenity co-hosted the award show.  Five weeks earlier in a ceremony held at the Westin Bonaventure in Los Angeles, California, on December 4, 1998, the awards for gay pornographic movies were presented in a new separate ceremony known as the GayVN Awards.\n\n15th AVN Awards: The 15th AVN Awards ceremony, organized by Adult Video News (AVN), took place January 10, 1998 at Caesars Palace, in Paradise, Nevada, U.S.A.  During the show, AVN presented AVN Awards (the industry's equivalent of the Academy Awards) in 54 categories honoring the best pornographic films released released between Oct. 1, 1996 and Sept. 30, 1997.  The ceremony was produced by Gary Miller and directed by Mark Stone.  Comedian Robert Schimmel hosted, with adult film actresses Racquel Darrian and Misty Rain as co-hosts.  At a pre-awards cocktail reception held the previous evening, 50 more AVN Awards, mostly for behind-the-scenes achievements, were given out by hosts Nici Sterling and Dave Tyree, however, this event was neither televised nor distributed on VHS tapes as was the main evening's ceremony.  Both events included awards categories for gay movies; the final year the show included both gay and heterosexual awards.  The gay awards were subsequently spun off into a separate show, the GayVN Awards.\n\nQuestion: What pornographic star is a member of the XRCO Hall of Fame and co-hosted the 13th AVN Awards Ceremony?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"porn_star_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the pornographic star.\"\n    },\n    \"is_xrco_hall_of_fame_member\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the porn star is a member of the XRCO Hall of Fame.\"\n    },\n    \"co_hosted_awards_ceremonies\": {\n      \"type\": \"array\",\n      \"description\": \"List of AVN Awards ceremonies co-hosted by the star.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"ceremony_number\": {\n            \"type\": \"integer\",\n            \"description\": \"The ordinal number of the AVN Awards ceremony.\"\n          },\n          \"ceremony_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year the AVN Awards ceremony took place.\"\n          }\n        },\n        \"required\": [\n          \"ceremony_number\",\n          \"ceremony_year\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"porn_star_name\",\n    \"is_xrco_hall_of_fame_member\",\n    \"co_hosted_awards_ceremonies\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "porn_star_name": {
        "type": "string",
        "description": "The name of the pornographic star."
      },
      "is_xrco_hall_of_fame_member": {
        "type": "boolean",
        "description": "Indicates if the porn star is a member of the XRCO Hall of Fame."
      },
      "co_hosted_awards_ceremonies": {
        "type": "array",
        "description": "List of AVN Awards ceremonies co-hosted by the star.",
        "items": {
          "type": "object",
          "properties": {
            "ceremony_number": {
              "type": "integer",
              "description": "The ordinal number of the AVN Awards ceremony."
            },
            "ceremony_year": {
              "type": "integer",
              "description": "The year the AVN Awards ceremony took place."
            }
          },
          "required": [
            "ceremony_number",
            "ceremony_year"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "porn_star_name",
      "is_xrco_hall_of_fame_member",
      "co_hosted_awards_ceremonies"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
