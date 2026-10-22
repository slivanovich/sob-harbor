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
Semyon Nomokonov: Semyon Danilovich Nomokonov (12 August 1900 – 12 June or 15 July 1973) was a Soviet sniper during World War II, credited with 367 kills, recorded in his sniper log.  An ethnic Buryat-Mongolian Hamnigan Evenk, Nomokonov was among the indigenous peoples of Russia who fought in the war.  He received the nickname Taiga Shaman from the enemies.

Vasilij Kvachantiradze: Vasil Kvachantiradze (Georgian: ვასილ შალვას ძე კვაჭანტირაძე Russian: Квачантирадзе, Василий Шалвович (Kvachantiradze, Vasily Shalvovich)); January 1907 – February 9, 1950) was a top Soviet sniper during World War II.  He entered Red Army service in 1941 and is credited with confirmed kills numbering at least 215 officers and soldiers of the German Wehrmacht during the Vitebsk-Orsha Offensive, and around 534 confirmed kills total during Operation Bagration or during the war.

Hermann Kreß: Hermann Kreß (23 July 1895 – 11 August 1943) was a German general (Generalleutnant) in the Wehrmacht during World War II who commanded the 4th Mountain Division.  He was also a recipient of the Knight's Cross of the Iron Cross.  Kreß was killed instantly by a shot in the head from a Soviet sniper on 11 August 1943 near Novorossiysk, Soviet Union.

Vasily Reshetnikov: Vasily Vasiliyevich Reshetnikov (Russian: Василий Васильевич Решетников ) (born December 23, 1919) was a Soviet pilot during World War II.  Reshetnikov flew 307 missions mainly as a pilot for a long-range bomber and in the summer of 1943, received the title of Hero of the Soviet Union.  After World War II concluded he was named commander of Air Division, Air Corps.  Reshetnikov was subsequently promoted to Colonel General and took command of Long-range Air Forces from 1969 to 1980 and was made Deputy Commander-in-Chief of the Air Force of the Soviet Union from 1980 to 1986.

Ivan Kharchenko: Ivan Ustinovich Kharchenko (Ukrainian: Іван Устинович Харченко , 23 September 1918 - 1 July 1989) was a Soviet Army Military engineering Colonel and Hero of the Soviet Union.  During World War II, he was a platoon commander.  Kharchenko received was promoted to Junior lieutenant in 1939, lieutenant in 1943 and senior lieutenant in 1944.  He reportedly personally defused more than 50,000 explosives, including bombs, mines and shells.  For his actions in defusing explosives, Kharchenko was named a Hero of the Soviet Union and awarded the Gold Star and Order of Lenin on 2 November 1944.  In the citation for the Hero of the Soviet Union award, it was stated that Kharchenko personally defused more than 1500 bombs weighing more than 500 kilograms each and 25,000 other explosive objects.  After World War II, Kharchenko continued his military service until retirement in 1964.  Until 1956 he was personally engaged in rendering innocuous explosive items left over from World War II.

War Machine (film): War Machine is a 2017 American satirical war film directed and written by David Michôd, based on the nonfiction book "The Operators" by Michael Hastings.  It is a fictionalized version of the events in the book based on United States Army General Stanley McChrystal.

Vasily Zaytsev: Vasily Grigoryevich Zaytsev; 23 March 1915 – 15 December 1991) was a Soviet sniper and a Hero of the Soviet Union during World War II.  Prior to 10 November, he killed 32 Axis soldiers with a standard-issue rifle.  Between 10 November 1942 and 17 December 1942, during the Battle of Stalingrad, he killed 225 enemy soldiers, including 11 snipers.

51st Berlin International Film Festival: The 51st annual Berlin International Film Festival was held from February 7 to 18, 2001.  The festival opened with war-drama film "Enemy at the Gates" by Jean-Jacques Annaud.  70 mm restored version of Stanley Kubrick's 1968 Sci-fi film "" was the closing film of the festival.  The Golden Bear was awarded to French-British film "Intimacy" directed by Patrice Chéreau.

Enemy at the Gates: Enemy at the Gates is a 2001 French-American war film written and directed by Jean-Jacques Annaud and based on William Craig's 1973 nonfiction book "", which describes the events surrounding the Battle of Stalingrad in the winter of 1942 and 1943.  The film's main character is a fictionalized version of sniper Vasily Zaytsev, a Hero of the Soviet Union during World War II.  It includes a snipers' duel between Zaytsev and a "Wehrmacht" sniper school director, Major Erwin König.

Noah Adamia: Noah Petrovich Adamiya (Georgian: ნოე ადამია , Noe Adamia; Russian: Ной Петрович Адамия ) (December 21, 1917 – July 3, 1942) was a Soviet sniper of the Soviet Maritime Forces and Hero of the Soviet Union during World War II.  He participated in the Sevastopol sniper movement and personally trained about 80 snipers.  Adamiya is credited with killing around 300 German soldiers during the Battle of Sevastopol.

Question: Enemy at the Gates is a 2001 French-American war film written and directed by Jean-Jacques Annaud and based on William Craig's nonfiction book, released in which year, the film's main character is a fictionalized version of sniper Vasily Grigoryevich Zaytsev, a Hero of the Soviet Union during World War II, was a Soviet sniper?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "book_details": {
      "type": "object",
      "properties": {
        "author": {
          "type": "string",
          "description": "The author of the nonfiction book the film is based on."
        },
        "publication_year": {
          "type": "integer",
          "description": "The publication year of the nonfiction book."
        }
      },
      "required": [
        "author",
        "publication_year"
      ],
      "additionalProperties": false
    },
    "main_character_details": {
      "type": "object",
      "properties": {
        "fictionalized_name": {
          "type": "string",
          "description": "The name of the main character in the film, who is a fictionalized version of a real person."
        },
        "real_person_details": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the real person the character is based on."
            },
            "role": {
              "type": "string",
              "description": "The role or profession of the real person."
            },
            "award": {
              "type": "string",
              "description": "A significant award received by the real person."
            }
          },
          "required": [
            "name",
            "role",
            "award"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "fictionalized_name",
        "real_person_details"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_release_year",
    "director",
    "book_details",
    "main_character_details"
  ],
  "additionalProperties": false
}
