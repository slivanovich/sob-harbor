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
Black Cowboy, Wild Horses: A True Story: Black Cowboy, Wild Horses: A True Story is a 1998 children's picture book by Julius Lester and illustrator Jerry Pinkney.  It is about an ex-slave and cowboy, Bob Lemmons, who, by himself, wrangles a herd of wild horses to a corral.

Wild Horses (Birdy song): "Wild Horses" is a song by English recording artist Birdy.  It was released as a digital download on 11 March 2016 in the United Kingdom, as the second single from her third studio album, "Beautiful Lies" (2016).  The song was written by Birdy and John McDaid and produced by TMS and Phil Cook.

Free-roaming horse management in North America: Management of free-roaming feral and semi-feral horses, (colloquially called "wild") on various public lands in North America is accomplished under the authority of law, either by the government of jurisdiction or efforts of private groups.  In western Canada, management is a provincial matter, with several associations and societies helping to manage wild horses in British Columbia and Alberta.  In Nova Scotia and various locations in the United States, management is under the jurisdiction of various federal agencies.  The largest population of free-roaming horses are found in the Western United States, where most of them are protected under the Wild Free-Roaming Horses and Burros Act of 1971 (WFRH&BA), and their management is primarily undertaken by the Bureau of Land Management (BLM), but also by the U. S. Forest Service (USFS)

Wild Horses (Wild Horses album): Wild Horses is the debut studio album by the British rock band, Wild Horses, co-produced with Trevor Rabin at Konk Studios in London, and released on 14 April 1980 on EMI Records.  It peaked at No. 38, and spent four weeks in the UK Albums Chart.

Mustang: The mustang is a free-roaming horse of the American west that first descended from horses brought to the Americas by the Spanish.  Mustangs are often referred to as wild horses, but because they are descended from once-domesticated horses, they are properly defined as feral horses.  The original mustangs were Colonial Spanish horses, but many other breeds and types of horses contributed to the modern mustang, resulting in varying phenotypes.  In the 21st century, mustang herds vary in the degree to which they can be traced to original Iberian horses.  Some contain a greater genetic mixture of ranch stock and more recent breed releases, while others are relatively unchanged from the original Iberian stock, most strongly represented in the most isolated populations.

Horse: The horse ("Equus ferus caballus") is one of two extant subspecies of "Equus ferus".  It is an odd-toed ungulate mammal belonging to the taxonomic family Equidae.  The horse has evolved over the past 45 to 55 million years from a small multi-toed creature, "Eohippus", into the large, single-toed animal of today.  Humans began to domesticate horses around 4000 BC, and their domestication is believed to have been widespread by 3000 BC.  Horses in the subspecies "caballus" are domesticated, although some domesticated populations live in the wild as feral horses.  These feral populations are not true wild horses, as this term is used to describe horses that have never been domesticated, such as the endangered Przewalski's horse, a separate subspecies, and the only remaining true wild horse.  There is an extensive, specialized vocabulary used to describe equine-related concepts, covering everything from anatomy to life stages, size, colors, markings, breeds, locomotion, and behavior.

Johnny McDaid: John "Johnny" McDaid (born 24 July 1976) is a Northern Irish singer, songwriter, musician and record producer from Derry.

Corolla Wild Horses Protection Act: The Corolla Wild Horses Protection Act ( ) is a bill that was introduced into the 113th United States Congress, where it passed the United States House of Representatives.  The bill would affect wild horses living in North Carolina.

Feral horse: A feral horse is a free-roaming horse of domesticated ancestry.  As such, a feral horse is not a wild animal in the sense of an animal without domesticated ancestors.  However, some populations of feral horses are managed as wildlife, and these horses often are popularly called "wild" horses.  Feral horses are descended from domestic horses that strayed, escaped, or were deliberately released into the wild and remained to survive and reproduce there.  Away from humans, over time, these animals' patterns of behavior revert to behavior more closely resembling that of wild horses.  Some horses that live in a feral condition but may be occasionally handled or managed by humans, particularly if privately owned, are referred to as "semi-feral".

Georgia Bruce: Georgia Bruce (born 7 May 1981) is an expert in equine behavior and psychology.  She specializes in the positive reinforcement based training method known as "Clicker Training".  Bruce has written two books about clicker training horses and has also produced a DVD training series on equine clicker training.  Bruce gives lessons, clinics, trick shows and clicker training demonstrations around Australia.  Her broad repertoire of horse training skills includes training trick horses, liberty horses, wild horses, starting young horses and retraining problem horses.  Bruce also has extensive experience training horses for high level performance in both dressage and reining.

Question: The song "Wild Horses" was written by Birdy and a songwriter from what city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "primary_artist_name": {
      "type": "string",
      "description": "The name of the primary recording artist for the song."
    },
    "song_writer_details": {
      "type": "array",
      "description": "Details about the individuals who wrote the song.",
      "items": {
        "type": "object",
        "properties": {
          "writer_name": {
            "type": "string",
            "description": "The name of the songwriter."
          },
          "writer_role": {
            "type": "string",
            "description": "The role of the individual in writing the song (e.g., 'writer', 'co-writer')."
          },
          "writer_origin_city": {
            "type": "string",
            "description": "The city of origin for the songwriter, if specified."
          },
          "writer_origin_country": {
            "type": "string",
            "description": "The country of origin for the songwriter, if specified."
          }
        },
        "required": [
          "writer_name",
          "writer_role"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "song_title",
    "primary_artist_name",
    "song_writer_details"
  ],
  "additionalProperties": false
}
