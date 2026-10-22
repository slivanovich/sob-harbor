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
Kevin Talley: Kevin Talley (born May 21, 1978) is an American heavy metal drummer for Dååth, Feared, Sylencer and Nothnegal.  He is the former drummer for Dying Fetus, Misery Index, Six Feet Under, Chimaira and Suffocation.  In addition, he was the touring drummer for Battlecross in 2013.

Misery Index (band): Misery Index is an American death metal band formed in 2001 in Baltimore, Maryland, United States, by Jason Netherton (vocals and bass guitar), Mike Harrison (vocals and guitar), and Kevin Talley (drums).  From 2006–2010, its line-up consisted of Netherton on vocals and bass guitar, Sparky Voyles on guitar, Mark Kloeppel on vocals and guitar, and Adam Jarvis on drums.  In 2010, Voyles left the band and was replaced by Darin Morris.

Suffocation (band): Suffocation is an American death metal band that was formed in 1990 in Centereach, Long Island, New York, United States.  The band comprises vocalist Frank Mullen, lead guitarist Terrance Hobbs, bassist Derek Boyer, rhythm guitarist Charlie Errigo, and drummer Eric Morotti.  Suffocation rose to prominence of death metal and created a blueprint for the genre for the 1990s with their 1991 debut album "Effigy of the Forgotten", and have released seven studio albums since formation.  The band's raw death metal style uses growled vocals with a downtuned guitar sound, fast and complex guitar riffs and drumming, open chord notes, breakdowns, and a sophisticated sense of songwriting.

Mike Smith (drummer): Mike Smith (born July 16, 1971 in Bronx, New York) is an American multi-instrumentalist, best known as the former drummer of the prominent New York-based technical death metal band Suffocation.  He performed on their 1990 demo "Reincremated", the 1991 EP, "Human Waste", their 1991 debut album "Effigy of the Forgotten", and their 1993 album "Breeding the Spawn".  He then departed from the band and was subsequently replaced by drummer Doug Bohn.  He returned when Suffocation reformed in 2002 after a four-year hiatus and performed on their 2004 release, "Souls to Deny", their 2006 self-titled album, and 2009's Blood Oath.  Smith left Suffocation for the second time in February 2012.

Blood Oath (album): Blood Oath is the sixth studio album by American death metal band Suffocation.  The band began recording in-studio on January 31 with Joe Cincotta (who worked on the band's last two releases).  The follow-up to 2006's self-titled record "Suffocation" was mixed by Zack Ohren and the cover artwork was once again designed by Jon Zig.  It is the band's last album to feature original drummer Mike Smith in full.  The track "Marital Decimation" is a re-recording of a track of the same name from the "Breeding the Spawn" album.

Pinnacle of Bedlam: Pinnacle of Bedlam is the seventh studio album by American death metal band Suffocation.  It is the band's first full-length record since "Pierced from Within" to not feature Mike Smith (although he makes a guest appearance on the final track), instead the album features returning drummer Dave Culross, making this his only full-length record with Suffocation and his first release overall with the band since 1998's "Despise the Sun".  Track 10, 'Beginning of Sorrow', is a re-recording of the track of the same name from the album "Breeding the Spawn".  It is also the band's last album with longtime guitarist Guy Marchais.

Terrance Hobbs: Terrance Hobbs (born April 6, 1970) is the lead guitarist in the American death metal band Suffocation.  Hobbs has been a constant member in the band since their first released title "Reincremated" along with band mates Frank Mullen and Mike Smith, who all met in high school.  Hobbs also played in the death metal project, Criminal Element, which featured fellow bassist" Derek Boyer".

Frank Mullen: Frank Mullen, (born January 1970) is the vocalist of the American death metal band Suffocation, and met band mates Terrance Hobbs and Mike Smith in high school.  He is recognized to be among the first to bring low-pitched vocals in death metal.  His approach on "Effigy of the Forgotten" could be considered to be the "blueprint" to the death growls as we know it today.  Unlike some death metal vocalists, his lyrics are pronounced more clearly.  He achieves this by simply opening his mouth wider, but still retaining his low-pitched growls.

Undead (Six Feet Under album): Undead is the ninth studio album by American death metal band Six Feet Under.  It is their first album to feature drummer Kevin Talley and guitarist Rob Arnold.

George Fisher (musician): George "Corpsegrinder" Fisher (born July 8, 1969) is an American extreme metal vocalist for the American death metal band Cannibal Corpse, the lesser-known melodic death metal band Paths of Possession, and the lesser-known extreme metal supergroup Serpentine Dominion.  He recorded two albums with Florida's Monstrosity before leaving and joining Cannibal Corpse in late 1995, replacing vocalist Chris Barnes, who is now the vocalist for Six Feet Under.  He also provided guest vocals for New York technical death metal band Suffocation on the songs "Reincremation" and "Mass Obliteration" from their debut album, "Effigy of the Forgotten", as well as guest vocals for California deathcore band Suicide Silence on the song "Control" from their fourth album, "You Can't Stop Me".  Fisher also performed guest vocals on Job for a Cowboy's 2014 album "Sun Eater" on the song "The Synthetic Sea."  As a death metal vocalist, Fisher employs the "death growl" extended vocal technique.

Question: Kevin Talley, former drummer for the American death metal band Suffocation, now drums for what band?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "drummer_name": {
      "type": "string",
      "description": "The name of the drummer."
    },
    "former_bands": {
      "type": "array",
      "description": "A list of bands the drummer was formerly a member of.",
      "items": {
        "type": "string"
      }
    },
    "current_bands": {
      "type": "array",
      "description": "A list of bands the drummer currently plays for.",
      "items": {
        "type": "string"
      }
    },
    "is_heavy_metal_drummer": {
      "type": "boolean",
      "description": "Indicates if the drummer is described as a heavy metal drummer."
    }
  },
  "required": [
    "drummer_name",
    "former_bands",
    "current_bands",
    "is_heavy_metal_drummer"
  ],
  "additionalProperties": false
}
