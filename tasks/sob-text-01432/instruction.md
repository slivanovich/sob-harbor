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
Black (Pearl Jam song): "Black" is a power ballad by the American rock band Pearl Jam.  The song is the fifth track on the band's debut album, "Ten" (1991).  Featuring lyrics written by vocalist Eddie Vedder and music written by guitarist Stone Gossard, "Black" is said to be about first relationships, though Vedder showed strong emotion while performing the song live in early years.  (In relationship with Beth Liebling from 1983-2000) Notably, Vedder now renders the added lyric "We belong together" as "I've been healed" or "We didn't belong together" indicating his moving on from the relationship and being content with how it ended.

We Belong Together (campaign): The We Belong Together Campaign is anchored by the National Domestic Workers Alliance and the Asian Pacific American Women's Forum along with other groups throughout the United States.  We Belong Together is an initiative that is taking place all over the United States, which seeks to brings women from across the nation to bring attention to immigration laws that impact women and also gather women together to fight for immigration reform.  This campaign was formed to address issues that are not taking into account the experiences of women, who make up the majority of the immigrant population in the United States.  The campaign offers a gender based analysis and focuses on the importance of maintaining nuclear families together.

You Belong to Me (ASV/Living Era): You Belong to Me is a 2004 compilation album of songs recorded by American singer Jo Stafford.  It is one of many Stafford compilations to have been released in the early 2000s under the title "You Belong to Me", the name derived from the song of the same name which became one of her best known hits during the 1950s.  This album was released on June 29, 2004 and appears on the ASV and Living Era labels.

Malegaon Ka Chintu: Malegaon Ka Chintu is an Indian silent comedy series which premiered on SAB TV on August 6, 2010.  The series is produced by Deepti Bhatnagar, and the story revolves around a character named Chintu.  The second season of the silent comedy in 2012, named Chintu Ban Gaya Gentleman, takes the eventful life of Chintu from the villages of Malegaon straight to exotic locales around the globe

69 Sexy Things 2 Do Before You Die: 69 Sexy Things 2 Do Before You Die (stylized 69 Sexy Things 2 Do B4U Die) was a Playboy TV adult newsmagazine profiling exotic locales, outdoor adventures and current erotic trends.

You Belong to Me (1952 song): "You Belong to Me" is a romantic pop music ballad from the 1950s.  The singer reminds his or her beloved love interest, soulmate, or sweetheart that whatever exotic locales and sights he/she experiences, "you belong to me" no matter what happens.

We Belong Together: "We Belong Together" is a song by American singer Mariah Carey from her tenth studio album, "The Emancipation of Mimi" (2005).  The song was released on March 29, 2005, through Island Records, as the second single from the album.  "We Belong Together" was written by Carey, Jermaine Dupri, Manuel Seal, and Johntá Austin, and produced by the former three.  As the song samples lyrics from Bobby Womack's "If You Think You're Lonely Now" (1981) and the Deele's "Two Occasions" (1987), several other songwriters are credited.  "We Belong Together" is built on a simple piano arrangement with an understated backbeat.  The lyrics chronicle a woman's desperation for her former lover to return.

Big Bang (2006 album): "Bigbang" or "We Belong Together", also referred to as "First Single" is the first single by the South Korean hip-hop boy band Big Bang.  It was released by the YG Entertainment label and remained in the charts for eight months.  The band's members – G-Dragon, Taeyang, Seungri, Daesung, and T.O.P – composed it.  Band leader G-Dragon composed the principal track "We Belong Together"; he and T.O.P. wrote the lyrics.  It presents a rhythmic up-tempo tune with rap passages.  The song "This Love" is a remake of the song of the same name by Maroon 5.

Eleanor Mercein Kelly: Eleanor Mercein Kelly (August 30, 1880 - October 11, 1968) was an American writer of fiction and nonfiction.  She wrote one biographical study, "The Chronicle of a Happy Woman: Emily A. Davison" (1928), but is best known for her romantic fiction, most of which was set in exotic locales.  She was widely traveled, and used her travels as inspiration for her novels.

Nostalgia 1907: Nostalgia 1907 (ノスタルジア１９０７ ) is a Sharp X68000, Sega Mega-CD, NEC PC-9801, and FM Towns adventure video game set in the year 1907.  During this time known as either the Edwardian era or the "Age of Men," the player must explore the exotic locales of that era (including the North Atlantic Ocean) and follow along with the story.  Drinking alcoholic beverages is considered to be part of the cut scene (as two men are drinking wine).  All the text in the game is in Japanese; literacy skills are required in order to play the game.

Question: What singer sang a song about her sweetheart that regardless of exotic locales and sights they belong together?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "singer_name": {
      "type": "string",
      "description": "The name of the singer."
    },
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "song_theme_elements": {
      "type": "array",
      "description": "Key elements or themes from the song's lyrics or description.",
      "items": {
        "type": "string"
      }
    },
    "release_era": {
      "type": "string",
      "description": "The era or decade when the song was a hit."
    }
  },
  "required": [
    "singer_name",
    "song_title",
    "song_theme_elements",
    "release_era"
  ],
  "additionalProperties": false
}
