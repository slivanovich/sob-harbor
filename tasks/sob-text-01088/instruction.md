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
205 – Room of Fear: 205 – Room of Fear (German: "205 - Zimmer der Angst" ) is a 2011 German horror film directed by Rainer Matsutani.  It's a remake of the Danish film "Room 205".  The film stars Jennifer Ulrich.

A Night of Horror: A Night of Horror (German: Nächte des Grauens ) is a 1916 silent German horror film directed by Richard Oswald, Arthur Robison and starring Werner Krauss.  It is the earliest known feature-length film to portray vampires, with vampire-like people appearing in the film.

Emily Cox (actress): Emily Cox (born February 23, 1985) is a British actress.  She played the supporting role of Brida in the British television series "The Last Kingdom" (2015).

Anatomy (film): Anatomy (German: "Anatomie" ) is a 2000 German horror film written and directed by Stefan Ruzowitzky that stars Franka Potente.  A sequel, "Anatomy 2" ("Anatomie 2") was released in 2003.  The film was a box-office success in Germany, and Columbia Pictures released the film's English-dubbed version in the United States theatrically.

The Devil's Plaything: The Devil's Plaything (German: "Der Fluch der schwarzen Schwestern" ) is a 1973 Swedish / Swiss / German horror film directed by Joseph W. Sarno.  The film, in its uncut version, features more suggestively sexual scenes.

Rammbock: Rammbock (also Rammbock: Berlin Undead and Siege of the Dead) is a 2010 German horror film directed by Marvin Kren, written by Benjamin Hessler, and starring Michael Fuith, Theo Trebs, Anka Graczyk, and Emily Cox as survivors of a rage virus in Berlin.  Besides its native Germany, it was theatrically released in Austria, the UK, and the US.

Mark of the Devil: Mark of the Devil (German: "Hexen bis aufs Blut gequält" , lit.  Witches Tortured till They Bleed) is a West German horror film released in 1970.  It is most remembered for US marketing slogans devised by Hallmark Releasing Corp. that included "Positively the most horrifying film ever made" and "Rated V for Violence", while sick bags were given free to the audience upon admission.

Succubus (film): Succubus (German: Necronomicon - Geträumte Sünden ) is a 1968 West German horror film directed by Jesús Franco.  The original German title translates as "Necronomicon - Dreamt Sins".  The film stars Janine Reynaud as Lorna Green, a performer at a nightclub who performs fictionalized acts that involve erotically charged sadomasochistic murders.  It is suggested that Lorna may be under mind control by a man who might be Satan (Michel Lemoine) which draws her to a night in the future when she begins to actually kill people.

The Tenderness of Wolves (film): The Tenderness of Wolves, (German: Die Zärtlichkeit der Wölfe ) is a 1973 West German horror film directed by Ulli Lommel.  The story is based on the crimes of German serial killer and cannibal Fritz Haarmann.  It was written by Kurt Raab, who also stars in the film, and produced by Rainer Werner Fassbinder.  It was entered into the 23rd Berlin International Film Festival.

They're Alive!: They're Alive is the debut album of German horror punk band The Other, released in 2004.  The cover art is inspired by classic horror film posters.  At the bottom, it has an actor "starring" section for the band members: "STARRING: Andy Only, Dr Caligari, Rod Usher, Sarge von Rock and... The Creature" (in classic horror films, the Gill-man is commonly referred to as the "The Creature")

Question: What is the name of the British television series featuring the role of Brida as played by a co-star of German horror film Rammbock?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "television_series": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the television series."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the television series."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "role_details": {
      "type": "object",
      "properties": {
        "role_name": {
          "type": "string",
          "description": "The name of the role played in the series."
        }
      },
      "required": [
        "role_name"
      ],
      "additionalProperties": false
    },
    "actress_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actress."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actress."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "co_starring_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the German horror film the actress co-starred in."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the film."
        }
      },
      "required": [
        "title",
        "genre",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "television_series",
    "role_details",
    "actress_details",
    "co_starring_film"
  ],
  "additionalProperties": false
}
