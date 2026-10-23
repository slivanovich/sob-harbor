{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEast Coast hip hop: East Coast hip hop is a regional subgenre of hip hop music that originated in the New York City area during the 1970s.  Hip hop is recognized to have originated and evolved first in New York; East Coast hip hop only became a distinct subgenre after artists from other regions of the United States emerged with different styles.  In contrast to other styles, East Coast hip hop music has prioritized complex lyrics for attentive listening rather than beats for dancing.  The main components of hip hop culture from that time and still today are MC'ing, DJ'ing, break dancing, and graffiti.\n\nMac &amp; Devin Go to High School: Mac & Devin Go to High School is a 2012 American direct-to-DVD stoner film directed by Dylan Brown.  The film stars rappers Snoop Dogg and Wiz Khalifa in the title roles, along with Mike Epps, Teairra Mari, Andy Milonakis, Luenell in supporting roles and the voice of Mystikal in a guest appearance.  The story follows two high school students, geeky Devin, and badman Mac who is a stoner.  He befriends Devin, and introduces him to cannabis.  The high school's name \"N. Hale\" is based on Nate Dogg's real name Nathaniel Hale and is also a play on the word \"inhale\".\n\nYoung, Wild &amp; Free: \"Young, Wild & Free\" is a song by American hip hop recording artists Snoop Dogg and Wiz Khalifa, featuring a guest appearance by American singer-songwriter Bruno Mars.  The track was first released on October 11, 2011 by Atlantic Records in the United States, as the lead single from the soundtrack of the film, \"Mac & Devin Go to High School\".  The song was produced by Mars, Philip Lawrence and Ari Levine, under their stage name, The Smeezingtons.  It was initially written by Calvin Broadus, Cameron Thomaz, The Smeezingtons and Christopher Brown.  However, since the single samples two different songs, \"Toot It & Boot It\" and \"Sneakin' in the Back\", more songwriting credits were added, making a total of seventeen.  The composition of the song begun when The Smeezingtons where doing a freestyle session in the studio and while they thought the track was never going to see the light of the day, Aaron Bay-Shuck considered it was a \"smash\" and asked them to finish it.  After its completion Snoop Dogg and Wiz Khalifa were added.\n\nMac &amp; Devin Go to High School (soundtrack): Mac & Devin Go to High School is the collaborative soundtrack to the film of the same name, by American West Coast hip hop recording artist Snoop Dogg and American rapper Wiz Khalifa.  It was released on December 13, 2011, by Atlantic Records.  The album features guest appearances from Bruno Mars, Juicy J, Curren$y and Mike Posner.  The album is supported by the lone hit single, \"Young, Wild & Free\".\n\nBeach House EP: Beach House EP is the debut extended play (EP) by American hip hop recording artist Ty Dolla Sign.  It was released on January 21, 2014, by Atlantic Records.  Ty mostly produced through the entirety of this EP, alongside the variety of the other record producers such as DJ Mustard, D'Mile and Young Chop, among others.  The EP features guest appearances from Wiz Khalifa, B.o.B, French Montana, Trey Songz, Twista, Jay Rock, Travis Scott and Fredo Santana, among others.  The EP was supported by two singles: \"Paranoid\" featuring B.o.B, and \"Or Nah\" featuring Wiz Khalifa.\n\nHip hop music: Hip hop music, also called hip-hop or rap music, is a music genre developed in the United States by inner-city African Americans in the 1970s which consists of a stylized rhythmic music that commonly accompanies rapping, a rhythmic and rhyming speech that is chanted.  It developed as part of hip hop culture, a subculture defined by four key stylistic elements: MCing/rapping, DJing/scratching with turntables, break dancing, and graffiti writing.  Other elements include sampling beats or bass lines from records (or synthesized beats and sounds), and rhythmic beatboxing.  While often used to refer solely to rapping, \"hip hop\" more properly denotes the practice of the entire subculture.  The term \"hip hop music\" is sometimes used synonymously with the term \"rap music\", though rapping is not a required component of hip hop music; the genre may also incorporate other elements of hip hop culture, including DJing, turntablism, scratching, beatboxing, and instrumental tracks.\n\nCoolaid: Coolaid is the fourteenth studio album by American West Coast hip hop recording artist Snoop Dogg.  It was released on July 1, 2016, by Doggystyle Records and eOne Music.  Recording sessions for the album took place during 2015 to 2016 at the Doggystyle Studios Records, in Diamond Bar, California.  The production on the album was handled by Snoop Dogg and other record producers, including Just Blaze, Swizz Beatz and Timbaland.  Snoop Dogg also enlisted a variety of guest vocalists such as Too $hort, Swizz Beatz, Jeremih, Wiz Khalifa, Trick Trick, E-40, Jazze Pha, Suga Free and October London, among others.\n\nSmokin' On: \"Smokin' On\" is a song by American rappers Snoop Dogg and Wiz Khalifa, from the soundtrack Mac & Devin Go to High School.  The song features fellow American rapper Juicy J.  The song produced by Drumma Boy.\n\nOpenair Frauenfeld: Openair Frauenfeld is an annual hip hop music festival that takes place in Frauenfeld in July.  It is considered to be the largest Openair festival in Switzerland and the largest Hip Hop music festival in Europe.  It was created in 1985 and has now taken place 22 times.  The event was originally hosted under the name \"Out in the Green Festival\" until it was changed to \"Openair Frauenfeld\" in 2007.  Since then it has hosted numerous high-profile celebrities and has attracted an annual turnout of around 150,000 people.  Some of the top headliners performing at Openair Frauenfeld have included Jay-Z, Eminem, Kanye West, Macklemore, Snoop Dogg, 50 Cent, Kendrick Lamar, , Wiz Khalifa, , and others.\n\nWest Coast hip hop: West Coast hip hop is a hip hop music subgenre that encompasses any artists or music that originate in the West Coast region of the United States.  The gangsta rap subgenre of West Coast hip hop began to dominate from a radio play and sales standpoint during the early 1990s with the birth of G-funk and the emergence of Suge Knight and Dr. Dre's Death Row Records.\n\nQuestion: What artist that specializes in a hip hop music subgenre that encompasses any artists or music that originate in the West Coast region of the United States recorded Mac &Devin Go to High School with Wiz Khalifa?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist who recorded the project.\"\n    },\n    \"hip_hop_subgenre\": {\n      \"type\": \"string\",\n      \"description\": \"The specific hip hop subgenre the artist specializes in.\"\n    },\n    \"subgenre_origin_region\": {\n      \"type\": \"string\",\n      \"description\": \"The geographical region associated with the hip hop subgenre.\"\n    },\n    \"collaboration_partner\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist with whom the project was recorded.\"\n    },\n    \"project_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the recorded project.\"\n    },\n    \"project_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of project (e.g., soundtrack, film).\"\n    }\n  },\n  \"required\": [\n    \"artist_name\",\n    \"hip_hop_subgenre\",\n    \"subgenre_origin_region\",\n    \"collaboration_partner\",\n    \"project_name\",\n    \"project_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_name": {
        "type": "string",
        "description": "The name of the artist who recorded the project."
      },
      "hip_hop_subgenre": {
        "type": "string",
        "description": "The specific hip hop subgenre the artist specializes in."
      },
      "subgenre_origin_region": {
        "type": "string",
        "description": "The geographical region associated with the hip hop subgenre."
      },
      "collaboration_partner": {
        "type": "string",
        "description": "The name of the artist with whom the project was recorded."
      },
      "project_name": {
        "type": "string",
        "description": "The name of the recorded project."
      },
      "project_type": {
        "type": "string",
        "description": "The type of project (e.g., soundtrack, film)."
      }
    },
    "required": [
      "artist_name",
      "hip_hop_subgenre",
      "subgenre_origin_region",
      "collaboration_partner",
      "project_name",
      "project_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
