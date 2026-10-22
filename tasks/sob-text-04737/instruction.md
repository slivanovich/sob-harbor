Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Welwyn Garden City F.C.: Welwyn Garden City Football Club is a football club based in Welwyn Garden City, Hertfordshire .  They currently play in Spartan South Midlands League Premier Division , Level 9 of the National League System.

Welwyn: Welwyn is a village and civil parish in Hertfordshire, England.  The parish also includes the villages of Digswell and Oaklands.  It is sometimes called Old Welwyn to distinguish it from the much newer settlement of Welwyn Garden City, about a mile to the south, though some residents dislike the suggestion of inferiority or irrelevance that tends to be implied by the moniker "Old" and prefer Welwyn Village.

Ayot Greenway: The Ayot Greenway is a rail trail which extends from Ayot St. Peter, just west of Welwyn Garden City and the A1(M) Motorway to Wheathampstead in Hertfordshire.  Part of National Cycle Network Route 57, it runs for three miles along a former branch line from Welwyn Garden City railway station towards Luton and Dunstable.

Digswell Arts Trust: Digswell Arts Trust was the brainchild of Henry Morris, a pioneering educationalist.  Through his enthusiasm, dedication and influence he persuaded the Government and the Welwyn Garden City Development Corporation to establish a Trust for professional artists in Welwyn Garden City, England.

Tewingas: The Tewingas were a tribe or clan of Anglo-Saxon England, whose territory was centred on the settlement of Welwyn in modern-day Hertfordshire, the site of an early Minster church, and the nearby settlement of Tewin.  Its name means either "the people of Tiwa" or "the worshippers of the God Tew".

Welwyn Garden City railway station: Welwyn Garden City railway station serves the town of Welwyn Garden City in Hertfordshire, England.  The station is approximately 20 mi north of London Kings Cross on the East Coast Main Line.  Welwyn Garden City station is managed and served by Great Northern.

Welwyn Garden City: Welwyn Garden City is a town in Hertfordshire, England.  It is located approximately 20 mi from Kings Cross, London.  Welwyn Garden City was the second garden city in England (founded 1920) and one of the first new towns (designated 1948).

Charles Purdom: Charles Benjamin Purdom, usually credited as C. B. Purdom (15 Oct 1883 – 8 July 1965), was a British author, drama critic, town planner, and economist.  He was one of the pioneers and founders of the first garden cities, Letchworth and Welwyn Garden City, the latter of which he was appointed Finance Director between 1919–1928.  He was then made Honorary Secretary, then Treasurer of the International Federation for Housing and Planning (1931–1935).  He was also founder of the Letchworth and Welwyn Garden City Theatre Society, now the Welwyn Drama Club.  He won the Howard Walden cup at the Welwyn Garden City Drama Festival and the David Belasco cup in New-York in 1927.  He was an author of many books on city development, on Shakespeare and Bernard Shaw plays, Harley Granville-Barker, and on producing plays.  He was editor of an English literary periodical called "Everyman", covering books, drama, music and travel and featured articles by renowned authors such as Ivor Brown, Arthur Machen, G. K. Chesterton, A. E. Coppard, and Bertrand Russell.  He was General Secretary of British Equity (1939–1940) and joint secretary of the London Theatre Council.  He was also the earliest biographer of Meher Baba.  He was father of the actor Edmund Purdom.  He died in Welwyn Garden City in 1965.

Cole Green Way: The Cole Green Way is a rail trail which runs east-west from the eastern edge of Welwyn Garden City to Hertford in Hertfordshire.  Part of National Cycle Network Route 61, and the Lea Valley Walk, it runs for more than six miles along the former Hertford, Luton & Dunstable branch line from Welwyn Garden City railway station to Hertford North railway station.

Quantum Care Limited: Quantum Care Limited is a company based in Welwyn Garden City, England, that runs both residential and nursing care homes (see residential care home and nursing care home).  The company's head office is 4 Silver Court, Watchmead, Welwyn Garden City, Hertfordshire, England AL7 1TS.  Quantum Care runs twenty-eight care homes, all but two in Hertfordshire.

Question: It is likely that in Anglo-Saxon England that the residents of Welwyn Garden City worshiped which diety?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_focus_entity": {
      "type": "string",
      "description": "The primary entity mentioned in the question for which information is sought."
    },
    "historical_period_of_inquiry": {
      "type": "string",
      "description": "The historical period specified in the question."
    },
    "entity_existed_during_period": {
      "type": "boolean",
      "description": "Indicates whether the question_focus_entity existed during the specified historical period according to the context."
    },
    "founding_details_of_entity": {
      "type": "object",
      "properties": {
        "founding_year": {
          "type": "integer",
          "description": "The year the question_focus_entity was founded."
        },
        "founding_description": {
          "type": "string",
          "description": "A description of the entity's founding or designation."
        }
      },
      "required": [
        "founding_year",
        "founding_description"
      ],
      "additionalProperties": false
    },
    "related_ancient_settlement_information": {
      "type": "object",
      "properties": {
        "settlement_name": {
          "type": "string",
          "description": "The name of the ancient settlement related to the area of the question_focus_entity."
        },
        "tribe_associated": {
          "type": "string",
          "description": "The name of the tribe or clan associated with the ancient settlement during the historical period."
        },
        "possible_deity_worshipped_by_tribe": {
          "type": "string",
          "description": "The deity possibly worshipped by the associated tribe."
        }
      },
      "required": [
        "settlement_name",
        "tribe_associated",
        "possible_deity_worshipped_by_tribe"
      ],
      "additionalProperties": false
    },
    "most_likely_deity_for_related_area_in_period": {
      "type": "string",
      "description": "Based on the context, the most likely deity worshipped in the related geographical area during the specified historical period, acknowledging the question's premise that Welwyn Garden City did not exist then."
    }
  },
  "required": [
    "question_focus_entity",
    "historical_period_of_inquiry",
    "entity_existed_during_period",
    "founding_details_of_entity",
    "related_ancient_settlement_information",
    "most_likely_deity_for_related_area_in_period"
  ],
  "additionalProperties": false
}
