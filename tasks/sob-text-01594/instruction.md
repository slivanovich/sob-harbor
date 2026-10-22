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
Konrad Kyeser: Konrad Kyeser (26 August 1366 – after 1405) was a German military engineer, author of "Bellifortis" (c. 1405), a book on military technology popular throughout the 15th century.  Originally conceived for King Wenceslaus, Kyeser dedicated the finished work to Rupert of Germany.

Bamboo-copter: The bamboo-copter, also known as the bamboo dragonfly or Chinese top (Chinese "zhuqingting" 竹蜻蜓 , Japanese "taketombo" 竹蜻蛉 ), is a toy helicopter rotor that flies up when its shaft is rapidly spun.  This helicopter-like top originated in Warring States period China around 400 BCE, and was the object of early experiments by George Cayley, the inventor of modern aeronautics.

George Cayley: Sir George Cayley, 6th Baronet (27 December 1773 – 15 December 1857) was a prolific English engineer and is one of the most important people in the history of aeronautics.  Many consider him to be the first true scientific aerial investigator and the first person to understand the underlying principles and forces of flight.

Nobody's Daughter: Nobody's Daughter is the fourth and final studio album by American alternative rock band Hole, released worldwide on April 27, 2010, through Mercury Records.  The album was originally conceived by Hole frontwoman Courtney Love as a solo project titled "How Dirty Girls Get Clean", following her poorly received solo debut "America's Sweetheart" (2004).  Much of the material featured on "Nobody's Daughter" originated from studio sessions for "How Dirty Girls Get Clean", which had been conceived in 2006 after a multitude of legal issues, drug addiction, and rehabilitation sentences had left Love "suicidal".  Love financed the making of the record herself, which cost nearly two million dollars.

Library of Living Philosophers: The Library of Living Philosophers is a series of books conceived of and started by Paul Arthur Schilpp in 1939; Schilpp remained editor until 1981.  The series has since been edited by Lewis Edwin Hahn (1981-2001), Randall Auxier (2001-2013), and Douglas R. Anderson (2013-2015).  The Library of Living Philosophers is currently edited by Sarah Beardsworth (2015-present).  Each volume is devoted to a single living philosopher of note, and contains, alongside an "intellectual autobiography" of its subject and a complete bibliography, a collection of critical and interpretive essays by several dozen contemporary philosophers on aspects of the subject's work, with responses by the subject.  The Library was originally conceived as a means by which a philosopher could reply to his or her interpreters while still alive, hopefully resolving endless philosophical disputes about what someone "really meant."  While its success in this line has been questionable—a reply, after all, can stand just as much in need of interpretation as an original essay—the series has become a noted philosophical resource and the site of much significant contemporary argument.

Symphony No. 3 (Khachaturian): The Symphony No. 3 by Aram Khachaturian, subtitled Symphony–Poem, was composed in 1947 for the 30th anniversary of the Russian Revolution, and premiered on Leningrad on December 13 by the Leningrad Philharmonic conducted by Yevgeny Mravinsky.  It was his last contribution to the genre.  Originally conceived as a symphonic poem, it is a single movement symphony featuring an organ solo and fifteen trumpets conceived as a hymn of praise of the Soviet Union, with Khachaturian saying that he "wanted this work to express the Soviet people’s joy and pride in their great and mighty country".  However, the work's raw and strident style, which has been related to the 1920s Soviet constructivist avantgarde, and unorthodox structure and instrumentation dissatisfied the Stalinist cultural authorities, and it was condemned as formalistic in the 1948 Zhdanov decree.

Marlboro Man: The Marlboro Man is a figure used in tobacco advertising campaigns for Marlboro cigarettes.  In the United States, where the campaign originated, it was used from 1954 to 1999.  The Marlboro Man was first conceived by Leo Burnett in 1954.  The images initially featured rugged men portrayed in a variety of roles but later primarily featured a rugged cowboy or cowboys, in nature with a cigarette.  The advertisements were originally conceived as a way to popularize filtered cigarettes, which at the time were considered feminine.

Plasma acceleration: Plasma acceleration is a technique for accelerating charged particles, such as electrons, positrons, and ions, using the electric field associated with electron plasma wave or other high-gradient plasma structures (like shock and sheath fields).  The plasma acceleration structures are created either using ultra-short laser pulses or energetic particle beams that are matched to the plasma parameters.  These techniques offer a way to build high performance particle accelerators of much smaller size than conventional devices.  The basic concepts of plasma acceleration and its possibilities were originally conceived by Toshiki Tajima and Prof. John M. Dawson of UCLA in 1979.  Initial designs of experiment for "wakefield" were conceived at UCLA by the group of Prof. Chan Joshi.  Current experimental devices show accelerating gradients several orders of magnitude better than current particle accelerators.

Deportation of Koreans in the Soviet Union: Deportation of Koreans in the Soviet Union, originally conceived in 1926, initiated in 1930, and carried through in 1937, was the first mass transfer of an entire nationality in the Soviet Union.  Almost the entire Soviet population of ethnic Koreans (171,781 persons) were forcefully moved from the Russian Far East to unpopulated areas of the Kazakh SSR and the Uzbek SSR in October 1937.  The official reason for the deportation was to stem "the penetration of the Japanese espionage into the Far Eastern Krai", as Koreans were at the time subjects of the Empire of Japan, which was hostile to the Soviet Union.  Estimates based on population statistics suggest that 40,000 deported Koreans died in 1937 and 1938 from starvation, exposure and difficulties adapting to their new environment.

Neptune Memorial Reef: The Neptune Memorial Reef originally conceived by Gary Levine and designed by artist Kim Brandell and known as the Atlantis Reef Project or the Atlantis Reef is an underwater columbarium in what was conceived by the creator as the world's largest man-made reef (covering over 600,000 square feet (65,000 m²) of ocean floor) at a depth of 40 feet.  As of 2012, the Reef occupies a half-acre space, but a planned expansion to 16 acres is underway.  The city design involves underwater roads leading to a central feature with benches and statuary.

Question: The bamboo-copter was originally conceived by the engineer of what nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "item_name": {
      "type": "string",
      "description": "The name of the item in question."
    },
    "engineer_associated_name": {
      "type": "string",
      "description": "The name of the engineer associated with the item."
    },
    "engineer_nationality": {
      "type": "string",
      "description": "The nationality of the associated engineer."
    },
    "engineer_specific_involvement_with_item": {
      "type": "string",
      "description": "The specific role or involvement of the engineer with the item as described in the context."
    },
    "item_initial_origin_period_and_location": {
      "type": "string",
      "description": "The original historical origin of the item as stated in the context."
    }
  },
  "required": [
    "item_name",
    "engineer_associated_name",
    "engineer_nationality",
    "engineer_specific_involvement_with_item",
    "item_initial_origin_period_and_location"
  ],
  "additionalProperties": false
}
