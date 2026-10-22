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
Lonerism: Lonerism is the second studio album by the Australian rock band Tame Impala, released on 5 October 2012 by Modular Recordings.  Like the band's debut studio album, "Innerspeaker" (2010), "Lonerism" was written, recorded, performed, and produced by Kevin Parker, with live member Jay Watson contributing on two tracks.  Recorded mostly in Perth, Australia, and Paris, France, "Lonerism" builds on the psychedelic sound of its predecessor by featuring fewer guitars and more synthesisers and samples. Parker attempted to incorporate his love for pop music into his songwriting for the record through catchier melodies.  Many tracks feature ambient sounds recorded by Parker with a dictaphone.  The album's theme of isolation is reflected in the album cover, featuring an image of a fenced-off Jardin du Luxembourg in Paris.

Red (Symbion Project album): Red is the debut full-length album by Symbion Project, a.k.a. Kasson Crooker.  Released in 1997, "Red" contains a collection of songs conceived as early as 1992.  The mostly instrumental album includes a mixture of downtempo, techno, and ambient songs, and many tracks feature Middle Eastern overtones.  "Only Girls Like to Gossip" became the foundation for the future Splashdown song "Waterbead".

Revenge (XXXTentacion album): Revenge is a mixtape by American rapper XXXTentacion, released on May 16, 2017 by Empire Distribution.  It consists of 8 previously released songs that were available for streaming on XXXTentacion's SoundCloud.  It was preceded by the lead single "Look at Me", which peaked at number 34 on the US "Billboard" Hot 100.

Gospel (song): "Gospel" is a song by Indonesian rapper Rich Chigga, South Korean rapper Keith Ape, and American rapper XXXTentacion.  It was released on May 12, 2017, by 88rising and Empire Distribution.  The song was produced by Ronny J.

XXXTentacion discography: The discography of American rapper XXXTentacion consists of one studio album, one mixtape, four extended plays and six singles (including 2 as a featured artist).

Personal File: Personal File is the 92nd album by the late American music icon Johnny Cash.  The two CD set was released on May 23, 2006 on the Legacy label.  "Personal File" contains 49 unreleased tracks on 2 CDs recorded between 1973 and 1982.  Given that all tracks on the album were previously unreleased "Personal File" is considered both a posthumous album and a compilation.  Recovered from a vault of material housed at the House of Cash studios, "Personal File" includes "Tin Pan Alley hits, traditional folk and gospel tunes, new originals and favorite covers"  – by Carter Family, Louvin Brothers, Johnny Horton, John Prine, Rodney Crowell, and Carlene Carter.  The album was compiled and produced by Gregg Geller with liner notes by Greil Marcus.  On most of the tracks, Cash performs alone, accompanying himself on guitar, and on many tracks Cash prefaces the song with remarks about its history and what it means to him.

The Piece Talks: The Piece Talks is the debut LP by hip-hop group C.R.A.C., made up of rapper Blu and rapper-producer Ta'Raach.  C.R.A.C is an acronym standing for "Collect Respect Anna Check".  Though the duo initially released the project independently, Tres Records became interested and decided to release the album commercially on April 22, 2008.  Not purely a rap album, many tracks prominently feature singing and talking and are more like skits than full songs.

17 (XXXTentacion album): 17 is the debut studio album by American rapper XXXTentacion.  It was released on August 25, 2017 by Bad Vibes Forever and Empire Distribution.  It features 11 tracks and was supported by the lead single "Revenge."  "17" is X's second solo commercial project, succeeding the compilation mixtape "Revenge" (2017).  It includes a guest appearance from Trippie Redd and production from X himself, Nick Mira, Taz Taylor, Natra Average, and Potsu.  The album experiments with a variety of genres, such as emo, indie rock, and lo-fi.

Jocelyn Flores: "Jocelyn Flores" is a song by American rapper XXXTentacion from his album "17" (2017).  It was written by X and is produced by Potsu.

Look at Me (XXXTentacion song): "Look at Me" (stylized as "Look At Me!")  is the debut single by American rapper XXXTentacion.  The song premiered on December 30, 2015 on the SoundCloud account of Rojas, the song's co-producer, before initially being released for digital download as a single on January 29, 2016, becoming a sleeper hit after its initial release until January 2017, in which the single was later re-released for digital download again with a remastered and clean version of the single on February 20, 2017, by Empire Distribution.  The song serves as the lead single from his debut commercial mixtape "Revenge".  The track was produced by Rojas and Jimmy Duval and heavily samples the song "Changes" by British dubstep DJ and record producer Mala.

Question: How many tracks does this album by American rapper XXXTentacion that had the song "Jocelyn Flores" feature?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album by XXXTentacion."
    },
    "artist_name": {
      "type": "string",
      "description": "The artist of the album."
    },
    "song_featured": {
      "type": "string",
      "description": "The song that is featured on the album."
    },
    "number_of_tracks": {
      "type": "integer",
      "description": "The total number of tracks on the album."
    }
  },
  "required": [
    "album_name",
    "artist_name",
    "song_featured",
    "number_of_tracks"
  ],
  "additionalProperties": false
}
