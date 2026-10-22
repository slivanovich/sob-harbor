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
Single Video Theory: Single Video Theory is a music documentary directed by Mark Pellington that follows the making of "Yield", the fifth album by the American alternative rock band Pearl Jam.  It was released first on VHS on August 4, 1998, and then on DVD on November 24, 1998.

David Hannan: David Hannan is a Australian cinematographer, specializing in underwater cinematography.  Hannan's footage has been featured in numerous films, including Sylvia Earle's "Mission Blue", Louie Psihoyos' "Racing Extinction", and Rob Stewart's "Sharkwater and Revolution".

Racing Extinction: Racing Extinction is a 2015 documentary about the ongoing Anthropogenic mass extinction of species and the efforts from scientists, activists and journalists to document it by Oscar-winning director Louie Psihoyos, who directed the documentary "The Cove" (2009).  The film received one Academy Award nomination, for best Original Song, and one Emmy nomination.  "Racing Extinction" premiered at the 2015 Sundance Film Festival, followed by limited theater release, with worldwide broadcast premiere on The Discovery Channel in 220 countries or territories on December 2, 2015.

BlazBlue: Chrono Phantasma: BlazBlue: Chrono Phantasma, released in Japan as BlazBlue: Chronophantasma (ブレイブルー クロノファンタズマ , BureiBurū Kuronofantazuma ) , is a 2-D fighting game developed by Arc System Works.  It is the third game of the Blazblue series, set after the events of "".  The game was originally to be released first as an arcade game in the early fourth quarter of 2012, which was later pushed forward to November 2012.  A PlayStation 3 version of the game was released in Japan on October 24, 2013, while it was released in the United States on March 25, 2014.  Due to limited hardware and disc space the game was not released on the Xbox 360.  An updated version of the game titled BlazBlue: Chrono Phantasma Extend (ブレイブルー クロノファンタズマ エクステンド , BureiBurū: Kuronofantazuma Ekusutendo , BlazBlue: Chronophantasma Extend) , dubbed as BlazBlue: Chrono Phantasma 2.0 (ブレイブルー クロノファンタズマ ２.０ , BureiBurū: Kuronofantazuma 2.0 , BlazBlue: Chronophantasma 2.0) in the Arcade version, was originally released for Arcades in October 2014, and for the PlayStation 3, PlayStation Vita, PlayStation 4, and Xbox One in April 2015.  It was released on June 30, 2015 in North America, with the European region version releasing on October 23, 2015.

Lamakera, Indonesia: Lamakera is a village in Indonesia.  It was known for being the place where the most manta rays are killed.  It was featured in the 2015 documentary film, Racing Extinction.

Tintin (magazine): "Tintin" magazine (French: "Le Journal de Tintin" ; Dutch: "Kuifje" ) was a weekly Franco-Belgian comics magazine of the second half of the 20th century.  Subtitled ""The Magazine for the Youth from 7 to 77"", it was one of the major publications of the Franco-Belgian comics scene and published such notable series such as "Blake and Mortimer", "Alix", and the principal title "The Adventures of Tintin".  Originally published by Le Lombard, the first issue was released in 1946, and it ceased publication in 1993.

Manta Ray (song): "Manta Ray" is an original song composed by J. Ralph and Anohni and performed by Anohni.  The song was released as the lead single from the soundtrack album of 2015 documentary "Racing Extinction" written by Anohni.

Tintin and I: Tintin and I (French: Tintin et moi) is a 2003 documentary by Anders Høgsbro Østergaard, about Belgian writer-artist Georges Remi, better known as Hergé, and his creation Tintin.  The film is a co-production of Denmark, Belgium, France, and Switzerland.

Tintin and the Golden Fleece: Tintin and the Golden Fleece (in the original French, "Tintin et le Mystère de La Toison d'or", meaning "Tintin and the Mystery of the Golden Fleece") is a film first released in France on 6 December 1961.  Featuring characters from "The Adventures of Tintin" comic book series written and drawn by the Belgian writer-artist Hergé, it was a live-action film with actors made-up to look like the characters and featured an original storyline not based on any of the books.

Mario Kart 64: Mario Kart 64 (マリオカート64 , Mario Kāto Rokujūyon ) is a 1996 go-kart racing game developed and published by Nintendo for the Nintendo 64 video game console.  It was the successor to "Super Mario Kart" for the Super Nintendo Entertainment System, and is the second game in the "Mario Kart" series.  It was released first in Japan on December 14, 1996, and in North America and Europe in 1997.  In January 2007, "Mario Kart 64" was released as a downloadable Virtual Console title on the Wii, and in December 2016 it was also made available on the Wii U.

Question: Which documentary was released first, Tintin and I or Racing Extinction?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "documentaries_compared": {
      "type": "array",
      "items": {
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
      }
    },
    "earliest_released_documentary_title": {
      "type": "string"
    },
    "earliest_release_year": {
      "type": "integer"
    }
  },
  "required": [
    "documentaries_compared",
    "earliest_released_documentary_title",
    "earliest_release_year"
  ],
  "additionalProperties": false
}
