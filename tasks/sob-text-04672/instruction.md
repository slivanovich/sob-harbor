{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nServing Sara: Serving Sara is a 2002 American romantic comedy film directed by Reginald Hudlin and starring Matthew Perry, Elizabeth Hurley, and Bruce Campbell.  Joe Tyler (Perry) is a process server who is given the assignment to serve Sara Moore (Hurley) with divorce papers.  He does so, but Moore persuades Tyler to serve Moore's husband instead so that she can get a larger portion of his money in the divorce.  The rest of the film follows their attempt to carry out Sara's plan.\n\nRostislav Čtvrtlík: Rostislav Čtvrtlík (9 November 1963 – 6 March 2011) was a Czech stage, television and voice actor.  He was the Czech voice of Matthew Perry in \"Friends\" and other TV shows and movies.\n\nUSNS Matthew Perry (T-AKE-9): USNS \"Matthew Perry\" (T-AKE-9) is a \"Lewis and Clark\"-class dry cargo ship of the United States Navy, named in honor of Commodore Matthew C. Perry (1794–1858), who led the effort to open Japan to trade with the West.\n\nSakoku: Sakoku (鎖国 , \"closed country\" but commonly translated as \"period of national isolation\") was the isolationist foreign policy of the Japanese Tokugawa shogunate under which relations and trade between Japan and other countries were severely limited, nearly all foreigners were barred from entering Japan and the common Japanese people were kept from leaving the country.  The policy was enacted by the Tokugawa shogunate under Tokugawa Iemitsu through a number of edicts and policies from 1633–39, and ended after 1853 when the American Black Ships commanded by Matthew Perry forced the opening of Japan to American (and, by extension, Western) trade through a series of unequal treaties.\n\nThe End of Longing: The End of Longing is a dark comedy play written by Matthew Perry.  The play which marked Perry's playwriting debut made its West End and world premiere at the Playhouse Theatre, in February 2016.  The play made its United States debut Off-Broadway in May 2017, at the The Lucille Lortel Theatre.\n\nBoxing in Japan: The history of boxing in Japan began in 1854 when Matthew Perry landed at Shimoda, Shizuoka soon after the Convention of Kanagawa.  At that time, American sailors often engaged in sparring matches on board their ships, with their fists wrapped in thin leather.  It was the first example of boxing conveyed to Japan.  In addition, an ōzeki-ranked sumo wrestler named Tsunekichi Koyanagi (小柳 常吉 ) was summoned by the Shogunate, and ordered to fight a boxer and a wrestler from the United States.  The three fought matches, using different martial arts' styles, before Perry and other spectators.  Koyanagi reportedly won.\n\nNakagusuku Bay: Nakagusuku Bay (中城湾 , Nakagusuku-wan ) is a bay on the southern coast of Okinawa Island on the Pacific Ocean in Japan.  The bay covers 220 km2 and ranges between 10 m to 15 m deep.  The bay is surrounded by the municipalities of Uruma, Kitanakagusuku, Nakagusuku, Nishihara, Yonabaru, Nanjō, all in Okinawa Prefecture.  In 1852, while visiting the Ryukyu Kingdom, Commodore Matthew Perry mapped Okinawa and labeled Nakagusuku Bay as \"Perry's Bay\".  During the final months of World War II, the bay became a U.S. Navy forward base, and was nicknamed \"Buckner Bay\".\n\nMatthew Perry: Matthew Langford Perry (born August 19, 1969) is a Canadian-American actor, best known for his role as Chandler Bing on the long-running NBC television sitcom \"Friends\", as well as his portrayal of Ron Clark in the 2006 television movie \"The Ron Clark Story\".\n\nJeddo, Japan: Jeddo and Yedo or Yeddo are anglicisations referring to the town and port of Edo, Japan and the adjacent large bay, and generally to the ruling shogunate of Japan during the 1850s and 1860s, which was based in Edo.  After 1868, Edo was renamed as Tokyo.  The names Jeddo and Yedo became commonly used by English-speaking people in the mid-1800s, following the expedition of Commodore Matthew Perry, which resulted in the opening of Japan to trade.  Neither name is in common use today, as a name of reference for Edo, or the bay, or the Tokugawa shogunate associated with Edo.  Following the Perry Expedition, there was an increase in popular interest in Japan, and a number of American communities were named Jeddo or Yeddo.\n\nMatthew Perry Monument (Newport, Rhode Island): Matthew Perry Monument is a statue commemorating Commodore Matthew C. Perry.  The statue is situated in Touro Park facing Bellevue Avenue in the heart of Newport, RI and was designed by John Quincy Adams Ward in 1869.  The pedestal was designed by Richard Morris Hunt.\n\nQuestion: What profession does Rostislav Čtvrtlík and Matthew Perry have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"shared_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The profession that both individuals have in common.\"\n    },\n    \"number_of_individuals\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of individuals discussed.\"\n    },\n    \"individuals\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each individual mentioned.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The full name of the individual.\"\n          },\n          \"primary_profession\": {\n            \"type\": \"string\",\n            \"description\": \"The main profession of the individual.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The nationality of the individual.\"\n          },\n          \"notable_work_or_role\": {\n            \"type\": \"string\",\n            \"description\": \"A significant work or role associated with the individual.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"primary_profession\",\n          \"nationality\",\n          \"notable_work_or_role\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"shared_profession\",\n    \"number_of_individuals\",\n    \"individuals\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "shared_profession": {
        "type": "string",
        "description": "The profession that both individuals have in common."
      },
      "number_of_individuals": {
        "type": "integer",
        "description": "The total number of individuals discussed."
      },
      "individuals": {
        "type": "array",
        "description": "Details about each individual mentioned.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The full name of the individual."
            },
            "primary_profession": {
              "type": "string",
              "description": "The main profession of the individual."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the individual."
            },
            "notable_work_or_role": {
              "type": "string",
              "description": "A significant work or role associated with the individual."
            }
          },
          "required": [
            "name",
            "primary_profession",
            "nationality",
            "notable_work_or_role"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "shared_profession",
      "number_of_individuals",
      "individuals"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
