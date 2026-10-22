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
Brother Bear (soundtrack): Brother Bear: An Original Walt Disney Records Soundtrack is the soundtrack to Disney's 2003 animated feature film "Brother Bear".  It contains the film's music composed by Mark Mancina and Phil Collins, as well as songs written by Collins, and performed by Tina Turner, The Blind Boys of Alabama, Oren Waters, The Bulgarian Women's Choir, and even Collins himself.  Much of the soundtrack in the film consists of the songs performed by Collins as a montage, much like what was done with the earlier Disney soundtrack to film "Tarzan", but not entirely.  The album was released on October 21, 2003 by Walt Disney Records.

Disney's Brother Bear (video game): Disney's Brother Bear is a video game released by Disney as a tie-in to the 2003 theatrical film "Brother Bear."

The Big Honey Hunt: The Big Honey Hunt is a children's book by Stan and Jan Berenstain, the first in the long-running Berenstain Bears series.  It was first published in 1962, by Beginner Books, an imprint of Random House co-founded and managed by Dr. Seuss.  The book introduces a family of anthropomorphic bears comprising Papa Bear, Mama Bear, and Small Bear (later renamed Brother Bear).

Brother Bear: Brother Bear is a 2003 American animated comedy-drama film produced by Walt Disney Feature Animation and released by Walt Disney Pictures.  It is the 44th Disney animated feature film.  In the film, an Inuit boy named Kenai pursues a bear in revenge for a battle that he provoked in which his oldest brother Sitka is killed.  He tracks down the bear and kills it, but the Spirits, angered by this needless death, change Kenai into a bear himself as punishment.  In order to be human again, Kenai must travel to a mountain where the Northern lights touch the earth, and learn to see through another's eyes, feel through another's heart, and discover the meaning of brotherhood.

Danny Mastrogiorgio: Daniel "Danny" Mastrogiorgio (born October 26, 1964) is an American stage, film and television actor who has also provided voice work for video games.  He is best known for providing the voice of Toni Cipriani in the 2005 video game "" and for his appearances in movies such as "Brother Bear" and "Enchanted."  He has also been in several television shows such as "Law & Order".

Look Through My Eyes: "Look Through My Eyes" is a song by English singer Phil Collins from the "Brother Bear" film soundtrack.  It was recorded by Everlife for the "Bridge to Terabithia" soundtrack and the "Disneymania 4" album.  The song was the film's first single.

No Way Out (Phil Collins song): "No Way Out" is a song by the English singer Phil Collins from the "Brother Bear" film soundtrack.

Brother Bear 2: Brother Bear 2 is a 2006 American animated comedy-drama film and the direct-to-video sequel to the animated feature "Brother Bear", which was released on August 29, 2006.  Melissa Etheridge contributed three songs to the film.  In the film, the adventures of bear brothers Kenai and Koda continue.  While the first film dealt with Kenai's relationship with Koda, this one focuses more on his bond with a young human, Nita.

David Metzger: David Metzger (born in 1960 in Corvallis, Oregon), is an American orchestrator and composer best known for his orchestrations of many Disney feature animation films of the past 20 years.  He has helped to shape the classic Disney orchestral sound on major Disney films including "Frozen", "Moana", "Planes", "Wreck-It Ralph", "Tarzan", "Haunted Mansion", and "Brother Bear".  He arranged 6 of the 7 songs in "Frozen" including the blockbuster "Let It Go" as well as much of the score.  In addition to his work for Disney, he has done orchestrations for over 50 major films.  He has also composed the musical score for Tarzan 2, Brother Bear 2, and Tarzan and Jane.  He also has numerous video game, theme park, TV, and commercial credits.

Fantasia (1940 film): Fantasia is a 1940 American animated film produced by Walt Disney and released by Walt Disney Productions.  With story direction by Joe Grant and Dick Huemer, and production supervision by Ben Sharpsteen, it is the third Disney animated feature film.  The film consists of eight animated segments set to pieces of classical music conducted by Leopold Stokowski, seven of which are performed by the Philadelphia Orchestra.  Music critic and composer Deems Taylor acts as the film's Master of Ceremonies, providing a live-action introduction to each animated segment.

Question: What was the number of the later film of Fantasia and Brother Bear?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_comparison": {
      "type": "object",
      "properties": {
        "first_film_title": {
          "type": "string",
          "description": "The title of the earlier film being compared."
        },
        "first_film_sequence_number": {
          "type": "integer",
          "description": "The sequence number of the earlier film."
        },
        "second_film_title": {
          "type": "string",
          "description": "The title of the later film being compared."
        },
        "second_film_sequence_number": {
          "type": "integer",
          "description": "The sequence number of the later film."
        }
      },
      "required": [
        "first_film_title",
        "first_film_sequence_number",
        "second_film_title",
        "second_film_sequence_number"
      ],
      "additionalProperties": false
    },
    "later_film_title": {
      "type": "string",
      "description": "The title of the film that was released later."
    },
    "later_film_sequence_number": {
      "type": "integer",
      "description": "The sequence number of the later film."
    }
  },
  "required": [
    "film_comparison",
    "later_film_title",
    "later_film_sequence_number"
  ],
  "additionalProperties": false
}
