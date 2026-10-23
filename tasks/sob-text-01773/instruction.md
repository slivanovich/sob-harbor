{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDeewana (1992 film): Deewana (English: 'Crazy' ) is a 1992 Indian romantic drama film directed by Raj Kanwar, and produced by Guddu Dhanoa and Lalit Kapoor and featuring Shah Rukh Khan, Divya Bharti and Rishi Kapoor in the lead.  This was Shah Rukh's debut release, and he appears only in the second half of the film.  He replaced Armaan Kohli, who walked out of the project due to creative differences after the first schedule.  The film released on June 25, 1992. \" Dil Aashna Hai\" was supposed to be the debut movie of Shahrukh Khan however \"Deewana\" was released first.\n\nMemorial Medical Center and Hurricane Katrina: Dr. Anna Pou was on duty at Memorial Medical Center when Hurricane Katrina struck New Orleans, Louisiana on August 29, 2005.  In the aftermath of the storm, after the levees failed and despite rising water and no electricity, she and other doctors and nurses attempted to continue caring for patients.  On Wednesday, August 31, United States Health and Human Services Secretary Mike Leavitt reassured the public that 2,500 patients would be evacuated from hospitals in Orleans Parish, although it wasn't clear at first where they would be moved to.  On September 11, 45 bodies were recovered from Memorial Medical Center, about five of whom had died before the disaster (originally thought to be eleven).  Out of an estimated 215 bodies found in nursing homes and hospitals in New Orleans, Memorial had the largest number.\n\nSnegithiye: Snegithiye (English:Oh Friend! \" (female)\" ) is a 2000 Tamil mystery thriller film directed by Priyadarshan.  The story is loosely based on the 1999 Marathi film \"Bindhaast\" written by Chandrakant Kulkarni.  The film notably features only female characters in the lead roles, played by Jyothika, Sharbani Mukherjee, Tabu and Ishita Arun.  Music was composed by Vidyasagar.  The film, released in 2000, proved to be an average grosser at the box office but bagged positive reviews from critics.  Today, it is considered a cult classic that was underrated at the time of its release.  Originally planned to be made as a bilingual, in Tamil and in Malayalam, the film released first in Tamil only, while the Malayalam dubbed version, \"Raakilipattu\", as well as the dubbed Hindi version, \"Friendship\", released seven years later.\n\n? (Enuff Z'nuff album): Enuff Z'nuff's 11th studio album, simply titled ? , is an odds and ends collection of previously unreleased studio material recorded throughout the band's career.  Although a few new tracks were recorded specifically for the album, the remainder of the songs were originally recorded during the sessions of their albums \"Animals With Human Intelligence\" and \"Paraphernalia\".  The ?  album was released first in Japan, where it peaked at #177.  A U.S. release followed soon after in October on Perris Records, as well as a European release on Frontiers Records in early 2005.\n\nSneha (actress): Suhasini Rajaram Naidu, popularly known by her stage name Sneha, is an Indian film actress, who works in the South Indian film industry.  She debuted in the Malayalam film \"Ingane Oru Nilapakshi\" (2000), directed by Anil – Babu and was later signed for the Tamil film \"Virumbugiren\", though it was only released two years later.  She started getting offers in Tamil and moved her focus to Kollywood, and the movie \"Ennavale\", where she starred opposite R. Madhavan, was released first in the same year.\n\nDinerral Shavers: Dinerral \"Dick\" Shavers (born c. 1981, died 28 December 2006) was a jazz drummer and educator from New Orleans, Louisiana.  Shavers was best known musically as a founding member of the Hot 8 Brass Band.  He also taught at a local high school and created music programs for poor local youths.  He appeared in the Spike Lee film \"When the Levees Broke\" discussing the devastation of his family home in the Lower 9th Ward.\n\nHuman (2015 film): Human is a 2015 documentary by French environmentalist Yann Arthus-Bertrand.  The film is almost entirely composed of exclusive aerial footage and first-person stories told into the camera.  It was the first movie to premiere in the General Assembly Hall of the United Nations, to an audience of 1,000 viewers, including the UN Secretary General Ban Ki-moon.\n\nToys in the Attic (2009 film): Toys in the Attic (Czech: Na půdě aneb Kdo má dneska narozeniny?  ; festival title: In the Attic: Who Has a Birthday Today?)  is a 2009 Czech-French-Japanese-Slovak primarily stop-motion animated fantasy comedy thriller family film directed by Jiří Barta and written by Edgar Dutka and Barta which depicts a community of toys and other objects in an attic who come to life when no human is around.  It is an international co-production of Czech, Japanese and Slovak companies.  The film was released first in the Czech Republic on 5 March 2009 and has been shown subtitled at film festivals internationally.  An American dub – adapted, produced and directed by Vivian Schilling and performed by actors including Forest Whitaker, Joan Cusack, Cary Elwes and Schilling herself – has been recorded, which the film was first shown with on 3 March 2012 at the New York International Children's Film Festival and was released nationally on 24 August 2012 by Hannover House.\n\nGame (2016 film): Game in Kannada, Oru Melliya Kodu (English: A thin line) in Tamil, is a 2016 Indian bilingual language crime thriller film directed by A. M. R. Ramesh.  This movie is an unofficial remake of the 2012 Spanish thriller El Cuerpo (Spanish title) also known as \"The Body\", and features Arjun Sarja, Shaam and Manisha Koirala in the lead roles.  With music composed by Ilayaraaja, the film was simultaneously shot in Kannada and Tamil; the former released first on February 26, 2016 while the later released on July 1, 2016.  The film was dubbed and released in Telugu as \"Notuku Potu\" in 2017.\n\nWhen the Levees Broke: When the Levees Broke: A Requiem in Four Acts is a 2006 documentary film directed by Spike Lee about the devastation of New Orleans, Louisiana following the failure of the levees during Hurricane Katrina.  It was filmed in late August and early September 2005, and premiered at the New Orleans Arena on August 16, 2006 and was first aired on HBO the following week.  The television premiere aired in two parts on August 21 and 22, 2006 on HBO.  It has been described by Sheila Nevins, chief of HBO's documentary unit, as \"one of the most important films HBO has ever made.\"  The title is a reference to the blues tune, \"When the Levee Breaks\", by Kansas Joe McCoy and Memphis Minnie, about the Great Mississippi Flood of 1927.\n\nQuestion: Which film was released first, When the Levees Broke or Human?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_a_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the first film being compared.\"\n    },\n    \"film_a_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the first film.\"\n    },\n    \"film_b_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the second film being compared.\"\n    },\n    \"film_b_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the second film.\"\n    },\n    \"earlier_release_film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film that was released first.\"\n    },\n    \"earlier_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film that was released first.\"\n    }\n  },\n  \"required\": [\n    \"film_a_title\",\n    \"film_a_release_year\",\n    \"film_b_title\",\n    \"film_b_release_year\",\n    \"earlier_release_film_title\",\n    \"earlier_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_a_title": {
        "type": "string",
        "description": "The title of the first film being compared."
      },
      "film_a_release_year": {
        "type": "integer",
        "description": "The release year of the first film."
      },
      "film_b_title": {
        "type": "string",
        "description": "The title of the second film being compared."
      },
      "film_b_release_year": {
        "type": "integer",
        "description": "The release year of the second film."
      },
      "earlier_release_film_title": {
        "type": "string",
        "description": "The title of the film that was released first."
      },
      "earlier_release_year": {
        "type": "integer",
        "description": "The release year of the film that was released first."
      }
    },
    "required": [
      "film_a_title",
      "film_a_release_year",
      "film_b_title",
      "film_b_release_year",
      "earlier_release_film_title",
      "earlier_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
