{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAcademy Award for Best Animated Feature: The Academy Awards are given each year by the Academy of Motion Picture Arts and Sciences (AMPAS or the Academy) for the best films and achievements of the previous year.  The Academy Award for Best Animated Feature is given each year for animated films.  An animated feature is defined by the Academy as a film with a running time of more than 40 minutes in which characters' performances are created using a frame-by-frame technique, a significant number of the major characters are animated, and animation figures in no less than 75 percent of the running time.  The Academy Award for Best Animated Feature was first given for films made in 2001.\n\nDragon Ball: Sleeping Princess in Devil's Castle: Dragon Ball: Sleeping Princess in Devil's Castle (ドラゴンボール 魔神城のねむり姫 , Doragon Bōru Majin-jō no nemuri hime ) is the second animated feature film based on the \"Dragon Ball\" manga by Akira Toriyama.  It was originally released in Japan on July 18, 1987 at the \"Toei Manga Matsuri\" film festival as part of a quadruple feature along with the first \"\" movie and the film versions of \"Hikari Sentai Maskman\" and \"Choujinki Metalder\".  An English dub by Funimation Productions was released on VHS in 1998.\n\nThe Magic Roundabout (film): The Magic Roundabout (released in France as Pollux - Le manège enchanté and redubbed in the United States as Doogal or The Lord of the Springs) is a 2005 French-British computer-animated adventure fantasy film based on the television series \"The Magic Roundabout\".\n\nPinocchio (1940 film): Pinocchio is a 1940 American animated musical fantasy film produced by Walt Disney Productions and based on the Italian children's novel \"The Adventures of Pinocchio\" by Carlo Collodi.  It was the second animated feature film produced by Disney, made after the success of \"Snow White and the Seven Dwarfs\" (1937).\n\nPinocchio's Daring Journey: Pinocchio's Daring Journey is a dark ride at Disneyland in California; Tokyo Disneyland; and the Disneyland Park in Paris.  Located in the Fantasyland section of each park, this ride is based on Disney's animated film version of the classic story, which was the studio's second animated feature film.  Stromboli's marionette show is also featured in the attraction, in which guests are inside a giant cage.  The version in Disneyland was the first attraction created by Disney to use holographic material, which appears on hand held mirror, in the scene where the boys turn into donkeys on Pleasure Island.  The Pepper's Ghost illusion (used extensively in the Haunted Mansion) is used when the Blue Fairy disappears, leaving a pile of fiber-optic fairy dust on the floor.\n\nBolexbrothers: bolexbrothers (alternatively Bolex Brothers) is an independent British animation studio based in Bristol.  The studio specialises in stop motion animation, producing numerous short films and commercials, as well as one stop motion feature film, \"The Secret Adventures of Tom Thumb\" (their second feature, \"The Magic Roundabout\", was computer animated).  Named after the Bolex brand of 16mm cameras once popular with animators, the studio was established in 1991 by animator and former theatrical effects designer Dave Borthwick , and colleague Dave Alex Riddett.\n\nTales of the Wizard of Oz: Tales of the Wizard of Oz is a 1961 animated television series produced by Crawley Films for Videocrafts (later known as Videocraft and ultimately Rankin/Bass Productions).  This is the second animated series produced by the studio, and the first by Rankin/Bass to feature traditional animation.\n\nAnnie Award for Best Animated Feature: The Annie Award for Best Animated Feature is an Annie Award introduced in 1992, awarded annually to the best animated feature film.  In 1998 the award was renamed Outstanding Achievement in an Animated Theatrical Feature, only to revert to its original title again in 2001.  Since the inception of Best Animated Feature at the Academy Awards in 2001, the Annie Award winner has matched up every year except for 2006, 2008, 2010, 2012, and 2014.\n\nAnnie Award for Music in a Feature Production: The Annie Award for Music in a Feature Production (or Annie Award for Music in an Animated Feature Production) is an Annie Award given annually to the best music in an animated feature film, theatrical or direct-to-video.  It began in 1997 as the \"Annie Award for Best Individual Achievement: Music in a Feature/Home Video Production\".  Throughout the following years, the title was renamed \"Outstanding Individual Achievement for Music in an Animated Feature Production\", \"Outstanding Individual Achievement for Music Score in an Animated Feature Production\", and \"Outstanding Music in an Animated Feature Production\" before changing to its current title in 2005.  It was retitled \"Best Music in an Animated Feature Production\" in 2006 for three years before being reverted to \"Music in an Animated Feature Production\" in 2009.\n\nPeter Pan (1953 film): Peter Pan is a 1953 American animated adventure film produced by Walt Disney and based on the play \"Peter Pan, or The Boy Who Wouldn't Grow Up\" by J. M. Barrie.  It is the 14th Disney animated feature film and was originally released on February 5, 1953, by RKO Radio Pictures.  \"Peter Pan\" is the final Disney animated feature released through RKO before Walt Disney's founding of his own distribution company, Buena Vista Distribution, later in 1953 after the film was released.  \"Peter Pan\" is also the final Disney film in which all nine members of Disney's Nine Old Men worked together as directing animators.  It is also the second Disney animated film starring Kathryn Beaumont, Heather Angel, and Bill Thompson after their roles in the animated feature \"Alice in Wonderland\".\n\nQuestion: The Bolexbrothers second animated feature was produced in which year ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"studio_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the animation studio.\"\n    },\n    \"feature_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The sequential number of the animated feature film for the studio.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the animated feature film.\"\n    },\n    \"production_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the animated feature film was produced.\"\n    },\n    \"animation_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of animation used for the film.\"\n    }\n  },\n  \"required\": [\n    \"studio_name\",\n    \"feature_number\",\n    \"film_title\",\n    \"production_year\",\n    \"animation_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "studio_name": {
        "type": "string",
        "description": "The name of the animation studio."
      },
      "feature_number": {
        "type": "integer",
        "description": "The sequential number of the animated feature film for the studio."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the animated feature film."
      },
      "production_year": {
        "type": "integer",
        "description": "The year the animated feature film was produced."
      },
      "animation_type": {
        "type": "string",
        "description": "The type of animation used for the film."
      }
    },
    "required": [
      "studio_name",
      "feature_number",
      "film_title",
      "production_year",
      "animation_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
