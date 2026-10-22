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
Burning the Process: Burning the Process is the major label debut album of alternative metal band Pressure 4-5, released on Dreamworks Records in 2001.  It features 11 tracks, three of which ("These Hands," "Beat the World," and "Even Worse") were featured on a prior three-song sampler release and were re-recorded for this album.  This would prove to be Pressure 4-5's first and only major label album, as the group disbanded in 2002.

Daniel Lopatin discography: Daniel Lopatin is a Brooklyn-based experimental musician who records primarily under the pseudonym Oneohtrix Point Never.  Early in his career as both a solo artist and as a member in several groups, he released a number of LPs and extended plays on a variety of independent labels.  In 2010, he signed to Editions Mego and released his major label debut "Returnal".  In 2011, he founded the record label Software.  In 2013, Lopatin signed to British electronic label Warp Records and released his label debut "R Plus Seven".

When It's Dark Out: When It's Dark Out is the third studio album by American rapper G-Eazy.  It was first made available for a pre-order on iTunes on November 27, 2015.  It was released on December 4, 2015, by RCA Records.  Recording sessions took place during 2014 to 2015, with G-Eazy himself, alongside his frequent collaborator Christoph Andersson, and record producer Southside were serving as the executive producers on the album.  The album features guest appearances from rappers E-40 and Big Sean, alongside recording artists Kehlani and Grace, while the production was provided by OZ, DJ Spinz, Boi-1da and Michael Keenan, among others.

Hero (Maren Morris album): Hero is the major label debut studio album by American singer Maren Morris, released on June 3, 2016, through Columbia Nashville.  It marks Morris' first release on a major label and her fourth overall.  The album debuted and peaked at number five on the "Billboard" 200 chart and was nominated for Best Country Album at the 59th Annual Grammy Awards.  It received mostly positive reviews from music critics and is considered by many publications as one of 2016's best albums.

Lotta That: "Lotta That" is a song by American rapper G-Eazy.  It was released on June 10, 2014, as the sixth single from his third studio album "These Things Happen" (2014).  The song was produced by Eazy himself and Christoph Andersson.  It also features guest appearances from American rapper ASAP Ferg and English rapper Danny Seth.

These Things Happen (G-Eazy album): These Things Happen is the second studio album by American rapper G-Eazy.  It was released on June 23, 2014, by RCA Records, serving as his first major-label debut with these affiliated record labels BPG and RVG.  It was released in North America, and released it on July 21, 2014, in the United Kingdom.  Recording sessions took place from 2013 to 2014, with the production on the album that primarily were handled by Christoph Andersson, Jay Ant, Blackbear, Jordan Evans and Matthew Burnett, among others.  Following the release, he began to embark his These Things Happen Tour, for the support of this album.

Foxy Shazam: Foxy Shazam is an American rock band from Cincinnati, Ohio (composed of lead vocalist Eric Nally, guitarist Loren Turner, pianist Sky White, bassist Daisy Caplan, trumpeter and back-up vocalist Alex Nauth, and drummer Aaron McVeigh).  They were formed in 2004.  The band released their debut album "The Flamingo Trigger" independently before signing with Ferret Music, under which they recorded their second album, "Introducing".  The following year, the band recorded its first major label record with producer John Feldmann.  Foxy Shazam signed with Sire Records and released its self-titled major label debut in 2010.  The band's fourth studio album, "The Church of Rock and Roll", was released in January 2012. " Gonzo", the band's fifth album, was released April 2, 2014.  They announced in October 2014 they were disbanding for an unknown length of time.

Skizzy Mars: Myles Mills (born June 8, 1993), better known by his stage name Skizzy Mars, is an American rapper, songwriter, and record producer from Harlem, New York.

Me, Myself &amp; I (G-Eazy and Bebe Rexha song): "Me, Myself & I" is a song by American rapper G-Eazy and American singer Bebe Rexha, billed together as "G-Eazy x Bebe Rexha".  It was released on October 14, 2015, as the first single for his second studio album "When It's Dark Out".  "Me, Myself & I" was written by Bebe Rexha, G-Eazy, Lauren Christy, TMS and Michael Keenan.  The song was originally produced by Bebe Rexha and TMS and re-produced by Michael Keenan, with additional production by Christoph Andersson and G-Eazy.  It is so far the highest-charting single for both G-Eazy and Bebe Rexha, peaking at number 7 on the US "Billboard" Hot 100.  It is featured in the "NBA 2K17" soundtrack.

Christoph Andersson: Christoph Reiner Andersson, also known by his stage name Monopol, is an American DJ and record producer based in New Orleans and Los Angeles.  He is best known for working with G-Eazy, and co-writing and producing for his two albums (including singles "Me, Myself & I", "Drifting", "I Mean It", "Let's Get Lost", and "Tumblr Girls"), Skizzy Mars, Devon Baldwin, and 90 Pounds of Pete.

Question: Christoph Andersson, collaborator of Skizzy Mars and Devon Baldwin, produced G Eazy's major label debut known as what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist whose album is being discussed."
    },
    "album_title": {
      "type": "string",
      "description": "The title of the album."
    },
    "album_type": {
      "type": "string",
      "description": "The type of album, e.g., 'major label debut'."
    },
    "producer_details": {
      "type": "object",
      "properties": {
        "producer_name": {
          "type": "string",
          "description": "The name of the producer."
        },
        "collaborated_with_other_artists": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other artists the producer is known for collaborating with."
        }
      },
      "required": [
        "producer_name"
      ],
      "additionalProperties": false
    },
    "record_label": {
      "type": "string",
      "description": "The record label that released the album."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the album was released."
    }
  },
  "required": [
    "artist_name",
    "album_title",
    "album_type",
    "producer_details",
    "record_label",
    "release_year"
  ],
  "additionalProperties": false
}
