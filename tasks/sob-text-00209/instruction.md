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
Josef Kainar: Josef Kainar (June 29, 1917 in Přerov, Austria-Hungary – November 16, 1971 in Dobříš, Czechoslovakia) was a Czech poet, lyrics writer, dramatic author and translator, but also a musician, illustrator, artist and journalist.  He was a member of artistic group Skupina 42 and literary group Ohnice.

Östen Warnerbring: Östen Warnerbring (November 22, 1934 – January 18, 2006) was a Swedish singer, musician, composer and lyrics writer who mastered several musical genres.  He started out as a jazz musician but over the years, he had huge successes both in the area of popular music and as a singer of Swedish poetry, put into music by himself.  In the 1970s, he became one of the first Swedish artists to use his native accent, of the province of Scania (Skåne) in the south of Sweden, also while singing.

Jacek Lusiński: Jacek Lusiński (born 30 April 1969) is a Polish film director, scriptwriter, lyrics writer and author of the book "Carte Blanche", published by Axis Mundi.  He makes feature films, documentaries, commercials and video clips.  He was graduated from the Lodz Film School.

Akira Sudou: Akira Sudou (須藤 あきら , born November 4, 1971 ) is a Japanese female rock vocalist.  She is arguably best known for her work as the vocalist and lyrics writer for SEKIRIA, the band that did the music for the anime series "" and played live in the movie Shuto Kōsoku Max.

Candles, Snow &amp; Mistletoe: Candles, Snow & Mistletoe is the 13th album by popular children's entertainers Sharon, Lois & Bram, originally released in 1993.  This holiday album is one of Sharon, Lois & Bram's biggest productions and recordings they worked on during their career.  The album is produced by Glen Roven, an Emmy-Award winning producer who has worked with Liza Minnelli.  Lyrics were written by Mark Saltzman who also worked with "Sesame Street".  This album, unlike previous Sharon, Lois & Bram albums, has a Broadway sound to the album.  It featured a complete orchestra and was recorded using the same microphones as The Manhattan Transfer.

Waris Ali Mirza: Sayyid Waris Ali Mirza Khan Bahadur (14 November 1901 – 20 November 1969), was the last Nawab of Murshidabad before a prolonged interregnum caused by a succession dispute within the family which was only resolved in 2014 by the Indian Supreme Court.  He succeeded his father, Wasif Ali Mirza.  Waris Ali was born on 14 November 1901 at Murshidabad as the eldest son of Wasif Ali Mirza by his first wife Sultan Dulhan Faghfur Jahan Begum Sahiba.  Waris Ali's maternal grandfather was Wala Kadir Sayyid Husain Ali Mirza Bahadur.  Waris Ali ruled for ten years, from 1959, until his death on 20 November 1969 at Calcutta.  Although he left three sons and three daughters, there was a long interregnum following his death because of succession dispute caused by his children's disinheritance for a variety of different reasons.  In August 2014 the Indian Supreme Court ruled that Mohammed Abbas Ali Mirza, a nephew of Waris Ali Mirza, was the fourth Nawab of Murshidabad in August 2014.

Candles Long Ago: Candles Long Ago is the 14th album by popular children's entertainers Sharon, Lois & Bram, originally released in 1993.  It is the first, and only, Chanukah album produced by the trio.  Unlike other Sharon, Lois & Bram albums, "Candles Long Ago" is a miniature album featuring only eleven songs, of which many appear on their previous album "Candles, Snow & Mistletoe" and one from their second album, "Smorgasbord".  O It was sold as part of the Sharon, Lois & Bram mini collection at a cheaper price than the trio's regular full-length albums.

Mikhail Tanich: Mikhail Isaievich Tanich (Tankhilevich) (Russian: Михаил Исаевич Танич ) (September 15, 1923 – April 17, 2008) was a popular Russian song lyrics writer of Jewish descent, a laureate of the Interior Ministry Award (1997), a laureate of the jubilee contest "The Song of the Year" devoted to the 25th anniversary of that television program, a laureate of nearly all the annual festivals "The Song of the Year", and a laureate of the "Ovation" National Music Award (1997).

Sesame Street: Sesame Street is a long-running American children's television series, produced by Sesame Workshop (formerly known as the Children's Television Workshop) and created by Joan Ganz Cooney and Lloyd Morrisett.  The program is known for its educational content, and images communicated through the use of Jim Henson's Muppets, animation, short films, humor, and cultural references.  The series premiered on November 10, 1969, to positive reviews, some controversy, and high viewership; it has aired on the U.S.'s national public television provider (PBS) since its debut, with its first run moving to premium channel HBO on January 16, 2016.

Sanjeev Tiwari: Sanjeev Tiwari is a story, screenplay, dialogue writer, lyrics writer and music composer of Bollywood working in bangla and Hindi films.  He was a renowned radio personality from Kolkata got the best male RJ award in the year 2007 He has written story screenplay & dialogues for television shows like Savdhaan India for Life Ok, for Channel V, title track for life Ok's serial Meri Maa, dialogues for the film Bloody Isshq written lyrics for films like Sooper Se Ooper,Morning Walk, Jal (film), Via Darjeeling, Yatra (film), Devaki (film), Chowky, Hothat Brishti and even written & composed songs for Bollywood films like, Hotel Beautifool

Question: Who is the lyrics writer for the album Candles, Snow & Mistletoe and the children television show that premiered in November 1969?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "lyrics_writer": {
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
    "associated_works": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "work_type": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "details": {
            "type": "object",
            "properties": {
              "release_year": {
                "type": "integer"
              },
              "premiere_date": {
                "type": "string"
              },
              "artists": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "creators": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            },
            "additionalProperties": false
          }
        },
        "required": [
          "work_type",
          "title"
        ],
        "additionalProperties": false
      }
    },
    "number_of_associated_works": {
      "type": "integer"
    }
  },
  "required": [
    "lyrics_writer",
    "associated_works",
    "number_of_associated_works"
  ],
  "additionalProperties": false
}
