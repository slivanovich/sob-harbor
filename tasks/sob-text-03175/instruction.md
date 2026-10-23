{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nA Bayou Legend: A Bayou Legend is an American opera composed by William Grant Still, with a libretto by his wife and frequent collaborator, Verna Arvey.\n\nStill Waters Youth Sinfo-Nia: Still Waters Sinfo-Nia is a predominantly African-American youth orchestra located in Atlanta, Georgia, United States.  It was originally called the William Grant Still Memorial Orchestra.  The organization was started in 1990 and has been led by David E. Robinson III.\n\nTroubled Island: Troubled Island is an American opera in three acts composed by William Grant Still, with a libretto begun by poet Langston Hughes and completed by Verna Arvey.  She married the composer following their collaboration.\n\nWilliam Grant Still: William Grant Still (May 11, 1895 – December 3, 1978) was an American composer, who composed more than 150 works, including five symphonies and eight operas.\n\nThe Juggler of Our Lady (opera): The Juggler of Our Lady is an opera in one act composed by Ulysses Kay to a libretto by Alexander King.  The libretto is based on Robert O. Blechman's 1953 book \"The Juggler of Our Lady.  A Medieval Legend\".  Composed in 1956, the opera premiered on 23 February 1962 in New Orleans, Louisiana performed by the Xavier University Opera Workshop.  It was performed again in 1972 by Opera/South in Jackson Mississippi in a double bill with William Grant Still's opera \"Highway 1, U.S.A.\".  The 1972 performance of both operas was also broadcast on Voice of America.\n\nMississippi Institute of Arts and Letters: The Mississippi Institute of Arts and Letters (MIAL) is a privately funded foundation created to recognize annually the greatest accomplishments in art, music, literature, and photography among Mississippians.  The idea was conceived by, among others, former Mississippi Governor William Winter, Dr. Cora Norman, Dr. Aubrey Lucas, and Dr. Noel Polk in 1978, and the first awards were given out in 1980.  Nominations for these awards may be made only by registered members of the Institute.  The winners are chosen by a jury of prominent academics in each of the seven fields: Fiction, Non-fiction, Visual Art, Concert Musical Composition, Popular Musical Composition, Photography, and Poetry.  The ceremony is held in a different Mississippi city each year.  Past winners have included Walker Percy, Ellen Douglas, Ellen Gilchrist, Richard Ford, Larry Brown, Rick Bass, Lewis Nordan, Beverly Lowry, Donna Tartt, Clifton Taulbert, Barry Hannah, Willie Morris, Leontyne Price, Cynthia Shearer, Stephen Ambrose, Steve Yarbrough, Tom Franklin, Brad Watson, Shelby Foote, Natasha Trethewey, Birney Imes, Maude Schyler Clay, William Grant Still, Morgan Freeman, Christopher Maurer, Wyatt Waters, Logan Skelton, and many others.  Lifetime achievement awards have been presented to artists such as Gulf Coast painter and potter Walter Anderson, Jackson writer Eudora Welty, and the distinguished film actor from the Delta, Morgan Freeman.\n\nMississippi Opera: The Mississippi Opera is an American opera company located in Jackson, Mississippi.  Founded in 1945, the company presents an annual season of opera consisting of two fully staged opera productions and smaller concerts and workshops open to the public.  The company's productions are performed at the Belhaven University Center for the Arts.  Composer William Grant Still and soprano Leontyne Price both have associations with the company.\n\nVerna Arvey: Verna Arvey (February 16, 1910 – November 22, 1987) was an American librettist, pianist and writer who is best known for her musical collaborations with her husband William Grant Still, a musician and composer.\n\nSymphony No. 1 &quot;Afro-American&quot;: Symphony No. 1 in A-flat, \"Afro-American\" (1930) by William Grant Still was the first symphony written by an African American and performed for a United States audience by a leading orchestra.  It was premiered in 1931 by the Rochester Philharmonic Orchestra.  It is a symphonic piece for full orchestra, including celeste, harp, and tenor banjo.  It combines a fairly traditional symphonic form with blues progressions and rhythms that were characteristic of popular African-American music at the time.  This combination expressed Still's integration of black culture into the classical forms.  Still used quotes from four dialect poems by early 20th-century African-American poet Paul Laurence Dunbar as epigraphs for each symphonic movement.\n\nWilliam Grant &amp; Sons: William Grant & Sons Ltd. is an independent, family-owned Scottish company which distills Scotch whisky and other selected categories of spirits.  It was established in 1887 by William Grant, and is now run by the descendants of the founder.  It is the largest of the handful of Scotch whisky distillers remaining in family ownership.  \"William Grant & Sons\" is often abbreviated to \"W. Grant & Sons\" or just \"Grant's\", after their blended whisky of the same name.\n\nQuestion: What was the birthdate of the composer who worked on A Bayou Legend with William Grant Still?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"opera_name\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the opera mentioned in the question.\"\n    },\n    \"primary_composer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the main composer of the opera.\"\n    },\n    \"collaborator_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who collaborated on the opera with the primary composer.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The specific role of the collaborator in the opera's creation (e.g., librettist).\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"description\": \"The birth date of the collaborator.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\",\n        \"birth_date\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"opera_name\",\n    \"primary_composer_name\",\n    \"collaborator_info\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "opera_name": {
        "type": "string",
        "description": "The title of the opera mentioned in the question."
      },
      "primary_composer_name": {
        "type": "string",
        "description": "The name of the main composer of the opera."
      },
      "collaborator_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person who collaborated on the opera with the primary composer."
          },
          "role": {
            "type": "string",
            "description": "The specific role of the collaborator in the opera's creation (e.g., librettist)."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the collaborator."
          }
        },
        "required": [
          "name",
          "role",
          "birth_date"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "opera_name",
      "primary_composer_name",
      "collaborator_info"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
