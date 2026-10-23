{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJohn Lemmon Films: John Lemmon Films is a traditional character animation studio based in Charlotte, North Carolina, United States, and is listed among five “prominent animation houses”.  The company was founded in 1984 by John Lemmon and Mike Rosinski.  Initially the animation studio worked exclusively in clay animation, but has since diversified into stop-motion, 2D animation and Flash animation, as well as web game design.  The company has produced clay animated TV commercials for clients including: Disney, Cartoon Network and Dairy Queen.  The studio has created clay-animated versions of well-known products, including the Coleman lantern, and has produced clay animated spots for Tandy Corporation’s chain of stores called McDuff Electronics and for Cedar Point.\n\nTweety's High-Flying Adventure: Tweety's High-Flying Adventure is a 2000 direct-to-video musical comedy animated film produced by Tom Minton and James T. Walker, written by Tom Minton, Tim Cahill and Julie McNally, and directed by James T. Walker, Karl Toerge, Charles Visser, and Kyung Won Lim, starring Tweety.  It also features other characters such as Sylvester (as the main antagonist), Bugs Bunny, Daffy Duck, Yosemite Sam, Lola Bunny (in a cameo as an anchorwoman), and Speedy Gonzales.  The animation was made overseas by the animation company Koko Enterprises.  The movie is an updated spoof of Jules Verne's \"Around the World in Eighty Days\".  It was the first (and, so far, the only) long form animated film featuring Tweety in the lead role.  Many of the key creative people from the 1995-2002 TV series \"The Sylvester & Tweety Mysteries\" also worked on \"Tweety's High-Flying Adventure\", which commenced shortly after the series wrapped production in May 1999.  Co-producer Tom Minton instigated the project, which was only the second internally produced direct-to-video animated film done at the Warner Bros.  Animation division in Sherman Oaks, California.  It was adapted into a game for the Game Boy Color in 2001.\n\nGay Purr-ee: Gay Purr-ee is a 1962 American animated film musical produced by United Productions of America and released by Warner Bros. It features the voice of Judy Garland in her only animated-film role, as well as Robert Goulet in his first feature film.  The film received positive reviews, but was a box office disappointment.\n\nJimmy Bryant (singer): James Howard Bryant (born June 2, 1929) is a singer, arranger and composer.  He is most well known for providing the singing voice of Tony (played onscreen by Richard Beymer) in the 1961 film musical \"West Side Story\".  While he received no screen credit, he states that Beymer was \"a nice guy, and every time he did an interview he would mention my name.\"  He also sang for James Fox in the 1967 film musical \"Thoroughly Modern Millie\", and sang in \"The Telephone Hour\" number in \"Bye Bye Birdie\".  He also sang in the group that performed the theme song of the TV series \"Batman\".\n\n3 al rescate: 3 to the Rescue (Spanish: 3 al Rescate ) is the first animated film made in the Dominican Republic.  It is based on an animated short titled \"3 for the Banquet\" by Raycast Animation Studio.  It was directed by Jorge Morillo and Luis Morillo, and written by Christian López, Edwin Gautreau and Lucy Bedeglez.  It was also produced by Raycast Animation Studio and Antena Latina Films.  It premiered on January 6, 2011 in the Dominican Republic.\n\nHell-Bent for Election: Hell-Bent For Election is a 1944 two-reel (thirteen minute) animated cartoon short subject now in the public domain.  The short was one of the first major films from United Productions of America (then known as \"Industrial Films\"), which would go on to become the most influential animation studio of the 1950s.  As UPA did not have a full staff or a studio location until the late-1940s, this film was made in animator Zack Schwartz's apartment with the help of moonlighters from various local Hollywood animation studios.  Among the moonlighters was Chuck Jones, who directed the film.\n\nJohn the Fearless (film): John the Fearless (Dutch: \"Jan zonder vrees\" ) is a 1984 Belgian animated film.  It is notable for being the first feature length animated film produced in Flanders in its entirety.  It is based on a novel by Constant de Kinder and features voice work by Belgian character actor Jan Decleir.  An English dubbed version of the film was produced by Canadian animation studio Cinar Films and was released on video in 1989 by Just For Kids Video.\n\nCrulic: The Path to Beyond: Crulic: The Path to Beyond (Romanian: Crulic - Drumul spre dincolo ) is a 2011 Romanian-Polish animated biographical film, directed by and starring Vlad Ivanov.  It tells the story of Claudiu Crulic, a Romanian citizen who died in a Polish prison while on a hunger strike.  The film was made with a mix of techniques including hand-drawn animation and animated photographs.  Artwork and animation was done at the animation studio DSG, by Dan Panaitescu, Raluca Popa, Dragos Stefan, Roxana Bentu and Tuliu Oltean.  The film won the Cristal for Best Feature Film at the 2012 Annecy International Animated Film Festival.\n\nDavid Hilberman: David Hilberman (18 December 1911 – 5 July 2007) was an American cartoon animator and one of the founders of classic 1940s animation.  An innovator in the animation industry, he co-founded United Productions of America (UPA).  The studio gave its artists great freedom and pioneered the modern style of animation.  As Animator and Professor Tom Sito noted: \"Arguably, no studio since Walt Disney exerted such a great influence on world animation.\"  He and Zack Schwartz went on to start Tempo Productions which became an early leader in television animated commercial production.  In short, he played an important role in the new directions the art form took in the 1940s and ‘50s.\n\nUPA (animation studio): United Productions of America, better known as UPA, was an American animation studio active from the 1940s through the 1970s.  Beginning with industrial and World War II training films, UPA eventually produced theatrical shorts for Columbia Pictures, notably the Mr. Magoo series.  In 1956, UPA produced a television series for CBS, \"The Boing-Boing Show,\" hosted by Gerald McBoing Boing.  In the 1960s, UPA produced syndicated Mr. Magoo and \"Dick Tracy\" television series and other series and specials, including the popular \"Mister Magoo's Christmas Carol\".  UPA also produced two animated features, \"1001 Arabian Nights\" and \"Gay Purr-ee\", and distributed Japanese films from Toho Studios in the 1970s and 1980s. \" Gerald McBoing Boing\" (2005–2007) is a more recent television series based on UPA's memorable character and licensed and co-produced by Cookie Jar Entertainment and Classic Media, for Cartoon Network.\n\nQuestion: UPA was an animation studio that created the 1962 film musical that gave who her only animated film voice role?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the animated film musical.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"producing_studio\": {\n      \"type\": \"string\",\n      \"description\": \"The animation studio that produced the film.\"\n    },\n    \"voice_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the voice actor.\"\n        },\n        \"role_significance\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the significance of this role for the actor.\"\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"role_significance\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"producing_studio\",\n    \"voice_actor\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the animated film musical."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "producing_studio": {
        "type": "string",
        "description": "The animation studio that produced the film."
      },
      "voice_actor": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the voice actor."
          },
          "role_significance": {
            "type": "string",
            "description": "Description of the significance of this role for the actor."
          }
        },
        "required": [
          "actor_name",
          "role_significance"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_year",
      "producing_studio",
      "voice_actor"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
