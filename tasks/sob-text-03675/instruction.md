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
Wasa Wasa: Wasa Wasa is the debut album by the psychedelic rock band Edgar Broughton Band.  The album was originally released as "Harvest SHVL 757" in July 1969 and was produced by Peter Jenner.  The 2004 CD reissue contained 5 previously unreleased bonus tracks, 4 of them being demos recorded by the band when they were a blues outfit called "The Edgar Broughton Blues Band".  These tracks feature guitarist Victor Unitt, who left the band when they started to go into psychedelic rock, stating the members of the band to be "sell-outs".  The last bonus track being a jamming session which was recorded on 21 January 1969, which was discovered when remastering the album.

Drill Your Own Hole: Drill Your Own Hole is the debut album by British grebo and psychedelic rock band Gaye Bykers on Acid, released in 1987 on Virgin Records, becoming their first release for the label after signing to them in late 1986.  After building up momentum through a couple of EPs in 1986, the band recorded "Drill Your Own Hole" with producer Alex Fergusson, mostly in South London.  Seven of the songs on the album were also featured in an accompanying film, also called "Drill Your Own Hole", that the band released alongside the album.  The film was a parody of themselves and the music industry.

H. P. Lovecraft II: H. P. Lovecraft II is the second album by the American psychedelic rock band H. P. Lovecraft and was released in September 1968 on Philips Records.  As with their debut LP, the album again saw the band blending psychedelic and folk rock influences, albeit with a greater emphasis on psychedelia than on their previous album release.  "H. P. Lovecraft II" failed to sell in sufficient quantities to reach the "Billboard" Top LPs chart or the UK Albums Chart, despite the band being a popular act on the U.S. psychedelic concert circuit.  Legend has it that the album was the first major label release to have been recorded by musicians who were all under the influence of LSD.

Bar Harbor, Maine: Bar Harbor is a town on Mount Desert Island in Hancock County, Maine, United States.  As of the 2010 census, its population is 5,235.  Bar Harbor is a popular tourist destination in the Down East region of Maine and home to the College of the Atlantic, Jackson Laboratory, and MDI Biological Laboratory (Salisbury Cove village).  Prior to a catastrophic 1947 fire, the town was a famous summer colony for the super-affluent elite.  Bar Harbor is home to the largest parts of Acadia National Park, including Cadillac Mountain, the highest point within twenty-five miles (40 km) of the coastline of the Eastern United States.  The town is served by the Hancock County-Bar Harbor Airport, which has flights on Cape Air and PenAir to Boston, as well as seasonal flights to Newark and Portland, ME on Elite Airways.

Ya Ho Wha 13: Founded in 1973 in the Los Angeles area, Ya Ho Wha 13, otherwise known as Ya Ho Wa 13 or Yahowha 13, is a psychedelic rock band fronted by Father Yod, spiritual leader of a religious cult/commune called the Source Family.  Ya Ho Wha without the vowels and spaces reduces to YHWH, the tetragrammaton.  The band recorded nine LPs full of their extreme psychedelic sound with tribal drums and distorted guitars, some of which were completely unrehearsed jam sessions, others which contained more conventional rock songs.

Apple (band): Apple were a British psychedelic rock band.  The band was founded in Cardiff in 1968 by Rob Ingram on guitar and Jeff Harrad on bass.  They released a single LP in 1969, titled "An Apple a Day".  The album was a commercial failure, and the band ceased to exist shortly after its release.  However, during the subsequent years several tracks from the LP, most notably "The Otherside" by Harrad, were dubbed classics of British psychedelic rock by critics, making "An Apple a Day" one of the most sought-after British psychedelic rarities.

The Amazing Charlatans: The Amazing Charlatans is a compilation album by the American psychedelic rock band The Charlatans that was released in 1996 by Big Beat Records.  The album is a collection of demos, tracks that appeared on singles, and previously unreleased sessions that the band recorded between August 1965 and early 1968, at a variety of different San Francisco studios.

Nice Dreams (album): Nice Dreams is the second album by psychedelic rock band Coke Weed.  It was released on April 17, 2012.  It was recorded in Bar Harbor, Maine and produced by Nick Stumpf.

Join the Dots (Toy album): Join the Dots is the second studio album by British psychedelic rock band TOY, released on 9 December 2013 in Europe and the UK (17 December, USA) through Heavenly Recordings.  The band recorded the album with Dan Carey, who also produced their debut album, and it took twice as long as their first album to record and master.  The first single to be released from the album was "Join the Dots", released in October, 2013, as a download and limited hand-stamped seven-inch vinyl.  A limited edition of the album included the EP "Join the Dubs" containing five Dub remixes.

Thank God for Mental Illness: Thank God for Mental Illness is the fifth studio album by American psychedelic rock band The Brian Jonestown Massacre.  After releasing "Take It from the Man! " and "Their Satanic Majesties' Second Request" in mid-1996, both of which display influences from 1960s psychedelic music, departing from the band's earlier shoegaze sound, the band recorded "Thank God for Mental Illness" through "tangible custom lo-fi stereo" in their San Francisco home studio on July 11, 1996 with the budget of $17.36.

Question: What psychedelic rock band recorded their second album in the town that is home to Cadillac Mountain?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the psychedelic rock band."
    },
    "album_details": {
      "type": "object",
      "properties": {
        "album_title": {
          "type": "string",
          "description": "The title of the band's second album."
        },
        "album_number": {
          "type": "integer",
          "description": "The sequential number of the album in the band's discography."
        }
      },
      "required": [
        "album_title",
        "album_number"
      ],
      "additionalProperties": false
    },
    "recording_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the album was recorded."
        },
        "state": {
          "type": "string",
          "description": "The state where the album was recorded."
        },
        "is_home_to_cadillac_mountain": {
          "type": "boolean",
          "description": "Indicates if the recording location is home to Cadillac Mountain."
        }
      },
      "required": [
        "city",
        "state",
        "is_home_to_cadillac_mountain"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band_name",
    "album_details",
    "recording_location"
  ],
  "additionalProperties": false
}
