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
Caitlin Stasey: Caitlin Jean Stasey (born 1 May 1990) is an Australian actress.  She is known for her role as Rachel Kinski in "Neighbours".  Previously she played Francesca Thomas in "The Sleepover Club", although her breakthrough movie role came in "Tomorrow, When the War Began", a 2010 movie adaption of the teen novel of the same name in which she played lead protagonist Ellie Linton.  She also played Lady Kenna in the American series "Reign" from 2013 to 2015 and had a recurring role in the ABC2 series "Please Like Me" from 2013 to 2016.  In 2017 Stasey starred as Ada on the Fox television drama "APB", which was cancelled after one season in May 2017.

Phyllomorpha laciniata: Phyllomorpha laciniata (the golden egg bug) is a species of coreid bug, and one of only two members of the genus "Phyllomorpha".  They are specific to the host plant "Paronychia argentea".  It is noted for its habit of laying its eggs on other members of its species, who act as mobile nests (oviposition substrate).  These co-opted egg carriers provide more protection for the eggs than laying them at static locations on plant leaves or stems.  While "Phyllomorpha laciniata" females can and do lay eggs on their host plant, the availability of suitable egg carriers seems to stimulate the deposition of mature eggs.

The Golden Egg: The Golden Egg (Dutch: Het Gouden Ei), published as The Vanishing in English-speaking countries, is a psychological thriller novella written by Dutch author Tim Krabbé, first published in 1984.  The plot centers on a man whose obsession over the fate of his missing lover from years ago drives him to confront her abductor and pay the ultimate sacrifice in order to know the truth.  The book was adapted into a 1988 film which was later remade in an English-language version by the same director.

Egg Bowl: The Battle for the Golden Egg, also informally known as the Egg Bowl, is an American college football rivalry game played annually between Southeastern Conference members Mississippi State University and Ole Miss (The University of Mississippi).  The rivalry is the tenth longest uninterrupted series in the United States.  The two teams first played each other in 1901.  Since 1927 the winning squad has been awarded possession of the "Golden Egg Trophy".  In cases where the game ended in a tie the previous winner retained possession of the trophy.  Ole Miss leads the series, 63–44–6.

The Vanishing (1993 film): The Vanishing is a 1993 American psychological thriller starring Jeff Bridges, Kiefer Sutherland, Nancy Travis and Sandra Bullock.  It is an American remake of a 1988 Franco-Dutch film also called "The Vanishing", and also directed by George Sluizer.

Abraham Whistler: Abraham Whistler is a fictional character in the Marvel Comics universe.  He is a vampire hunter and the mentor of Blade.  Screenwriter David S. Goyer created him for the 1998 film "Blade" (in which the part was played by Kris Kristofferson), but he first appeared on screen in "Spider-Man: The Animated Series" where he was voiced by Malcolm McDowell and later by Oliver Muirhead.  In 2006, Abraham Whistler appeared in the television show "".  He shares many traits and is partially inspired by the character Jamal Afari.  His first appearance in a comic can be found in the comic book movie adaption of the Blade II movie, but his face is also seen on 2 covers of the Max imprint Blade comic from Marvel.

Hiranyagarbha: Hiraṇyagarbha (Sanskrit: हिरण्यगर्भः ; literally the 'golden womb' or 'golden egg', poetically translated as 'universal germ') is the source of the creation of universe or the manifested cosmos in Vedic philosophy, as well as an avatar of Vishnu in the Bhagavata Purana.  It finds mention in one hymn of the Rigveda (RV 10.121), known as the Hiraṇyagarbha Sūkta, suggesting a single creator deity (verse 8: "yo deveṣv ādhi devā eka āsīt ", Griffith: "He is the God of gods, and none beside him.") , identified in the hymn as Prajāpati.  The concept of the "golden womb" is again mentioned in the Vishvakarman Sūkta (RV 10.82).

Angry Birds Stella (TV series): Angry Birds Stella is a Finnish computer-animated TV series based on the game "Angry Birds Stella" that was produced by Rovio Entertainment.  The first episode, "A Fork in the Friendship", aired on ToonsTV in November 1, 2014.  The series recounts the tale of Stella, along with her friends Luca, Willow, Poppy and Dahlia, as they work their way against Gale, the former friend of Stella, that is the queen of the pigs in Golden Island.  The first season focuses on Gale trying to hunt for the Golden Egg, but, fails as seen in the final episode of season 1, "To The Bitter End".  The second season focuses on Gale returning and trying to hunt for the Golden Egg again, and she succeeded as seen in "The Golden Queen", the 9th episode of season 2.  Also, Dahlia, one of the birds, tries searching for the egg as well for an experiment, but this time, she fails, as seen in "It's Mine!" , the 6th episode of season 2.  Soon enough, the birds realize how dangerous this egg can be, as seen in "Premonition", the 11th episode in season 2, which in when Gale with the Golden Egg, anything that is touched with it, turns to gold.  However, when that happens, another thing turns to stone, the opposite of gold, which causes nature, and even worse, food to be turned to stone as well.  Now, it is up to the Stella gang to save Golden Island before it is too late.  They do succeed, as seen in "You Asked For It", the 13th and final episode of season 2 and the series finale of "Angry Birds Stella", where after a long awful night, Stella and her gang launch the Golden Egg out of the island, never to be seen again.  Gale does not mind because when she saw the Golden Egg after she broke out of the gold in the episode, she ran away, back into her castle.

Clint de Ganon: Clint de Ganon is an American drummer and percussionist from Hastings, New York.  Clint has played in many Broadway hits including Hairspray and Footloose - writing the drum score for both.  He was also the drummer for the movie adaption of Hairspray.  Currently, Clint can be found at the Stephen Sondheim Theatre where he is the drummer for Broadway musical .

Golden Lamp of Knowledge: The Golden Lamp of Knowledge is a trophy given to winners between quiz bowl matches between Mississippi State University and the University of Mississippi.  Using the Golden Egg trophy for winners of football games between the universities as a model, the trophy is passed back and forth between the schools.  Since quiz bowl tournaments often have teams facing each other more than once, the trophy is only awarded once per tournament, with the team winning the most matches against the other in a tournament taking home the trophy.

Question: what actors starred in the 1993 movie adaption of The Golden Egg?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie adaptation."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the movie."
    },
    "original_source_title": {
      "type": "string",
      "description": "The title of the original work the movie was adapted from."
    },
    "actors": {
      "type": "array",
      "description": "A list of actors who starred in the movie.",
      "items": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor."
          }
        },
        "required": [
          "actor_name"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "movie_title",
    "release_year",
    "original_source_title",
    "actors"
  ],
  "additionalProperties": false
}
