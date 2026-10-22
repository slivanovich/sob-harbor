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
Demobbed (2000 film): Demobbed (Russian: ДМБ , "DMB " ) is a cult Russian comedy film by Roman Kachanov, offering an absurdistic view on the Russian army by the eyes of a conscript.  The brutal rituals of Dedovshchina, a major problem within Russian society, is shown not as a tragedy, but as an idylically insane process of resocialization.

Yolki: Yolki (Russian: Ёлки, "Spurce trees" ), also known as Six Degrees of Celebration, is a 2010 Russian comedy film directed by Timur Bekmambetov.  Two sequels have been released, including Yolki 2 in 2011 and Yolki 3 in 2013.  The films in the series represent a Russian tradition of the New Year's Movie where films that take place during the holiday season tap into the vein of hope, optimism, and possibility associated with New Year's in the Russian culture.  Other examples include "The Irony of Fate" and "The Irony of Fate 2" (also directed by Bekmambetov).  Typically such films are released in December, just before the start of the holidays in Russia.

Inadequate People: Inadequate People (Russian: Неадекватные люди , "Neadekvatnye lyudi " ) is a 2011 Russian comedy film directed by .

The Best Movie 2: The Best Movie 2 (Russian: Самый лучший фильм 2 , "Samiy luchshiy film 2 " ) is a 2009 Russian comedy from Monumental Pictures (Sony Pictures Entertainment) and Comedy Club Production, continuation of 2008 "The Best Movie" film, spoofing such famous Russian films as "Zhara", "The Irony of Fate 2" and TV-programs: "Malakhov+", "King of Ring" and "Taxi".

The Best Movie 3: The Best Movie 3 (Russian: Самый лучший фильм 3 , "Samiy luchshiy film 3 " ) is a 2011 Russian comedy from Monumental Pictures (Sony Pictures Entertainment) and Comedy Club Production, continuation of 2009 The Best Movie 2 film, spoofing such famous Russian films as "Admiral", "Burnt by the Sun 2", "Stilyagi", "Black Lightning", and others.

Cloud-Paradise: Cloud-Paradise (Russian: Облако-рай , "Oblako-ray " ) is a 1990 Russian comedy film directed by Nikolai Dostal.  It was voted best film of 1992 by 90 Russian critics.

Timur Bekmambetov: Timur Nuruakhitovich Bekmambetov (Russian: Тиму́р Нуруахи́тович Бекмамбе́тов , ] ; Kazakh: Темір Нұрбақытұлы Бекмамбетoв , Temir Nurbaqıtulı Bekmambetov; born June 25, 1961) is a Russian-Kazakh director, producer and screenwriter who has worked on films, music videos and commercials.  He is best known for the film "Night Watch" (2004) and its sequel "Day Watch" (2006), and the American films "Wanted" (2008) and "" (2012).

Drumroll (film): Drumroll (Russian: Barabaniada , "Барабаниада " ) is a 1993 Russian comedy film directed by Sergei Ovcharov.  It was entered into the 18th Moscow International Film Festival where it won the Special Silver St. George and the Prix of Ecumenical Jury.  The picture also won the Special Jury Prize at Kinotavr.

Assia and the Hen with the Golden Eggs: Assia and the Hen with the Golden Eggs (Russian: Курочка Ряба , translit.  Kurochka Ryaba) is a 1994 Russian comedy film directed by Andrei Konchalovsky.  It was entered into the 1994 Cannes Film Festival.

The Best Movie: The Best Movie (Russian: Самый лучший фильм , "Samy luchshiy film") is a 2008 Russian comedy film from TNT and Comedy Club Russia, spoofing such famous Russian films as "Night Watch" and "Day Watch", "The 9th Company", "Heat" and TV series: "My Fair Nanny", "Dalnoboyshchiki" and "Brigada".  The movie includes numerous cameos by Russian celebrities, some of them involving a humorous touch on their public image.  For instance, socialite Kseniya Sobchak appears as a luxury prostitute, and gay icon Boris Moiseev plays a rough-and-tumble policeman, his only line being: "You gonna sign it all, you faggot!"

Question: What 2004 film is the director of Yolki (a Russian comedy film), most famous for?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "original_film_title": {
      "type": "string",
      "description": "The title of the film mentioned in the question that led to identifying the director."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the director."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "most_famous_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film the director is most famous for, matching the specified year."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the most famous film."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "original_film_title",
    "director",
    "most_famous_film"
  ],
  "additionalProperties": false
}
