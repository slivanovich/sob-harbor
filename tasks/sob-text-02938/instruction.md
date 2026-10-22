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
The Third Jungle Book: The Third Jungle Book by Pamela Jekel (ISBN  , 1992), originally illustrated by Nancy Malick, is a collection of new stories about Mowgli, the feral child character, and his animal companions, created by Rudyard Kipling and featured in Kipling's "The Jungle Book" (1894) and "The Second Jungle Book" (1895).

Baloo: Baloo (Hindi: भालू "Bhālū", "bear") is a main fictional character featured in Rudyard Kipling's "The Jungle Book" from 1894 and "The Second Jungle Book" from 1895.  Baloo, a bear, is the strict teacher of the cubs of the Seeonee wolf pack.  His most challenging pupil is the "man-cub" Mowgli.  Baloo and Bagheera, a panther, save Mowgli from Shere Khan the tiger and endeavor to teach Mowgli the Law of the Jungle in many of "The Jungle Book" stories.

Andy Engman: Andrew "Andy" Alfons Engman (November 21, 1911 – July 16, 2004) was a Swedish/Finnish cartoon animator.  Engman worked for Walt Disney Studios in Burbank, California from the animating of "Snow White and the Seven Dwarfs" (1937 film) to the completion of "The Jungle Book" (1967 film), about 1937 to 1971.  He started out as an "In-Betweener" animator.  He did some Donald Duck and Goofy cartoons as a character animator, and went on to being a special effects animator.  Later he went into production in a middle management position.  He also worked on the effect animations of "Make Mine Music" (1946) and the layout of "Der Fuehrer's Face" (1943).

Jungle Cubs: Jungle Cubs is an American animated series produced by Disney for ABC in 1996.  It was is a television series based on the 1967 film "The Jungle Book", but set in the youth of the animal characters.  The show was a hit, running for two seasons in syndication before its re-runs to the Disney Channel.  The show was broadcast on Toon Disney, but was taken off the schedule in 2001.  Re-runs aired on Disney Junior in the US from 2012 to 2013.  The show did air in the United Kingdom on Disney Cinemagic and in Latin America until it was removed.  The show's theme song is a hip-hop version of the classic song, "The Bare Necessities" performed by Lou Rawls.  As of May 31, 2016, every episode of the series is available for purchase on the iTunes Store.  The animated series will premiere on Disney Junior (including Latin America, United Kingdom and Ireland, Portugal, Italy, France, Germany and Southeast Asia) on August 5, 2017.

The Jungle Book 2: The Jungle Book 2 is a 2003 animated film produced by DisneyToon Studios and released by Walt Disney Pictures and Buena Vista Distribution.  The theatrical version of the film was released in France on February 5, 2003, and released in the United States on February 14, 2003.  The film is a sequel to Walt Disney's 1967 film "The Jungle Book", and stars Haley Joel Osment as the voice of Mowgli and John Goodman as the voice of Baloo.

Mowgli: Mowgli is a fictional character and the protagonist of Rudyard Kipling's "The Jungle Book" stories.  He is a naked feral child from the Pench area in Seoni, India, who originally appeared in Kipling's short story "In the Rukh" (collected in "Many Inventions", 1893) and then went on to become the most prominent and memorable character in his collections "The Jungle Book" and "The Second Jungle Book" (1894–1895), which also featured stories about other characters.

Raksha (The Jungle Book): Raksha (Hindi: रक्षा / "Rakṣā" or Mother Wolf as initially named) is a fictional character featured in Rudyard Kipling's Mowgli stories, collected in "The Jungle Book" and "The Second Jungle Book".  She is a female Indian wolf, member of the Seeonee pack, who while suckling her own cubs decides also to adopt a human "cub" that her mate Father Wolf has found wandering in the jungle, naming him "Mowgli" (which means "frog" in the Speech of the Jungle) because of his hairlessness.

Hathi: Shree.  Hathi is a fictional character created by Rudyard Kipling for the Mowgli stories collected in "The Jungle Book" (1894) and "The Second Jungle Book" (1895).  Hathi is a bull elephant that lives in the jungle.  Kipling named him after "hāthī" (हाथी),(ہاتھی) the Hindi and Urdu word for "elephant".

Gianni Blu: Gianni Mancini (born May 24, 1993), better known by his stage name Gianni Blu is the Chicago based EDM DJ/producer/songwriter who began his career with his early original records featuring Chicago rap artists like Lil Bibby, King Louie, and Sasha Go Hard.  After several popular house & trap remixes, Gianni veered his attention to making pop friendly EDM dance music.  In 2016 Gianni’s single “Feeling It” received support from Martin Garrix in addition to charting on Spotify’s US & Global Viral Charts.  Dancing Astronaut and Mixmag described Gianni Blu as a, “rising future house phenom” whose 2017 release “Thinking About You” featuring Kaskade collaborator Sansa, “embraces a future house production that results in an upbeat and powerfully smooth, enticing track”.

King Louie: King Louie (Hindi: राजा लुई ; Urdu: بادشاہ لوئی‎ ) is a fictional character introduced in Walt Disney's 1967 animated musical film, "The Jungle Book".  Unlike the majority of the adapted characters in the film, Louie was not in Rudyard Kipling's original works.

Question: EDM DJ/producer/songwriter, Gianni Blu, worked with what fictional character from the 1967 film "The Jungle Book"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "collaborator_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "type": {
          "type": "string"
        },
        "collaboration_context": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "type",
        "collaboration_context"
      ],
      "additionalProperties": false
    },
    "fictional_character_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "origin_film": {
          "type": "string"
        },
        "origin_year": {
          "type": "integer"
        },
        "is_original_kipling_character": {
          "type": "boolean"
        }
      },
      "required": [
        "name",
        "origin_film",
        "origin_year",
        "is_original_kipling_character"
      ],
      "additionalProperties": false
    },
    "answer_summary": {
      "type": "string",
      "description": "The name of the fictional character from the 1967 film that shares a name with Gianni Blu's collaborator."
    }
  },
  "required": [
    "artist_details",
    "collaborator_details",
    "fictional_character_details",
    "answer_summary"
  ],
  "additionalProperties": false
}
