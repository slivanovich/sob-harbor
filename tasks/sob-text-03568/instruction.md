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
Phil Spector: Phillip Harvey Spector (born Harvey Phillip Spector, December 26, 1939) is an American record producer, musician, and songwriter who developed the Wall of Sound, a music production formula he described as a "Wagnerian" approach to rock and roll.  Spector is considered the first auteur among musical artists for acting not only as a producer, but also the creative director, writing or choosing the material, and masterminding all phases of the recording process.  Additionally, Spector helped engender the idea of the studio as its own distinct instrument.  For these contributions, he is acknowledged as one of the most influential figures in pop music history.  Later in his life, Spector became notorious for his solitary lifestyle and eccentric personality, which was brought to wider notice during the media coverage surrounding his trials and conviction for murder in the 2000s.

Silence Is Easy: Silence Is Easy is the second studio album by English indie rock group Starsailor, released in September 2003 on EMI.  The album cover is loosely based on Echo & the Bunnymen's "Heaven Up Here".  The song "Some of Us" was featured in an episode of "Bones" entitled A Boy in a Bush and in the closing credits of the Belgian film "The Memory of a Killer" (a.k.a. "The Alzheimer Case").  The album contains some of the last productions by Phil Spector ("Silence Is Easy" and "White Dove").  The album sold 54,296 copies on its opening week of release, charting at No.2 in the UK album charts.  It was certified gold in the UK in 2003.

Spirit of Purity: Spirit of Purity is the debut album by the Swedish Christian black metal band Sanctifica, released on Little Rose Productions and Rivel Records in March 2000.  With this album the band established itself as one of the leading Christian black metal bands of the early 2000s (decade), representing technical and chaotic style.  Considered by many as the band's best album, "Spirit of Purity" was well received by both the press and fans, although the style quickly earned Sanctifica their "Emperor clone" label, which the band later tried to escape by switching the music style.  Music videos were shot for the songs "The Dark Desires" and "Spirit of Purity," released on the video compilation "Power from the Sky".

Celle massacre: The Celle massacre (euphemistically called ""Celler Hasenjagd"", "hare chase of Celle") was a massacre of concentration camp inmates that took place in Celle, Prussian Hanover, in the last weeks of the Second World War.  On 8 April, 1945 over 3,000 concentration camp internees were killed in an Allied air raid and subsequent attacks by SS guards, Gestapo, and Nazi party officials, as well as members of the public.  Some of the perpetrators of the massacre were later tried but all of those convicted for the crime were set free in the early 1950s.

Ocean Colour Scene Anthology: Ocean Colour Scene Anthology is a 2003 album by Ocean Colour Scene (OCS), the 3-CD and 50-track album contains all of their hits, selected highlights of their B-sides combined with some new tracks.  Both OCS and their manager Chris Cradock were not happy about this album's release, believing their old label were "cashing in on the fanbase".  The third disc contains a cover of The Who's early single "Anyway, Anyhow, Anywhere".  The Anthology charted at #75 in the UK album charts.

Wake Pig: Wake Pig is 3's third studio album.  It was released on October 26, 2004 by Planet Noise Records.  It was re-released on November 1, 2005 by Metal Blade Records.  The album contains tracks that were previously featured on the band's 2003 album, Summercamp Nightmare.

Darts (album): Darts is a 2003 album from the Benevento/Russo Duo.  Made up of only Marco Benevento and Joe Russo, the album contains the two playing only keyboards and drums, respectively.  It was recorded live at the Knitting Factory and the Tribeca Rock Club, both venues in New York City.

Freda': Freda' (Swedish for Friday) is a pop group from Gnosjö in Sweden, first active from 1983-1993.  Singer and songwriter Uno Svenningsson later tried with a solo career, before the band was re-united in 2009.  The name comes from that they won a rock band competition on a Friday.  The group, which broke through in 1986 with the song "Vindarna", received a Grammis Award in 1988. , and again in 1990.

Hope (Harem Scarem album): Hope is a 2008 album by the Canadian hard rock band Harem Scarem.  This was supposed to be the band's twelfth and final studio album, before returning in 2013 with Mood Swings II.  The European version of the album contains an acoustic version of "Higher", which was originally from their 2003 album of the same name.

Isabella Braña: Isabella Braña is a fictional character from the American CBS Daytime soap opera "The Young and the Restless".  She was portrayed by Eva Longoria, created by Kay Alden and introduced by former executive producer Edward J. Scott on March 8, 2001.  During her run, the character gave birth to Paul Williams' (Doug Davidson) son and later tried to kill his ex-wife, Christine Blair (Lauralee Bell).  Described as "crazy", "evil" and a "whack job", Longoria said the character was a challenge to portray.  The actress was let go and Longoria last aired on August 15, 2003.

Question: What rock group's 2003 album contains some of the last productions by a record producer later tried and convicted of murder?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "rock_group_name": {
      "type": "string",
      "description": "The name of the rock group."
    },
    "album": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the album."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the album was released."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    },
    "producer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the record producer."
        },
        "notable_event": {
          "type": "string",
          "description": "The significant event that made the producer notorious."
        },
        "produced_tracks_on_album": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of tracks on the album produced by this producer."
        }
      },
      "required": [
        "name",
        "notable_event",
        "produced_tracks_on_album"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "rock_group_name",
    "album",
    "producer"
  ],
  "additionalProperties": false
}
