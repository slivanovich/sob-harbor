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
Thank Me Later: Thank Me Later is the debut studio album by Canadian rapper and singer Drake.  It was released on June 15, 2010, by Aspire Music Group, Young Money Entertainment, Cash Money Records and Universal Motown Records.  Recording sessions took place at various recording studios from 2009 to 2010, including executive production from Drake himself, alongside Lil Wayne, Cortez Bryant and Gee Roberson.  The album was mostly produced by Drake's frequent collaborators such as 40 and Boi-1da; as well as its contributions from Timbaland and Swizz Beatz, among others.  The album features guest appearances from a female rapper and Young Money's label-mate Nicki Minaj, alongside other artists such as The-Dream and Kanye West, among others.

Controlla: "Controlla" is a song by Canadian rapper Drake, recorded for his studio album "Views".  The song was released as the fourth single from the album in the US on June 7, 2016.  The dancehall song was written by Drake, Matthew Samuels, Dwayne Chin-Quee, Stephen McGregor, Moses Davis, Donald Dennis, Gary Jackson, Patrick Roberts, Andrew Thomas, and produced by Boi-1da, Supa Dups, Di Genius, TheFinal1 and Allen Ritter.

BedRock: "BedRock" is the second single by hip hop group Young Money Entertainment from their debut collaboration album "We Are Young Money".  It is performed by Young Money artists Lil Wayne, Gudda Gudda, Nicki Minaj, Drake, Tyga, Jae Millz, and features R&B singer Lloyd.  It was released as a CD in the United Kingdom on March 22, 2010.  "BedRock" is featured as a bonus track on the Japanese and New Zealand editions of Nicki Minaj's debut studio album, "Pink Friday".

Pink Friday: Pink Friday is the debut studio album by Trinidadian-American recording artist Nicki Minaj, released on November 22, 2010, by Young Money, Cash Money and Universal Motown.  After signing a recording contract with Young Money Entertainment in 2009, Minaj began planning the album that same year and work continued into 2010.  Minaj enlisted a variety of producers whose efforts resulted in a primarily hip hop record, which sees additional influences from R&B and pop music.  The album features guest vocals from Eminem, Rihanna, Drake, will.i.am, Kanye West and Natasha Bedingfield.

Every Girl (Young Money song): "Every Girl" (album version titled "Every Girl in the World") is a song by rap group Young Money released as the 1st single from their debut collaboration album titled "We Are Young Money".  It was legally released to the iTunes Store on June 11, 2009.  Young Money Entertainment rappers Lil Wayne, Drake, Jae Millz, Gudda Gudda, and Mack Maine make appearances on the track.  The video was shot on February 13, 2009 and was released on April 6 of that same year.  The song was leaked to the internet on January 28, 2009, just two days after "Prom Queen" was officially released.

We Are Young Money: We Are Young Money is the first compilation album by American hip hop record label Young Money Entertainment, and released on December 21, 2009 by Young Money Entertainment and Cash Money Records.  The album garnered a positive reception but critics were divided on the quality of the label's choice of artists.  "We Are Young Money" debuted at number 9 on the "Billboard" 200 and spawned three singles: "Every Girl", "BedRock" and "Roger That".  The album was certified Gold by the Recording Industry Association of America for sales of over 500,000 copies in the United States.

Young Money: Rise of an Empire: Young Money: Rise of an Empire is the second compilation album by American record label Young Money Entertainment.  The album was released on March 11, 2014, by Young Money Entertainment, Cash Money Records and Republic Records.  "Rise of an Empire"' s recording process took place from 2013 to 2014.  It contains contributions from several Young Money recording artists including, Lil Wayne, Drake, Nicki Minaj, Tyga, Christina Milian, Shanell, Mack Maine, Jae Millz, Cory Gunz, Gudda Gudda, Lil Twist, Chanel West Coast and PJ Morton, among others.

Trophies (song): "Trophies" is a song by Canadian rapper Drake.  The song was produced by Hit-Boy, 40 and Hagler.  The song was originally meant for Drake's third studio album "Nothing Was the Same", however, it would be cut off the final track listing.  After Drake released the song for free in December 2013, it was then announced to be included on the Young Money Entertainment compilation "".  On February 27, 2014, it was released as the album's second official single and credited as Young Money featuring Drake.  It has peaked at number 50 on the US "Billboard" Hot 100 chart.

Views (album): Views is the fourth studio album by Canadian rapper and singer Drake.  It was released on April 29, 2016, by Young Money Entertainment, Cash Money Records and Republic Records.  Recording sessions took place from 2015 to 2016, with both Drake and his longtime collaborator and record producer 40 serving as the records executive producers.  40 also primarily handled the production on the album alongside each of these several other record producers such as Nineteen85, Maneesh Bidaye, Kanye West and Jordan Ullman, among others.  The album contains the elements of genres such as R&B, dancehall, hip hop and pop, among others.

If You're Reading This It's Too Late: If You're Reading This It's Too Late is the fourth mixtape by Canadian rapper Drake.  It was released through the iTunes Store without prior announcement on February 13, 2015, by Cash Money Records.  The physical edition of the project was released by Cash Money Records; as well as OVO Sound, Young Money Entertainment and Republic Records.  There is a debate upon whether this project is a mixtape or a studio album; although it was released commercially through his record label, Drake himself referred to the project as a mixtape.

Question: Controlla was recorded for what studio album that was the fourth by Drake, and was released on April 29, 2016 by Young Money Entertainment?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the studio album."
    },
    "artist": {
      "type": "string",
      "description": "The primary artist of the album."
    },
    "album_type": {
      "type": "string",
      "description": "The type of album, e.g., studio album."
    },
    "album_number": {
      "type": "integer",
      "description": "The sequential number of the album for the artist."
    },
    "release_date": {
      "type": "string",
      "description": "The release date of the album."
    },
    "record_labels": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of record labels that released the album."
    },
    "recorded_song": {
      "type": "string",
      "description": "The song that was recorded for this album."
    }
  },
  "required": [
    "album_name",
    "artist",
    "album_type",
    "album_number",
    "release_date",
    "record_labels",
    "recorded_song"
  ],
  "additionalProperties": false
}
