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
Rev (Ultra Vivid Scene album): Rev is the third album by Ultra Vivid Scene, released in 1992.  The single "Blood and Thunder" reached number 27 on the "Billboard" Modern Rock Tracks chart.

Crash (UK band): Crash were an indie rock band formed in 1984 in New York City, centered on frontman-songwriter Mark Dumais, who took their name from the J. G. Ballard novel.  The band moved to London in 1987.  Crash released three singles and an album, but are perhaps most notable for containing members who went on to form Ultra Vivid Scene, John Moore's Expressway, and Something Pretty Beautiful.

Ultra Series: The Ultra Series (ウルトラシリーズ , Urutora Shirīzu ) is the collective name for all the shows produced by Tsuburaya Productions featuring Ultraman, his many brethren, and the myriad Ultra Monsters.  The Ultra Series is one of the prominent tokusatsu superhero genre productions from Japan, along with Toei produced series "Kamen Rider", "Super Sentai" and the "Metal Heroes".  The Ultra franchise is also one of the most well known examples of the "daikaiju" (大怪獣, "huge monster") genre, which also includes Toho's "Godzilla" series, and Daiei Film's "Gamera" series.  However, the Ultra Series also falls into the "kyodai hīro" (巨大ヒーロー, "giant hero") subgenre of tokusatsu shows.

Joy 1967–1990: Joy 1967–1990 is the second album by Ultra Vivid Scene, released in 1990.

Idlewild (They Might Be Giants album): Idlewild is a compilation album by the alternative rock band They Might Be Giants.  It was released in 2014, and is the third anthology released by the group through its own Idlewild Recordings.  The album includes songs previously released between 1999's "Long Tall Weekend" and 2013's "Nanobots".  The press release for the album notes it is "neither a 'best of' nor a 'rarities' set, it is an ultra – vivid illustration of the bands prodigious output and singular musical vision."

Kurt Ralske: Kurt Ralske is an American visual artist and musician.  He is the former singer and guitarist in alternative rock band Ultra Vivid Scene.

Warpaint (band): Warpaint is an American indie rock band from Los Angeles, California, formed in 2004.  The current lineup comprises founders Emily Kokal (vocals, guitar), Theresa Wayman (guitar, vocals) and Jenny Lee Lindberg (bass, vocals), and Stella Mozgawa (drums), who joined the band in 2009.

Ultra Vivid Scene (album): Ultra Vivid Scene is the debut album by Ultra Vivid Scene, released in 1988.  Kurt Ralske was the writer, producer, and sole performer.

Ultra Vivid Scene: Ultra Vivid Scene was an American alternative rock band, started by Kurt Ralske.

Knox Chandler: Knox Chandler is a session guitarist and cellist.  In the early to mid-1970s, Chandler attended the Hammonasset School and Bard College in the late 1970s.  He has worked with such acts as Depeche Mode (he also collaborated with Dave Gahan on his solo album "Paper Monsters"), Lori Carson, The Golden Palominos, the Psychedelic Furs, Ultra Vivid Scene, Maggie Estep, the Creatures and R.E.M..  He was also the touring guitarist for Siouxsie and the Banshees' 2002 "Seven Year Itch" tour and toured with Cyndi Lauper and Lou Reed.

Question: Ultra Vivid Scene and Warpaint are bands in what genre?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "bands_queried": {
      "type": "array",
      "description": "Information about each band mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "specific_genre": {
            "type": "string",
            "description": "The specific genre of the band as mentioned in the context."
          }
        },
        "required": [
          "band_name",
          "specific_genre"
        ],
        "additionalProperties": false
      }
    },
    "number_of_bands": {
      "type": "integer",
      "description": "The total number of bands for which the genre was queried."
    },
    "common_genre_category": {
      "type": "string",
      "description": "The overarching genre category that encompasses all specific genres of the queried bands."
    }
  },
  "required": [
    "bands_queried",
    "number_of_bands",
    "common_genre_category"
  ],
  "additionalProperties": false
}
