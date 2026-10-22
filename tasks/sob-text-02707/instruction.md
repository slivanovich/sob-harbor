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
Ruler X (Rio Azul): Ruler X (also Governor X) is the designation given by archaeologists to a pre-Columbian Maya ruler at the site of Rio Azul, whose name glyphs have otherwise not been satisfactorily deciphered.  Ruler X is associated with Tomb 1 located in Structure C-1, where a mural inscription on the walls of the tomb carries the Long Count date of 8.19.1.9.13.  This date, equivalent to September 27, 417 CE in the proleptic Gregorian calendar, has been interpreted as the birth date of this ruler.

Angela Lansbury: Dame Angela Brigid Lansbury, {'1': ", '2': ", '3': ", '4': "} (born 16 October 1925) is a British-American-Irish actress who has appeared in theatre, television and film, as well as a producer, voice actress, singer, and songwriter.  Her career has spanned seven decades, much of it in the United States, and her work has attracted international attention.

The Search for Robert Johnson: The Search for Robert Johnson is a 1991 UK television documentary film about the Delta blues musician Robert Johnson, hosted by John Hammond, and produced and directed by Chris Hunt.  In it, Hammond travels through the American Deep South to pursue topics such as Johnson's birth date, place and parents, his early musical development, performances and travels, romances, his mythic "pact with the devil," his untimely murder in his late twenties, the discovery of possible offspring, and the uncertainty over where Johnson is buried.  Throughout, Johnson's music is both foreground and background, from recordings of Johnson and as performed on camera by Hammond, David Honeyboy Edwards, and Johnny Shines.

Thomas D. Singleton: Thomas Day Singleton (Birth date unknown – November 25, 1833) was a United States Representative from South Carolina.  He was born near Kingstree, South Carolina but his birth date is unknown.

Hippolytus (archbishop of Gniezno): Hippolytus or Hipolit (died c. 1027) was an early medieval archbishop of Gniezno.  His place and date of birth date are unknown but the medieval historian Jan Długosz claims that he was of noble birth and a Roman citizen.  Modern scholars generally agree that he was not Polish.

Cédula de identidad (Costa Rica): In Costa Rica, in recent years, a cédula de identidad, has been a credit card-sized plastic card.  On one side, it includes a photo of the person, a personal identification number, and the card's owner personal information (complete name, gender, birth date, and others), and the user's signature.  On the reverse, it may include additional information such as the date when the ID card was granted, expiration date of the ID card, and other such as their fingerprints, and all the owner's information in matrix code.  Every Costa Rican citizen must carry an ID card immediately after turning 18.

Fortuosity: "Fortuosity" is the first song in the 1967 motion picture The Happiest Millionaire.  It was first performed by Tommy Steele playing the part of "John Lawless" (the butler).  The song was written by Robert and Richard Sherman.  Richard Sherman stated that the word meant "Faith and Good Fortune".  "Fortuosity" is another nonsense word alongside the name of another one of their songs,"Supercalifragilisticexpialidocious".  Steele also sings the song, "I'll Always Be Irish", in the movie.

Akhund Mullah Mohammad Kashani: Akhund Mullah Mohammad Kashani, known as lunar tiles in 1833 was born in Kashan.  In place of his birth date and age of his birth is not mentioned during the 84 years of his life, to guess.  According to Syed Jalaluddin Homai, he, along with Jahangir Khan Qashqai as two distinguished professor in philosophy and jurisprudence, literature and jurisprudence have.  He taught for fifty years and foster outstanding students in the fields of intellectual and traditional sciences.  He died in 1914 in Isfahan and was buried in Takht-e Foulad.

Astro Boy (2003 TV series): Astro Boy (アストロボーイ・鉄腕アトム , Asutoro Bōi: Tetsuwan Atomu , lit.  "Astro Boy: Mighty Atom") is a remake of the 1960s anime series of the same name created by Osamu Tezuka, which was produced by his company, Tezuka Productions, Sony Pictures Entertainment Japan, Dentsu, and Fuji Television network.  It was also shown on Animax, who have broadcast the series across its respective networks worldwide, including Japan, Southeast Asia, South Asia, East Asia, and other regions.  It was created to celebrate the birth date of Atom/Astro Boy (as well as the 40th anniversary of the original TV series).  Under the original English name (instead of "Mighty Atom"), it kept the same classic art style as the original manga and anime, but was revisioned and modernized with more lush, high-quality, near-theatrical animation and visuals.  It combined the playfulness of the early anime with the darker, more serious and dramatic Science fiction themes of the manga and the 1980 series.  The anime broadcast in Japan on the same date as Atom's/Astro's birth in the manga (April 6, 2003) across Animax and Fuji Television.  It was directed by Kazuya Konaka and written by Chiaki J. Konaka at the beginning of the series.  Other writers included were Keiichi Hasegawa, Sadayuki Murai, Ai Ohta, Hirotoshi Kobayashi, Kenji Konuta, and Marc Handler, who was also executive story editor.

Don't Let Me Down (Disney song): "Don't Let Me Down" by Robert & Richard Sherman is a song from the 1971 Walt Disney musical film, "Bedknobs and Broomsticks".  It is sung by Angela Lansbury in reply to David Tomlinson's "sales pitch" song, "Eglantine" where Tomlinson begs Lansbury to join his magic act.  The song is often cut from TV presentations of the film.

Question: what is the birth date of the singer of "Don't Let Me Down" by Robert and Richard Sherman?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "song_writers": {
      "type": "array",
      "description": "The writers of the song.",
      "items": {
        "type": "string"
      }
    },
    "singer_details": {
      "type": "object",
      "properties": {
        "singer_name": {
          "type": "string",
          "description": "The name of the singer."
        },
        "singer_birth_date": {
          "type": "string",
          "description": "The birth date of the singer in 'DD Month YYYY' format."
        },
        "singer_nationalities": {
          "type": "array",
          "description": "The nationalities of the singer.",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "singer_name",
        "singer_birth_date",
        "singer_nationalities"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "song_writers",
    "singer_details"
  ],
  "additionalProperties": false
}
