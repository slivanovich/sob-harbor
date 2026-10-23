{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLights Out (2013 film): Lights Out is a 2013 Swedish supernatural horror short film directed, written, co-produced, shot and scored by David F. Sandberg and co-produced by and starring Lotta Losten.  The film was released online on 30 December 2013 on both Vimeo and YouTube.  The short film was the basis of an eponymous 2016 film adaption, also directed by Sandberg and featuring Losten.\n\nMeridian (film): Meridian is a 2016 film noir thriller film directed by Curtis Clark and written by Clark and James Harmon Brown.  The film stars Kevin Kilner, Reid Scott, and Elyse Levesque, and focuses on detectives investigating the disappearances of three men in 1940s Los Angeles.  It was released on Netflix and Xiph.org in September 2016.\n\nKickboxer: Retaliation: Kickboxer: Retaliation is an upcoming American martial arts film directed and written by Dimitri Logothetis.  Logothetis was attracted to the original Jean Claude Van Damme’s Kickboxer because of his martial arts background and that’s what inspired him to pursue the rights to the original, develop a reboot of the franchise and ultimately write, produce and direct a contemporary version of the pop culture, iconic Kickboxer.  It was important that Logothetis to convince Van Damme to step into the role of mentor to ordain a new, high octane Kickboxer who has a sixth degree black belt in BJJ, Alain Moussi.  Because Kickboxer: Vengeance was such a successful independent feature in the world market, it generated a sequel.  It is a sequel to the 2016 film \"\".  The film stars Alain Moussi, Jean-Claude Van Damme, Christopher Lambert, Ronaldinho, Mike Tyson and Hafþór Júlíus Björnsson.  Aside from Moussi and Van Damme, Sara Malakul Lane and Sam Medina are reprising their roles from the previous film.\n\nJohnny Frank Garrett's Last Word: Johnny Frank Garrett's Last Word is a 2016 film directed by Simon Rumley.  It is a work of fiction based on the Jesse Quackenbush documentary \"The Last Word\", about the trial, conviction, and execution of a Texas man named Johnny Frank Garrett.  It played at the 2016 South by Southwest Midnighters, Festival Favorites, Shorts Programs and Special Events lineup\n\nPhantom Detective: Phantom Detective (; lit.  Detective Hong Gil-Dong: Disappeared Village) is a 2016 South Korean film noir comedy action film directed and written by Jo Sung-hee.  Its central protagonist is a modern iteration of the classic Korean folk hero Hong Gildong.  It was released in South Korea on May 4, 2016.  It was released in U.S. and Canada on 20 May 2016.\n\nSoundararaja: Soundararaja (சௌந்தரராஜா) is an Indian film actor and short film producer who appears in Tamil films.  Following a stint as a system engineer had worked in Singapore and France he bagun considering acting as career.  He was working as a background actor, playing minor supporting roles for over five years; he started his career as villain role in S.R.Prabakaran in \"Sundarapandian\" (2012), \"Varuthapadatha Valiber Sangam\" (2013), \"Jigarthanda\"(2014), in between he did many roles in various projects again in 2016 he acted as Villain again in \"Dharma Durai (2016 film) \"(2016) with his best friend \"Vijay Sethupathi\".  In the same year 2016 he got introduced as a second Hero in \"Enakku Veru Engum Kilaigal Kidayathu\" (2016), with \"Goundamani\".  which earned critical and commercial success, turned Soundararaja into a popular name in Tamil cinema.\n\nTye Sheridan: Tye Kayle Sheridan (born November 11, 1996) is an American actor.  Sheridan made his feature film debut in Terrence Malick's experimental drama film \"The Tree of Life\" (2011) and had his first leading role in Jeff Nichols's film \"Mud\" (2012).  He also co-starred in David Gordon Green's drama \"Joe\" (2013).  In 2015, he starred in the drama \"The Stanford Prison Experiment\".  Sheridan played Cyclops in the 2016 film \"\", and will portray the lead character, Wade Watts, in Steven Spielberg's adaptation of Ernest Cline's \"Ready Player One\", which is scheduled for a March 30, 2018 release. .  He will also be reprising his role as Cyclops in the upcoming film \"\".\n\nRoh Jeong-eui: Roh Jeong-eui (born July 31, 2001) is a South Korean actress.  She is known for her role as Dong-i in 2016 film \"Phantom Detective\".\n\nThe Lennon Report: The Lennon Report is a 2016 film written by Walter Vincent and directed by Jeremy Profe, about the night John Lennon was shot and killed in 1980.  The film is produced by Gabriel Francisco and Rafael Francisco.  The film stars Richard Kind, Adrienne C. Moore, and Stef Dawson.  Karen Tsen Lee plays Yoko Ono.\n\nDileep Raj: Dileep Raj (born 2 September 1978) is an Indian actor, film director and television director and producer known for his work in Kannada cinema.He has appeared in 24 films.  After having found success in television and as a supporting actor, he made his film debut as a lead with Boy Friend in 2005.  He shot to popularity with the blockbuster film Milana (2007), in which he played the role of a protagonist alongside Puneeth Rajkumar.  In his 2016 film, \"U Turn\", he essays a leading role in the dramatic thriller.He has also acted in stage roles, including the leading role in the play \"Treadmill\".\n\nQuestion:  Roh Jeong-eui plays the role of Dong-i in a 2016 film directed by who?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actress.\"\n    },\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"character_name\",\n    \"actress_name\",\n    \"director_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "character_name": {
        "type": "string",
        "description": "The name of the character played by the actress."
      },
      "actress_name": {
        "type": "string",
        "description": "The name of the actress."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "character_name",
      "actress_name",
      "director_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
