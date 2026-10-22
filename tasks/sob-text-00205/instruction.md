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
Undead (film): Undead is a 2003 Australian zombie science fiction horror comedy film written and directed by Michael and Peter Spierig and starring Felicity Mason, Mungo McKay and Rob Jenkins.  It was then-relatively-unknown "Good Game" presenter Steven O'Donnell's first film role.

AACTA Award for Best Visual Effects or Animation: The AACTA Award for Best Visual Effects or Animation (previously Best Visual Effects) is an award presented by the Australian Academy of Cinema and Television Arts (AACTA) for achievements in visual effects in film, television, documentary and short film.  The award was first presented by the Australian Film Institute (AFI)at the Australian Film Institute Awards (known commonly as the AFI Awards) from 2006-2010, prior to the establishment of the Academy.  In 2014 the award for Best Visual Effects was renamed Best Visual Effects or Animation.  Additionally, this category is now open to any film, television or documentary production, regardless of geography, which has had 100% of its visual effects and animation made in Australia.

Jigsaw (2017 film): Jigsaw is an upcoming American horror film directed by Michael and Peter Spierig, written by Josh Stolberg and Peter Goldfinger, and starring Matt Passmore, Callum Keith Rennie, Clé Bennett, and Hannah Emily Anderson.  It is the eighth installment in the "Saw" franchise, picking up over a decade after the death of the eponymous Jigsaw killer during the police investigation of a new succession of murders that fit his "modus operandi". " Saw 3D" was originally deemed the final installment of the series, before Lionsgate Films commissioned the production of "Jigsaw" from a pitch by Stolberg and Goldfinger.  Filming began on November 2016, with post production following in January.

Predestination (film): Predestination is a 2014 Australian science fiction thriller film written and directed by Michael and Peter Spierig.  The film stars Ethan Hawke, Sarah Snook and Noah Taylor, and is based on the short story ""—All You Zombies—"" by Robert A. Heinlein.

Oscar Isaac: Oscar Isaac (born Óscar Isaac Hernández Estrada; March 9, 1979) is a Guatemalan-American actor and musician.  He played lead film roles in the comedy-drama "Inside Llewyn Davis" (2013), for which he received a Golden Globe Award nomination, the crime drama "A Most Violent Year" (2014), the science fiction thriller "Ex Machina" (2015), in which he played Nathan Hamlet Bateman, and Poe Dameron in "".  In 2006, he portrayed Saint Joseph, husband of Mary, in "The Nativity Story".  He also portrayed José Ramos-Horta, former president of East Timor, in the Australian film "Balibo" for which he won the AACTA Award for Best Actor in a Supporting Role.  He has portrayed characters of many different nationalities and ethnicities, such as mixed European, American, Egyptian, Polish, English, French, Mexican, East Timorese, Italian, Welsh, Indonesian, Greek, Cuban, Israeli, and Armenian.

The Big Picture (2000 film): The Big Picture is the first short film directed by the Michael and Peter Spierig.  The film was released in 2000.

AACTA Award for Best Short Animation: The AACTA Award for Best Short Animation, is a short film award presented by the Australian Academy of Cinema and Television Arts (AACTA) to the producer and director of an Australian short animated film that is "a self-contained and continuous animated film of short fiction or documentary of less than 40 minutes in duration."  Prior to the establishment of the Academy in 2011, the award was presented by the Australian Film Institute (AFI) at the annual Australian Film Institute Awards (more commonly known as the AFI Awards) from 1979–2010.  The award is presented at the AACTA Awards Luncheon, a black tie event which celebrates achievements in film production, television, documentaries and short films.

Matt Villa: Matt Villa is an Australian film editor, most famous for editing "The Great Gatsby", for which he won Best Editing at the 3rd AACTA Awards alongside Jason Ballantine and Jonathan Redmond.  Villa won his second AACTA Award the following year for "Predestination".

The Spierig Brothers: Identical twin brothers Peter Spierig and Michael Spierig ( ; born 29 April 1976), known together professionally as The Spierig Brothers, are German-born Australian film directors, producers and screenwriters.

Daybreakers: Daybreakers is a 2009 Australian-American science fiction horror film written and directed by Michael and Peter Spierig.  The film takes place in a futuristic world overrun by vampires.  A vampiric corporation sets out to capture and farm the remaining humans while researching a blood substitute.  Lead vampire hematologist Edward Dalton's (Ethan Hawke) work is interrupted by human survivors led by former vampire "Elvis" (Willem Dafoe), who has a cure that can save the human species.

Question: Question: Michael and Peter Spierig directed this 2014 science fiction film that won Matt Villa his second AACTA Award. 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "directors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the film's directors."
    },
    "genre": {
      "type": "string",
      "description": "The primary genre of the film."
    },
    "award_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the award received."
        },
        "recipient_name": {
          "type": "string",
          "description": "The name of the person who received the award."
        },
        "award_number_for_recipient": {
          "type": "integer",
          "description": "The sequential number of this award for the specific recipient (e.g., 1st, 2nd)."
        }
      },
      "required": [
        "award_name",
        "recipient_name",
        "award_number_for_recipient"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "directors",
    "genre",
    "award_details"
  ],
  "additionalProperties": false
}
