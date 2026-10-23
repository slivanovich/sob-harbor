{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRobert Weiss (choreographer): Robert Weiss is an American ballet dancer, choreographer, and Artistic Director of Carolina Ballet.  He began his professional career at age 17 joining the New York City Ballet under George Balanchine, eventually becoming a Principal Dancer.  Balanchine created several roles for him, including Ballo della Regina.  Weiss remained with the New York City Ballet for 16 years.  He later served as Artistic Director of the Pennsylvania Ballet from 1982 to 1990.  Weiss then became the founding Artistic Director of Carolina Ballet in 1997 where he has remained to this day.\n\nJohn Clifford (choreographer): John Clifford, born June 12th is the founder / artistic director of the original Los Angeles Ballet (1974–1985), and the chamber sized touring ensemble, Ballet of Los Angeles (1988–1991) and the creator of “CASABLANCA, THE DANCE” produced by Warner Bros.  Theatre Ventures, Inc. (which premiered in Beijing, China at the historic \"Great Hall of the People\" in 2005) and his Los Angeles Dance Theater.  Before that time,Clifford was a principal dancer and choreographer with George Balanchine’s New York City Ballet, (1966–1974) and guest artist from 1974–1980, and was widely considered to be Balanchine’s protégé (Saturday Review).  He choreographed his first (of 8) ballets for the NYC Ballet under Balanchine at age 20 thus making him the 2nd youngest choreographer in history ever to be attached to a major company.  The first was Balanchine himself who was 20 yrs-old when he choreographed his first ballet for Serge Diaghilev's \"Ballets Russes.\"  During his time with Balanchine, in his early 20's, he also was a guest choreographer with co's ranging from the San Francisco Ballet, to the Royal Winnipeg Ballet, to the Deutsche Oper Ballet in Berlin.  Clifford's works were also featured in many TV shows and movies, such as \"Flashdance,\" \"The Man Who Loved Women,\" and TV series such as \"Dynasty,\" \"Glitter,\" and other shows produced by Blake Edwards and Aaron Spelling.\n\nHeather Watts: Heather Watts (born September 27, 1953), was a principal ballerina with New York City Ballet.  A native of California, Ms. Watts was born as Linda Heather Watts in Long Beach on September 27, 1953.  As a little girl, she was a troublemaking child.  She had always wanted to be an actress.  An acting coach advised her taking ballet classes, seeing as she was incredibly dramatic (and clumsy).  She started dancing at the age of 10, came to New York at the age of 13 on a Ford Foundation summer scholarship to attend the School of American Ballet, the official school of the New York City Ballet.  She moved permanently to New York at age 15, again on a Ford Foundation scholarship to the School of American Ballet.  Watts joined the New York City Ballet in 1970 and was promoted to principal dancer by company founder George Balanchine in 1979.  George Balanchine took Watts into his companies \"because he would not let such a talent disappear.\"  During Ms. Watts's tenure with the company, she had numerous principal roles created for her by George Balanchine, Jerome Robbins, and Peter Martins among others.  Mr. Balanchine gave Ms. Watts the principal roles in many of his existing masterpieces, including \"Agon\", Concerto Barocco, \"Apollo\", Symphony in C, \"Theme and Variations\" and \"Serenade\".  Ms. Watts performed around the world and starred in numerous \"Dance in America\" television programs, and she performed opposite frequent partner Mikhail Baryshnikov at the White House in a national televised performance of Balanchine's \"Rubies\" for President and Mrs. Carter.  Ms. Watts retired from the stage in a gala performance at Lincoln Center in 1995.\n\nMarina Eglevsky: Marina Eglevsky is an American ballet dancer born in New York City.  She is the daughter of ballet star Andre Eglevsky and ballerina Leda Anchutina Eglevsky.  Marina studied at the School of American Ballet and the American Ballet Theatre School.  Marina performed professionally in New York City Ballet's production of \"The Nutcracker,\" with the Eglevsky Ballet Company, and as a guest in various companies and engagements.\n\nSchool of American Ballet: The School of American Ballet (SAB) is an American classical ballet school and is the associate school of the New York City Ballet, a ballet company based at the Lincoln Center for the Performing Arts in New York City.  The school trains students from the age of six, with professional vocational ballet training for students aged 11–18.  Graduates of the school achieve employment with leading ballet companies worldwide, most notably in the United States with New York City Ballet, American Ballet Theatre, Boston Ballet, and San Francisco Ballet.\n\nVera Zorina: Vera Zorina (January 2, 1917 – April 9, 2003) was a Norwegian ballerina, theatre and film actress, and choreographer.  Today she is chiefly remembered for her films choreographed by her then husband, George Balanchine.  They include \"The Goldwyn Follies\", \"I Was an Adventuress\" with Erich Von Stroheim and Peter Lorre, \"Louisiana Purchase\" with Bob Hope and dancing to \"That Old Black Magic\" in Paramount Pictures' \"Star Spangled Rhythm\".\n\nHolly Hynes: Holly Hynes is an accomplished costume designer with over 250 ballets to her credit, including more than 70 at the New York City Ballet.  Ms. Hynes' designs are also on view in companies around the world, including American Ballet Theatre, San Francisco Ballet, Bolshoi Ballet, National Ballet of Canada, Kirov Ballet, Royal Ballet, Paris Opera Ballet, Royal Danish Ballet, La Scala Theatre Ballet, Koninklijk Ballet van Vlaanderen, Houston Ballet, BalletMet, Pennsylvania Ballet, Ballet Vancouver, Les Grands Ballets Canadiens, American Repertory Ballet, Pacific Northwest Ballet, Atlanta Ballet, Richmond Ballet, Nashville Ballet, Miami City Ballet, Alberta Ballet, Joffrey Ballet, Kansas City Ballet , and the Suzanne Farrell Ballet at The John F. Kennedy Center for the Performing Arts, where she serves as the resident costume designer.\n\nNew York City Ballet: New York City Ballet (NYCB) is a ballet company founded in 1948 by choreographer George Balanchine and Lincoln Kirstein.  Léon Barzin was the company's first music director.  Balanchine and Jerome Robbins are considered the founding choreographers of the company.  City Ballet grew out of earlier troupes: the Producing Company of the School of American Ballet, 1934; the American Ballet, 1935, and Ballet Caravan, 1936, which merged into American Ballet Caravan, 1941; and directly from the Ballet Society, 1946.\n\nLes Noces (Robbins): Les Noces is a ballet choreographed by Jerome Robbins, subsequently New York City Ballet balletmaster, to the 1923 version of Stravinsky's eponymous music for American Ballet Theatre with sets by Oliver Smith under the supervision of Rosaria Sinisi, costumes by Patricia Zipprodt, and lighting by Jennifer Tipton.  The premiere took place March 30, 1965, at the New York State Theater, Lincoln Center.  The choreographer re-staged \"Les Noces\" for New York City Ballet to a recording of the piece by the Pokrovsky Ensemble, sung in the full-throated style of traditional Russian village wedding celebrations.  The restaging premiered May 20, 1998, again at the New York State Theater.  It was Robbins' last work.\n\nGeorge Balanchine: George Balanchine (born Giorgi Melitonovich Balanchivadze; January 22, 1904April 30, 1983) was a choreographer.  Styled as the father of American ballet, he co-founded the New York City Ballet and remained its Artistic Director for more than 35 years.\n\nQuestion: Vera Zorina (January 2, 1917 – April 9, 2003) was a Norwegian ballerina, theatre and film actress, and choreographer, today she is chiefly remembered for her films choreographed by her then husband, who (born January 22, 1904 - April 30, 1983) was a choreographer, styled as the father of American ballet, he co-founded the New York City Ballet and remained its Artistic Director for more than 35 years?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_identified\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person identified as Vera Zorina's husband.\"\n    },\n    \"relationship_to_vera_zorina\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the identified person to Vera Zorina.\"\n    },\n    \"person_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"full_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the identified person.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"description\": \"The birth date of the identified person.\"\n        },\n        \"death_date\": {\n          \"type\": \"string\",\n          \"description\": \"The death date of the identified person.\"\n        },\n        \"roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Key professional roles or titles held by the identified person.\"\n        },\n        \"years_as_artistic_director_of_nycb\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of years the person served as Artistic Director of New York City Ballet.\"\n        }\n      },\n      \"required\": [\n        \"full_name\",\n        \"birth_date\",\n        \"death_date\",\n        \"roles\",\n        \"years_as_artistic_director_of_nycb\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_identified\",\n    \"relationship_to_vera_zorina\",\n    \"person_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_identified": {
        "type": "string",
        "description": "The name of the person identified as Vera Zorina's husband."
      },
      "relationship_to_vera_zorina": {
        "type": "string",
        "description": "The relationship of the identified person to Vera Zorina."
      },
      "person_details": {
        "type": "object",
        "properties": {
          "full_name": {
            "type": "string",
            "description": "The full name of the identified person."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the identified person."
          },
          "death_date": {
            "type": "string",
            "description": "The death date of the identified person."
          },
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Key professional roles or titles held by the identified person."
          },
          "years_as_artistic_director_of_nycb": {
            "type": "integer",
            "description": "The number of years the person served as Artistic Director of New York City Ballet."
          }
        },
        "required": [
          "full_name",
          "birth_date",
          "death_date",
          "roles",
          "years_as_artistic_director_of_nycb"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_identified",
      "relationship_to_vera_zorina",
      "person_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
