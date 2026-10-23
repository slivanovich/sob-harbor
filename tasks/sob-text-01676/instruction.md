{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDrama Desk Award for Outstanding Director: This is a list of winners of the Drama Desk Award for Outstanding Director introduced in 1955 to honour directors of plays and directors of musicals.  From 1968, multiple awards were presented for each season.  In 1975 the category was retired and divided into Drama Desk Award for Outstanding Director of a Play and Drama Desk Award for Outstanding Director of a Musical, with each discipline receiving its own.\n\nDrama Desk Award for Outstanding Set Design: The Drama Desk Award for Outstanding Set Design is an annual award presented by Drama Desk in recognition of achievements in the theatre among Broadway, Off Broadway and Off-Off Broadway productions.  In the 1998 ceremony the category was separated, to honor both plays and musicals.  The category was reinstated in the 2010 ceremony.\n\nEugene Lee (designer): Eugene Lee (Scenic Designer) was born in Beloit, Wisconsin, in 1939.  He attended Beloit Memorial High School.  He has been resident designer at Trinity Repertory Company in Providence, Rhode Island, since 1967.  He has BFA degrees from the Art Institute of Chicago and Carnegie Mellon University, an MFA from Yale Drama School and three honorary Ph.Ds.  Mr. Lee has won Tony Awards for Bernstein’s \"Candide\", Sondheim’s \"Sweeney Todd\", and \"Wicked\", as well as the Drama Desk Award for Outstanding Set Design.  He is the production designer for NBC’s \"Saturday Night Live\".  Other New York theatre work includes Amazing Grace, \"Alice in Wonderland\", \"The Normal Heart\", \"Agnes of God\", \"Ragtime\", \"Uncle Vanya\", \"Ruby Sunrise\", \"Bounce\", and \"A Number\".  Film credits include Coppola’s \"Hammett\", Huston’s \"Mr. North\" and Malle’s \"Vanya on 42nd Street\".  Mr. Lee is an adjunct professor at Brown University, resident set designer at Trinity Repertory Company, and lives with his wife Brooke in Providence, where they raised their two sons.\n\nRichard Hudson (stage designer): Richard Hudson (born 9 June 1954) is a Zimbabwean stage designer best known for his work for \"The Lion King\", which won him the Tony Award for Best Scenic Design and the Drama Desk Award for Outstanding Set Design.  He studied at Wimbledon School of Art.\n\nTim Hatley: Tim Hatley is a British set and costume designer for theater and film.  He is the winner of the Tony Award for Best Set Design and Best Costume Design, the Drama Desk Award for Outstanding Set Design, the Drama Desk Award for Outstanding Costume Design, and the Laurence Olivier Award for Best Set Design.\n\nAn Inspector Calls: An Inspector Calls is a play written by English dramatist J. B. Priestley, first performed in 1945 in the Soviet Union and in 1946 in the UK.  It is one of Priestley's best known works for the stage, and is considered to be one of the classics of mid-20th century English theatre.  The play's success and reputation has been boosted in recent years by a successful revival by English director Stephen Daldry for the National Theatre in 1992, and a tour of the UK in 2011–2012.\n\nRob Howell: Robert (Rob) Stuart Howell is a British costume and set designer.  He is primarily known for his work on the London stage.  Howell won the Olivier Award for his set design for the musical \"Matilda the Musical\" in 2012.  He has also designed both scenery and costumes for several Broadway shows, and won the Drama Desk Award for Outstanding Set Design for \"Ghost the Musical\" in 2012.\n\nIan MacNeil (scenic designer): Ian MacNeil (born 1960) is a British scenic designer.  He won the 1994 Drama Desk Award for Outstanding Set Design for \"An Inspector Calls\" and the 2009 Tony Award for Best Scenic Design of a Musical for \"Billy Elliot The Musical\".\n\nDale Ferguson (designer): Dale Ferguson is an Australian theatrical scenic and costume designer who was nominated for the Tony Award for Best Costume Design, the Tony Award for Best Scenic Design, and the Drama Desk Award for Outstanding Set Design for the 2009 Broadway revival of \"Exit the King\".\n\nBrothers Quay: Stephen and Timothy Quay ( ; born June 17, 1947) are American identical twin brothers better known as the Brothers Quay or Quay Brothers.  They are influential stop-motion animators.  They are also the recipients of the 1998 Drama Desk Award for Outstanding Set Design for their work on the play \"The Chairs\".\n\nQuestion: What play write's play won a Drama Desk Award for Outstanding Set Design?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"playwright_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the playwright.\"\n    },\n    \"play_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"play_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the play that won the award.\"\n        },\n        \"designer_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the designer who won the award for the play.\"\n        }\n      },\n      \"required\": [\n        \"play_title\",\n        \"designer_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"award_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"award_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the award won.\"\n        },\n        \"award_category\": {\n          \"type\": \"string\",\n          \"description\": \"The specific category of the award.\"\n        },\n        \"award_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the award was won.\"\n        }\n      },\n      \"required\": [\n        \"award_name\",\n        \"award_category\",\n        \"award_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"playwright_name\",\n    \"play_details\",\n    \"award_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "playwright_name": {
        "type": "string",
        "description": "The name of the playwright."
      },
      "play_details": {
        "type": "object",
        "properties": {
          "play_title": {
            "type": "string",
            "description": "The title of the play that won the award."
          },
          "designer_name": {
            "type": "string",
            "description": "The name of the designer who won the award for the play."
          }
        },
        "required": [
          "play_title",
          "designer_name"
        ],
        "additionalProperties": false
      },
      "award_details": {
        "type": "object",
        "properties": {
          "award_name": {
            "type": "string",
            "description": "The name of the award won."
          },
          "award_category": {
            "type": "string",
            "description": "The specific category of the award."
          },
          "award_year": {
            "type": "integer",
            "description": "The year the award was won."
          }
        },
        "required": [
          "award_name",
          "award_category",
          "award_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "playwright_name",
      "play_details",
      "award_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
