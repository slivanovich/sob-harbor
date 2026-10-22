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
True-Life Adventures: True-Life Adventures series is a collection of fourteen full length and short subject documentary films produced by Walt Disney Productions roughly between the years 1948 and 1960.  The series won eight Academy Awards for the studio including three Academy Award for Best Documentary Feature awards for "The Living Desert", "The Vanishing Prairie" and "White Wilderness", and five Best Two Reel Live Action Short awards for "Seal Island", "In Beaver Valley", "Nature's Half Acre", "Water Birds", and "Bear Country".  It inspired a daily panel comic strip that was distributed from 1955 to 1971 and drawn by George Wheeler.  Several of the films were adapted in comic book format as one shots in the Dell Comics Four Color series.  The films were among the earliest production experience for Roy E. Disney.  Also this film series was the launching pad for Disney's new distributor, Buena Vista International.  TV episodes are from Disney's anthology TV series.

James Goodwin: James Goodwin (c1800 – after 1835) was a convict escapee and explorer in Van Diemen's Land (now Tasmania).  In March 1828, he escaped from the notorious Sarah Island prison with fellow convict, Thomas Connolly and the two were the first white men to pass through the Lake St Clair region.  Assuming Goodwin was then taken on to Hobart, he is the first white man to have traversed Tasmania from west to east.

Virginia Dox: Virginia Dox (1851–1941) was a 19th-century American missionary, educator and explorer in the Intermountain West, and later a noted public speaker and fundraising agent for educational causes including Whitman College and Berea College.  Under the auspices of the New West Education Commission, she founded schools in Idaho and New Mexico.  She was the first white woman to explore the Grand Canyon, and also the first white woman to visit the Havasupai.  Her vivid depictions of Western life for Eastern audiences earned her the nickname of "the female Bret Harte".

Oz the Great and Powerful: Oz the Great and Powerful is a 2013 American fantasy adventure film directed by Sam Raimi and produced by Joe Roth, from a screenplay written by David Lindsay-Abaire and Mitchell Kapner.  The film stars James Franco, Michelle Williams, Rachel Weisz and Mila Kunis, with Zach Braff, Bill Cobbs, Joey King, and Tony Cox in supporting roles.  Based on L. Frank Baum's "Oz" novels and set 20 years before the events of the original novel, "Oz the Great and Powerful" is a spiritual prequel to the 1939 Metro-Goldwyn-Mayer film, "The Wizard of Oz".  The film tells the story of Oscar Diggs, a deceptive magician who arrives in the Land of Oz and encounters three witches: Theodora, Evanora, and Glinda.  Oscar is then enlisted to restore order in Oz, while struggling to resolve conflicts with the witches and himself.

First white child: The birth of the first white child is a widely used concept to mark the establishment of a European colony in the New World, especially in the historiography of the United States.  In Texas, the birth of the first white child is recorded in local histories on the county level.

Puszcza Biała: Puszcza Biała (] , "White Wilderness") is the name given to the forest that extends in Poland from Pułtusk to Ostrów Mazowiecka.  It is part of the Mazovian lowlands and consists of small trees, mostly pine.

The Man Who Walked Through Time: The Man Who Walked Through Time (1968) is the late Colin Fletcher's chronicle of the first white person to walk a continuous route through Grand Canyon National Park.  When Fletcher conducted the trip in 1963, the park did not encompass the entire length of the canyon; it was later expanded so it did.  Fletcher thus only walked about half of the physical canyon, though he was correct in saying he was the first to walk the section of the canyon designated as a national park.  Kenton Grua, a professional river guide, was the first white person to walk the entire length of the Grand Canyon, in 1977.  He was inspired by Fletcher's book but set out to "do it right" by walking it from end to end, not just the section inside the park.

Ikkemotubbe: Ikkemotubbe is a fictional Chickasaw Indian chief living in Yoknapatawpha County, Mississippi.  He appears in novels and short stories of William Faulkner, such as in the collection of stories titled "III The Wilderness": "Red Leaves," "A Justice," and "A Courtship".  He is referenced extensively in Faulkner's popular classic 'The Bear" as the original owner of the land that was sold to Carothers McCaslin, the first white landowner of the woods in which the story takes place.  After a steamboat trip to New Orleans, his name is "Frenchified" to "L'Homme" or "De l'Homme" ('The Man'), which he himself later re-Anglicizes to "Doom."

Rewa, Madhya Pradesh: Rewa    is a city in the north-eastern part of Madhya Pradesh state in India.  It is the administrative centre of Rewa District and Rewa Division.  The city lies about 420 km northeast of the state capital Bhopal and 130 km south of the city of Allahabad.  Rewa derives its name from another name for the Narmada River.  Rewa is connected to Allahabad via NH 27 and Sidhi, Satna, Maihar and Varansi via NH-7.  In nearby Sidhi district, a part of the erstwhile princely state of Rewa, and now a part of Rewa division, the world's first white tiger, a mutant variant of the Bengal tiger, was caught.  Worlds first white tiger safari is located in Satna district of Rewa division.

White Wilderness (film): White Wilderness is an American nature documentary produced by Walt Disney Productions in 1958 noted for its propagation of the misconception of lemming suicide.

Question: Which movie was produced first White Wilderness or Oz the Great and Powerful ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "first_produced_movie": {
      "type": "string",
      "description": "The title of the movie that was produced first."
    },
    "first_movie_production_year": {
      "type": "integer",
      "description": "The production year of the first movie."
    },
    "second_produced_movie": {
      "type": "string",
      "description": "The title of the movie that was produced second."
    },
    "second_movie_production_year": {
      "type": "integer",
      "description": "The production year of the second movie."
    },
    "comparison_result": {
      "type": "string",
      "description": "A statement indicating which movie was produced first."
    }
  },
  "required": [
    "first_produced_movie",
    "first_movie_production_year",
    "second_produced_movie",
    "second_movie_production_year",
    "comparison_result"
  ],
  "additionalProperties": false
}
