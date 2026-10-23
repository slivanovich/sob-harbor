{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFrank Mickens: Dr. Frank Mickens (June 22, 1946 – July 9, 2009), was a nationally recognized New York City educator as principal of Boys and Girls High School at 1700 Fulton Street in the Bedford-Stuyvesant neighborhood of Brooklyn, one of America's toughest areas.  The seventeenth largest high school in the United States, Boys and Girls High School has a student population of over four thousand students.  Boys and Girls High School was built in the 1970s as a model 'education option' school, and Mickens successfully embraced this initiative as an administrator in the New York City Department of Education.  His cigar-chomping tough no-nonsense 'take charge' clawhammer approach earned Mickens 'tough love' comparisons to Joe Louis Clark and the controversial nickname 'The Chancellor of Fulton Street'.\n\nAnthony Salerno: Anthony \"Fat Tony\" Salerno (August 15, 1911 – July 27, 1992) was a New York mobster who served as underboss and front boss of the Genovese crime family from 1981 until his conviction in 1986.  Usually seen wearing a fedora and chomping on a cigar, he was nicknamed \"Fat Tony\" due to his size.\n\nTom Kapatos: Thomas Kapatos, also known as \"The Greek\" (died January 22, 1977) was a New York City mobster and an enforcer to Mickey Spillane during his war against Jimmy Coonan during the 1960s.  He was born to Greek-American emigrants from Karpathos and his last name \"Kapatos\" is derived from the island.  On the afternoon of January 22, 1977, Kapatos was gunned down on West 34th Street by a hired assassin in the employ of Anthony \"Fat Tony\" Salerno; he had been one of many of who had been killed in a six-month killing spree to secretly eliminate Spillane's associates.\n\nLew Baker: Lewis \"Lew\" Baker (born c. 1825, date of death unknown) was a patrolman in the New York Police Department who was simultaneously employed as a \"slugger\" for Tammany Hall.  He was involved in voter intimidation and election fraud during the 1840s and 1850s.  A close friend and associate of Irish mob boss John Morrissey, Baker frequently battled supporters of the nativist Know-Nothing movement for over a decade.  He is most remembered however as the assassin of William \"Bill the Butcher\" Poole.  Baker shot and killed Poole in a Broadway saloon during a brawl.  Both Baker and Morrissey were placed on trial for murder, but were acquitted.\n\nMafia Commission Trial: The Mafia Commission Trial (February 25, 1985 – November 19, 1986), officially known as United States v. Anthony Salerno, et al., was a criminal trial in New York City, United States.  Using evidence obtained by the Federal Bureau of Investigation, eleven organized crime figures, including the heads of New York's so-called \"Five Families,\" were indicted by United States Attorney Rudolph Giuliani under the Racketeer Influenced and Corrupt Organizations Act (RICO) on charges including extortion, labor racketeering, and murder for hire.  The case struck a blow against \"The Commission,\" a loose organization of the New York Mafia organizations that met to resolve disputes or discuss criminal activities, sometimes likened to organized crime's board of directors.  \"Time\" magazine called this \"Case of Cases\" possibly \"the most significant assault on the infrastructure of organized crime since the high command of the Chicago Mafia was swept away in 1943,\" and quoted Giuliani's stated intention: \"Our approach... is to wipe out the five families.\"\n\nDenise Borino-Quinn: Denise Borino-Quinn (January 6, 1964 – October 27, 2010) was an American television actress who had a recurring role as Ginny Sacramoni, the wife of New York mob boss Johnny Sack in the television series \"The Sopranos\".\n\nVincent Palermo: Vincent \"Vinny Ocean\" Palermo (born June 4, 1944) is a former American mobster who was \"de facto\" boss of the New Jersey DeCavalcante crime family before becoming a government witness.  Fictional mob boss Tony Soprano, the protagonist of the HBO series \"The Sopranos\", is said to be based upon Palermo.\n\nMichael James Genovese: Michael James Genovese (April 9, 1919 – October 31, 2006) was an alleged boss of the Pittsburgh crime family.  References to Michael Genovese as the brother of Vito Genovese are to a different Michael Genovese; Michael James Genovese was first cousin to New York mob boss Vito Genovese.\n\nBrotherhood (U.S. TV series): Brotherhood is an American crime drama television series created by Blake Masters about the intertwining lives of the Irish-American Caffee brothers from Providence, Rhode Island: Tommy (Jason Clarke) is a local politician and Michael (Jason Isaacs) is a gangster involved with New England's Irish Mob.  The show also features their mother Rose (Fionnula Flanagan), cousin Colin Carr (Brían F. O'Byrne), childhood friend and Rhode Island state detective Declan Giggs (Ethan Embry), Irish mob boss Freddie Cork (Kevin Chapman), Tommy's wife Eileen (Annabeth Gish), and Michael's criminal partner Pete McGonagle (Stivi Paskoski).\n\nAbraham Weinberg: Abraham \"Bo\" Weinberg (January 7, 1900 – September 9, 1935) was a Jewish New York City mobster who became a hitman and chief lieutenant for the Prohibition-era gang boss Dutch Schultz.  As Schultz expanded his bootlegging operations into Manhattan during Prohibition, he recruited Abe Weinberg and his brother George into his gang.  Abe Weinberg would become one of Schultz's top gunmen during the Manhattan Bootleg Wars and was a later suspect in the high-profile gangland slayings of Jack \"Legs\" Diamond, Vincent \"Mad Dog\" Coll, and mob boss Salvatore Maranzano.\n\nQuestion: What was the nickname of Anthony Salerno, a large cigar-chomping New York mob boss said to be involved in the killing of Tom \"The Greek\" Kapatos in 1977?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"mobster_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the mobster.\"\n    },\n    \"nickname\": {\n      \"type\": \"string\",\n      \"description\": \"The nickname of the mobster.\"\n    },\n    \"reason_for_nickname\": {\n      \"type\": \"string\",\n      \"description\": \"The reason given for the mobster's nickname.\"\n    },\n    \"involved_in_killing\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"victim_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person killed.\"\n        },\n        \"killing_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the killing occurred.\"\n        },\n        \"role_in_killing\": {\n          \"type\": \"string\",\n          \"description\": \"The mobster's role in the killing.\"\n        }\n      },\n      \"required\": [\n        \"victim_name\",\n        \"killing_year\",\n        \"role_in_killing\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"mobster_name\",\n    \"nickname\",\n    \"reason_for_nickname\",\n    \"involved_in_killing\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "mobster_name": {
        "type": "string",
        "description": "The full name of the mobster."
      },
      "nickname": {
        "type": "string",
        "description": "The nickname of the mobster."
      },
      "reason_for_nickname": {
        "type": "string",
        "description": "The reason given for the mobster's nickname."
      },
      "involved_in_killing": {
        "type": "object",
        "properties": {
          "victim_name": {
            "type": "string",
            "description": "The name of the person killed."
          },
          "killing_year": {
            "type": "integer",
            "description": "The year the killing occurred."
          },
          "role_in_killing": {
            "type": "string",
            "description": "The mobster's role in the killing."
          }
        },
        "required": [
          "victim_name",
          "killing_year",
          "role_in_killing"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "mobster_name",
      "nickname",
      "reason_for_nickname",
      "involved_in_killing"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
