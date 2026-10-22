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
Luna Park (1992 film): Luna Park (Russian: Луна-парк ; 1992) is a Franco-Russian produced film.  The second feature film of Russian director Pavel Lungin, it depicts the story of a young antisemitic skinhead leader, Andrei Leonov (Andrei Gutin) who is forced to come to terms with the discovery that his father, Naoum Kheifitz (Oleg Borisov) is of Jewish ancestry .  The film, of the "chernukha" (Russian: чернуха, roughly "black stuff"), genre, follows Andrei as he explores his heritage and the relationship he begins with his father.

Nadezhda Mikhalkova: Nadezhda Nikitichna Mikhalkova (Russian: Надежда Никитична Михалкова; born September 27, 1986) is a Russian actress.

Big Noyd: TaJuan Akeem Perry, (born May 7, 1975), better known by his stage name, Big Noyd, is an American rapper from Queensbridge, Queens, New York.  He is closely affiliated with Mobb Deep, and he is featured on all of their albums except Blood Money.  He is of Puerto Rican and African American descent.  He also has one daughter born Tiara Perry, who still lives in Queensbridge, Queens.

Jepchirchir: Jepchirchir (also spelled Chepchirchir) is a name of Kenyan origin, traditionally used among the Kalenjin people and meaning a daughter born after a short labour.  It may also mean "daughter of Chirchir".  The male variant of this name is Kipchirchir.

Lino Ventura: Angiolino Giuseppe Pasquale "Lino" Ventura (14 July 1919 – 22 October 1987) was an Italian-born actor who starred in French films.  Raised by his Italian mother in Paris, after a first career as a professional wrestler was ended by injury he was offered a part as a gang boss in the 1954 film "Touchez pas au grisbi" and rapidly became one of France's favourite film actors, playing opposite many other stars and working with leading directors such as Jacques Becker, Louis Malle, Claude Sautet, Jean-Pierre Melville and Claude Miller.  Usually portraying a tough man, either a criminal or a cop, he also featured as a leader of the Resistance in "L'armée des ombres".  Having a daughter born handicapped, he and his wife founded a charity Perce-Neige (Snowdrop) which aids such children and their parents.  Though he never renounced his Italian citizenship, he was voted 23rd in a poll for the 100 greatest Frenchmen.

Sophie Webster: Sophie Lauren Webster is a fictional character from the British ITV soap opera, "Coronation Street".  She was born on-screen during the episode broadcast on 4 November 1994.  She was played by Ashleigh Middleton from 1994 until 1997 and by Emma Woodward from 8 June 1997 until 25 April 2004.  Brooke Vincent took over the role on 12 May 2004.  Sophie is the second daughter born to Kevin (Michael Le Vell) and Sally Webster (Sally Dynevor) and younger sister to Rosie Webster (Emma Collinge/Helen Flanagan) and elder sister to half siblings Jack Webster and deceased Jake Webster.  Sophie's storylines have included her constant rivalry with Rosie, her converting to Christianity and her lesbian relationships with both Sian Powers (Sacha Parkinson) and Maddie Heath (Amy James-Kelly).  In 2015, it was announced that Vincent would take a four-month break from the show at the end of her contract, departing in October 2016.  Vincent returned as Sophie on-screen on 6 February 2017, along with sister Rosie, after actress Flanagan agreed to reprise her role back in October 2016.

Boris Plotnikov: Boris Grigoryevich Plotnikov (Russian: Борис Григорьевич Плотников , born 2 April 1949) is a Soviet and Russian film actor.  His film debut was as Sotnikov in "The Ascent", the acclaimed final film of Russian director Larisa Shepitko.

Vladimir Makeranets: Vladimir Ilyich Makeranets (Russian: Влади́мир Ильи́ч Макера́нец , born 6 May 1947) is a Soviet and Russian director of photography, producer and film director, Head of the Ural Department of the Russian Union of Filmmakers, president of the Ural Guild of Cinematographers.

Burnt by the Sun: Burnt by the Sun (Russian: Утомлённые солнцем , translit.  "Utomlyonnye solntsem", literally "wearied by the sun") is a 1994 film by Russian director and screenwriter Nikita Mikhalkov and Azerbaijani screenwriter Rustam Ibragimbekov.  The film depicts the story of a senior Red Army officer, played by Mikhalkov, and his family during the Great Purge of the late 1930s in the Stalinist Soviet Union.  It also stars Oleg Menshikov, Ingeborga Dapkūnaitė and Mikhalkov's daughter Nadezhda Mikhalkova.

Sunstroke (2014 film): Sunstroke (Russian: Солнечный удар; translit.  "Solnechnyy udar") is a 2014 drama film by Russian director Nikita Mikhalkov.  It is set in Russia during the Red Terror in 1920 and in 1907, and is loosely based on the story "Sunstroke" and the book "Cursed Days" by Nobel Prize-winning Russian writer Ivan Bunin.  The film was selected as the Russian entry for the Best Foreign Language Film at the 88th Academy Awards but it was not nominated.

Question: What was the name of the Russian director who created a 1994 film in which his daughter born in 1986 co-starred?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "release_year": {
          "type": "integer"
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    },
    "co_starring_daughter": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        },
        "role_description": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "birth_year",
        "role_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "director",
    "film",
    "co_starring_daughter"
  ],
  "additionalProperties": false
}
