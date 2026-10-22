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
World of Our Own: World of Our Own is the third studio album by Irish boy band Westlife.  It was released through RCA Records on 12 November 2001.  It reached number one in the United Kingdom and includes the singles "Queen of My Heart" (which was a double A-side with "When You're Looking Like That"), "World of Our Own" (which was a double A-side with "Angel"), "Bop Bop Baby", and the final single from the group's last album, "Uptown Girl". " Evergreen" was later covered by Will Young as his winner's single for the 2002 "Pop Idol" competition.  It is the first album to have a title track.

Steeve Epesse-Titi: Steeve Gaston Epesse-Titi (born 5 July 1979) is a French former professional footballer who played as a defender.  He played in the Football League for Exeter City during the 2000–01 season.

Marco Bos: Marco Bos (born 5 July 1979 in Roden) is a former Dutch cyclist.

Sergio Pupovac: Sergio Pupovac, also known as Serdo or Serdjio Pupovac (born 5 July 1979) is a French-born Luxembourgian footballer, who currently plays in Luxembourg for FC UNA Strassen.  Last name Pupovac is, however, of Serbian origin.

Michael Gardiner: Michael Strickland Gardiner (born 5 July 1979) is a former Australian rules footballer who played for the West Coast Eagles and the St Kilda Football Club in the Australian Football League (AFL).  Originally from Albany, Western Australia, Gardiner played for the Claremont Football Club in the West Australian Football League (WAFL) before being drafted by West Coast with the number-one pick in the 1996 National Draft.  He made his debut for the club in 1997, and over the next seasons replaced Ryan Turnbull as the club's first-choice ruckman.  After being named in the All-Australian team in 2003, Gardiner missed most of the 2004 season due to injury.  Loss of form and a series of off-field controversies led to him being traded to St Kilda at the end of the 2006 season, having played total of 129 games for West Coast.  During his time at St Kilda, Gardiner added another 52 games, including St Kilda's 2009 and 2010 losing grand final teams, before retiring at the end of the 2011 season.

Bop Bop Baby: "Bop Bop Baby" (meaning 'dance, dance, dance to the distortion!')  is a song by Irish boy band Westlife and it was released on 20 May 2002 as the third single from their third studio album "World of Our Own" (2001).  The single peaked at No. 5 on the UK Singles Chart.  However, during an interview, the band claimed this was due to the obscure choice of single, as they would have much preferred to release "Why Do I Love You" - and had even recorded a video for it.  The song was written by band members Shane Filan and Brian McFadden, alongside producers and writers Chris O'Brien and Graham Murphy.  It sold over 120,000 copies in the UK.

To Be or Not to Bop: To Be or Not to Bop: Memoirs of Dizzy Gillespie is a 1979 book written by jazz musician, composer and band leader Dizzy Gillespie.  The book was released in July 1979 by Doubleday.  The University of Minnesota Press re-released the book in 2009.

Bop Bop: "Bop Bop" is a song recorded by Romanian singer Inna for her eponymous and fourth studio album (2015) and its Japanese counterpart, "Body and the Sun" (2015).  Featuring the vocals of American recording artist Eric Turner, it was made available for digital consumption on 14 July 2015 through Roton and Empire Music.  The recording was written by Sebastian Barac, Carl Bjorsell, Marcel Botezan, Julimar J-Son Santos, Thomas Troelsen and Eric Turner, while production was handled by Bjorsell, Troelsen, Turner and Play & Win.  A dance-pop track, "Bop Bop" was described as a departure from the singer's previous work.

Shane Filan: Shane Steven Filan (born 5 July 1979) is an Irish singer and songwriter.  He was one of the lead singers and frontman of boy band Westlife until the group disbanded in 2012.  After the group disbanded, Filan released his debut solo album, "You and Me", in 2013.

Marieke van Wanroij: Marieke van Wanroij (born 5 July 1979) is a Dutch professional racing cyclist.

Question: Which of the writers of the song "Bop Bop Baby" was born 5 July 1979?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song in question."
    },
    "target_birth_date": {
      "type": "string",
      "description": "The specific birth date mentioned in the question for filtering writers."
    },
    "matching_writer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the writer who matches the birth date criterion."
        },
        "role": {
          "type": "string",
          "description": "The role of the person in relation to the song (e.g., writer)."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the matching writer, confirming the match."
        }
      },
      "required": [
        "name",
        "role",
        "birth_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "target_birth_date",
    "matching_writer"
  ],
  "additionalProperties": false
}
