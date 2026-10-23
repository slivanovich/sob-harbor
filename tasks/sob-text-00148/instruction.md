{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBridge Theatre: The Bridge Theatre is a new commercial theatre building near Tower Bridge in London, due to open on 18 October 2017.  It has been developed by Nick Starr and Nicholas Hytner and is the residency of their founded London Theatre Company, following their tenancy as executive director and artistic director, respectively, at the National Theatre.\n\nGilman &amp; Gonzalez-Falla Theatre Foundation: Gilman & Gonzalez-Falla Theatre Foundation give awards to new songwriters and book writers.  The award was set in 1991 up by the American Theatre Wing Board Member, Sondra Gilman, and Texas Art Commissioner, Celso Gonzalez-Falla.  The Musical Theatre Award is accompanied by a grant of $25,000.  A number of smaller grants (between $1,000- $5,000) are also awarded at the ceremony.  To qualify the \"writers must have had at least one musical produced in either a commercial or a professional non-profit theatre in America.\"\n\nBrandon Oldenburg: Brandon Oldenburg was an early employee of Reel FX Creative Studios (1995), doing a combination of design and special effects for television and film.  Serving as Senior Creative director for 15 years, he worked with such clients as Troublemaker Studios, Pixar, Disney, DreamWorks and Blue Sky Studios.  From 1998 to 2009 Oldenburg oversaw a joint venture with William Joyce and Reel FX.  Oldenburg and Joyce’s other collaborations include Halloween decor for Martha Stewart, Parade Floats for Disney and Title Design for feature films.  Their most recent story is now in production at DreamWorks called \"The Guardians of Childhood\".  Oldenburg's work has won many industry accolades, most recently the Distinguished Alumni of the Year from Ringling College of Art and Design, where he received his BFA in Illustration and sits on the Board of Trustees.  Oldenburg and renowned designer Brad Oldham collaborated on a giant sculptural series for a $1.4 million commission called The Traveling Man, which has drawn national attention.  Brandon's illustrations have graced the covers for such prestigious authors' books as Elmore Leonard and Michael Chabon.\n\nBryan Savery: Bryan Savery is an arts manager and producer of film and theatre.  He is the producer for The Red Room Theatre Company, projects producer for Somerset House, the Associate Producer for Peshkar Productions and consultant for the Waltham Forrest Cinema Project.  As well producing theatre and Film he is a Fellow of the Royal Society of Arts, Trustee of the Queen's Theatre, sits on the board of the Unicorn Theatre and is a former Vice Chair of the Independent Theatre Council (2003–2009).  In 2012, he was given Freedom of the City of London.\n\nJeffery Kissoon: Jeffery Kissoon (born 4 September 1947) is an actor with credits in British theatre, television, film and radio.  He has performed with the Royal Shakespeare Company at venues such as the Royal National Theatre, under directors including Peter Brook, Peter Hall, Robert Lepage, Janet Suzman, Calixto Bieito and Nicholas Hytner.  He has acted in genres from Shakespeare and modern theatre to television drama and science fiction, playing a range of both leading and supporting roles, from Mark Antony in \"Antony and Cleopatra\" and Prospero and Caliban in \"The Tempest\", to Malcolm X in \"The Meeting\" and Mr Kennedy in the children's TV series \"Grange Hill\".\n\nPeople (play): People is a play by the English playwright Alan Bennett.  Dealing with the travails of a crumbling stately home and its ageing owner, the play premièred at the National Theatre in 2012.  The production, directed by long-time Bennett collaborator Nicholas Hytner, featured Frances de la Tour, Nicholas le Prevost, Peter Egan and Linda Bassett.  It received widespread acclaim from London's theatre critics.  It toured the UK in 2013 with a cast including Siân Phillips, Brigit Forsyth and Selina Cadell.\n\nFemi Elufowoju Jr.: Femi Elufowoju Jr. (born 31 October 1962) is a British-born Nigerian actor, performer, and director.  He is the first theatre director of African descent to establish a national touring company in the UK.  His stage work has been featured at the Royal Court Theatre, the Royal National Theatre, the West Yorkshire Playhouse, Manchester's Royal Exchange, the Theatre Royal, Stratford East and the Soho Theatre, and he has worked under such notable theatre directors as Sir Richard Eyre, Nicholas Hytner, Yvonne Brewster, John Retallack, Annabel Arden, Jude Kelly and Annie Castledine.\n\nTanny B. Crane: Anne \"Tanny\" B. Crane is the President and CEO of Crane Group, Chair of the Board of Directors for the Federal Reserve Bank of Cleveland, and Director on the Board of Wendy's International.  Tanny Crane, granddaughter of Crane Plastics Company founder Robert Crane Sr, in 1987 as Director of Human Resources, and was promoted to Vice President of Sales and Marketing in 1993.  She became the President of Crane Plastics in 1996.  In January, 2003, she succeeded Jameson Crane to her current position.  She is also a member of the Dean's Advisory Council of the Fisher College of Business at The Ohio State University, sits on the Board of the United Way of Central Ohio, is a member of the Columbus Partnership and the Columbus Foundation, and sits on the Board of the Greater Columbus Chamber of Commerce.\n\nThe Old Vic: The Old Vic is a 1,000-seat, not-for-profit producing theatre, located just south-east of Waterloo station on the corner of the Cut and Waterloo Road in Lambeth, London, England.  Established in 1818 as the Royal Coburg Theatre, and renamed in 1833 the Royal Victoria Theatre, in 1871 it was rebuilt and reopened as the Royal Victoria Palace.  It was taken over by Emma Cons in 1880 and formally named the Royal Victoria Hall, although by this time it was already known as the \"Old Vic\".  In 1898, a niece of Cons, Lilian Baylis assumed management and began a series of Shakespeare productions in 1914.  The building was damaged in 1940 during air raids and it became a Grade II* listed building in 1951 after it reopened.\n\nJoyce Hytner: Joyce Anita Hytner OBE is a British theatrical fundraiser who sits on the board of the Old Vic, the Royal Court Theatre, the Criterion Theatre, the Quintessentially Foundation, Manchester International Festival, and works for the fundraising consultancy Act IV.\n\nQuestion: Joyce Hytner sits on the board of which 1,000-set theatre?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"theatre_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the theatre.\"\n    },\n    \"seat_capacity\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of seats in the theatre.\"\n    },\n    \"board_member\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who sits on the theatre's board.\"\n    },\n    \"theatre_attributes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_not_for_profit\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the theatre is a not-for-profit organization.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The general location of the theatre.\"\n        }\n      },\n      \"required\": [\n        \"is_not_for_profit\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"theatre_name\",\n    \"seat_capacity\",\n    \"board_member\",\n    \"theatre_attributes\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "theatre_name": {
        "type": "string",
        "description": "The name of the theatre."
      },
      "seat_capacity": {
        "type": "integer",
        "description": "The number of seats in the theatre."
      },
      "board_member": {
        "type": "string",
        "description": "The name of the person who sits on the theatre's board."
      },
      "theatre_attributes": {
        "type": "object",
        "properties": {
          "is_not_for_profit": {
            "type": "boolean",
            "description": "Indicates if the theatre is a not-for-profit organization."
          },
          "location": {
            "type": "string",
            "description": "The general location of the theatre."
          }
        },
        "required": [
          "is_not_for_profit",
          "location"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "theatre_name",
      "seat_capacity",
      "board_member",
      "theatre_attributes"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
